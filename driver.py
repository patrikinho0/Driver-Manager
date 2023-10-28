class Driver:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.status = "Free"
        self.reservation_detail = None

    def assign_reservation(self, reservation_detail):
        self.status = "Busy"
        self.reservation_detail = reservation_detail
    
    def conclude_reservation(self):
        self.status = "Free"
        self.reservation_detail = None

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "reservation_detail": self.reservation_detail
        }