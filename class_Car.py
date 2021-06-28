class Car:
    no_of_objects = 0
    def __init__(self,model,year,type_of_car,unique_id):
        self.model = model
        self.year=year
        self.type_of_car = type_of_car
        self.unique_id=unique_id
        Car.no_of_objects += 1
        
    def no_of_vehicles(self):
        return Car.no_of_objects