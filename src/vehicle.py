class Vehicle():
    '''
    This is a vehicle class. It has a number of wheels.
    '''

    def __init__(self, num_of_wheels: int):
        '''
        To initialise a vehicle by supplying the number of wheels

        Args:
            num_of_wheels (int): number of wheels a vehicle has
        '''
        self._num_of_wheels = num_of_wheels

    @property
    def num_of_wheels(self) -> int:
        '''
        To access the number of wheels a vehicle can have

        Returns:
            int: the number of wheels specified
        '''
        return self._num_of_wheels


\\\\\\\--==='';';',...,,......