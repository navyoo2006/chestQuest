# ==============================================================================
# Authors: Navid Yoosefi, Methsaan Wickramasinghe 
# File name: chestQuest.pyw
# Description:
# - Goal is to find treasure chests on an island
# - "hot", "cold", "warm" give hints about where next chest is
# - chests are the easiest to get and abundant source of gold
# - Different weather conditions effect how much the energy is decreased
# - moving around consumes certain amount of health depending on distance
# - healstones increase health but cost 140 gold
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
    
    # Process - Take total energy, energy factor and distance moved, calculate energyLost
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


# Defining the function eval_distance_chest(gold, distanceFromChest, x, y, win, textObj)
def eval_distance_chest(gold, distanceFromChest, x, y, win, textObj):
    
    # Process/Output - Using text graphics to print hot, warm, cold or chest found given distance
    # between player and chest dig chest and return new total if 15 pixels or less, return
    # original amount otherwise
    if distanceFromChest < 30:
        textObj.setText("You found a chest!")
        textObj.setTextColor("chartreuse1")
        print("You found a chest!")
        
        # Process/Output - Calling upon show_chest, Showing the chest once it is found
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


# Defining the function eval_distance_wheel(gold, energy, energyFactor, distanceFromWheel, wheelSpun, textObj)
def eval_distance_wheel(gold, energy, energyFactor, distanceFromWheel, wheelSpun, textObj):
    
    # Process - Spin the wheel, if player 15 pixels away from wheel or less,
    # return new amount of gold, energy and energy factor and textObj depending on condition
    if distanceFromWheel < 15 and not(wheelSpun):
        spin = spin_wheel(gold, energy, energyFactor, textObj)
        return True, spin[0], spin[1], spin[2], spin[3], spin[4]
    
    else:
        return False, gold, energy, energyFactor, False, False


# Defining the function eval_distance_healstone(gold, energy, distanceFromHealStone)
def eval_distance_healstone(gold, energy, distanceFromHealStone, textObj):
    
    # Process - Heal if player is 15 pixels away from healstone or less,
    # return new amount of gold, energy and/or text after healing, reduce gold by 15
    if distanceFromHealStone < 15 and gold-30 >= 0:
        return gold-30, heal(energy, textObj)
    
    # Output - Using text graphics to print appropiate messages and setting text colour to red
    elif distanceFromHealStone < 15:
        textObj.setText("You must have 140 gold to purchase the healstone!")
        textObj.setTextColor("red")
        print("You must have 100 gold to purchase the healstone!")
        return gold, energy
    
    else:
        return gold, energy


# Defining the function spin_wheel(gold, energy, energyFactor, textObj)
def spin_wheel(gold, energy, energyFactor, textObj):

    # Initializing powerBoostCounter
    powerBoostCounter = 0
    
    # Setting the wheel as a list with items on the wheel
    wheel = ["40 gold"] + ["10 gold"] * 3 + ["3 gold"] * 5 + \
            ["Power boost"] * 3 + ["Energy boost"] * 4 + \
            ["Nothing"] * 30 + ["Time boost"] * 6
    
    # Process - Generating a wheel spin
    wheelSpin = random.choice(wheel)
    
    # Process/Output - Return the new amount of gold, energy, energy factor and other values depending on
    # what the wheel landed on (ex. 40 gold, 10 gold, 3 gold...) with a message that states what they got on
    # the wheel using text graphics
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


# Defining the function heal(energy, textObj)
def heal(energy, textObj):
    
    # Output - Using text graphics to print healing and how many energy points earned
    textObj.setText("Healing...")
    textObj.setTextColor("chartreuse1")
    
    # Output - Allowing a 3 second gap between messages
    time.sleep(3)
    textObj.setText("You earned 15000 energy points")
    print("Healing... You earned 15000 energy points.")
    
    # Process - Increase the energy and return the new total energy
    return energy + 15000


