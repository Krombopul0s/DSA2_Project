#Student: Timothy LaRoy
#Student ID: 010892950

import packData
import hashTable
import sorter
import trucks
import datetime
from datetime import datetime
from packData import packages
from sorter import packageReference

#sets up menu options table and defines options
menuOptions = hashTable.HashTable(7)

menuOptions.add(1, 'Load trucks & deliver packages- 1')
menuOptions.add(2, 'Get Info for package(s) ------- 2')
menuOptions.add(3, 'Update package data ----------- 3')
menuOptions.add(4, 'Exit -------------------------- 4')

global trucksSorted
trucksSorted = False
#displays menu until exited.
def displayMenu():
    print()
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    for i in range(1, 5):
        print(menuOptions.getItem(i))
    print()
    print('Note: If you are having difficulies with system, please run program again and select option 4 before trying again.')
    print('Thank you.')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    
def loadTrucks():
    #create trucks
    global truck1, truck2, truck3
    truck1 = trucks.Truck(1)
    truck2 = trucks.Truck(2)
    truck3 = trucks.Truck(3)
    
    #sort packages
    sorter.sortPackages(packages)

    from sorter import sortedLoad1, sortedLoad2, sortedLoad3

    #add sorted packages to trucks
    truck1Load = sortedLoad1
    truck2Load = sortedLoad2
    truck3Load = sortedLoad3

    #delvier packages
    truck1.deliverPackages(truck1Load, 8, 0)
    truck2.deliverPackages(truck2Load, 9, 5)
    truck3.deliverPackages(truck3Load, 13, 0)

    #prints out report of all packages and mileage for each truck
    for i in range(1,41):
        package = packageReference.getItem(i)
        print('Package #: ' + ' ' + str(package.packageID) + ' ' + package.address + ' ' + package.status + ' at ' + str(package.deliveryTime))
        print('Deadline was: ' + package.deadline)
        print('~~~~~')
    print('Total miles for each truck: ')
    print('Truck 1: ' + ' ' + str(int(truck1.mileage)))
    print('Truck 2: ' + ' ' + str(int(truck2.mileage)))
    print('Truck 3: ' + ' ' + str(int(truck3.mileage)))
    print('Total: ' + str(int(truck1.mileage) + int(truck2.mileage) + int(truck3.mileage)))

def packageStatus():
    print('You may search for a single package and get delivery status as of desired time or all package statuses within a time frame.')
    prompt = int(input('Are you looking for one, or multiple packages? (Please enter 1 for 1 package or 2 for multiple): '))
    #searching for one package at a certain time, returns delivery status
    if prompt == 1:
        id = int(input('Please input the package ID you are looking for: '))
        startTime = datetime.strptime(str(input('Please enter the time (24 hour clock HH:MM): ')), '%H:%M')
        if trucksSorted == True:
            box = packageReference.getItem(id)
            time = box.deliveryTime
            t2Start = datetime.strptime(str('09:05'))
            t3Start = datetime.strptime(str('13:00'))
            if startTime.time() < time:
                if box.truckNum == 2 and startTime.time() < t2Start.time():
                    print('Package at Hub. Awaiting departure.')
                elif box.truckNum == 3 and startTime.time() < t3Start.time():
                    print('Package at Hub. Awaiting departure.')
                else:
                    print('\nPackage is on its way! \n')
                    print()
                    print('Package ID: ' + str(box.packageID))
                    print(box.address)
                    print('Delivery Dealine: ' + box.deadline)
                    print(box.notes)    
            else:
                print('\nPackage was delivered at: \n' + time.strftime('%H:%M:%S'))
                print()
                print('Package ID: ' + str(box.packageID))
                print(box.address)
                print('Delivery Dealine: ' + box.deadline)
                print('Special notes: ' + box.notes)
        else:
            print('Plase load the trucks first!')
    #searching for a window of time and returning all packages by truck
    if prompt == 2:
        trucks = [truck1, truck2, truck3]
        startTimeFrame = datetime.strptime(str(input('Please enter the start time (24 hour clock HH:MM): ')), '%H:%M')
        endTimeFrame = datetime.strptime(str(input('Please enter the end time (24 hour clock HH:MM): ')), '%H:%M')
        for truck in trucks:
            print('Truck ' + str(truck.truckNum) + ': \n')
            for box in truck.manifest:
                time = box.deliveryTime
                #if the delivery time is prior to start time print delivered
                if time < startTimeFrame.time():
                    print('Package ' + str(box.packageID) + ' was delivered at: ' + time.strftime('%H:%M:%S'))
                    print('~~~~~')
                elif time < endTimeFrame.time() and time > startTimeFrame.time():
                    print('Package ' + str(box.packageID) + ' expected to be delivered within given time frame.')
                    print('~~~~~')
                elif time > endTimeFrame.time():
                    print('Package ' + str(box.packageID) + ' is out for delivery. Expected later than given time frame.')
                    print('~~~~~')
                    #elif time < startTime.time() and "Delayed" in box.notes:
                     #   print('Package ' + str(box.packageID) + ' may be delayed or set for later delivery today')


def updatePackage():
    #updates address if possible and resorts truck. 
    print('Warning, you can only update a delivery address prior to it being delivered.')
    id = int(input('Please provide package ID from tracking information: '))
    updateAddress = str(input('Please provide the updated address: (i.e. 123 front st)'))
    currTime = datetime.strptime(str(input('Please enter current time (HH:MM): ')), '%H:%M')
    box = packageReference.getItem(id)
    if box.deliveryTime < currTime.time():
        print('Unfortunately, the package was delivered to the address on file. Please file ticket with WGUPS.')
    else:
        #update address for package ID in truck manifest, resort truck, and deliver what hasn't been delivered yet.
        trucks = [truck1, truck2, truck3]
        modBoxList = []
        resortTruck = None
        for truck in trucks:
            for box in truck.manifest:
                if box.packageID == id:
                    box.address = updateAddress
                    resortTruck = truck
                    print('Updating packge information and resorting truck for delivery.')
                    
        count = 0
        for box in resortTruck.manifest:
            time = box.deliveryTime
            if time > currTime.time():
                count += 1
                modBoxList.append(box)
        currTime = resortTruck.manifest[-count].deliveryTime
        try:
            resortTruck.manifest = sorter.truckSorter(modBoxList)
        except:
            print('I\'m sorry. Please verify the validity and format of the address you entered and try again.')
            exit()
        resortTruck.deliverPackages(truck.manifest, currTime.hour, currTime.minute)
        for box in resortTruck.manifest:
            print('Package #: ' + ' ' + str(box.packageID) + ' ' + box.status + ' at ' + str(box.deliveryTime))
            print('~~~~~')
            
        print('Total miles for resorted truck: ' + str(resortTruck.mileage))    
        

#displays menu until you exit.
if __name__=='__main__':
    while(True):
        displayMenu()
        option = ''
        try:
            option = int(input('Enter option number: '))
        except:
            print('Hmmm, I\'m having trouble finding that option, please try another or check your input ...')
        match option:
            case 1:
                try:
                    print('\n' + 'Loading both trucks . . . . .')
                    trucksSorted = True
                    loadTrucks()
                except:
                    print('There seems to have been an error. Please try running the program again and exiting using option 4.')
                    exit()
            case 2:
                try:
                    packageStatus()
                except:
                    exit()
            case 3:
                try:
                    updatePackage()
                except:
                    exit()
            case 4:
                print('Thank you for choosing WGUPS for your delivery needs!')
                print()
                exit()
            case default:
                print('Please choose from the options below: ')

