"""
 Physical Sensor API Process
 Input: from real world
 Output: cured sensor signals
"""

from typing import Any
import glob
import json
from pathlib import Path
from os import sep
import random

class PhySensor:

    """
        Abstract Physical Sensor class
    """

    def __init__(self, name: str, work_range, config_file: str):
        assert isinstance(name, str) and len(name)>0
        assert isinstance(work_range, tuple) and len(work_range)==2
        file_path = f"{Path.cwd()}{sep}PhyRobotAPI{sep}{config_file}"
        assert isinstance(config_file, str) and \
            glob.glob(file_path), \
                f"Configuration file {config_file} is not found!"
        self._id = name
        self._range = work_range
        config_js = open(file_path, encoding="utf-8").read()
        self._config = json.loads(config_js)

    def read(self) -> Any:
        """
            read the sensor value
            out: cured sensor value
        """
        pass

    def __repr__(self) -> str:
        return f"Sensor: {self._id} range: {self._range}"


class DistanceSensor(PhySensor):
    """
        Proximity distance sensor monodimensional
    """
    def __init__(self, name, work_range, config_file):
        super().__init__(name, work_range, config_file)
        self._type = "distance"

    def read(self) -> float:
        """
            Read the distance sensor from the hardware layer
            skip all physical issues
        """
        return random.uniform(0,10) # Random forward distance in meters

class TemperatureSensor(PhySensor):
    """
        Temperature sensor monodimensional
    """
    def __init__(self, name, work_range, config_file):
        super().__init__(name, work_range, config_file)
        self._type = "temperature"

    def read(self) -> float:
        return random.uniform(0,30) # Random environment temperature in C°
    
class PressionSensor(PhySensor):
    """
        Pression sensor monodimensional
    """
    def __init__(self, name, work_range, config_file):
        super().__init__(name, work_range, config_file)
        self._type = "pression"

    def read(self) -> float:
        return random.uniform(980,1040) # Random environment pression in hPA

if __name__ == "__main__":

    # Instantiate sensors
    ds1 = DistanceSensor("test_distance_sensor", (-10,10), "test.json")
    ts1 = TemperatureSensor("test_temperature_sensor", (-1,1), "test.json")
    ps1 = PressionSensor("test_pression_sensor", (-1,1), "test.json")

    print(ds1.read())
    print(ts1.read())
    print(ps1.read())



