# Python - Laboratory MQTT

This project is associated to the MQTT Laboratory in order to design and create a simple MQTT application emulating 
an IoT scenario where multiple electric vehicles periodically publish telemetry information related to GPS location, 
speed and battery level. Furthermore, each vehicle at the startup publish a description (retained) message containing
information associated to its unique identification, manufacturer and model. An external consumer subscribe to receive
both telemetry and description messages from all the available vehicles.

The project use the Python Libray Paho that can be installed with the following command: 

```bash
pip install paho-mqtt
```