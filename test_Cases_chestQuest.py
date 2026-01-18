# Test Cases:
# Functions were tested from within the functions itself and by the main program

# dist(x1, y1, x2, y2)
def dist(x1, y1, x2, y2):
    distance = math.sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)
    print("the distance is:", distance)
    return distance

# Input - 338.0
# Output - "The distance is:", 338"
# Output - "Distance: 338"
# Pass/Fail - PASS

# Input - 636.0
# Output - "The distance is:", 636.0"
# Output - "Distance: 636.0"
# Pass/Fail - PASS


# lose_energy(energy, distance, energyFactor)
def lose_energy(energy, distance, energyFactor):
    energyLost = distance*energyFactor
    print("energy lost:", energyLost)
    print("new energy:", energy - energyLost)
    return energy - energyLost

# Input - "Distance moved:" - 454.89
# Output - energy lost: 909.78
# Output - new energy: 2590.21
# Output - "Energy: 2590.21"
# Pass/Fail - PASS

# Input - "Distance moved:" - 405.35
# Output - energy lost: 851.24
# Output - new energy: 2648.75
# Output - "Energy: 2648.75"
# Pass/Fail - PASS


# dig_chest(gold)
def dig_chest(gold):
    goldEarned = random.randint(30, 40)
    print("You earned", goldEarned, "gold!")
    print("new gold:", gold + goldEarned)
    return gold + goldEarned

# Chest: 465 456
# Input - "Coordinates: 454.75 462.77"
# Output - "You earned 31 gold!"
# Output - "new gold: 31"
# Output - "Gold: 31"
# Pass/Fail - PASS

# Chest: 158 340
# Input - Coordinates: 158.26 334.55
# Output - "You earned 38 gold!"
# Output - "new gold: 38"
# Output - "Gold: 38"
# Pass/Fail - PASS


# eval_distance_chest(gold, distanceFromChest)
def eval_distance_chest(gold, distanceFromChest, x, y, win, textObj):
    
    if distanceFromChest < 30:
        textObj.setText("You found a chest!")
        textObj.setTextColor("chartreuse1")
        print("You found a chest!")
        print("chest distance:", distanceFromChest)
        show_chest(x, y, win)
        return dig_chest(gold)
    
    elif distanceFromChest < 75:
        textObj.setText("Hot!")
        textObj.setTextColor("blue")
        print("Hot!")
        print("chest distance:", distanceFromChest)
        return gold
    
    elif distanceFromChest < 180:
        textObj.setText("Warm")
        textObj.setTextColor("blue")
        print("Warm")
        print("chest distance:", distanceFromChest)
        return gold
    
    else:
        textObj.setText("Cold")
        textObj.setTextColor("blue")
        print("Cold")
        return goldif distanceFromChest < 15:
        print("You found a chest!")
        print("chest distance:", distanceFromChest)
        return dig_chest(gold)
        
# Chest: 243 565
# Input - "Coordinates: 340.56 380.63"
# Output - "Cold"
# Output - "Chest distance: 208.59"
# Pass/Fail - PASS

# Chest: 368 423
# Input - "Coordinates: 341.56 332.55"
# Output - "Warm"
# Output - "chest distance: 94.23"
# Pass/Fail - PASS

# Chest: 270 522
# Input - "Coordinates: 235.39 512.85"
# Output - "Hot!"
# Output - "chest distance: 35.79"
# Pass/Fail - PASS

# Chest: 173 189
# Input - "Coordinates: 183.30 192.320"
# Output - You found a chest!
# Output - chest distance: 10.82
# Pass/Fail - PASS

# eval_distance_wheel(gold, energy, energyFactor, distanceFromWheel, wheelSpun)
def eval_distance_wheel(gold, energy, energyFactor, distanceFromWheel, wheelSpun, textObj):
    if distanceFromWheel < 15 and not(wheelSpun):
        spin = spin_wheel(gold, energy, energyFactor, textObj)
        print("distance from wheel:", distanceFromWheel, "wheelSpun:", wheelSpun)
        return True, spin[0], spin[1], spin[2], spin[3], spin[4]
    
    else:
        return False, gold, energy, energyFactor, False, False

