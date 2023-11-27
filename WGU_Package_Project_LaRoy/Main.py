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
    for i in range(1, 5):
        print(menuOptions.getItem(i))
    print()
    
def loadTrucks():
    #create trucks
    truck1 = trucks.Truck(1)
    truck2 = trucks.Truck(2)
    truck3 = trucks.Truck(3)
    
    sorter.sortPackages(packages)

    from sorter import sortedLoad1, sortedLoad2, sortedLoad3

    #add sorted packages to trucks
    truck1Load = sortedLoad1
    truck2Load = sortedLoad2
    truck3Load = sortedLoad3

    truck1.deliverPackages(truck1Load, 8, 0)
    truck2.deliverPackages(truck2Load, 9, 5)
    truck3.deliverPackages(truck3Load, 13, 0)
    #----should return list of packages with delivered times and time all packages were delivered

    for i in range(1,41):
        package = packageReference.getItem(i)
        print('Package #: ' + ' ' + str(package.packageID) + ' ' + package.status + ' at ' + str(package.deliveryTime))
        print('~~~~~')
        print()
    print('Total miles for each truck: ')
    print('Truck 1: ' + ' ' + str(truck1.mileage) + '\n')
    print('Truck 2: ' + ' ' + str(truck2.mileage) + '\n')
    print('Truck 3: ' + ' ' + str(truck3.mileage) + '\n')

def packageStatus():
    prompt = int(input('Are you looking for one, or multiple pakcages? (Please enter 1 for 1 package or 2 for multiple): '))
    if prompt == 1:
        id = int(input('Please input the package ID you are looking for: '))
        startTime = datetime.strptime(str(input('Please enter the time (HH:MM): ')), '%H:%M')
        if trucksSorted == True:
            box = packageReference.getItem(id)
            time = box.deliveryTime
            print(time)
            if startTime.time() < time:
                print('\nPackage is on its way! \n')
            else:
                print('\nPackage was delivered at: \n' + time.strftime('%H:%M:%S'))
        if prompt == 2:
            return

     #should take time and compare to delivered time, if time is earlier or later display appropriate
     #range should get all statuses during range
     #needs to access global package info 

def updatePackage():
     print('Handle option \'Option 3\'')
     #update address for package ID globally
     #find the truck this package is on
     #resort truck sorter.sortpackages(truckWhatever)
     #call deliver again for that truck

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
                print('\n' + 'Loading both trucks . . . . .')
                trucksSorted = True
                loadTrucks()
            case 2:
                packageStatus()
            case 3:
                updatePackage()
            case 4:
                print('Thank you for choosing WGUPS for your delivery needs!')
                exit()
            case default:
                print('Please choose from the options below: ')

