import matplotlib.pyplot as plt
import math

def getDogAge(age, dog_age, human_age, step=1/12):
    i = 0
    while int(i) < age:
        i += step
        dog_age.append(round(i, 2))
        human_age.append(round(16*math.log(i)+31, 2))


def showGraph(xData, yData, xLabelX, yLabel):
    plt.plot(xData, yData)
    plt.xlabel('Dog age')
    plt.ylabel('Human age')
    plt.suptitle('How old is my dog in human years?')
    plt.show()

def printDogAgeTable(age, xLabelX, yLabel):
    dog_age = []
    human_age = []
    getDogAge(age, dog_age, human_age, 1)

    print("{:<10}".format(xLabelX), "{:<10}".format(yLabel))

    i = 0
    while i < len(dog_age):
        print("{:<10}".format(dog_age[i]), "{:<10}".format(human_age[i]))
        i+=1

def main():
    dog_age = []
    human_age = []
    getDogAge(30, dog_age, human_age)
    printDogAgeTable(30, 'Dog age', 'Human age')
    showGraph(dog_age, human_age, 'Dog age', 'Human age')

if __name__ == '__main__':
    main()