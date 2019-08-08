from flask import Blueprint, render_template, request, json, Response, current_app
from instance.config import mqtt_metrics, prometheus_metrics
from prometheus_client import Summary, Counter, Histogram, Gauge, generate_latest
import socket


mqtt = Blueprint('mqtt', __name__)


@mqtt.route('/broker/bytes/received')
def bytesReceived():
    mqtt_metrics['bytes']['received'] = float(request.args.get('value'))
    prometheus_metrics["bytes_received"].labels(
        f'{request.path}').set(float(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/bytes/sent')
def bytesSent():
    mqtt_metrics['bytes']['sent'] = float(request.args.get('value'))
    prometheus_metrics['bytes_sent'].labels(
        f'{request.path}').set(float(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/clients/connected')
def clientConnected():
    mqtt_metrics['client']['connected'] = int(request.args.get('value'))
    prometheus_metrics['client_connected'].labels(
        f'{request.path}').set(int(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/clients/active')
def clientActive():
    mqtt_metrics['client']['active'] = int(request.args.get('value'))
    prometheus_metrics['client_active'].labels(
        f'{request.path}').set(int(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/clients/expired')
def clientExpired():
    mqtt_metrics['client']['expired'] = int(request.args.get('value'))
    prometheus_metrics['client_expired'].labels(
        f'{request.path}').set(int(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/clients/disconnected')
def clientDisconnected():
    mqtt_metrics['client']['disconnected'] = int(request.args.get('value'))
    prometheus_metrics['client_disconnected'].labels(
        f'{request.path}').set(int(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/clients/inactive')
def clientInactive():
    mqtt_metrics['client']['inactive'] = int(request.args.get('value'))
    prometheus_metrics['client_inactive'].labels(
        f'{request.path}').set(int(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/clients/maximum')
def clientMaximum():
    mqtt_metrics['client']['maximum'] = int(request.args.get('value'))
    prometheus_metrics['client_maximum'].labels(
        f'{request.path}').set(int(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/clients/total')
def clientTotal():
    mqtt_metrics['client']['total'] = int(request.args.get('value'))
    prometheus_metrics['client_total'].labels(
        f'{request.path}').set(int(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/heap/current')
def heapCurrent():
    mqtt_metrics['heap']['current'] = int(request.args.get('value'))
    prometheus_metrics['heap_current'].labels(
        f'{request.path}').set(int(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/heap/maximum')
def heapMaximum():
    mqtt_metrics['heap']['maximum'] = int(request.args.get('value'))
    prometheus_metrics['heap_maximum'].labels(
        f'{request.path}').set(int(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/messages/stored')
def messageStore():
    mqtt_metrics['messages']['stored'] = int(request.args.get('value'))
    prometheus_metrics['messages_stored'].labels(
        f'{request.path}').set(int(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/messages/received')
def messageReceived():
    mqtt_metrics['messages']['received'] = int(request.args.get('value'))
    prometheus_metrics['messages_received'].labels(
        f'{request.path}').set(int(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/messages/sent')
def messageSent():
    mqtt_metrics['messages']['sent'] = int(request.args.get('value'))
    prometheus_metrics['messages_sent'].labels(
        f'{request.path}').set(int(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/store/messages/count')
def storeMessageCount():
    mqtt_metrics['messages']['count'] = int(request.args.get('value'))
    prometheus_metrics['store_count'].labels(
        f'{request.path}').set(int(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/store/messages/bytes')
def storeMessageBytes():
    mqtt_metrics['store']['in_bytes'] = int(request.args.get('value'))
    prometheus_metrics['store_in_bytes'].labels(
        f'{request.path}').set(int(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/publish/messages/dropped')
def publishMessageDropped():
    mqtt_metrics['publish']['messages']['drop'] = int(
        request.args.get('value'))
    prometheus_metrics['publish_msg_drop'].labels(
        f'{request.path}').set(int(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/publish/messages/received')
def publishMessageReceived():
    mqtt_metrics['publish']['messages']['received'] = int(
        request.args.get('value'))
    prometheus_metrics['publish_msg_received'].labels(
        f'{request.path}').set(int(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/publish/messages/sent')
def publishMessageSent():
    mqtt_metrics['publish']['messages']['sent'] = int(
        request.args.get('value'))
    prometheus_metrics['publish_msg_sent'].labels(
        f'{request.path}').set(int(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/publish/bytes/received')
def publishBytesReceived():
    mqtt_metrics['publish']['bytes']['received'] = int(
        request.args.get('value'))
    prometheus_metrics['publish_bytes_received'].labels(
        f'{request.path}').set(int(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/publish/bytes/sent')
def publishBytesSent():
    mqtt_metrics['publish']['bytes']['sent'] = int(request.args.get('value'))
    prometheus_metrics['publish_bytes_sent'].labels(
        f'{request.path}').set(int(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/retained messages/count')
def retainCount():
    mqtt_metrics['retained_messages_count'] = int(request.args.get('value'))
    prometheus_metrics['retain_msg'].labels(f'{request.path}').set(
        int(request.args.get('value').replace(' seconds', '')))
    return ('', 204)


@mqtt.route('/broker/version')
def version():
    mqtt_metrics['version'] = request.args.get('value')
    prometheus_metrics['broker_version'].info(
        {'version': request.args.get('value').replace('mosquitto version ', '')})
    return ('', 204)


@mqtt.route('/broker/uptime')
def uptime():
    mqtt_metrics['uptime'] = request.args.get('value').replace(' seconds', '')
    prometheus_metrics['broker_uptime'].labels(f'{request.path}').set(
        int(request.args.get('value').replace(' seconds', '')))
    return ('', 204)


@mqtt.route('/broker/load/messages/received/1min')
def loadMessageReceived1Min():
    mqtt_metrics['load']['message']['received']['1 min'] = request.args.get(
        'value')
    prometheus_metrics["load_msg_received_1_min"].labels(
        f'{request.path}').set(float(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/load/messages/received/5min')
def loadMessageReceived5Min():
    mqtt_metrics['load']['message']['received']['5 min'] = request.args.get(
        'value')
    prometheus_metrics["load_msg_received_5_min"].labels(
        f'{request.path}').set(float(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/load/messages/received/15min')
def loadMessageReceived15Min():
    mqtt_metrics['load']['message']['received']['15 min'] = request.args.get(
        'value')
    prometheus_metrics["load_msg_received_15_min"].labels(
        f'{request.path}').set(float(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/load/messages/sent/1min')
def loadMessageSent1Min():
    mqtt_metrics['load']['message']['sent']['1 min'] = request.args.get(
        'value')
    prometheus_metrics["load_msg_sent_1_min"].labels(
        f'{request.path}').set(float(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/load/messages/sent/5min')
def loadMessageSent5Min():
    mqtt_metrics['load']['message']['sent']['5 min'] = request.args.get(
        'value')
    prometheus_metrics["load_msg_sent_5_min"].labels(
        f'{request.path}').set(float(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/load/messages/sent/15min')
def loadMessageSent15Min():
    mqtt_metrics['load']['message']['sent']['15 min'] = request.args.get(
        'value')
    prometheus_metrics["load_msg_sent_15_min"].labels(
        f'{request.path}').set(float(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/load/publish/dropped/1min')
def loadPublishDrop1Min():
    mqtt_metrics['load']['publish']['drop']['1 min'] = request.args.get(
        'value')
    prometheus_metrics["load_publish_drop_1_min"].labels(
        f'{request.path}').set(float(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/load/publish/dropped/5min')
def loadPublishDrop5Min():
    mqtt_metrics['load']['publish']['drop']['5 min'] = request.args.get(
        'value')
    prometheus_metrics["load_publish_drop_5_min"].labels(
        f'{request.path}').set(float(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/load/publish/dropped/15min')
def loadPublishDrop15Min():
    mqtt_metrics['load']['publish']['drop']['15 min'] = request.args.get(
        'value')
    prometheus_metrics["load_publish_drop_15_min"].labels(
        f'{request.path}').set(float(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/load/publish/sent/1min')
def loadPublishSent1Min():
    mqtt_metrics['load']['publish']['sent']['1 min'] = request.args.get(
        'value')
    prometheus_metrics["load_publish_sent_1_min"].labels(
        f'{request.path}').set(float(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/load/publish/sent/5min')
def loadPublishSent5Min():
    mqtt_metrics['load']['publish']['sent']['5 min'] = request.args.get(
        'value')
    prometheus_metrics["load_publish_sent_5_min"].labels(
        f'{request.path}').set(float(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/load/publish/sent/15min')
def loadPublishSent15Min():
    mqtt_metrics['load']['publish']['sent']['15 min'] = request.args.get(
        'value')
    prometheus_metrics["load_publish_sent_15_min"].labels(
        f'{request.path}').set(float(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/load/publish/received/1min')
def loadPublishReceived1Min():
    mqtt_metrics['load']['publish']['received']['1 min'] = request.args.get(
        'value')
    prometheus_metrics["load_publish_received_1_min"].labels(
        f'{request.path}').set(float(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/load/publish/received/5min')
def loadPublishReceived5Min():
    mqtt_metrics['load']['publish']['received']['5 min'] = request.args.get(
        'value')
    prometheus_metrics["load_publish_received_5_min"].labels(
        f'{request.path}').set(float(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/load/publish/received/15min')
def loadPublishReceived15Min():
    mqtt_metrics['load']['publish']['received']['15 min'] = request.args.get(
        'value')
    prometheus_metrics["load_publish_received_15_min"].labels(
        f'{request.path}').set(float(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/load/bytes/received/1min')
def loadBytesReceived1Min():
    mqtt_metrics['load']['bytes']['received']['1 min'] = request.args.get(
        'value')
    prometheus_metrics["load_bytes_received_1_min"].labels(
        f'{request.path}').set(float(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/load/bytes/received/5min')
def loadBytesReceived5Min():
    mqtt_metrics['load']['bytes']['received']['5 min'] = request.args.get(
        'value')
    prometheus_metrics["load_bytes_received_5_min"].labels(
        f'{request.path}').set(float(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/load/bytes/received/15min')
def loadBytesReceived15Min():
    mqtt_metrics['load']['bytes']['received']['15 min'] = request.args.get(
        'value')
    prometheus_metrics["load_bytes_received_15_min"].labels(
        f'{request.path}').set(float(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/load/bytes/sent/1min')
def loadBytesSent1Min():
    mqtt_metrics['load']['bytes']['sent']['1 min'] = request.args.get('value')
    prometheus_metrics["load_bytes_sent_1_min"].labels(
        f'{request.path}').set(float(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/load/bytes/sent/5min')
def loadBytesSent5Min():
    mqtt_metrics['load']['bytes']['sent']['5 min'] = request.args.get('value')
    prometheus_metrics["load_bytes_sent_5_min"].labels(
        f'{request.path}').set(float(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/load/bytes/sent/15min')
def loadBytesSent15Min():
    mqtt_metrics['load']['bytes']['sent']['15 min'] = request.args.get('value')
    prometheus_metrics["load_bytes_sent_15_min"].labels(
        f'{request.path}').set(float(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/load/connections/1min')
def loadConnection1Min():
    mqtt_metrics['load']['connections']['1 min'] = request.args.get('value')
    prometheus_metrics["load_connections_1_min"].labels(
        f'{request.path}').set(float(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/load/connections/5min')
def loadConnection5Min():
    mqtt_metrics['load']['connections']['5 min'] = request.args.get('value')
    prometheus_metrics["load_connections_5_min"].labels(
        f'{request.path}').set(float(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/load/connections/15min')
def loadConnection15Min():
    mqtt_metrics['load']['connections']['15 min'] = request.args.get('value')
    prometheus_metrics["load_connections_15_min"].labels(
        f'{request.path}').set(float(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/load/sockets/1min')
def loadSocket1Min():
    mqtt_metrics['load']['socket']['1 min'] = request.args.get('value')
    prometheus_metrics["load_socket_1_min"].labels(
        f'{request.path}').set(float(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/load/sockets/5min')
def loadSocket5Min():
    mqtt_metrics['load']['socket']['5 min'] = request.args.get('value')
    prometheus_metrics["load_socket_5_min"].labels(
        f'{request.path}').set(float(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/load/sockets/15min')
def loadSocket15Min():
    mqtt_metrics['load']['socket']['15 min'] = request.args.get('value')
    prometheus_metrics["load_socket_15_min"].labels(
        f'{request.path}').set(float(request.args.get('value')))
    return ('', 204)


@mqtt.route('/broker/subscriptions/count')
def subscriptionCount():
    mqtt_metrics['subscriptions'] = request.args.get('value')
    prometheus_metrics['subscriptions_count'].labels(
        f'{request.path}').set(int(request.args.get('value')))

    return ('', 204)


@mqtt.route('/metrics')
def metrics():
    return render_template('metrics.html', metrics=mqtt_metrics)


@mqtt.route('/prometheus_metrics')
def prometheusMetrics():
    res = []
    for v in prometheus_metrics.values():
        res.append(generate_latest(v))
    return Response(res, mimetype="text/plain")