# Defining the function get_coords(win)
def get_coords(win):
    
    # Input/Process - Get and return the x and y coordinates from the user on mouse click
    coord = win.getMouse()
    xCoord = coord.getX()
    yCoord = coord.getY()
    return xCoord, yCoord


# Defining the function generate_cords()
def generate_coords():
    
    # Process - Generating the x and y coordinates for the chest
    chestx = random.randrange(100, 570)
    chesty = random.randrange(100, 570)
    
    # Process - Generating heal_stonex and heal_stoney
    heal_stonex = random.randrange(100, 600)
    heal_stoney = random.randrange(100, 600)
    
    # Initializing the variables for the coordinates
    wheelx = -1
    wheely = -1
    xCoords = []
    yCoords = []
    
    # Process - while the list elements is 0:
    while len(xCoords) == 0:
        
        # Process - Generating the wheel distance and determining the correct wheel distance
        # using a loop, conditions and calculations
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

            # Process - Setting out of bound as coords less than 0 or greater than 600
            outOfBound = wheelx < 0 or wheely < 0 or wheelx > 600 or wheely > 600
            
            # Process - If not outOfBound, append the elements
            if not outOfBound:
                
                xCoords.append(wheelx)
                yCoords.append(wheely)
                
    # Process - Determine the values of wheelx and wheely and return all the coordinates at the end
    wheelx = random.choice(xCoords)
    wheely = yCoords[xCoords.index(wheelx)]
    
    return chestx, chesty, heal_stonex, heal_stoney, wheelx, wheely


# Defining the function game_over(win)
def game_over(win):
    
    # Output - Using text graphics to print "GAME OVER" with different colours, fonts...
    gameOverText = Text(Point(300, 300), "GAME OVER")
    gameOverText.setFace("helvetica")
    gameOverText.setTextColor("red")
    gameOverText.setStyle("bold")
    gameOverText.setSize(36)
    gameOverText.draw(win)
    print("Game Over!")


# Defining the function generate generate_weather(energyFactor)
def generate_weather(energyFactor):
    
    # 3-10 chance for sunny, 4-10 chance for cloudy, 2-10 chance for rainy, 1-10 chance
    # for thunderstorm
    weather_list = ["Sunny"] * 3 + ["Cloudy"] * 4 + ["Rainy"] * 2 + ["Thunderstorm"] * 1

    # Setting newEnergyFactor equal to energyFactor
    newEnergyFactor = energyFactor

    # Generating random weather from list
    weather = random.choice(weather_list)
    
    # Increase newEnergyFactor by 5% to 15% or keeping it the same based on the weather conditions
    if weather == "Sunny":
        newEnergyFactor *= 1.05
        
    elif weather == "Rainy":
        newEnergyFactor *= 1.1
        
    elif weather == "Thunderstorm":
        newEnergyFactor *= 1.15
        
    else:
        newEnergyFactor *= 1
        
    # Process - Returning weather and newEnergyFactor when the conditions have been exited
    return weather, newEnergyFactor


# Defining the function make_character(x, y, win)
def make_character(x, y, win):

    # Process - Creating the points for the character
    waist = Point(x, y-20)
    shoulder = Point(x, y+20)
    headCenter = Point(x, y+27)
    foot1 = Point(x-10, y-30)
    foot2 = Point(x+10, y-30)
    hand1 = Point(x-10, y+20)
    hand2 = Point(x+10, y+20)

    # Process - Creating the head of the character
    head = Circle(headCenter, 7)
    
    # Process - Creating the line to connect the points for the characters body
    body = Line(waist, shoulder)
    arms = Line(hand1, hand2)
    leg1 = Line(foot1, waist)
    leg2 = Line(foot2, waist)

    # Output - Drawing the body parts of the character
    body.draw(win)
    head.draw(win)
    arms.draw(win)
    leg1.draw(win)
    leg2.draw(win)

    # Output - Filling the characters head with black
    head.setFill("black")

    # Process - Using a loop to set the width of the body, legs and arms
    for i in [body, leg1, leg2, arms]:
        i.setWidth(3)

    # Process - Returning the character at the end
    return [body, head, arms, leg1, leg2]


