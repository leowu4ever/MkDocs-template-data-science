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
    
    def drive(self, num_of_miles: float) -> None:
        '''
        Drive the vehicle for a given number of miles

        Args:
            num_of_miles (float): how far to drive the vehicle
        '''
        print('starting engine')
        print(f'driving forward for {num_of_miles} mile(s)')
        print('stopping')
        
