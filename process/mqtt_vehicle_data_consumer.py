import paho.mqtt.client as mqtt
from conf.mqtt_conf_params import MqttConfigurationParameters


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    device_info_topic = "{0}/{1}/+/{2}".format(
                    MqttConfigurationParameters.MQTT_BASIC_TOPIC,
                    MqttConfigurationParameters.VEHICLE_TOPIC,
                    MqttConfigurationParameters.VEHICLE_INFO_TOPIC)

    mqtt_client.subscribe(device_info_topic)

    print("Subscribed to: " + device_info_topic)

    device_telemetry_topic = "{0}/{1}/+/{2}".format(
        MqttConfigurationParameters.MQTT_BASIC_TOPIC,
        MqttConfigurationParameters.VEHICLE_TOPIC,
        MqttConfigurationParameters.VEHICLE_TELEMETRY_TOPIC)

    mqtt_client.subscribe(device_telemetry_topic)

    print("Subscribed to: " + device_telemetry_topic)


# Define a callback method to receive asynchronous messages
def on_message(client, userdata, message):
    message_payload = str(message.payload.decode("utf-8"))
    print(f"Received IoT Message: Topic: {message.topic} Payload: {message_payload}")


# Configuration variables
vehicle_id = "python-vehicle-consumer-{0}".format(MqttConfigurationParameters.MQTT_USERNAME)
message_limit = 1000

mqtt_client = mqtt.Client(vehicle_id)
mqtt_client.on_message = on_message
mqtt_client.on_connect = on_connect

# Set Account Username & Password
mqtt_client.username_pw_set(MqttConfigurationParameters.MQTT_USERNAME, MqttConfigurationParameters.MQTT_PASSWORD)

print("Connecting to " + MqttConfigurationParameters.BROKER_ADDRESS + " port: " + str(MqttConfigurationParameters.BROKER_PORT))
mqtt_client.connect(MqttConfigurationParameters.BROKER_ADDRESS, MqttConfigurationParameters.BROKER_PORT)

mqtt_client.loop_forever()
