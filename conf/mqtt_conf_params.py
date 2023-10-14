class MqttConfigurationParameters(object):

    BROKER_ADDRESS = "<BROKER_IP_ADDRESS>"
    BROKER_PORT = 7883
    MQTT_USERNAME = "<your_username>"
    MQTT_PASSWORD = "<your_password>"
    MQTT_BASIC_TOPIC = "/iot/user/{0}".format(MQTT_USERNAME)
    VEHICLE_TOPIC = "vehicle"
    VEHICLE_TELEMETRY_TOPIC = "telemetry"
    VEHICLE_INFO_TOPIC = "info"