# Defining the function make_wheel(x, y, win)
def make_wheel(x, y, win):

    # Initializing objects, center and points
    objects = []
    center = Point(x, y)
    points = []
    
    # Process/Output - Creating the stand, setting the colours and appending
    # it to the objects list, drawing it afterwards
    stand = Rectangle(Point(x-15, y), Point(x+15, y-35))
    stand.setFill("#4d0914")
    stand.setOutline("#4d0914")
    objects.append(stand)
    stand.draw(win)
    
    # Process - Creating the segments on the wheel using trigonomotry and the unit circle,
    # defining them as xCoords and yCoords
    xCoords = [math.sqrt(3)/2*25, 0, -math.sqrt(3)/2*25, -math.sqrt(3)/2*25, 0, math.sqrt(3)/2*25]
    yCoords = [1/2*25, 1*25, 1/2*25, -1/2*25, -1*25, -1/2*25]

    # Process - Defining p as a point and appending it to points, within a loop 6 times
    for i in range(6):
        p = Point(x + xCoords[i], y + yCoords[i])
        points.append(p)

    # Process/Output - Creating the wheel, appending it to objects and drawing it with colour
    wheel = Circle(center, 25)
    wheel.setFill("#ff5349")
    wheel.setOutline("#4d0914")
    objects.append(wheel)
    wheel.draw(win)
    
    # Process/Output - Creating 6 lines, appending it to objects and drawing it with colour
    for i in range(6):
        l = Line(points[i], center)
        objects.append(l)
        l.setOutline("#4d0914")
        l.draw(win)

    # Process - Returning objects at the end
    return objects


# Defining the function show_chest(x, y, win)
def show_chest(x, y, win):

    # Process - Creating the front and front border of the chest with a filled colours
    front = Rectangle(Point(x-25, y+10), Point(x+25, y-10))
    front.setFill("#a5836c")
    frontBorder = Rectangle(Point(x-27, y+12), Point(x+27, y-12))
    frontBorder.setFill("#5c5f00")

    # Process - Creating the top and top border of the chest with filled colours
    topBorder = Polygon(Point(x-27, y+12), Point(x+27, y+12), Point(x+20, y+22), Point(x-20, y+22))
    topBorder.setFill("#a5836c")
    top = Polygon(Point(x-25, y+14), Point(x+25, y+14), Point(x+18, y+20), Point(x-18, y+20))
    top.setFill("black")

    # Process - Creating the keyhole of the chest with a yellow-like colour
    keyHole = Rectangle(Point(x-3, y+12), Point(x+3, y+8))
    keyHole.setFill("#5c5f00")

    # Storing the graphics of the chest into a list called sprites
    sprites = [frontBorder, front, topBorder, top, keyHole]

    # Process/Output - Flashing the chest using draw/undraw, a nested loop and time.sleep
    for i in range(5):
        for j in range(len(sprites)):
            sprites[j].draw(win)
        time.sleep(0.4)
        for j in range(len(sprites)):
            sprites[j].undraw()
        time.sleep(0.2)


# Defining the function make_healstone(x, y, win)
def make_healstone(x, y, win):

    # Initializing l as an empty list
    l = []
    
    # Process - Creating the outline of the healstone with colour, using the necessary points 
    outline = Polygon(Point(x+20, y), Point(x, y-30), Point(x-20, y), Point(x-6, y+20), Point(x+9, y+40), Point(x+6, y+20), Point(x+20, y))
    outline.setFill("darkslategray2")
    outline.setOutline("darkslategray4")

    # Process - Creating the stand of the healstone with black colour
    stand = Rectangle(Point(x-15, y), Point(x+15, y-30))
    stand.setFill("black")
    stand.setOutline("black")

    # Process - Creating the second stand for the healstone with black colour
    stand2 = Circle(Point(x, y-30), 15)
    stand2.setFill("black")
    stand2.setOutline("black")

    # Output - drawing the stands and the outline of the healstone
    stand.draw(win)
    stand2.draw(win)
    outline.draw(win)

    # Process - Creating the corners of the healstone using necessary points
    corners = [Point(x+20, y), Point(x, y-30), Point(x-20, y), Point(x-6, y+20), Point(x+9, y+40), Point(x+6, y+20), Point(x+20, y)]

    # Process/Output - Creating the lines to connect the corners for the healstone, drawing the black coloured lines
    for i in range(len(corners)):
        
        l.append(Line(corners[i], Point(x-9, y+3)))
        l[i].setOutline("black")
        l[i].draw(win)

    # Process - Returning the heal stone graphics as a list + 1
    return [stand, stand2, outline] + l


