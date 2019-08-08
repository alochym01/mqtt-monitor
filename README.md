### using flask as mqtt-exporter

#### SYS topic
-   https://github.com/mqtt/mqtt.github.io/wiki/SYS-Topics
-   edit `/etc/mosquitto/mosquitto.conf` file and add a following line
    -   `sys_interval 60 # how long mosquitto update SYS topic metrics`
#### using paho as mqtt-client
-   https://github.com/eclipse/paho.mqtt.python
##### install paho
-   pip install paho-mqtt
-   `mqtt_sub/config.py` => config paho mqtt client
-   `mqtt_sub/mqtt_sub.py` => coding mqtt client which subscribe to $SYS
##### how to use
-   **Create a client instance**
-   **Connect to a broker using one of the connect*() functions**
    ```python
    def on_connect(client, userd, flags, rc):
    """Connect to MQTT Server. Check a log in /var/log/message."""
    syslog.syslog(f"MQTT connect rc: {str(rc)}")
    ```
-   **Call one of the loop\*() functions to maintain network traffic flow with the broker**
-   **Use subscribe() to subscribe to a topic and receive messages**
-   **Use publish() to publish messages to the broker**
-   **Use disconnect() to disconnect from the broker**
-   **Use on_message to do all your logic**
    ```python
    def on_message(client, userd, msg):
    """All logic will be executing here"""
    url = f"{config.MQTT_EXPORTER_SERVER}:{config.MQTT_EXPORTER_PORT}/{msg.topic.replace('$SYS/', '')}"
    params = {"value": msg.payload}
    print(url)
    rq = requests.get(url, params=params)
    syslog.syslog(f"{url} - GET - {rq.status_code} - {rq.text}")
    ```
-   if have any error should be checked `/var/log/message`
-   when mqtt client subscribe successfully, all metrics should sent to flask
##### return code value
-   0: Connection successful
-   1: Connection refused - incorrect protocol version
-   2: Connection refused - invalid client identifier
-   3: Connection refused - server unavailable
-   4: Connection refused - bad username or password
-   5: Connection refused - not authorised

#### flask as mqtt-exporter
##### install flask
-   pip install flask requests prometheus_client
##### config flask
-   `flask/instance/config.py` is store all variables
    -   `prometheus_metrics` is a variable which is stored all mqtt metrics
    -   can be changed as you wish
-   `flask/app/views/mqtt.py` has url `http://127.0.0.1:5000/prometheus_metrics` which is used for prometheus monitor
    ```bash
    (virtual-python-env) [hadn@hadn flask]$ flask routes
    Endpoint                       Methods  Rule
    -----------------------------  -------  ------------------------------------
    mqtt.bytesReceived             GET      /broker/bytes/received
    mqtt.bytesSent                 GET      /broker/bytes/sent
    mqtt.clientActive              GET      /broker/clients/active
    mqtt.clientConnected           GET      /broker/clients/connected
    mqtt.clientDisconnected        GET      /broker/clients/disconnected
    mqtt.clientExpired             GET      /broker/clients/expired
    mqtt.clientInactive            GET      /broker/clients/inactive
    mqtt.clientMaximum             GET      /broker/clients/maximum
    mqtt.clientTotal               GET      /broker/clients/total
    mqtt.heapCurrent               GET      /broker/heap/current
    mqtt.heapMaximum               GET      /broker/heap/maximum
    mqtt.loadBytesReceived15Min    GET      /broker/load/bytes/received/15min
    mqtt.loadBytesReceived1Min     GET      /broker/load/bytes/received/1min
    mqtt.loadBytesReceived5Min     GET      /broker/load/bytes/received/5min
    mqtt.loadBytesSent15Min        GET      /broker/load/bytes/sent/15min
    mqtt.loadBytesSent1Min         GET      /broker/load/bytes/sent/1min
    mqtt.loadBytesSent5Min         GET      /broker/load/bytes/sent/5min
    mqtt.loadConnection15Min       GET      /broker/load/connections/15min
    mqtt.loadConnection1Min        GET      /broker/load/connections/1min
    mqtt.loadConnection5Min        GET      /broker/load/connections/5min
    mqtt.loadMessageReceived15Min  GET      /broker/load/messages/received/15min
    mqtt.loadMessageReceived1Min   GET      /broker/load/messages/received/1min
    mqtt.loadMessageReceived5Min   GET      /broker/load/messages/received/5min
    mqtt.loadMessageSent15Min      GET      /broker/load/messages/sent/15min
    mqtt.loadMessageSent1Min       GET      /broker/load/messages/sent/1min
    mqtt.loadMessageSent5Min       GET      /broker/load/messages/sent/5min
    mqtt.loadPublishDrop15Min      GET      /broker/load/publish/dropped/15min
    mqtt.loadPublishDrop1Min       GET      /broker/load/publish/dropped/1min
    mqtt.loadPublishDrop5Min       GET      /broker/load/publish/dropped/5min
    mqtt.loadPublishReceived15Min  GET      /broker/load/publish/received/15min
    mqtt.loadPublishReceived1Min   GET      /broker/load/publish/received/1min
    mqtt.loadPublishReceived5Min   GET      /broker/load/publish/received/5min
    mqtt.loadPublishSent15Min      GET      /broker/load/publish/sent/15min
    mqtt.loadPublishSent1Min       GET      /broker/load/publish/sent/1min
    mqtt.loadPublishSent5Min       GET      /broker/load/publish/sent/5min
    mqtt.loadSocket15Min           GET      /broker/load/sockets/15min
    mqtt.loadSocket1Min            GET      /broker/load/sockets/1min
    mqtt.loadSocket5Min            GET      /broker/load/sockets/5min
    mqtt.messageReceived           GET      /broker/messages/received
    mqtt.messageSent               GET      /broker/messages/sent
    mqtt.messageStore              GET      /broker/messages/stored
    mqtt.metrics                   GET      /metrics
    mqtt.prometheusMetrics         GET      /prometheus_metrics
    mqtt.publishBytesReceived      GET      /broker/publish/bytes/received
    mqtt.publishBytesSent          GET      /broker/publish/bytes/sent
    mqtt.publishMessageDropped     GET      /broker/publish/messages/dropped
    mqtt.publishMessageReceived    GET      /broker/publish/messages/received
    mqtt.publishMessageSent        GET      /broker/publish/messages/sent
    mqtt.retainCount               GET      /broker/retained messages/count
    mqtt.storeMessageBytes         GET      /broker/store/messages/bytes
    mqtt.storeMessageCount         GET      /broker/store/messages/count
    mqtt.subscriptionCount         GET      /broker/subscriptions/count
    mqtt.uptime                    GET      /broker/uptime
    mqtt.version                   GET      /broker/version
    static                         GET      /static/<path:filename>
    ```
##### how to use flask
-   using systemd to start
-   create `mkdir /var/log/flask/` and chown for flask user
-   if has any url not found, should check `var/log/flask/app.log` file. ***Remember daily check***
-   All mqtt client and flask should be run in same machine with mqtt server
