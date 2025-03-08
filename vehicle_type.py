from enum import Enum


class VehicleType(Enum):
    """Represents the type of a vehicle.

    Vehicles can be of type MOTORCYCLE, CAR, or TRUCK.
    """
    MOTORCYCLE = 1
    CAR = 2
    TRUCK = 3
