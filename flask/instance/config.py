import os
from prometheus_client import Summary, Counter, Histogram, Gauge, Info
from prometheus_client.core import CollectorRegistry


basedir = os.path.abspath(os.path.dirname(__file__))


class DevelopmentConfig():
    """Development configurations."""

    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig():
    """Production configurations."""

    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

mqtt_metrics = {
    "bytes": {
        "sent": 0,
        "received": 0,
    },
    "client": {
        "total": 0,
        "inactive": 0,
        "disconnected": 0,
        "active": 0,
        "connected": 0,
        "expired": 0,
        "maximum": 0,
    },
    "connection": 0,
    "load": {
        "message": {
            "sent": {
                "1 min": 0,
                "5 min": 0,
                "15 min": 0
            },
            "received": {
                "1 min": 0,
                "5 min": 0,
                "15 min": 0
            }
        },
        "publish": {
            "sent": {
                "1 min": 0,
                "5 min": 0,
                "15 min": 0
            },
            "received": {
                "1 min": 0,
                "5 min": 0,
                "15 min": 0
            },
            "drop": {
                "1 min": 0,
                "5 min": 0,
                "15 min": 0
            }
        },
        "bytes": {
            "sent": {
                "1 min": 0,
                "5 min": 0,
                "15 min": 0
            },
            "received": {
                "1 min": 0,
                "5 min": 0,
                "15 min": 0
            }
        },
        "socket": {
            "1 min": 0,
            "5 min": 0,
            "15 min": 0
        },
        "connections": {
            "1 min": 0,
            "5 min": 0,
            "15 min": 0
        }
    },
    "messages": {
        "sent": 0,
        "received": 0,
        "sent": 0,
    },
    "publish": {
        "messages": {
            "drop": 0,
            "received": 0,
            "send": 0,
        },
        "bytes": {
            "send": 0,
            "received": 0,
        }
    },
    "store": {
        "count": 0,
        "in_bytes": 0,
    },
    "subscriptions": 0,
    "retained_messages_count": 0,
    "heap": {
        "current": 0,
        "maximum": 0,
    },
    "uptime": 0

}
registry = CollectorRegistry()
prometheus_metrics = {
    "bytes_received":               Gauge('broker_bytes_received', 'Broker Bytes Receieved', labelnames=['path'], registry=registry),
    "bytes_sent":                   Gauge('broker_bytes_sent', 'Broker Bytes Sent', labelnames=['path'], registry=registry),
    "client_total":                 Gauge('broker_client_total', 'Broker clients total', labelnames=['path'], registry=registry),
    "client_inactive":              Gauge('broker_client_inactive', 'Broker clients inactive', labelnames=['path'], registry=registry),
    "client_disconnected":          Gauge('broker_client_disconnected', 'Broker clients disconnected', labelnames=['path'], registry=registry),
    "client_active":                Gauge('broker_client_active', 'Broker clients active', labelnames=['path'], registry=registry),
    "client_connected":             Gauge('broker_client_connected', 'Broker clients connected', labelnames=['path'], registry=registry),
    "client_expired":               Gauge('broker_client_expired', 'Broker clients expired', labelnames=['path'], registry=registry),
    "client_maximum":               Gauge('broker_client_maximum', 'Broker clients maximum', labelnames=['path'], registry=registry),
    "broker_connection":            Gauge('broker_connection', 'Broker connection', labelnames=['path'], registry=registry),
    "load_msg_sent_1_min":          Gauge('load_msg_sent_1_min', 'Broker load message sent 1 min', labelnames=['path'], registry=registry),
    "load_msg_sent_5_min":          Gauge('load_msg_sent_5_min', 'Broker load message sent 5 min', labelnames=['path'], registry=registry),
    "load_msg_sent_15_min":         Gauge('load_msg_sent_15_min', 'Broker load message sent 15 min', labelnames=['path'], registry=registry),
    "load_msg_received_1_min":      Gauge('load_msg_received_1_min', 'Broker load message received 1 min', labelnames=['path'], registry=registry),
    "load_msg_received_5_min":      Gauge('load_msg_received_5_min', 'Broker load message received 5 min', labelnames=['path'], registry=registry),
    "load_msg_received_15_min":     Gauge('load_msg_received_15_min', 'Broker load message received 15 min', labelnames=['path'], registry=registry),
    "load_publish_sent_1_min":      Gauge('load_publish_sent_1_min', 'Broker load publish sent 1 min', labelnames=['path'], registry=registry),
    "load_publish_sent_5_min":      Gauge('load_publish_sent_5_min', 'Broker load publish sent 5 min', labelnames=['path'], registry=registry),
    "load_publish_sent_15_min":     Gauge('load_publish_sent_15_min', 'Broker load publish sent 15 min', labelnames=['path'], registry=registry),
    "load_publish_received_1_min":  Gauge('load_publish_received_1_min', 'Broker load publish received 1 min', labelnames=['path'], registry=registry),
    "load_publish_received_5_min":  Gauge('load_publish_received_5_min', 'Broker load publish received 5 min', labelnames=['path'], registry=registry),
    "load_publish_received_15_min": Gauge('load_publish_received_15_min', 'Broker load publish received 15 min', labelnames=['path'], registry=registry),
    "load_publish_drop_1_min":      Gauge('load_publish_drop_1_min', 'Broker load publish drop 1 min', labelnames=['path'], registry=registry),
    "load_publish_drop_5_min":      Gauge('load_publish_drop_5_min', 'Broker load publish drop 5 min', labelnames=['path'], registry=registry),
    "load_publish_drop_15_min":     Gauge('load_publish_drop_15_min', 'Broker load publish drop 15 min', labelnames=['path'], registry=registry),
    "load_bytes_sent_1_min":        Gauge('load_bytes_sent_1_min', 'Broker load bytes sent 1 min', labelnames=['path'], registry=registry),
    "load_bytes_sent_5_min":        Gauge('load_bytes_sent_5_min', 'Broker load bytes sent 5 min', labelnames=['path'], registry=registry),
    "load_bytes_sent_15_min":       Gauge('load_bytes_sent_15_min', 'Broker load bytes sent 15 min', labelnames=['path'], registry=registry),
    "load_bytes_received_1_min":    Gauge('load_bytes_received_1_min', 'Broker load bytes received 1 min', labelnames=['path'], registry=registry),
    "load_bytes_received_5_min":    Gauge('load_bytes_received_5_min', 'Broker load bytes received 5 min', labelnames=['path'], registry=registry),
    "load_bytes_received_15_min":   Gauge('load_bytes_received_15_min', 'Broker load bytes received 15 min', labelnames=['path'], registry=registry),
    "load_socket_1_min":            Gauge('load_socket_1_min', 'Broker load bytes received 1 min', labelnames=['path'], registry=registry),
    "load_socket_5_min":            Gauge('load_socket_5_min', 'Broker load bytes received 5 min', labelnames=['path'], registry=registry),
    "load_socket_15_min":           Gauge('load_socket_15_min', 'Broker load bytes received 15 min', labelnames=['path'], registry=registry),
    "load_connections_1_min":       Gauge('load_connections_1_min', 'Broker load bytes received 1 min', labelnames=['path'], registry=registry),
    "load_connections_5_min":       Gauge('load_connections_5_min', 'Broker load bytes received 5 min', labelnames=['path'], registry=registry),
    "load_connections_15_min":      Gauge('load_connections_15_min', 'Broker load bytes received 15 min', labelnames=['path'], registry=registry),
    "heap_current":                 Gauge('heap_current', 'Broker heap current', labelnames=['path'], registry=registry),
    "heap_maximum":                 Gauge('heap_maximum', 'Broker heap maximum', labelnames=['path'], registry=registry),
    "messages_stored":              Gauge('messages_stored', 'Broker messages stored', labelnames=['path'], registry=registry),
    "messages_received":            Gauge('messages_received', 'Broker messages received', labelnames=['path'], registry=registry),
    "messages_sent":                Gauge('messages_sent', 'Broker messages sent', labelnames=['path'], registry=registry),
    "publish_msg_drop":             Gauge('publish_msg_drop', 'Broker publish_msg drop', labelnames=['path'], registry=registry),
    "publish_msg_received":         Gauge('publish_msg_received', 'Broker publish_msg received', labelnames=['path'], registry=registry),
    "publish_msg_sent":             Gauge('publish_msg_sent', 'Broker publish_msg sent', labelnames=['path'], registry=registry),
    "publish_bytes_received":       Gauge('publish_bytes_received', 'Broker publish_bytes received', labelnames=['path'], registry=registry),
    "publish_bytes_sent":           Gauge('publish_bytes_sent', 'Broker publish_bytes sent', labelnames=['path'], registry=registry),
    "store_count":                  Gauge('store_count', 'Broker store message count', labelnames=['path'], registry=registry),
    "store_in_bytes":               Gauge('store_in_bytes', 'Broker store message in byte', labelnames=['path'], registry=registry),
    "subscriptions_count":          Gauge('subscription_count', 'Broker subscription count', labelnames=['path'], registry=registry),
    "retain_msg":                   Gauge('retain_msg', 'Broker retain message', labelnames=['path'], registry=registry),
    "broker_version":               Info('broker_version', 'Broker Version', registry=registry),
    "broker_uptime":                Gauge('broker_uptime', 'Broker uptime', labelnames=['path'], registry=registry),
}
