class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.park = [0,big, medium, small]

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if self.park[carType] > 0:
            self.park[carType]=-1
            return True
        else:
            return False