#Defining the function create_background(weather, win, weatherList)
def create_background(weather, win, weatherList):

    # Initializing newWeatherList as an empty list
    newWeatherList = []
    
    # Process/Output - Undrawing prior weather graphics
    for i in weatherList:
        i.undraw()

    # Process - Determining the background colour if the weather is cloudy 
    if weather == "Cloudy":
        win.setBackground("#E3CF57")

    # Process - If the weather is "Rainy", aet the background colour to dark orange
    elif weather == "Rainy":
        win.setBackground("darkorange4")

        # Process - Generating 10 puddles given the generated centers and radiis, points and shapes
        # afterwards setting the colours
        for i in range(10):
            puddleCenterx = random.randrange(600)
            puddleCentery = random.randrange(600)
            
            radii1 = random.randrange(25, 100)
            radii2 = random.randrange(25, 100)
            
            puddle = Oval(Point(puddleCenterx-radii1, puddleCentery-radii2), Point(puddleCenterx+radii1, puddleCentery+radii2))

            puddle.setFill("#3D59AB")
            puddle.setOutline("#3D59AB")

            # Process/Output - Drawing the puddles and appending it to newWeatherList
            puddle.draw(win)
            newWeatherList.append(puddle)

        # Process - Generating 500 raindrops given the generated locations, created points and shapes
        # afterwards setting the colours
        for i in range(500):
        
            randLocationx = random.randrange(600)
            randLocationy = random.randrange(600)
            
            raindrop = Circle(Point(randLocationx, randLocationy), 1)
            
            raindrop.setFill("#5C665E")
            raindrop.setOutline("#5C665E")

            # Process/Output - Drawing the raindrops and appending them to newWeatherList
            raindrop.draw(win)
            newWeatherList.append(raindrop)

    # Process - If the weather is "thunderstorm", change the background colour
    elif weather == "Thunderstorm":
        win.setBackground("#5E2612")

        # Process - Generating 60 puddles given the generated centers and radiis, points and shapes
        # afterwards setting different colours than rainy puddles
        for i in range(60):
        
            puddleCenterx = random.randrange(600)
            puddleCentery = random.randrange(600)
            
            radii1 = random.randrange(30, 70)
            radii2 = random.randrange(30, 70)
            
            puddle = Oval(Point(puddleCenterx-radii1, puddleCentery-radii2), Point(puddleCenterx+radii1, puddleCentery+radii2))
            puddle.setFill("#5C665E")
            puddle.setOutline("#5C665E")

            # Process/Output - Drawing the puddles and appending them to newWeatherList
            puddle.draw(win)
            newWeatherList.append(puddle)

        # Process - Generating 500 raindrops given the generated locations, created points and shapes
        # afterwards setting the colours  
        for i in range(500):
            
            randLocationx = random.randrange(600)
            randLocationy = random.randrange(600)

            # Process - Creating rectangle raindrops with necessary points to make them larger 
            raindrop = Rectangle(Point(randLocationx-2, randLocationy-2), Point(randLocationx+2, randLocationy+2))
            
            raindrop.setFill("#3D59AB")
            raindrop.setOutline("#3D59AB")

            # Process/Output - Drawing the raindrops and appending them to newWeatherList
            raindrop.draw(win)
            newWeatherList.append(raindrop)
            
    # Process - Otherwise, if the weather is sunny, set the background to orange
    else:
        win.setBackground("orange")

    # Process - Return newWeatherList at the end
    return newWeatherList


