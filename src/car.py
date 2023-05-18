from vehicle import Vehicle

class Car(Vehicle):
    '''
    A car class which inherits from Vehicle.
    '''
    def __init__(self, num_of_wheels: int, brand: str):
        '''
        Initialise a car with the given number of wheels.

        Args:
            num_of_wheels (int): the number of wheels a vehicle has
        '''
        super().__init__(num_of_wheels)
        self._brand = brand
        
        
    @property
    def brand(self) -> str:
        '''
        Return the brand of the car.

        Returns:
            str: the brand of the car
        '''
        return self._brand
    

