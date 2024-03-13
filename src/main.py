import json
import logging
import os
import time

import psycopg2
import requests
from signalrcore.hub_connection_builder import HubConnectionBuilder


class App:
    def __init__(self):
        self._hub_connection = None
        self.ticks = 10
        self.conn = None

        # To be configured by your team
        self.host = os.environ.get("HOST")
        self.token = os.environ.get("TOKEN")
        self.t_max = os.environ.get("T_MAX")
        self.t_min = os.environ.get("T_MIN")
        self.database_url = os.environ.get("DATABASE_URL")

        # Set up database connection
        self.database_connection()

    def __del__(self):
        if self._hub_connection is not None:
            self._hub_connection.stop()

        if self.conn is not None:
            self.conn.close()

    def start(self):
        """Start Oxygen CS."""
        self.setup_sensor_hub()
        self._hub_connection.start()
        print("Press CTRL+C to exit.")
        while True:
            time.sleep(2)

    def setup_sensor_hub(self):
        """Configure hub connection and subscribe to sensor data events."""
        self._hub_connection = (
            HubConnectionBuilder()
            .with_url(f"{self.host}/SensorHub?token={self.token}")
            .configure_logging(logging.INFO)
            .with_automatic_reconnect(
                {
                    "type": "raw",
                    "keep_alive_interval": 10,
                    "reconnect_interval": 5,
                    "max_attempts": 999,
                }
            )
            .build()
        )
        self._hub_connection.on("ReceiveSensorData", self.on_sensor_data_received)
        self._hub_connection.on_open(lambda: print("||| Connection opened."))
        self._hub_connection.on_close(lambda: print("||| Connection closed."))
        self._hub_connection.on_error(
            lambda data: print(f"||| An exception was thrown closed: {data.error}")
        )

    def on_sensor_data_received(self, data):
        """Callback method to handle sensor data on reception."""
        try:
            print(data[0]["date"] + " --> " + data[0]["data"], flush=True)
            timestamp = data[0]["date"]
            temperature = float(data[0]["data"])
            self.take_action(temperature)
            self.save_event_to_database(timestamp, temperature)
        except Exception as err:
            print(err)

    def take_action(self, temperature):
        """Take action to HVAC depending on current temperature."""
        if float(temperature) >= float(self.t_max):
            self.send_action_to_hvac("TurnOnAc")
        elif float(temperature) <= float(self.t_min):
            self.send_action_to_hvac("TurnOnHeater")

    def send_action_to_hvac(self, action):
        """Send action query to the HVAC service."""
        r = requests.get(f"{self.host}/api/hvac/{self.token}/{action}/{self.ticks}")
        details = json.loads(r.text)
        print(details, flush=True)

    def save_event_to_database(self, timestamp, temperature):
        """Save sensor data into database."""
        try:
            if self.conn is not None:
                cursor = self.conn.cursor()

                # Insert data into the table
                insert_query = (
                    """INSERT INTO "Oxygene" (temperature, date) VALUES (%s, %s)"""
                )
                cursor.execute(insert_query, (temperature, timestamp))
                self.conn.commit()

                print("Data inserted successfully!")

                cursor.close()

        except Exception as e:
            print("Error inserting data into PostgreSQL database:", e)

    def database_connection(self):
        try:
            self.conn = psycopg2.connect(self.database_url)
        except Exception as e:
            print("Error connecting to PostgreSQL database:", e)


if __name__ == "__main__":
    app = App()
    app.start()
