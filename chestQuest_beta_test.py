# ==============================================================================
# Authors: Navid Yoosefi, Methsaan Wickramasinghe 
# File name: chestQuest.py
# Description:
# - Goal is to find treasure chests on an island
# - "hot", "cold", "warm" give hints about where next chest is
# - chests are the easiest to get and abundant source of gold
# - Different weather conditions effect how much the energy is decreased
# - moving around consumes certain amount of health depending on distance
# - healstones increase health but cost money
# - wheels offer a random prize such as health, decreased energy consumption for 10 seconds, and money
# - level resets every 60 seconds - location of wheels, healstones and chests changes
# 600 x 600 px screen
# ==============================================================================

# Importing modules
import random
import math
import time
from graphics import *

# Defining the function dist(x1, y1, x2, y2)
def dist(x1, y1, x2, y2):
    # Process - Calculating the distance and returning the distance given 2 coordinates
    distance = math.sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)
    return distance

# Defining the function lose_energy(energy, distance, energyFactor)
def lose_energy(energy, distance, energyFactor):
    # Process - Take total energy, energy factor and distance moved,
    # and return the amount of energy remaining
    energyLost = distance*energyFactor
    return energy - energyLost

# Defining the function dig_chest(gold)
def dig_chest(gold):
    # Process/Output - Taking the total amount of gold, adding a random amount of gold from
    # 30-40, display message and return total
    goldEarned = random.randint(30, 40)
    print("You earned", goldEarned, "gold!")
    return gold + goldEarned

# Defining the function eval_distance_chest(gold, distanceFromChest)
def eval_distance_chest(gold, distanceFromChest, x, y, win, textObj):
    # Process/Output - hot, warm or cold given distance between player and chest
    # dig chest and return new total if 15 pixels or less, return
    # original amount otherwise
    if distanceFromChest < 30:
        textObj.setText("You found a chest!")
        textObj.setTextColor("chartreuse1")
        print("You found a chest!")
        show_chest(x, y, win)
        return dig_chest(gold)
    elif distanceFromChest < 75:
        textObj.setText("Hot!")
        textObj.setTextColor("blue")
        print("Hot!")
        return gold
    elif distanceFromChest < 180:
        textObj.setText("Warm")
        textObj.setTextColor("blue")
        print("Warm")
        return gold
    else:
        textObj.setText("Cold")
        textObj.setTextColor("blue")
        print("Cold")
        return gold

# Defining the function eval_distance_wheel(gold, energy, energyFactor, distanceFromWheel)
def eval_distance_wheel(gold, energy, energyFactor, distanceFromWheel, wheelSpun, textObj):
    # Process - Spin a the wheel if player 15 pixels away from wheel or less,
    # return new amount of gold, energy and energy factor depending on result
    if distanceFromWheel < 15 and not(wheelSpun):
        spin = spin_wheel(gold, energy, energyFactor, textObj)
        return True, spin[0], spin[1], spin[2], spin[3], spin[4]
    else:
        return False, gold, energy, energyFactor, False, False

# Defining the function eval_distance_healstone(gold, energy, distanceFromHealStone)
def eval_distance_healstone(gold, energy, distanceFromHealStone, textObj):
    # Process - Heal if player is 15 pixels away from healstone or less,
    # return new amount of gold and energy after healing, reduce gold by 15
    if distanceFromHealStone < 15 and gold-30 >= 0:
        return gold-30, heal(energy, textObj)
    elif distanceFromHealStone < 15:
        textObj.setText("You must have 140 gold to purchase the healstone!")
        textObj.setTextColor("red")
        print("You must have 100 gold to purchase the healstone!")
        return gold, energy
    else:
        return gold, energy

# Defining the function spin_wheel(gold, energy, energyFactor)
def spin_wheel(gold, energy, energyFactor, textObj):
    # Setting the wheel as a list with items on the wheel
    wheel = ["40 gold"] + ["10 gold"] * 3 + ["3 gold"] * 5 + \
            ["Power boost"] * 30000 + ["Energy boost"] * 4 + \
            ["Nothing"] * 30 + ["Time boost"] * 6
    powerBoostCounter = 0
    # Process - Generating a wheel spin
    wheelSpin = random.choice(wheel)
    # Process/Output - Return the new amount of gold, energy and energy factor depending on what the wheel landed on
    # with a message that states what they got on the wheel
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

# Defining the function heal(energy)Increase energy, return new total energy
def heal(energy, textObj):
    # Process - Increase the energy and return the new total energy
    textObj.setText("Healing...")
    textObj.setTextColor("chartreuse1")
    time.sleep(3)
    textObj.setText("You earned 15000 energy points")
    print("Healing... You earned 5000 energy points.")
    return energy + 15000

