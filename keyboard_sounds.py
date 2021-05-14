'''
Create a sound board where you press keys 1 - 9 to play the respective animal sounds.
There must be an introductory start screen that states the program name at the top and then presents
a list of animal names in alphabetical form. Try to match this with the code not hand written.

When a key is pressed, the corresponding animal silhouette will be displayed on the screen. After the sound is complete
the program will return to the start screen. Optional, the animal name text must change colour to red showing that it
has already been listened to. If an animal sound has been player concurrently for more than 3 times, an easter egg
sound must play along with its image. Thus the program must keep track of the number of times an animal sound was
and reset the rest.

1. start with while loop. Define which buttons will be assigned to which animal.
2. each key pressed will assign the respective number to the 'choice' variable. <- better solution was found!!
3. The choice variable will then be used in the play sound function to call the respective sound and play it.
4. The function will also then display the respective image of the animal and change the text colour of that animal
   to red.

logic:

check if key is pressed
    check how many times it has been pressed
        if it is less than three, display animal and play sound
        if 3 times then display joke and sound
    Return to Start
'''
import pygame, sys, time
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

pygame.init()
font = pygame.font.Font("assets/font/Arcade.ttf",30)
clock = pygame.time.Clock()
title_image = pygame.image.load("assets/images/title.png")


windowWidth = 800
windowHeight = 1000

surface = pygame.display.set_mode((windowWidth,windowHeight))
pygame.display.set_caption('Keyboard Fun!')

volume = 0.5

counter = [10,11,12,13,14]
animals = []

pygame.mixer.init()
pygame.mixer.music.load('assets/sounds/OGG/Dreaming.ogg')
pygame.mixer.music.play(-1)

def animalList():

    for animal in animals:
        if animal["a_count"] < 10:
            write = str(animal["a_count"]) + " - " + str(animal["name"])
            surface.blit((font.render(write,False,animal["fontcolour"])),animal["position"])

def animalSound(x):

    global counter

    counter.insert(0,x)

    if counter[0] == counter[1] and counter[1] == counter[2]:
        animals[9]["sound"].set_volume(volume)
        animals[9]["sound"].play()
        pygame.draw.rect(surface, (20, 20, 0), (0, 500, 800, 400))
        surface.blit(animals[9]["image"], (((windowWidth / 2) - (363 / 2)), 500))
        pygame.display.update()
        time.sleep(animals[9]["dudu"])

    else:
        animals[x]["sound"].set_volume(volume)
        animals[x]["sound"].play()
        pygame.draw.rect(surface, (20, 20, 0), (0, 500, 800, 400))
        surface.blit(animals[x]["image"], (((windowWidth / 2) - (363 / 2)), 500))
        animals[x]["fontcolour"] = (150,0,0)
        pygame.display.update()
        time.sleep(animals[x]["dudu"])

def quitGame():

    pygame.quit()
    sys.exit()

# animals

animals.append({"name" : "Cat", "image" : pygame.image.load("assets/images/cat.png"), "sound" : pygame.mixer.Sound("assets/sounds/OGG/cat.ogg"), "a_count" : 1, "dudu" : 4, "position" : (250,500), "fontcolour" : (255,255,255)})
animals.append({"name" : "Chicken", "image" : pygame.image.load("assets/images/chicken.png"), "sound" : pygame.mixer.Sound("assets/sounds/OGG/chicken.ogg"), "a_count" : 2, "dudu" : 5.5, "position" : (250,530), "fontcolour" : (255,255,255)})
animals.append({"name" : "Cow", "image" : pygame.image.load("assets/images/cow.png"), "sound" : pygame.mixer.Sound("assets/sounds/OGG/cow.ogg"), "a_count" : 3, "dudu" : 4, "position" : (250,560), "fontcolour" : (255,255,255)})
animals.append({"name" : "Dog", "image" : pygame.image.load("assets/images/dog.png"), "sound" : pygame.mixer.Sound("assets/sounds/OGG/dog.ogg"), "a_count" : 4, "dudu" : 8, "position" : (250,590), "fontcolour" : (255,255,255)})
animals.append({"name" : "Horse", "image" : pygame.image.load("assets/images/horse.png"), "sound" : pygame.mixer.Sound("assets/sounds/OGG/horse.ogg"), "a_count" : 5, "dudu" : 2, "position" : (250,620), "fontcolour" : (255,255,255)})
animals.append({"name" : "Mouse", "image" : pygame.image.load("assets/images/mouse.png"), "sound" : pygame.mixer.Sound("assets/sounds/OGG/mouse.ogg"), "a_count" : 6, "dudu" : 2, "position" : (250,650), "fontcolour" : (255,255,255)})
animals.append({"name" : "Pig", "image" : pygame.image.load("assets/images/pig.png"), "sound" : pygame.mixer.Sound("assets/sounds/OGG/pig.ogg"), "a_count" : 7, "dudu" : 2, "position" : (250,680), "fontcolour" : (255,255,255)})
animals.append({"name" : "Rooster", "image" : pygame.image.load("assets/images/rooster.png"), "sound" : pygame.mixer.Sound("assets/sounds/OGG/rooster.ogg"), "a_count" : 8, "dudu" : 2, "position" : (250,710), "fontcolour" : (255,255,255)})
animals.append({"name" : "Sheep", "image" : pygame.image.load("assets/images/sheep.png"), "sound" : pygame.mixer.Sound("assets/sounds/OGG/sheep.ogg"), "a_count" : 9, "dudu" : 2, "position" : (250,740), "fontcolour" : (255,255,255)})
animals.append({"name" : "Boude", "image" : pygame.image.load("assets/images/butt-cat.png"), "sound" : pygame.mixer.Sound("assets/sounds/OGG/laugh.ogg"), "a_count" : 10, "dudu" : 3, "position" : (250,770), "fontcolour" : (255,255,255)})

# Main Loop

while True:

    surface.fill((20,20,0))
    surface.blit(title_image, (0,150))
    animalList()

    for event in GAME_EVENTS.get():

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_1:

                animalSound(0)
                # cat

            if event.key == pygame.K_2:

                animalSound(1)
                # chicken

            if event.key == pygame.K_3:

                animalSound(2)
                # cow

            if event.key == pygame.K_4:

                animalSound(3)
                # dog

            if event.key == pygame.K_5:

                animalSound(4)
                # horse

            if event.key == pygame.K_6:

                animalSound(5)
                # mouse

            if event.key == pygame.K_7:

                animalSound(6)
                #  pig

            if event.key == pygame.K_8:

                animalSound(7)
                # rooster

            if event.key == pygame.K_9:

                animalSound(8)
                # sheep

            if event.key == pygame.K_ESCAPE:
                quitGame()

        if event.type == GAME_GLOBALS.QUIT:
            quitGame()

    clock.tick(60)
    pygame.display.update()

