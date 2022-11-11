from dataclasses import dataclass
from Route import Route

@dataclass

class DriverInfo:
    """Info about driver.
    Args:
        driver_id (int): Driver ID
        full_name (str): Drivers first name
        date_of_birth (int): Drivers date of birth
        experience (int): Driver work experience
    """
    driver_id: int
    full_name: str
    date_of_birth: int
    experience: int

class PassengerInfo:
    """Info about Passenger.
    Args:
    passenger_id (int): Passenger ID.
    full_name (str): Passenger full name.
    date_of_birth (int): Passenger date of birth
    """
    passenger_id: int
    full_name: str
    date_of_birth: int

class Driver:
    def __init__(self):
        self.DriverInfo_ = None

    def driver_info(self):
        return self.DriverInfo_

    def DriverInfo(self, driver_info: DriverInfo):
        if isinstance(driver_info, DriverInfo):
            self.DriverInfo_ = driver_info

class Passenger:

    def __init__(self) -> None:
        self.PassengerInfo_ = None

    def PassengerInfo_(self):
        return self._PassengerInfo_

    def passenger_info(self, PassengerInfo_: PassengerInfo) -> None:
        if isinstance(PassengerInfo_, PassengerInfo):
            self._PassengerInfo_ = PassengerInfo_