# Defining the function get_coords()
def get_coords(win):
    # Input/Process - While true, read and error check the x and y coordinates from the user
    coord = win.getMouse()
    xCoord = coord.getX()
    yCoord = coord.getY()
    return xCoord, yCoord

# Defining the function generate_cords()
def generate_coords():
    # Process - Generating the x and y coordinates for the chest
    chestx = random.randrange(100, 570)
    chesty = random.randrange(100, 570)
    # Process - Generating healstonex_cord and healstoney_cord
    heal_stonex = random.randrange(100, 600)
    heal_stoney = random.randrange(100, 600)
    # Initializing the variables for the coordinates
    wheelx = -1
    wheely = -1
    xCoords = []
    yCoords = []
    # while the list elements is 0:
    while len(xCoords) == 0:
        # Process - Determining the correct wheel distance
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
            # Process - If not outOfBound, append the elements
            if not outOfBound:
                xCoords.append(wheelx)
                yCoords.append(wheely)
    # Process - Generate xCoords and yCoords and return the coordinates
    wheelx = random.choice(xCoords)
    wheely = yCoords[xCoords.index(wheelx)]
    return chestx, chesty, heal_stonex, heal_stoney, wheelx, wheely

# Defining the function game_over()
def game_over(win):
    gameOverText = Text(Point(300, 300), "GAME OVER")
    gameOverText.setFace("helvetica")
    gameOverText.setTextColor("red")
    gameOverText.setStyle("bold")
    gameOverText.setSize(36)
    gameOverText.draw(win)
    print("Game Over!")

# Defiining the function generate generate_weather()
def generate_weather(energyFactor):
    # Initializing variables
    # 3-10 chance for sunny, 4-10 chance for cloudy, 2-10 chance for rainy, 1-10 chance
    # for thunderstorm
    weather_list = ["Sunny"] *3 + ["Cloudy"] * 4 + ["Rainy"] * 2 + ["Thunderstorm"]
    newEnergyFactor =  energyFactor

    # Generating random weather from list
    weather = random.choice(weather_list)

    # Increase the energy factor by 25-60% based on the weather conditions
    if weather == "Sunny":
        newEnergyFactor *= 1.05
    elif weather == "Rainy":
        newEnergyFactor *= 1.1
    elif weather == "Thunderstorm":
        newEnergyFactor *= 1.15
    else:
        newEnergyFactor *= 1
   
    # Returning weather and energyFactor when the conditions have been exited
    return weather, newEnergyFactor

def make_character(x, y, win):
    waist = Point(x, y-20)
    shoulder = Point(x, y+20)
    headCenter = Point(x, y+27)
    foot1 = Point(x-10, y-30)
    foot2 = Point(x+10, y-30)
    hand1 = Point(x-10, y+20)
    hand2 = Point(x+10, y+20)
    body = Line(waist, shoulder)
    head = Circle(headCenter, 7)
    arms = Line(hand1, hand2)
    leg1 = Line(foot1, waist)
    leg2 = Line(foot2, waist)
    body.draw(win)
    head.draw(win)
    arms.draw(win)
    leg1.draw(win)
    leg2.draw(win)
    head.setFill("black")
    for i in [body, leg1, leg2, arms]:
        i.setWidth(3)
    return [body, head, arms, leg1, leg2]

def make_wheel(x, y, win):
    objects = []
    stand = Rectangle(Point(x-15, y), Point(x+15, y-35))
    stand.setFill("#4d0914")
    stand.setOutline("#4d0914")
    objects.append(stand)
    center = Point(x, y)
    points = []
    xCoords = [math.sqrt(3)/2*25, 0, -math.sqrt(3)/2*25, -math.sqrt(3)/2*25, 0, math.sqrt(3)/2*25]
    yCoords = [1/2*25, 1*25, 1/2*25, -1/2*25, -1*25, -1/2*25]
    stand.draw(win)
    for i in range(6):
        p = Point(x + xCoords[i], y + yCoords[i])
        points.append(p)
    wheel = Circle(center, 25)
    wheel.draw(win)
    wheel.setFill("#ff5349")
    wheel.setOutline("#4d0914")
    objects.append(wheel)
    for i in range(6):
        l = Line(points[i], center)
        objects.append(l)
        l.draw(win)
        l.setOutline("#4d0914")
    return objects

