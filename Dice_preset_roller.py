from CustomDieAndDiceClassesReal import *

def printLegend():

    print("\n"
          "Legend\n"
          "\n"
          "  Adjusting Presets\n"
          "    1st: The preset\n"
          "    2nd: The action\n"
          "\n"
          "  Misc\n"
          "    F: Free roll\n"
          "    S: Save presets")

def freeRoll():

    dice = []

    average = []

    high = []
    
    printt = False

    while not printt:

        try:

            value = input("Dice: ")

            

            if value == "":
                
                printt = True

            elif value.isdigit():

                value = int(value)

                newVal = CustomDie(value)
                
                dice.append(newVal.value)
                print(" - " + str(newVal.value))

                newCurrAv = value/2 + 0.5
                average.append(newCurrAv)

                high.append(value)

            else:

                raise ValueError

        except ValueError:
            print("Please enter either nothing or an integer")
                

    print("")
    print("Roll: " + str(sum(dice)) + "  { Min: " + str(len(dice)) + ", Max: " + str(sum(high)) + ", Ave: " + str(sum(average)) + "}")
    print("")

def savePresets(presets):

    file_name = input("Name of file: ")

    with open(file_name, "w") as file:

        for preset in presets:

            file.write(preset.name + ", ")

            file.write(str(preset.modifier) + ", ")
            
            for die in preset.presetList:

                file.write(str(die.sides) + ", ")

            file.write("\n")

    with open(file_name, "r") as file:

        contents = file.read()

        print(contents)
            

def loadPresets(presets):

    file_name = input("Name of file: ")

    with open(file_name, "r") as file:

        saved_presets = file.readlines()

        for i, preset in enumerate(saved_presets):

            saved_presets[i] = saved_presets[i].split(", ")

            del saved_presets[i][-1]

        print(saved_presets)

        presets = [DicePreset(), DicePreset(), DicePreset(), DicePreset(), DicePreset(), DicePreset(), DicePreset(), DicePreset(), DicePreset(), DicePreset()]



        print(len(presets[0].presetList))

        print(len(presets[1].presetList))

        print(len(saved_presets))










            
        i = 0
        
        for preset in saved_presets:

            presets[i].name = saved_presets[i][0]

            print("name: " + str(presets[i].name))
            
            presets[i].modifier = int(saved_presets[i][1])

            print("len before: "+ str(len(presets[i].presetList)))

            #print("modifier: " + str(preset1s[i].modifier))

            print(preset)

            if len(saved_presets[i][2:]) > 2:

                dice = saved_presets[i][2:]

                print(dice)
                print("t")

                for die in dice:

                    presets[i].addDie(CustomDie(int(die)))





            
            

            print("len: " + str(len(presets[i].presetList)))
            print("minimum: " + str(presets[i].minimum))
            print("maximum: " + str(presets[i].maximum))
            print("average: " + str(presets[i].average))
            print("total: " + str(presets[i].total))

            for j in presets[i].presetList:

                print("die" + str(j.sides))

                


            i = i + 1

    #presets = [DicePreset(), DicePreset(), DicePreset(), DicePreset(), DicePreset(), DicePreset(), DicePreset(), DicePreset(), DicePreset(), DicePreset()]

            
        

def printPresets(presets):

    index = 0
    
    for dice in presets:

        print("  " + str(index + 1) + ".)", end = "")

        if len(dice.presetList) != 0:
            
            print(dice.name + "\n    { Min: " + str(dice.minimum) + ", Max: " + str(dice.maximum) + ", Ave: " + str(dice.average) + "}")

            #for die in dice.presetList:
                #print( + ", ", end = "")
                
        else:
            print("")

        index = index + 1
        

def roll(presets, selection):

    selection = selection - 1

    if presets[selection].presetList:

        presets[selection].rollAll()

        for die in presets[selection].presetList:

            print("Dice: " + str(die.sides))
            print(" - " + str(die.value))
        
        

        

        print("Roll: " + str(presets[selection].total), end = "")

    else:

        print("Empty preset", end = "")

        
    

def set(presets, selection):

    selection = selection - 1

    presets[selection].reset()

    presets[selection].modifier = 0

    while True:

        try:
        
            diceSize = input("Dice Size: ")

            if diceSize == "":

                returned_modifier = input("Modifier: ")

                if returned_modifier !=  "":

                    presets[selection].modifier = int(returned_modifier)

                returned_name = input("Name: ")

                if returned_name != "":

                    presets[selection].name = returned_name

                break

            elif diceSize.isnumeric():

                presets[selection].addDie(CustomDie(int(diceSize)))

            else:

                raise ValueError

        except ValueError:

            print("Please enter either nothing or an integer")

        

def askWhich(presets):

    while True:

        selection = input("Select: ")
        #selection = [selection[0, -2], selection[-1]]
        print("")

        try:

            if selection[0: -1].isnumeric() or (len(selection) == 1 and selection.isnumeric()):

                if selection.isnumeric():

                    selection = int(selection)

                    roll(presets, selection)

                    break

                elif selection[-1].upper() == "S":

                        selection = int(selection[0:-1])

                        set(presets, selection)

                        break

            elif selection.upper() == "F":

                freeRoll()

                break

            elif selection.upper() == "S":

                savePresets(presets)

                break

            elif selection.upper() == "L":

                loadPresets(presets)

                break

            else:

                raise ValueError


            '''

                    

            if len(selection) == 1:

                if selection.isnumeric():
                
                    selection = int(selection) - 1

                    #presets[selection].rollAll()

                    #print("Roll: " + str(presets[selection].total), end = "")

                    roll(presets, selection)

                    break

                elif selection.upper() == "F":

                    freeRoll()

                    break

                elif selection.upper() == "S":

                    savePresets()
                
            elif len(selection) == 2:

                if selection[1] == "s":
                
                    set(presets, selection)

                    break

            

            else:

                raise ValueError

            '''

        except ValueError:

            print("Check the legend for proper selection format.")

        except IndexError:

            if selection == "":

                print("You must type something before pressing enter.")

            else:

                print("Unknown index error.")

def enterToContinue():

    enter = input()

    print("\n" * 49)
    print("\n" * 49)


def main():
    presets = [DicePreset(), DicePreset(), DicePreset(), DicePreset(), DicePreset(), DicePreset(), DicePreset(), DicePreset(), DicePreset(), DicePreset()]

    while True:

        printLegend()

        print("\n")
        print("Presets")
        print("")
        
        printPresets(presets)

        print("\n")
    
        askWhich(presets)

        #print(presets[0].presetList[0].sides)

        enterToContinue()
        


if __name__ == "__main__":
    main()
