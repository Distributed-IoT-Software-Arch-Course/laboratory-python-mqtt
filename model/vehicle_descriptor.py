import json


class VehicleDescriptor:

    def __init__(self, uuid, manufacturer, model, driverId):
        self.uuid = uuid
        self.manufacturer = manufacturer
        self.model = model
        self.driverId = driverId

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
