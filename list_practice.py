print("Hello World")

## Project part 1.3
mattList = ["Matt", "made", "a", "list", "of", "strings"]
print(mattList)

## Project part 1.4
print(mattList[0])

## Project part 1.5
print(mattList[4])

## Project part 1.6
print(len(mattList))

## Project part 1.7
print(mattList[-1])
print(mattList[-6])

## Project part 1.8
#mattList[42]          Error - outside of list range (past 5)

var = -6
print(mattList[var])

## Project part 1.9
print(mattList[0] + mattList[1] + mattList[2])

## Project part 1.10
letters = []
letters += 'Flower'
print(letters)

##numbers = []
##numbers += 123.4      Error - can't iterate through floats

## Project part 1.11
intList = [14, 7, 22, 656, 32, 90, 1417]
bothList = mattList + intList
print(bothList)

## Project part 1.12
for i in range(len(mattList)):
    print(mattList[i])

## Project part 1.13
check = ["Does", "this", "list", "look", "the", "same"]
checkCopy = ["Does", "this", "list", "look", "the", "same"]
notCopy = ["This", "list", "is", "bad"]

print(check == checkCopy) #should be true
print(check == notCopy) #should be false
print(check < notCopy) # should be true
print(notCopy >= checkCopy) # should be true

#Project part 1.14
def cube_list(values):
    for i in range(len(values)):
        values[i] **= 3
        print(values[i])
cubeThis = [2, 4, 6, 8, 10, 20]
cube_list(cubeThis)

#Created by Matt Goeckel, see lists_practice.ipynb for individual outputs.