# Defining the function create_scale(x, y, win, ticks)
def create_scale(x, y, win, ticks):
    # Defining scale as an empty list
    scale = []

    # Process - Creating the x and y points of the scale
    xpointLinex = Point(0,590)
    ypointLinex = Point(600,590)
    xpointLiney = Point(10,0)
    ypointLiney = Point(10, 600)

    # Process - Creating the scale by drawing a line to connect the points
    lineY = Line(xpointLiney, ypointLiney)
    lineX = Line(xpointLinex, ypointLinex)

    # Process - Setting the thickness of the scale as 3
    lineX.setWidth(3)
    lineY.setWidth(3)

    # Process/Output - Drawing the scales and appending them to scale
    lineY.draw(win)
    lineX.draw(win)
    scale.append(lineY)
    scale.append(lineX)

    # Process - Creating the tick marks for the x-axis of the scale using a loop
    for i in range(0, 600, ticks):

        # Process - Creating the points for the tick marks
        tickMarkPointx = Point(i, y)
        tickMarkPointy = Point(i, y - 20)

        # Process - Creating the line to connect the tick marks given the points
        tickMarks = Line(tickMarkPointx, tickMarkPointy)

        # Process/Output - Setting the thickness of the tick marks as 3 and drawing them
        tickMarks.setWidth(3)
        tickMarks.draw(win)

        # Process/Output - Creating the text for the x-axis tick mark numbers, appending
        # tickMarks and num to scale and drawing the numbers for the tick marks
        num = Text(Point(i, y - 30), str(i))
        scale.append(tickMarks)
        scale.append(num)
        num.draw(win)
        
    # Process - Creating the tick marks for the y-axis of the scale using a loop
    for i in range(0, 600, ticks):

        # Process - Creating the points for the tick marks
        tickMarkPointx = Point(x, i)
        tickMarkPointy = Point(x + 20, i)

        # Process - Creating the line to connect the tick marks given the points
        tickMarks = Line(tickMarkPointx, tickMarkPointy)

        # Process/Output - Setting the thickness of the tick marks as 3 and drawing them
        tickMarks.setWidth(3)
        tickMarks.draw(win)

        # Process/Output - Creating the text for the y-axis tick mark numbers, appending
        # tickMarks and num to scale and drawing the numbers for the tick marks
        num = Text(Point(x + 30, i), str(i))
        scale.append(tickMarks)
        scale.append(num)
        num.draw(win)
        
    # Process - Returning the scale at the end
    return scale

#Defining the function instructions(win)
def instructions(win):
    
    # Process  - Setting the background colour of the window
    window.setBackground("#53CDA5")

    # Process - Creating the text for the welcome message header with the necessary point
    header = Text(Point(300, 500), "Welcome to Chest Quest!")

    # Process - Setting the size, font, colour and properties of the header
    header.setSize(30)
    header.setStyle("bold")
    header.setFace("courier")
    header.setTextColor("blue")

    # Process - Creating the text for the instructions with the necessary point
    instructions = Text(Point(300, 300), '''Click around to find hidden chests and earn gold.
    Use space wisely! Moving around consumes energy.
    Healstones increase energy, but cost 140 gold.
    Wheels offer gold, energy, time and other prizes (sometimes).
    Out of time = restart level
    Out of energy = game over
    Click anywhere to start. ''')

    # Process - Setting the size, font and colour of the instructions 
    instructions.setSize(16)
    instructions.setFace("helvetica")
    instructions.setTextColor("red")

    # Output - Drawing the header and the instructions onto the screen
    header.draw(window)
    instructions.draw(window)

    # Input/Output - On mouse click, undraw the instructions and the header
    window.getMouse()
    header.undraw()
    instructions.undraw()

