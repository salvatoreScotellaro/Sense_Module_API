from PhyRobotAPI.PhySens import DistanceSensor, PressionSensor, TemperatureSensor 
from bottle import Bottle, run, response
import json

# Create server app to respond to sense_app requests
server = Bottle()

@server.route('/', method='GET')
def test():
    print('Server test')

@server.route('/read_sensors', method='GET')
def read_sensors() -> dict:

    global sensors

    try:
        data = {sensor_id: (sensor.read(),sensor._type) for sensor_id, sensor in sensors.items()}
    except Exception as e:
        print(f"{e} occurred.")

    response.content_type = 'application/json'
    return json.dumps(data)

@server.route('/read_sensors/<type>', method='GET')
def read_sensors(type:str) -> dict:

    global sensors

    try:
        data = {sensor_id: (sensor.read(),type) for sensor_id, sensor in sensors.items() if sensor._type == type}
    except Exception as e:
        print(f"{e} occurred.")

    response.content_type = 'application/json'
    return json.dumps(data)

if __name__ == "__main__":

    # Instantiate sensors
    ds1 = DistanceSensor("distance_sensor_1", (-1,1), "test.json")
    ts1 = TemperatureSensor("temperature_sensor_1", (-1,1), "test.json")
    ps1 = PressionSensor("pression_sensor_1", (-1,1), "test.json")

    sensors = {
        ds1._id: ds1,
        ts1._id: ts1,
        ps1._id: ps1
    }

    run(server, host="localhost", port=8002)
    