def show_chest(x, y, win):
    front = Rectangle(Point(x-25, y+10), Point(x+25, y-10))
    front.setFill("#a5836c")
    frontBorder = Rectangle(Point(x-27, y+12), Point(x+27, y-12))
    frontBorder.setFill("#5c5f00")
    topBorder = Polygon(Point(x-27, y+12), Point(x+27, y+12), Point(x+20, y+22), Point(x-20, y+22))
    topBorder.setFill("#a5836c")
    top = Polygon(Point(x-25, y+14), Point(x+25, y+14), Point(x+18, y+20), Point(x-18, y+20))
    top.setFill("black")
    keyHole = Rectangle(Point(x-3, y+12), Point(x+3, y+8))
    keyHole.setFill("#5c5f00")
    sprites = [frontBorder, front, topBorder, top, keyHole]
    for i in range(5):
        for j in range(len(sprites)):
            sprites[j].draw(win)
        time.sleep(0.4)
        for j in range(len(sprites)):
            sprites[j].undraw()
        time.sleep(0.2)

def make_healstone(x, y, win):
    outline = Polygon(Point(x+20, y), Point(x, y-30), Point(x-20, y), Point(x-6, y+20), Point(x+9, y+40), Point(x+6, y+20), Point(x+20, y))
    outline.setFill("darkslategray2")
    outline.setOutline("darkslategray4")
    stand = Rectangle(Point(x-15, y), Point(x+15, y-30))
    stand.setFill("black")
    stand.setOutline("black")
    stand2 = Circle(Point(x, y-30), 15)
    stand2.setFill("black")
    stand2.setOutline("black")
    stand.draw(win)
    stand2.draw(win)
    outline.draw(win)
    corners = [Point(x+20, y), Point(x, y-30), Point(x-20, y), Point(x-6, y+20), Point(x+9, y+40), Point(x+6, y+20), Point(x+20, y)]
    l = []
    for i in range(len(corners)):
        l.append(Line(corners[i], Point(x-9, y+3)))
        l[i].setOutline("black")
        l[i].draw(win)
    return [stand, stand2, outline] + l

def create_background(weather, win, weatherList):
    for i in weatherList:
        i.undraw()
    newWeatherList = []
    if weather == "Cloudy":
        win.setBackground("#E3CF57")
    elif weather == "Rainy":
        win.setBackground("darkorange4")
        for i in range(10):
            puddleCenterx = random.randrange(600)
            puddleCentery = random.randrange(600)
            radii1 = random.randrange(25, 100)
            radii2 = random.randrange(25, 100)
            puddle = Oval(Point(puddleCenterx-radii1, puddleCentery-radii2), Point(puddleCenterx+radii1, puddleCentery+radii2))
            puddle.setFill("#3D59AB")
            puddle.setOutline("#3D59AB")
            puddle.draw(win)
            newWeatherList.append(puddle)
        for i in range(500):
            randLocationx = random.randrange(600)
            randLocationy = random.randrange(600)
            raindrop = Circle(Point(randLocationx, randLocationy), 1)
            raindrop.setFill("#5C665E")
            raindrop.setOutline("#5C665E")
            raindrop.draw(win)
            newWeatherList.append(raindrop)
    elif weather == "Thunderstorm":
        win.setBackground("#5E2612")
        for i in range(60):
            puddleCenterx = random.randrange(600)
            puddleCentery = random.randrange(600)
            radii1 = random.randrange(30, 70)
            radii2 = random.randrange(30, 70)
            puddle = Oval(Point(puddleCenterx-radii1, puddleCentery-radii2), Point(puddleCenterx+radii1, puddleCentery+radii2))
            puddle.setFill("#5C665E")
            puddle.setOutline("#5C665E")
            puddle.draw(win)
            newWeatherList.append(puddle)
        for i in range(500):
            randLocationx = random.randrange(600)
            randLocationy = random.randrange(600)
            raindrop = Rectangle(Point(randLocationx-2, randLocationy-2), Point(randLocationx+2, randLocationy+2))
            raindrop.setFill("#3D59AB")
            raindrop.setOutline("#3D59AB")
            raindrop.draw(win)
            newWeatherList.append(raindrop)
    else:
        win.setBackground("orange")
    return newWeatherList

