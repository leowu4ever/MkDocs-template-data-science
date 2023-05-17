class Vehicle():
    
    def __init__(self, num_of_wheels: int):
        '''
        To initialise a vehicle by supplying the number of wheels

        Args:
            num_of_wheels (int): the number of wheels a vehicle can have
        '''
        self._num_of_wheels = num_of_wheels
    
    @property
    def num_of_wheels(self) -> int:
        '''
        To access the number of wheels a vehicle can have

        Returns:
            int: number of wheels specified
        '''
        return self._num_of_wheels
