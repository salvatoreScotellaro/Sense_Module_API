from bottle import Bottle, run, response
import requests
import json

app = Bottle()

@app.route('/sense', method='GET')
def sense():

    try:
        resp = requests.get('http://localhost:8002/read_sensors')
        print(resp)
        sensor_data = resp.json()

        perceptions = compute_perceptions(sensor_data)

        response.content_type = 'application/json'
        return json.dumps(perceptions)

    except Exception as e:
        print(f'Error occurred {e}')

def compute_perceptions(sensor_data:dict) -> list:

    perceptions = {}

    distances = [data for _,(data,type) in sensor_data.items() if type == "distance"]
    temperatures = [data for _,(data,type) in sensor_data.items() if type == "temperature"]
    pressions = [data for _,(data,type) in sensor_data.items() if type == "pression"]
    
    avg_pression = sum(pressions)/len(pressions)
    avg_temperature = sum(temperatures)/len(temperatures)

    perceptions['obstacles'] = 'No obstacle' if all(distance > 3.0 for distance in distances) else 'Obstacle'
    
    if avg_temperature > 30: perceptions['temperature'] = 'Hot'
    elif avg_temperature < 15: perceptions['temperature'] = 'Cold'
    else: perceptions['temperature'] = 'Moderate'

    if avg_pression < 1010: perceptions['pression'] = 'Low'
    elif avg_pression < 1020: perceptions['pression'] = 'Normal'
    else: perceptions['pression'] = 'High'

    return perceptions

if __name__ == "__main__":
    run(app, host='localhost', port=8001)