def create_scale(x, y, win, ticks):
    scale = []
    xpointLinex = Point(0,590)
    ypointLinex = Point(600,590)
    xpointLiney = Point(10,0)
    ypointLiney = Point(10, 600)
    lineY = Line(xpointLiney, ypointLiney)
    lineX = Line(xpointLinex, ypointLinex)
    lineX.setWidth(3)
    lineY.setWidth(3)
    lineY.draw(win)
    lineX.draw(win)
    scale.append(lineY)
    scale.append(lineX)
    for i in range(0, 600, ticks):
        tickMarkPointx = Point(i, y)
        tickMarkPointy = Point(i, y - 20)
        tickMarks = Line(tickMarkPointx, tickMarkPointy)
        tickMarks.setWidth(3)
        tickMarks.draw(win)
        num = Text(Point(i, y - 30), str(i))
        num.draw(win)
        scale.append(tickMarks)
        scale.append(num)
    for i in range(0, 600, ticks):
        tickMarkPointx = Point(x, i)
        tickMarkPointy = Point(x + 20, i)
        tickMarks = Line(tickMarkPointx, tickMarkPointy)
        tickMarks.setWidth(3)
        tickMarks.draw(win)
        num = Text(Point(x + 30, i), str(i))
        num.draw(win)
        scale.append(tickMarks)
        scale.append(num)
    return scale
       
def moveObj(x, y, obj):
    for i in obj:
        i.move(x, y)

# Main program
# Initializing the x and y coordiantes, amount of gold, energy, energy factor and level
playerx = 40
playery = 40
playerGold = 0
playerEnergy = 20000
level = 1

# Initializing gameOver and time variables
gameOver = False
t = time.time()
seconds = 0

# Capturing the values of weather and energyFactor
map_weather, playerEnergyFactor = generate_weather(2)

# Process - Capturing the values of the coordinates from total_cords() in the main program
chestx, chesty, healStonex, healStoney, wheelx, wheely = generate_coords()

powerBoostObtained = False
temp = False
powerBoostTime = 0
wheelObtained = False
timeBoostObtained = False
timeLimit = 25
wheelDrawn = True

