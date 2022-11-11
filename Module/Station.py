from dataclasses import dataclass

@dataclass
class StationInfo:
    """Info about station.

    Args:
        passenger_id (int): Passenger ID.
        city (str): City where station
        transport(str): transport model

    """
    passenger_id: int
    city: str
    transport: str

class Station:

    def __init__(self):
        self._station_info = None

    def station_info(self) -> str:
        return self._station_info

    def station_info(self, station_info: StationInfo) -> None:
        if isinstance(station_info, StationInfo):
            self._station_info = StationInfo