# Defining the function moveObj(x, y, obj)
def moveObj(x, y, obj):

    # Process - Moving the objects to given x, y coordinates
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

# Initializing more variables
powerBoostObtained = False
temp = False
powerBoostTime = 0
wheelObtained = False
timeBoostObtained = False
timeLimit = 25
wheelDrawn = True

# Process - Capturing the values of weather and energyFactor, passing in argument of
# 2 in for generate_weather
map_weather, playerEnergyFactor = generate_weather(2)

# Process - Capturing the values of the coordinates from generate_coords()
chestx, chesty, healStonex, healStoney, wheelx, wheely = generate_coords()

# Input/Process - Creating the window and setting the coordinates of the window for the graphics
window = GraphWin("Chest Quest", 600, 600)
window.setCoords(0, 0, 600, 600)

# Process - Calling upon the function instructions with window passed in as the argument
instructions(window)

# Process - Capturing the sprites from the respective functions
weatherSprites = create_background(map_weather, window, [])
player = make_character(playerx, playery, window)
playerWheel = make_wheel(wheelx, wheely, window)
playerHealstone = make_healstone(healStonex, healStoney, window)

# Process - Capturing the sprites and passing in the necessary arguments
gameScale = create_scale(0, 600, window, 50)

# Process - Creating the in-game texts to display the necessary variables on-screen
weatherText = Text(Point(300, 550), "Weather: " + map_weather)
timeLeftText = Text(Point(300, 530), "Time left: 30s")
levelText = Text(Point(300, 510), "Level " + str(level))
energyText = Text(Point(300, 490), "Energy: " + str(playerEnergy))
goldText = Text(Point(300, 470), "Gold: " + str(playerGold))
tempText = Text(Point(300, 445), "")

# Setting infoText as a list with the in-game texts defined above
infoText = [weatherText, timeLeftText, levelText, energyText, goldText, tempText]

# Process/Output - Setting the size, colour and properties of each of the in-game texts and drawing them
for i in infoText:
    i.setSize(14)
    i.setStyle("bold")
    i.setTextColor("gray10")
    i.setFace("courier")
    i.draw(window)

