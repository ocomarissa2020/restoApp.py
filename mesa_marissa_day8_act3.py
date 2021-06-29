class House (object):
    def __init__(self, floorSize,noOfFloors,noOfDoors ):
        self.floorSize = floorSize
        self.noOfFloors = noOfFloors
        self.noOfDoors = noOfDoors
    def switchOn(self):
        print ('The switch is On.')
    def lightOpen(self):
        print('The light is Open.')
    def ovenOpen(self):
        print('The oven is Open.')