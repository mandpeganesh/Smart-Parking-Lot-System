from vehicle_type import VehicleType
from vehicle import Vehicle


class ParkingSpot:
    def __init__(self, spot_id):
        self.spot_id = spot_id
        self.vehicle_type = VehicleType.MOTORCYCLE  # default vehicle type
        self.parked_vehicle = None

    def is_available(self) -> bool:
        return self.parked_vehicle is None

    def park_vehicle(self, vehicle: Vehicle) -> None:
        if self.is_available() and vehicle.get_type() == self.vehicle_type:
            self.parked_vehicle = vehicle
        else:
            raise ValueError("Invalid vehicle type or spot is not available")

    def unpark_vehicle(self) -> None:
        self.parked_vehicle = None

    def get_vehicle_type(self) -> VehicleType:
        return self.vehicle_type

    def get_parked_vehicle(self) -> Vehicle:
        return self.parked_vehicle

    def get_spot_id(self) -> int:
        return self.spot_id
