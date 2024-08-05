import logging

from dataclasses import dataclass
import time

import paho.mqtt.client as mqtt
from paho.mqtt import enums as mqtt_enums
from paho.mqtt import reasoncodes as mqtt_reasoncodes

_log = logging.getLogger(__name__)  

@dataclass
class ConnectionConfiguration:
    host: str
    port: int


def try_connect(client: mqtt.Client, config: ConnectionConfiguration):
    # set on connect callback
    client.on_connect = try_on_connect
    
    # connect
    _log.info(f'Connecting to {config.host}:{config.port}')

    client.connect(config.host, config.port, 60)
    client.username_pw_set('user', 'password')

    # start loop
    _log.info('Starting loop')
    client.loop_start()

    # wait for connection
    time.sleep(3)
    assert client.is_connected()

    # stop loop
    _log.info('Stopping loop')
    client.loop_stop()

    # disconnect
    client.disconnect()


def try_on_connect(client: mqtt.Client, userdata, flags, reason_code, properties):
    m_topic = '%SYS/#'

    _log.info(f'Connected to {client._host}:{client._port}') 

    # assert connection
    _log.info(f'reason_code: {reason_code}')
    assert reason_code == 0 

    # subscribe to a topic
    client.subscribe(m_topic)


    # assert subscription
    assert m_topic in client._topics
    _log.info(f'Subscribed to {m_topic}')

    # disconnect
    client.disconnect()

if __name__ == '__main__':
    # configure logging
    logging.basicConfig(level=logging.DEBUG)

    # create a client instance
    client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)

    # try connecting
    try_connect(client, ConnectionConfiguration('localhost', 1883))
