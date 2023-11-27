import csv
import Main

#create data structure (hash table?) for everything in and define package and truck objects
class Package:
    def __init__(self, packageID, address, deadline, notes, deliveryStatus):
        self.packageID = packageID
        self.address = address
        self.deadline = deadline
        self.notes = notes
        self.status = deliveryStatus

#reads in data for packages (I used built-in dictionary for this because the FAQ's said you just can't use them as a hash table which I built elsewhere)
with open("C:/Users/Timla/Documents/WGU/python_projects/WGU_Package_Project_LaRoy/Cleaned_Package_Data.csv", "r") as csvfile:
    packages = Main.HashTable()
    reader = csv.DictReader(csvfile)
    for row in reader:
        #use data to create package object
        newPack = Package(int(row['PackageID']), row['Address'] + ', ' + row['City'] + ', ' + row['State'] + ' ' + row['Zip'], row['DeliveryDeadline'], row['Notes'], None)
        #add object to hashtable
        packages.add(newPack.packageID, newPack)

#-----Tests package upload, insertion into hashtable, and individual package modification-----
print(packages.getList())
print(packages.getPackage(37))
currPackage = packages.getPackage(37)
currPackage.status = 'Out for Delivery'
print(currPackage.status)


#reads in distance data and adds to array only the relevant dstance values from table
with open("C:/Users/Timla/Documents/WGU/python_projects/WGU_Package_Project_LaRoy/Cleaned_Distance_Data.csv", "r") as csvfile:
    tempDistanceData = []
    cleanedDistanceData = []
    reader = csv.reader(csvfile)

    for row in reader:
        tempDistanceData.append(row)
    i = 1
    j = 1
    for i in range(len(tempDistanceData)):
        for k in range(j):
            cleanedDistanceData.append(tempDistanceData[i][k])
        j += 1
cleanedDistanceData.pop(0)  
print(cleanedDistanceData)

#pre-cleaned and sorted by zip-code (should help with efficiency) and special notes

#generate table for distance data

#if special notes say it is delayed or goes in truck 2, it automatically goes in truck two which is going to leave later

#then use something to generate shortest route within each truck
#prioritize delivery deadline and generate shortest route within those, then shortest route from last priority package