window = GraphWin("Chest Quest", 600, 600)
window.setCoords(0, 0, 600, 600)

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
Click anywhere to start.
''')
instructions.setSize(20)
instructions.setFace("helvetica")
instructions.setTextColor("red")
header.draw(window)
instructions.draw(window)

window.getMouse()

header.undraw()
instructions.undraw()

weatherSprites = create_background(map_weather, window, [])
player = make_character(playerx, playery, window)
playerWheel = make_wheel(wheelx, wheely, window)
playerHealstone = make_healstone(healStonex, healStoney, window)

gameScale = create_scale(0, 600, window, 50)

weatherText = Text(Point(300, 550), "Weather: " + map_weather)
timeLeftText = Text(Point(300, 530), "Time left: 30s")
levelText = Text(Point(300, 510), "Level " + str(level))
energyText = Text(Point(300, 490), "Energy: " + str(playerEnergy))
goldText = Text(Point(300, 470), "Gold: " + str(playerGold))
tempText = Text(Point(300, 445), "")
infoText = [weatherText, timeLeftText, levelText, energyText, goldText, tempText]
for i in infoText:
    i.setSize(14)
    i.setStyle("bold")
    i.setTextColor("gray10")
    i.setFace("courier")
    i.draw(window)

print("Chest:", chestx, chesty)
print("Wheel: {:.2f}".format(wheelx), "{:.2f}".format(wheely))
print("Healstone:", healStonex, healStoney)
print("Distance: {:.2f}".format(dist(chestx, chesty, wheelx, wheely)))
print("Level:", level)
print("Energy Factor:", playerEnergyFactor)
print("Weather:", map_weather)

# While gameOver = false
while not(gameOver):
    # Process - Capturing the values of the x coordinates and y coordinates
    xMove, yMove = get_coords(window)
    # Process/Output - Creating and printing the timer to count in seconds
    seconds += time.time() - t
    t = time.time()
    timeLeftText.setText("{:.2f}".format(timeLimit - seconds) + "s")
    print("{:.2f}".format(seconds), "s")
    # Process/Output - Determining the distance and coordinates and printing them
    distMoved = dist(playerx, playery, xMove, yMove)
    moveObj(xMove-playerx, yMove-playery, player)
    playerx = xMove
    playery = yMove
    print("Coordinates:", playerx, playery, "Distance moved:", "{:.4f}".format(distMoved))
    playerEnergy = lose_energy(playerEnergy, distMoved, playerEnergyFactor)
    if playerEnergy < 0:
        playerEnergy = 0
    print("Energy: {:.2f}".format(playerEnergy))
    # Process - Capturing the values of the functions
    tempPlayerGold = eval_distance_chest(playerGold, \
                    dist(playerx, playery, chestx, chesty), chestx, chesty, window, tempText)
    if tempPlayerGold > playerGold:
        playerGold = tempPlayerGold
        tempText.setText("")
        tempText.setTextColor("gray10")
        moveObj(40-playerx, 40-playery, player)
        playerx = 40
        playery = 40
        # Process - If the user guesses where the chest is, set up new level
        # Capturing the values of weather and energyFactor
        map_weather, playerEnergyFactor = generate_weather(playerEnergyFactor)
        weatherSprites = create_background(map_weather, window, weatherSprites)
        tempWheelx = wheelx
        tempWheely = wheely
        tempHealstonex = healStonex
        tempHealstoney = healStoney
        wheelx, wheely, chestx, chesty, healStonex, healStoney = generate_coords()
        moveObj(healStonex-tempHealstonex, healStoney-tempHealstoney, playerHealstone)
        for i in player:
            i.undraw()
            i.draw(window)
        for i in playerHealstone:
            i.undraw()
            i.draw(window)
        if not(wheelDrawn):
            for i in playerWheel:
                i.draw(window)
            wheelDrawn = True
        else:
            for i in playerWheel:
                i.undraw()
                i.draw(window)
        moveObj(wheelx-tempWheelx, wheely-tempWheely, playerWheel)

        #Incrememnt level by 1 and playerEnergyFactor by 0.2
        level += 1
        seconds = 0
        t = time.time()
        timeLimit = 30
        playerEnergyFactor += 0.4
        levelText.setText("Level " + str(level))
        weatherText.setText("Weather: " + map_weather)
        for i in infoText:
            i.undraw()
            i.draw(window)
        for i in gameScale:
            i.undraw()
            i.draw(window)
        print("Chest:", chestx, chesty)
        print("Wheel:", wheelx, wheely)
        print("Healstone:", healStonex, healStoney)
        print("Distance:", dist(chestx, chesty, wheelx, wheely))
        print("Level:", level)
        print("Weather:", map_weather)
        # Capturing values of functions
    if not(wheelObtained):
        wheelSpun, playerGold, playerEnergy, playerEnergyFactor, timeBoostObtained, powerBoostObtained = eval_distance_wheel(playerGold, playerEnergy, playerEnergyFactor, dist(playerx, playery, wheelx, wheely), wheelObtained, tempText)
        if wheelSpun:
            wheelObtained = True
            for i in range(len(playerWheel)):
                playerWheel[i].undraw()
            wheelDrawn = False
    if powerBoostObtained and not(temp):
        temp = True
        powerBoostTime = seconds
    elif powerBoostObtained:
        if seconds - powerBoostTime >= 10:
            powerBoostObtained = False
            temp = False
            playerEnergyFactor *= 2

    playerGold, playerEnergy = eval_distance_healstone(playerGold, \
                playerEnergy, dist(playerx, playery, healStonex,\
                healStoney), tempText)
    # Output - For each click, display the amount of energy and gold after all sprites evaluated
    goldText.setText("Gold: " + str(playerGold))
    energyText.setText("Energy: {:.2f}".format(playerEnergy))
    print("Gold:", playerGold)
    print("Energy: {:.2f}".format(playerEnergy))
    print("Energy factor: {:.2f}".format(playerEnergyFactor))

    # Process/Output - If the energy runs out, print the message that the game is over
    if playerEnergy == 0:
        game_over(window)
        gameOver = True

    # Process/Output - If the timer runs out, print the message that they are out of time,
    # reset coordinates
    if timeBoostObtained:
        timeLimit = 40
    # Process/Output - If the timer runs out, print the message that they are out of time,
    # reset coordinates
    if seconds >= timeLimit:
        seconds = 0
        tempWheelx = wheelx
        tempWheely = wheely
        tempHealstonex = healStonex
        tempHealstoney = healStoney
        chestx, chesty, healStonex, healStoney, wheelx, wheely = generate_coords()
        moveObj(40-playerx, 40-playery, player)
        moveObj(healStonex-tempHealstonex, healStoney-tempHealstoney, playerHealstone)
        playerx = 40
        playery = 40
        if not(wheelDrawn):
            for i in range(len(playerWheel)):
                playerWheel[i].draw(window)
            wheelDrawn = True
        moveObj(wheelx-tempWheelx, wheely-tempWheely, playerWheel)
        wheelObtained = False
        tempText.setText("Out of time.")
        tempText.setTextColor("red")
        print("Out of time.")
        print("Chest:", chestx, chesty)
        print("Wheel: {:.2f}".format(wheelx), "{:.2f}".format(wheely))
        print("Healstone:", healStonex, healStoney)
        print("Distance: {:.2f}".format(dist(chestx, chesty, wheelx, wheely)))
        print("Level:", level)
        print("Energy Factor:", playerEnergyFactor)
        print("Weather:", map_weather)

window.getMouse()

window.close()