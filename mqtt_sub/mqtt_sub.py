import config
import paho.mqtt.client as mqtt
import os
import json
import sys
import time
import syslog
import requests


def on_connect(client, userd, flags, rc):
    """Connect to MQTT Server. Check a log in /var/log/message."""
    syslog.syslog(f"MQTT connect rc: {str(rc)}")


def on_message(client, userd, msg):
    """All logic will be executing here"""
    url = f"{config.MQTT_EXPORTER_SERVER}:{config.MQTT_EXPORTER_PORT}/{msg.topic.replace('$SYS/', '')}"
    params = {
        "value": msg.payload
    }
    print(url)
    rq = requests.get(url, params=params)
    syslog.syslog(f"{url} - GET - {rq.status_code} - {rq.text}")


def main():
    mqtts = mqtt.Client(config.MQTT_ID)
    mqtts.username_pw_set(config.MQTT_USERNAME, config.MQTT_PASSWORD)
    mqtts.on_connect = on_connect
    mqtts.on_message = on_message
    while True:
        # Try to connect to server if fail retry again after 5 second
        try:
            # return code value
            #     0: Connection successful
            #     1: Connection refused - incorrect protocol version
            #     2: Connection refused - invalid client identifier
            #     3: Connection refused - server unavailable
            #     4: Connection refused - bad username or password
            #     5: Connection refused - not authorised
            rc = mqtts.connect(config.MQTT_SERVER,
                               config.MQTT_PORT, keepalive=120)
            # subscribe SYS topic
            mqtts.subscribe("$SYS/#", 0)
            while rc == 0:
                rc = mqtts.loop()
        except Exception as e:
            syslog.syslog(f"MQTT disconnect {str(e)}")
            time.sleep(5)
            continue


if __name__ == "__main__":
    sys.exit(main())
