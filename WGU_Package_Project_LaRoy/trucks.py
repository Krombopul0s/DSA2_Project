import hashTable
import datetime
from packData import distanceData
from sorter import packageReference

#creates truck object that contains a hashTable for it's manifest
class Truck:

    def __init__(self, truckNum, time=900):
        self.truckNum = truckNum
        self.manifest = []
        self.mileage = 0.0
        
    #"delivers" package, increments time and mileage to simulate duration and distance of route
    def deliverPackages(self, load, hour, minute):
        time = datetime.datetime(2023, 11, 27, hour=hour, minute=minute)
        
        #for each package in manifest
        for box in load:
            distance = box.distanceToBox
            self.mileage += float(distance)
            travelTime = float(distance)/(18/60)
            deliveryTime = datetime.timedelta(minutes = travelTime)
            time += deliveryTime
            referenceBox = packageReference.getItem(box.packageID)
            referenceBox.status = 'Delivered'
            referenceBox.deliveryTime = time.time()
            self.manifest.append(referenceBox)
        return
    
    #gets the route data for packages on each truck
    def getRouteData(self, truck):
        #calculate route length in miles and time
        #Determine if packages on truck can be delivered in time, raise error if not
        return
    
    
        
    