# Wheel: 514.37 554.28
# Input - "Coordinates: 512.85 552.92"
# Output - "distance from wheel: 2.04 wheelSpun: False"
# Output - "Gold: 0"
# Output - "Energy: 1895.46"
# Output - "Energy factor: 2.30"
# Pass/Fail - PASS

# Wheel: 55.05 528.91
# Input - "Coordinates: 51.085 527.87"
# Output - "distance from wheel 4.10 wheelSpun: False"
# Output - "Gold: 3"
# Output - "Energy: 2377.59"
# Output - "Energy factor: 2.30"
# Pass/Fail - PASS


# eval_distance_healstone(gold, energy, distanceFromHealStone)
def eval_distance_healstone(gold, energy, distanceFromHealStone, textObj):
    if distanceFromHealStone < 15 and gold-30 >= 0:
        print("distance from heal stone:", distanceFromHealStone)
        print("new gold:", gold-30, "heal:", heal(energy)
        return gold-30, heal(energy, textObj)
    
    # Output - Using text graphics to print appropiate messages and setting text colour to red
    elif distanceFromHealStone < 15:
        textObj.setText("You must have 140 gold to purchase the healstone!")
        textObj.setTextColor("red")
        print("You must have 100 gold to purchase the healstone!")
        return gold, energy
    
    else:
        print("distance from heal stone:", distanceFromHealStone)
        print("gold:", gold, "energy:", energy)
        return gold, energy

# Healstone: 171 351
# Input - "Coordinates: 159.26 348.58"
# Output - "distance from heal stone: 11.98"
# Output - "new gold: -30 healed energy: 3124.95"
# Output - "Gold: -15"
# Output - "Energy: 3124.95"
# Pass/Fail - PASS

# Healstone: 150 100
# Input - "Coordinates: 147.24 90.15"
# Output - "distance from heal stone: 10.22"
# Output - "new gold: -30 healed energy: 4116.05"
# Output - "Gold: -15"
# Output - "Energy: "4116.05"
# Pass/Fail - PASS

# Healstone: 376 479
# Input "Coordinates: 371.62"
# Output - "You must have 100 gold to purchase the healstone!"
# Output - Gold: 0
# Pass/Fail - PASS

# spin_wheel(gold, energy, energyFactor, textObj)
def spin_wheel(gold, energy, energyFactor, textObj):

    powerBoostCounter = 0
    
    wheel = ["40 gold"] + ["10 gold"] * 3 + ["3 gold"] * 5 + \
            ["Power boost"] * 3 + ["Energy boost"] * 4 + \
            ["Nothing"] * 30 + ["Time boost"] * 6
    
    wheelSpin = random.choice(wheel)

    print("You landed on", wheelSpin)
    
    if wheelSpin == "40 gold":
        textObj.setText("You earned 40 gold.")
        textObj.setTextColor("blue")
        print("You earned 40 gold.")
        return [gold + 40, energy, energyFactor, False, False]
    
    elif wheelSpin == "10 gold":
        textObj.setText("You earned 10 gold.")
        textObj.setTextColor("blue")
        print("You earned 10 gold.")
        return [gold + 10, energy, energyFactor, False, False]
    
    elif wheelSpin == "3 gold":
        textObj.setText("You earned 3 gold.")
        textObj.setTextColor("blue")
        print("You earned 3 gold.")
        return [gold + 3, energy, energyFactor, False, False]
    
    elif wheelSpin == "Power boost":
        textObj.setText("You earned a 15-second power boost.\nYour movement will use 10 times less energy.")
        textObj.setTextColor("blue")
        powerBoostCounter += 1
        print("You earned 15 seconds of power boost. Your movement will use 10 times less energy than usual.")
        return [gold, energy, energyFactor / 10, False, True]
    
    elif wheelSpin == "Energy boost":
        textObj.setText("You earned 5000 energy points.")
        textObj.setTextColor("blue")
        print("You earned 5000 energy points.")
        return [gold, energy + 5000, energyFactor, False, False]
    
    elif wheelSpin == "Time boost":
        textObj.setText("You earned 15 extra seconds.")
        textObj.setTextColor("blue")
        print("You earned 15 extra seconds.")
        return [gold, energy, energyFactor, True, False]
    
    else:
        textObj.setText("You get nothing!")
        textObj.setTextColor("red")
        print("You get nothing!")
        return [gold, energy, energyFactor, False, False]

# Wheel: 194.10 447.07
# Input - "Coordinates: 194.32"
# Output - "You landed on 3 gold"
# Output - "You earned 3 gold."
# Output - "Gold: 3"
# Pass/Fail - PASS

# Wheel: 267 503.07
# Input - "Coordinates: 266"
# Output - "You landed on 40 gold"
# Output - "You earned 40 gold."
# Output - "Gold: 40"
# Pass/Fail - PASS

# Wheel: 109 87.99
# Input - "Coordinates: 108.88"
# Output - "You landed on 10 gold"
# Output - "You earned 10 gold."
# Output - "Gold: 10"
# Pass/Fail - PASS

# Wheel: 597.59 8.24
# Input - "Coordinates: 593.99"
# Output - "You landed on Energy boost"
# Output - "You earned 5000 energy points."
# Output - "Energy: 23890.71"
# Pass/Fail - PASS

# Wheel: 3.12 239.33
# Input - "Coordinates: 12.02"
# Output - "You landed on Power boost"
# Output - "You earned 15 seconds of power boost. Your movement will use 10 times less energy than usual."
# Output - "Energy: 19615.14"
# Input - "Coordinates: 314.52"
# Output - "Energy: 19548.54"
# Pass/Fail - PASS

# Wheel: 515 14.10
# Input - "Coordinates: 514.86"
# Output - "You landed on Time Boost"
# Output - "You earned 15 extra seconds"
# Pass/Fail - PASS

# Wheel: 20.73 596.53
# Input "Coordinates: 511.85"
# Output - "You landed on Nothing"
# Output - "You get Nothing!"
# Pass/Fail - PASS


# Def heal(energy, textObj)
def heal(energy, textObj):

    textObj.setText("Healing...")
    textObj.setTextColor("chartreuse1")
    
    time.sleep(3)
    textObj.setText("You earned 15000 energy points")
    print("Healing... You earned 15000 energy points.")
    
    return energy + 15000

# Healstone: 151 335
# Input "Coordinates: 151.25"
# Output - "Energy: 4926.37"
# Output - "Healing... You earned 15000 energy points."
# Output - "Energy: 19926.37"
# Output - "Gold: 110"
# Pass/Fail - PASS


# def game_over
def game_over(win):
    gameOverText = Text(Point(300, 300), "GAME OVER")
    gameOverText.setFace("helvetica")
    gameOverText.setTextColor("red")
    gameOverText.setStyle("bold")
    gameOverText.setSize(36)
    gameOverText.draw(win)
    print("Game Over!")

# Input - 522.87
# Output - Energy: 0.00
# Output - Game Over!
# Pass/Fail - PASS

#def generate_cords()
def generate_coords():
    
    chestx = random.randrange(100, 570)
    chesty = random.randrange(100, 570)
    heal_stonex = random.randrange(100, 600)
    heal_stoney = random.randrange(100, 600)
    wheelx = -1
    wheely = -1
    xCoords = []
    yCoords = []
    
    while len(xCoords) == 0:
        wheel_distance = random.randrange(300, 848)
        for i in range(360):
            
            if i == 90:
                wheelx = chestx
                wheely = chesty + wheel_distance
                
            elif i == 180:
                wheelx = chestx - wheel_distance
                wheely = chesty
                
            elif i == 270:
                wheelx = chestx
                wheely = chesty - wheel_distance
                
            else:
                wheelx = chestx + wheel_distance*math.cos(math.radians(i))
                wheely = chesty + wheel_distance*math.sin(math.radians(i))
            outOfBound = wheelx < 0 or wheely < 0 or wheelx > 600 or wheely > 600
            
            if not outOfBound:
                xCoords.append(wheelx)
                yCoords.append(wheely)
                
    wheelx = random.choice(xCoords)
    wheely = yCoords[xCoords.index(wheelx)]
    print("Chest x:", chestx, "Chest y:", chesty)
    print("Wheel x: {:.2f}".format(wheelx), "Wheel y: {:.2f}".format(wheely))
    print("Healstone x:", heal_stonex, "Healstone y", heal_stoney)
    return chestx, chesty, heal_stonex, heal_stoney, wheelx, wheely

# Input - "Coordinates: "41.07"
# Output - "Wheel x: 45.67 Wheel y: 27.13"
# Output - "You get nothing!"
# Pass/Fail - PASS

# Input - "Coordinates: 534.89"
# Output - "Healstone x: 540 Healstone y 304"
# Output - "Healing... You earned 15000 energy points."
# Output - "Gold: 110"
# Output - "Energy: 33880.53"
# Pass/Fail - PASS

# Input - "Coordinates: 500"
# Output - "Chest x: 504 Chest y: 128"
# Output - "You found a chest!
# Output - "You earned 37 gold!"
# Output - "Chest x: 136 Chest y: 138"
# Pass/Fail - PASS


# Def get_coords(win)
def get_coords(win):
    
    coord = win.getMouse()
    xCoord = coord.getX()
    yCoord = coord.getY()
    return xCoord, yCoord

# Input - 362.60
# Output - "Coordinates: 362.60"
# Pass/Fail - PASSED

# Input - 538.90
# Output - "Coordinates: 538.90"
# Pass/Fail - PASSED


#def generate_weather(energyFactor)
def generate_weather(energyFactor):
    weather_list = ["Sunny"] * 3 + ["Cloudy"] * 4 + ["Rainy"] * 2 + ["Thunderstorm"] * 1
    newEnergyFactor = energyFactor
    weather = random.choice(weather_list)
    print("weather", weather)

    if weather == "Sunny":
        newEnergyFactor *= 1.05
        print("new energy factor:", newEnergyFactor)
    elif weather == "Rainy":
        newEnergyFactor *= 1.1
        print("new energy factor:", newEnergyFactor)
    elif weather == "Thunderstorm":
        newEnergyFactor *= 1.15
        print("new energy factor:", newEnergyFactor)
    else:
        newEnergyFactor *= 1
        print("new energy factor:", newEnergyFactor)
    
    return weather, newEnergyFactor

# Input - "Coordinates: 351.59"
# Output - "weather Sunny"
# Output - "new energy factor: 2.1"
# Output - "Energy factor: 2.10"
# Output - "Energy: 18983.09"
# Pass/Fail - PASS

# Input - "Coordinates: 349.58"
# Output - "weather Cloudy"
# Output - "new energy factor: 2.00"
# Output - "Energy factor: 2"
# Output - "Energy: 19134.23"
# Pass/Fail - PASS

# Input - "Coordinates: 392.65"
# Output - "weather Rainy"
# Output - "new energy factor: 2.2"
# Output - "Energy factor: 2.2"
# Output - "Energy: 18800.60"
# Pass/Fail - PASS

# Input - "Coordinates: 365.61"
# Output - "weather Thunderstorm"
# Output - "new energy factor: 2.3"
# Output - "Energy factor: 2.3"
# Output - "Energy: 18772.66"
# Pass/Fail - PASS


#def instructions(win)
def instructions(win):
    
    window.setBackground("#53CDA5")
    header = Text(Point(300, 500), "Welcome to Chest Quest!")
    header.setSize(30)
    header.setStyle("bold")
    header.setFace("courier")
    header.setTextColor("blue")
    
    instructions = Text(Point(300, 300), '''Click around to find hidden chests and earn gold.
    Use space wisely! Moving around consumes energy.
    Healstones increase energy, but cost 140 gold.
    Wheels offer gold, energy, time and other prizes (sometimes).
    Out of time = restart level
    Out of energy = game over
    Click anywhere to start. ''')
    
    instructions.setSize(16)
    instructions.setFace("helvetica")
    instructions.setTextColor("red")
    header.draw(window)
    instructions.draw(window)
    window.getMouse()
    header.undraw()
    instructions.undraw()

# Input - Mouse click
# Output - Game Screen
# Pass/Fail - PASS