from bottle import Bottle, run, response
import requests

app = Bottle()

@app.route('/sense', method='GET')
def sense():
    print('Hello capo.')

    try:
        resp = requests.get('localhost/pression')
        sensor_data = resp.json()

        perceptions = compute_perceptions(sensor_data)

        response.content_type = 'application/json'
        response.body = f'{"perceptions": perceptions}'

    except Exception as e:
        print(f'Error occurred {e}')

def compute_perceptions(sensor_data) -> list:

    perceptions = sensor_data
    return perceptions

if __name__ == "__main__":
    run(app, host='localhost', port=8001)
