import random

class CustomDie:
    def __init__(self, sides, value = "none"):
        self.sides = sides
        if value == "none":
            self.__value = random.randrange(1, self.sides + 1)
        else:
            self.__value = value
    
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if (value < 1) or (value > self.sides):
            raise ValueError("Die value must be from 1 to " + str(self.sides))
        else:
            self.__value = value
        

    def roll(self):
        self.__value = random.randrange(1, self.sides + 1)


class DicePreset:
    def __init__(self, presetList = [], modifier = 0, name = ""):
        self.__presetList = presetList
        self.__modifier = modifier
        self.__total = modifier
        self.__average = modifier
        self.__minimum = modifier
        self.__maximum = modifier
        self.__rocks = modifier
        self.name = "blank"

        if self.__presetList:
            
            for die in self.__presetList:
                self.__average = self.__average + (die.sides/2) + 0.5
                self.__minimum = self.__minimum + 1
                self.__maximum = self.__maximum + die.sides
                self.__rocks = self.__rocks + 4

                
        

    @property
    def presetList(self):
        return tuple(self.__presetList)

    @property
    def modifier(self):
        return self.__modifier

    @modifier.setter
    def modifier(self, value):
        self.__total = self.__total - self.__modifier
        self.__average = self.__average - self.__modifier
        self.__minimum = self.__minimum - self.__modifier
        self.__maximum = self.__maximum - self.__modifier
        self.__modifier = value
        self.__total = self.__total + self.__modifier
        self.__average = self.__average + self.__modifier
        self.__minimum = self.__minimum + self.__modifier
        self.__maximum = self.__maximum + self.__modifier

    @property
    def total(self):
        return self.__total

    @property
    def average(self):
        return self.__average

    @property
    def minimum(self):
        return self.__minimum

    @property
    def maximum(self):
        return self.__maximum

    def reset(self):
        self.__presetList = []
        self.__total = self.__modifier
        self.__average = self.__modifier
        self.__minimum = self.__modifier
        self.__maximum = self.__modifier

    def addDie(self, die):
        self.__presetList.append(die)
        self.__total = self.__total + self.__presetList[-1].value
        self.__average = self.__average + (die.sides/2) + 0.5
        self.__minimum = self.__minimum + 1
        self.__maximum = self.__maximum + die.sides       

    def rollAll(self):
        self.__total = self.__modifier

        for die in self.__presetList:
            die.roll()
            self.__total = self.__total + die.value

            
        