# While gameOver = false
while not(gameOver):
    
    # Process - Capturing the values of the users x coordinates and y coordinates and passing in window as the argument
    xMove, yMove = get_coords(window)
    
    # Process/Output - Creating the timer to count in seconds and using the
    # text graphics to print it to the screen
    seconds += time.time() - t
    t = time.time()
    timeLeftText.setText("{:.2f}".format(timeLimit - seconds) + "s")
    print("{:.2f}".format(seconds), "s")

    
    # Process/Output - Determining the distance moved by the user and the amount to move
    # by capturing the values of dist and moveObj
    distMoved = dist(playerx, playery, xMove, yMove)
    moveObj(xMove-playerx, yMove-playery, player)

    # Setting playerx as xMove and playery as yMove
    playerx = xMove
    playery = yMove

    # Output - Printing the rounded values of the coordinates and distance moved
    print("Coordinates:,{:.2f}".format(playerx, playery), "Distance moved:", "{:.2f}".format(distMoved))

    # Process - Determining the playerEnergy by capturing the value of lose_energy
    playerEnergy = lose_energy(playerEnergy, distMoved, playerEnergyFactor)

    # Process - if playerEnergy is less than 0, player energy is equal to 0
    if playerEnergy < 0:
        playerEnergy = 0

    # Output - Printing the rounded value of playerEnergy
    print("Energy: {:.2f}".format(playerEnergy))

    
    # Process - Determining the value of tempPlayerGold by capturing the values of the respective functions
    tempPlayerGold = eval_distance_chest(playerGold, \
                    dist(playerx, playery, chestx, chesty), chestx, chesty, window, tempText)

    # Process - If tempPlayerGold is greater than playerGold, playerGold is now equal to tempPlayerGold
    # and create the text for tempText
    if tempPlayerGold > playerGold:
        playerGold = tempPlayerGold
        tempText.setText("")
        tempText.setTextColor("gray10")

        # Process - Calling upon moveObj with 40 less than the player coordinates as arguments
        moveObj(40-playerx, 40-playery, player)

        # Setting the x and y player coordinates as 40
        playerx = 40
        playery = 40
        
        # Process - If the user guesses where the chest is, set up new level
        # Process - recapturing the values of weather and the sprites of create_background
        map_weather, playerEnergyFactor = generate_weather(playerEnergyFactor)
        weatherSprites = create_background(map_weather, window, weatherSprites)

        # Initializing temporary variables
        tempWheelx = wheelx
        tempWheely = wheely
        tempHealstonex = healStonex
        tempHealstoney = healStoney

        # Process - Recapturing coordinates from generate_coords
        wheelx, wheely, chestx, chesty, healStonex, healStoney = generate_coords()

        # Process - Calling upon moveObj with updated arguments
        moveObj(healStonex-tempHealstonex, healStoney-tempHealstoney, playerHealstone)

        # Process/Output - Resetting the display of the sprites by undrawing and redrawing them
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
                
        # Process - Calling upon moveObj with updated arguments
        moveObj(wheelx-tempWheelx, wheely-tempWheely, playerWheel)

        # Incrememnt level by 1 and playerEnergyFactor by 0.4, reset/initialize variables
        level += 1
        playerEnergyFactor += 0.4
        seconds = 0
        t = time.time()
        timeLimit = 30

        # Process - Creating the level text and weather text
        levelText.setText("Level " + str(level))
        weatherText.setText("Weather: " + map_weather)

        # Process/Output - Reset text and gameScale by undrawing and redrawing
        for i in infoText:
            i.undraw()
            i.draw(window)
            
        for i in gameScale:
            i.undraw()
            i.draw(window)
        
    # Process - if wheelObtained is false, recapture wheel function values
    if not(wheelObtained):
        wheelSpun, playerGold, playerEnergy, playerEnergyFactor, timeBoostObtained, powerBoostObtained = eval_distance_wheel(playerGold, playerEnergy, playerEnergyFactor, dist(playerx, playery, wheelx, wheely), wheelObtained, tempText)

        # Process - If the wheel is spun, then the wheel is obtained
        if wheelSpun:
            wheelObtained = True

            # Process/Output - Undrawing the wheel if they already spun it
            for i in range(len(playerWheel)):
                playerWheel[i].undraw()

            # Negating wheelDrawn
            wheelDrawn = False

    # Process - If the user recieves the powerBoost and temp remains false, temp is true and store powerBoostTime
    if powerBoostObtained and not(temp):
        temp = True
        powerBoostTime = seconds

    # Process - if the powerboost is obtained, check if the time passed is more than or equal to 10 seconds
    elif powerBoostObtained:
        if seconds - powerBoostTime >= 10:

            # Reinitialize powerBoostObtained and temp
            powerBoostObtained = False
            temp = False

            # Process - double playerEnergyFactor
            playerEnergyFactor *= 2
            
    # Process - Determining the gold and energy level after using the healstone
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

    # Process/Output - If they recieved the time boost, the time limit is now 40 seconds
    if timeBoostObtained:
        timeLimit = 40
        
    # Process - If the timer runs out, reset seconds and reset coordinates
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

        # Process/Output - if the wheel isn't drawn, draw the wheel again and set wheel drawn
        # to True
        if not(wheelDrawn):
            for i in range(len(playerWheel)):
                playerWheel[i].draw(window)
            wheelDrawn = True

        # Process - generating wheel coordinates and setting wheelObtained as False
        moveObj(wheelx-tempWheelx, wheely-tempWheely, playerWheel)
        wheelObtained = False

        # Output - Printing the text that they are out of time in the red colour
        tempText.setText("Out of time.")
        tempText.setTextColor("red")
        print("Out of time.")

window.getMouse()
window.close()