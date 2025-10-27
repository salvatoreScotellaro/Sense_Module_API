## Sense Module API

---

This repository contains a simple implementation of an API to represent the Sense module of a robot. In particular, this has been realized within the following files.

- The `PhySens.py` file contains the implementation of an abstract class `PhySensor`, and of some child classes to represent specific sensors, such as `DistanceSensor`, `TemperatureSensor` and `PressionSensor`.

- The `phySens_server.py` file contains the implementation of a simple server application that receives requests from the sense module API, and returns sensors' data. In particular the followig two endpoints have been defined.

    - `/read_sensors/` endpoint returns a JSON containing data from all available sensors, appropriately formatted.
    - `/read_sensors/<type>` endpoint uses the wildcard `<type>` to return only a specific type of data. Possible values for this parameter are `distance`, `temperature` and `pression`. Also in this case the response contains am appropriately formatted JSON.

- The `sense_app.py` file contains the implementation of the actual API using a `Bottle` app. In this case just one endpoint is defined, which is the `/sense` one. This makes a request to the PhySens server, retrieves data from the JSON in the response and derives perceptions, on the basis of some very simple logic. Finally, returns the perceptions as a JSON.

---

### How to Run
To run the code, there are two possible ways. Starting from the simplest one, this is summarized in the following points.

- Start WSL and create a new directory for the project with any name.
- Clone this repository, whose link is https://github.com/salvatoreScotellaro/Sense_Module_API.git.
- Call the directory cloned with command `cd Sense_Module_API`.
- Create a new virtual environment with `python3 -m venv venv`.
- Activate the virual environment using `source venv/bin/activate`.
- Install project with required dependencies using `pip install .`.
- Start the PhySens server with command `python3 phySens_server.py`.
- Start the Sense Module API with command `python3 sense_app.py` in another terminal window.
- Hit the endpoint at this link: http://localhost:8001/sense.

Another possibility is use the `.zip` file provided as delivery of the homework. In this case, the procedure is described by the following points.

- Start WSL and create a new directory for the project with any name.
- Copy the `.zip` file in the created directory and unzip it with `unzip sense_module_API.zip`.
- Call the directory with the command `cd sense_module_API`.
- Create a new virtual environment with `python3 -m venv venv`.
- Activate the virual environment using `source venv/bin/activate`.
- Install project with required dependencies using `pip install .`.
- Start the PhySens server with command `python3 phySens_server.py`.
- Start the Sense Module API with command `python3 sense_app.py` in another terminal window.
- Hit the endpoint at this link: http://localhost:8001/sense.
