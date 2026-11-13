import pygame, random

pygame.init()
pygame.mixer.init()
game_name = pygame.display.set_caption('Tamagotchi')
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 35)
running = True
background_color = (180, 240, 255)
ui_color = (20, 180, 220)
game_state = 'start screen'
topleftx = 150
toplefty = 100
played = False
eating = False
food_index = 3
water_index = 3
tennisXX = 150
tennisYY = 375
grabbed = False
opened_options = False
animal_noise = pygame.mixer.Channel(1)
channel2 = pygame.mixer.Channel(2)
food_bowl_sprites = ['Tomagatchi/empty_food_bowl.png', 
                        'Tomagatchi/little_food_bowl.png',
                        'Tomagatchi/medium_food_bowl.png', 
                        'Tomagatchi/full_food_bowl.png']

water_bowl_sprites = ['Tomagatchi/empty_water_bowl.png',
                      'Tomagatchi/little_water_bowl.png',
                      'Tomagatchi/medium_water_bowl.png',
                      'Tomagatchi/full_water_bowl.png']

names = ['   Kyle', 'Cartman', 'Enrique', '   Stan', '  Kenny', 'Barthal', '   Oreo', 'Juanito', 'Winston', '   Dale', '   John']
cat_names = ['Baby Y', ' Sassy', 'Dallas', 'Noodle', ' Jimmy']
dog_names = ['Starlight', 'Summer', '    Mac', ' Scrappy']

background_songs = [
    'Tomagatchi/Elektronomia - Sky High [NCS Release].mp3',
    'Tomagatchi/Jim Yosef - Firefly [NCS Release].mp3', 
    'Tomagatchi/Tobu & Itro - Sunburst.mp3',
    'Tomagatchi/Cloud 9 - Itro & Tobu.mp3'
    ]

###MAIN PAGE STUFF###
guy = pygame.image.load("Tomagatchi/dog.png")
animal_image = pygame.transform.scale(guy,(175, 175))
animal_rect = animal_image.get_rect(topleft=(topleftx, toplefty))
screen.blit(animal_image, (topleftx, toplefty))


thirst_button1 = pygame.image.load('Tomagatchi/drink.png')
thirst_button2 = pygame.transform.scale(thirst_button1, (100, 100))
thirst_button = thirst_button2.get_rect(topleft=(350, 375))
screen.blit(thirst_button2, (350, 375))

hunger_button1 = pygame.image.load('Tomagatchi/feed.png')
hunger_button2 = pygame.transform.scale(hunger_button1, (100, 100))
hunger_button = hunger_button2.get_rect(topleft=(225, 375))
screen.blit(hunger_button2, (225, 375))

settings1 = pygame.image.load('Tomagatchi/settings.png')
settings2 = pygame.transform.scale(settings1, (75, 75))
settings = settings2.get_rect(topleft=(425, 0))
screen.blit(settings2, (425, 0))

options1 = pygame.image.load('Tomagatchi/options.png')
options2 = pygame.transform.scale(options1, (100, 100))
options = options2.get_rect(topleft=(-10, 425))
options_clickable = pygame.mask.from_surface(options2)

exit1 = pygame.image.load('Tomagatchi/exit.png')
exit3 = pygame.transform.scale(exit1, (30, 30))
exit_options = exit3.get_rect(topleft=(0, 346))
screen.blit(exit3, (0, 346))

tennis1 = pygame.image.load('Tomagatchi/tennis_ball.png')
tennis2 = pygame.transform.scale(tennis1, (100, 100))
tennis = tennis2.get_rect(topleft=(tennisXX, tennisYY))
screen.blit(tennis2, (tennisXX, tennisYY))
screen.blit(options2, (-10, 425))

class animal:
    def __init__(self, pic, pet_type, sound, hunger, thirst, happiness, dead, name):
        self.pic = pic
        self.pet_type = pet_type
        self.sound = sound
        self.hunger = hunger
        self.thirst = thirst
        self.happiness = happiness
        self.dead = dead
        self.name = name

    def move_pet_random(self, pic):
        global topleftx
        global toplefty
        chance = random.randint(1, 175)
        if (chance == 1):
            if (topleftx == 480):
                pass
            else:
                topleftx += 10
        elif (chance == 2):
            if (toplefty == 150):
                pass
            else:
                toplefty += 10
        elif (chance == 3):
            if (topleftx == 40):
                pass
            else:
                topleftx -= 10
        elif (chance == 4):
            if (toplefty == 10):
                pass
            else:
                toplefty -= 10
        else:
            pass
        screen.blit(pic, (topleftx, toplefty))

    def check_health(self):
        if (self.thirst <= 0 or self.hunger <= 0):
            self.dead = True
        else:
            self.dead = False
        return self.dead

    def draw_settings(self):
        global background_color
        global ui_color
        mouse_pos = pygame.mouse.get_pos()
        screen.fill(background_color)
        header = font.render('Settings:', True, 'Black')
        screen.blit(header, (195, 50))
        themes = font.render('Themes:', True, 'Black')
        screen.blit(themes, (50, 100))
        ###CHOICE 1###
        choice1 = pygame.draw.rect(screen, 'Black', (60, 145, 75, 75,), border_radius=5,)
        pygame.draw.polygon(screen, (55, 204, 110), [(70, 155), (125, 155), (70, 210)])
        pygame.draw.polygon(screen, (103, 232, 209), [(125, 210), (125, 155), (70, 210)])

        ###CHOICE 2###
        choice2 = pygame.draw.rect(screen, 'Black', (150, 145, 75, 75,), border_radius=5,)
        pygame.draw.polygon(screen, (188, 130, 255), [(160, 155), (215, 155), (160, 210)])
        pygame.draw.polygon(screen, (255, 220, 100), [(215, 210), (215, 155), (160, 210)])

        ###CHOICE 3###
        choice3 = pygame.draw.rect(screen, 'Black', (240, 145, 75, 75,), border_radius=5,)
        pygame.draw.polygon(screen, (152, 118, 197), [(250, 155), (305, 155), (250, 210)])
        pygame.draw.polygon(screen, (221, 214, 234), [(305, 210), (305, 155), (250, 210)])

        ###CHOICE 4###
        choice4 = pygame.draw.rect(screen, 'Black', (330, 145, 75, 75,), border_radius=5,)
        pygame.draw.polygon(screen, (180, 240, 255), [(340, 155), (395, 155), (340, 210)])
        pygame.draw.polygon(screen, (20, 180, 220), [(395, 210), (395, 155), (340, 210)])


        ###EXIT TO MAIN STUFF###
        exit1 = pygame.image.load('Tomagatchi/exit.png')
        exit2 = pygame.transform.scale(exit1, (50, 50))
        exit = exit2.get_rect(topleft=(0, 0))
        screen.blit(exit2, (0, 0))

        if (choice1.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN):
            background_color = (55, 204, 110)
            ui_color = (103, 232, 209)
            return background_color, ui_color

        if (choice2.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN):
            background_color = (188, 130, 255)
            ui_color = (255, 220, 100)
            return background_color, ui_color

        if (choice3.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN):
                background_color = (152, 118, 197)
                ui_color = (221, 214, 234)
                return background_color, ui_color

        if (choice4.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN):
                background_color = (180, 240, 255)
                ui_color = (20, 180, 220)
                return background_color, ui_color
        
        if (exit.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN):
            global game_state
            game_state = 'main'

    def walk_and_drink(self, pet_type, name):
        global topleftx
        global toplefty
        global water_index
        if (topleftx % 2 == 1):
            topleftx += 1
        if (toplefty % 2 == 1):
            toplefty += 1
        if (topleftx > 40):
            topleftx -= 2
        if (toplefty > 80):
            toplefty -= 2
        elif (topleftx < 40):
            topleftx += 2
        elif (toplefty < 80):
            toplefty += 2
        pet = 'Tomagatchi/cat.png'
        if (pet_type == 'cat'):
            pet = 'Tomagatchi/cat.png'
        if (pet_type == 'dog'):
            pet = 'Tomagatchi/dog.png'
        if (pet_type == 'pig'):
            pet = 'Tomagatchi/piggy.png'
            if (name == '   Dale'):
                pet = 'Tomagatchi/dale.png'
            if (name == '   John'):
                pet = 'Tomagatchi/john pork.jpeg'
        animal = pygame.image.load(pet)              
        image = pygame.transform.scale(animal,(175, 175))
        screen.blit(image, (topleftx, toplefty))
        if (toplefty == 80 and topleftx == 40):
            if (water_index == 0):
                pass
            else:
                while self.thirst < 100:
                    self.thirst += 5
                water_index -= 1
        return self.thirst
    
    def walk_and_eat(self, pet_type, name):
        global topleftx
        global toplefty
        global food_index
        if (topleftx % 2 == 1):
            topleftx += 1
        if (toplefty % 2 == 1):
            toplefty += 1
        if (topleftx > 40):
            topleftx -= 2
        if (toplefty > 160):
            toplefty -= 2
        elif (topleftx < 40):
            topleftx += 2
        elif (toplefty < 160):
            toplefty += 2
        pet = 'Tomagatchi/cat.png'
        if (pet_type == 'cat'):
            pet = 'Tomagatchi/cat.png'
        if (pet_type == 'dog'):
            pet = 'Tomagatchi/dog.png'
        if (pet_type == 'pig'):
            pet = 'Tomagatchi/piggy.png'
            if (name == '   Dale'):
                pet = 'Tomagatchi/dale.png'
            if (name == '   John'):
                pet = 'Tomagatchi/john pork.jpeg'
        animal = pygame.image.load(pet)              
        image = pygame.transform.scale(animal,(175, 175))
        screen.blit(image, (topleftx, toplefty))
        if (toplefty == 160 and topleftx == 40):
            if (food_index == 0):
                pass
            else:
                while self.hunger < 100:
                    self.hunger += 5
                food_index -= 1
        return self.hunger
        
    def redraw_everything_main(self, pet_type, name):
        global food_index
        global water_index
        global game_state
        pet_pic = 'Tomagatchi/cat.png'
        if (pet_type == 'cat'):
            pet_pic = 'Tomagatchi/cat.png'
        if (pet_type == 'dog'):
            pet_pic = 'Tomagatchi/dog.png'
        if (pet_type == 'pig'):
            pet_pic = 'Tomagatchi/piggy.png'
            if (name == '   Dale'):
                pet_pic = 'Tomagatchi/dale.png'
            if (name == '   John'):
                pet_pic = 'Tomagatchi/john pork.jpeg'
        screen.fill(background_color)
        pygame.draw.line(screen, 'Black', (0, 350), (500, 350), 10)
        pygame.draw.rect(screen, ui_color, (0, 350, 500, 150))

        food_sprite = food_bowl_sprites[food_index]
        fb = pygame.image.load(food_sprite)
        food_bowl = pygame.transform.scale(fb, (75, 55))
        screen.blit(food_bowl, (10, 225))

        water_sprite = water_bowl_sprites[water_index]
        wb = pygame.image.load(water_sprite)
        water_bowl = pygame.transform.scale(wb, (75, 50))
        screen.blit(water_bowl, (10, 150))

        animal = pygame.image.load(pet_pic)
        image = pygame.transform.scale(animal,(175, 175))
        image.get_rect(topleft=(topleftx, toplefty))
        screen.blit(image, (topleftx, toplefty))

        if (self.hunger <= 60 or self.thirst <= 60):
            if (self.hunger <= 60 and food_index > 0):
                self.hunger = self.walk_and_eat(self.pet_type, self.name)

            if (self.thirst <= 60 and water_index > 0):
                self.thirst = self.walk_and_drink(self.pet_type, self.name)

        elif (tennisYY <= 275):
            self.chase_ball(pet_type)

        else:
            self.move_pet_random(image)

        if (game_state == 'main'):

            settings1 = pygame.image.load('Tomagatchi/settings.png')
            settings2 = pygame.transform.scale(settings1, (30, 30))
            settings2.get_rect(topleft=(470, 0))
            screen.blit(settings2, (470, 0))

            thirst_button1 = pygame.image.load('Tomagatchi/drink.png')
            thirst_button2 = pygame.transform.scale(thirst_button1, (100, 100))
            thirst_button2.get_rect(topleft=(350, 375))
            screen.blit(thirst_button2, (350, 375))

            hunger_button1 = pygame.image.load('Tomagatchi/feed.png')
            hunger_button2 = pygame.transform.scale(hunger_button1, (100, 100))
            hunger_button2.get_rect(topleft=(225, 375))
            screen.blit(hunger_button2, (225, 375))

            options1 = pygame.image.load('Tomagatchi/options.png')
            options2 = pygame.transform.scale(options1, (100, 100))
            options = options2.get_rect(topleft=(-10, 425))
            screen.blit(options2, (-10, 425))

            happiness1 = font.render(f'Happiness: {self.happiness}', True, 'Black')
            screen.blit(happiness1, (0, 360))

            hunger1 = font.render(f'Hunger: {self.hunger}', True, 'Black')
            screen.blit(hunger1, (0, 385))

            thirst1 = font.render(f'Thirst: {self.thirst}', True, 'Black')
            screen.blit(thirst1, (0, 410))

        if (game_state == 'main but options' ):
            pygame.draw.line(screen, 'Black', (0, 350), (500, 350), 10)
            pygame.draw.rect(screen, ui_color, (0, 350, 500, 150))
            tennis1 = pygame.image.load('Tomagatchi/tennis_ball.png')
            tennis2 = pygame.transform.scale(tennis1, (100, 100))
            tennis = tennis2.get_rect(topleft=(tennisXX, tennisYY))
            screen.blit(tennis2, (tennisXX, tennisYY))
            exit1 = pygame.image.load('Tomagatchi/exit.png')
            exit3 = pygame.transform.scale(exit1, (30, 30))
            exit3.get_rect(topleft=(0, 346))
            screen.blit(exit3, (0, 346))
    
    def drain_stat(self, pet_type):
        chance = random.randint(1, 250)
        if (pet_type == 'dog'):
            if (chance == 1):
                self.thirst -= 5
            elif (chance == 2):
                self.hunger -= 2.5
        elif (pet_type == 'cat'):
            if (chance == 1):
                self.thirst -= 2.5
            elif (chance == 2):
                self.hunger -= 5
        else:
            if (chance == 1):
                self.hunger -= 5

            elif (chance == 2):
                self.thirst -= 5

    def confirm_pet_and_describe(self, pet_type):
        screen.fill(background_color)
        if (pet_type == 'dog'):
            animale = pygame.image.load('Tomagatchi/dog.png')
            animale1 = pygame.transform.scale(animale, (175, 175))
            screen.blit(animale1, (300, 100))
            text1 = font.render('You have chosen dog!', True, 'Black')
            text2 = font.render('Dog\'s special ability', True, 'Black')
            text3 = font.render('is to reduce ', True, 'Black')
            text4 = font.render('hunger loss by 50%', True, 'Black')
            text5 = font.render('Is this the pet', True, 'Black')
            text6 = font.render('that you want?', True, 'Black')
            screen.blit(text1, (25, 75))
            screen.blit(text2, (25, 100))
            screen.blit(text3, (25, 125))
            screen.blit(text4, (25, 150))
            screen.blit(text5, (25, 175))
            screen.blit(text6, (25, 200))
        elif (pet_type == 'cat'):
            animale = pygame.image.load('Tomagatchi/cat.png')
            animale1 = pygame.transform.scale(animale, (175, 175))
            screen.blit(animale1, (300, 100))
            text1 = font.render('You have chosen cat!', True, 'Black')
            text2 = font.render('Cat\'s special ability', True, 'Black')
            text3 = font.render('is to reduce ', True, 'Black')
            text4 = font.render('thirst loss by 50%', True, 'Black')
            text5 = font.render('Is this the pet', True, 'Black')
            text6 = font.render('that you want?', True, 'Black')
            screen.blit(text1, (25, 75))
            screen.blit(text2, (25, 100))
            screen.blit(text3, (25, 125))
            screen.blit(text4, (25, 150))
            screen.blit(text5, (25, 175))
            screen.blit(text6, (25, 200))
        elif (pet_type == 'pig'):
            animale = pygame.image.load('Tomagatchi/piggy.png')
            animale1 = pygame.transform.scale(animale, (175, 175))
            screen.blit(animale1, (300, 100))
            text4 = font.render('pig.', True, 'Black')
            screen.blit(text4, (100, 150))
        confirm_start1 = pygame.image.load('Tomagatchi/confirm_button.png')
        confirm_start = pygame.transform.scale(confirm_start1, (300, 150))
        back_button1 = pygame.image.load('Tomagatchi/back_button.png')
        back_button = pygame.transform.scale(back_button1, (350, 150))
        confirm_rect = confirm_start.get_rect(topleft=(200, 270))
        back_rect = back_button.get_rect(topleft=(210, 360))
        confirm_clickable = pygame.mask.from_surface(confirm_start)
        back_clickable = pygame.mask.from_surface(back_button)
        mouseX, mouseY = pygame.mouse.get_pos()
        relative_confirm_X = mouseX - 200
        relative_confirm_Y = mouseY - 270
        relative_back_X = mouseX - 210
        relative_back_Y = mouseY - 360
        screen.blit(back_button, (210, 360))
        screen.blit(confirm_start, (200, 270))
        return confirm_rect, back_rect, confirm_clickable, back_clickable, relative_confirm_X, relative_confirm_Y, relative_back_X, relative_back_Y

    def calc_happiness(self):
        sum = self.thirst + self.hunger
        avg = sum / 2
        self.happiness = avg

    def restart(self):
        global game_state
        screen.fill('Grey')
        message = font.render('Your pet has died.', True, 'Black')
        second_message = font.render('Press any key to play again.', True, 'Black')
        screen.blit(message, (150, 200))
        screen.blit(second_message, (100, 300))

    def pick_pet(self):
        screen.fill(background_color)
        font1 = font.render('Choose your pet!', True, 'Black')
        screen.blit(font1, (150, 25))
        pup = pygame.image.load('Tomagatchi/dog.png')
        pupp = pygame.transform.scale(pup, (150, 150))
        puppy_rect = pupp.get_rect(topleft=(50, 100))
        screen.blit(pupp, (50, 100))
        cat = pygame.image.load('Tomagatchi/cat.png')
        catt = pygame.transform.scale(cat, (150, 150))
        cat_rect = catt.get_rect(topleft=(300, 100))
        screen.blit(catt, (300, 100))
        pig1 = pygame.image.load('Tomagatchi/piggy.png')
        pigg = pygame.transform.scale(pig1, (180, 180))
        pig_rect = pigg.get_rect(topleft =(50, 300))
        screen.blit(pigg, (40, 300))
        start_cat_clickable = pygame.mask.from_surface(catt)
        start_dog_clickable = pygame.mask.from_surface(pupp)
        start_pig_clickable = pygame.mask.from_surface(pigg)
        mouseX, mouseY = pygame.mouse.get_pos()
        start_relativeX_pup = mouseX - 50
        start_relativeY_pup = mouseY - 100
        start_relativeX_cat = mouseX - 300
        start_relativeY_cat = mouseY - 100
        start_relativeX_pig = mouseX - 50
        start_relativeY_pig = mouseY - 300
        return puppy_rect, cat_rect, start_relativeX_pup, start_relativeY_pup, start_relativeX_cat, start_relativeY_cat, start_cat_clickable, start_dog_clickable, pig_rect, start_pig_clickable, start_relativeX_pig, start_relativeY_pig

    def begin_game(self):
        screen.fill(background_color)
        title = pygame.image.load('Tomagatchi/title.png')
        title1 = pygame.transform.scale(title, (550, 300))
        screen.blit (title1, (-15, 0))
        start_b = pygame.image.load('Tomagatchi/start.png')
        scale_start_b = pygame.transform.scale(start_b, (200, 100))
        start_b_rect = scale_start_b.get_rect(topleft=(145, 300))
        screen.blit(scale_start_b, (145, 300))
        start_button = pygame.mask.from_surface(scale_start_b)
        quit_b = pygame.image.load('Tomagatchi/quit button.png')
        scale_quit_b = pygame.transform.scale(quit_b, (210, 120))
        screen.blit(scale_quit_b, (137, 400))
        quit_b_rect = scale_quit_b.get_rect(topleft=(137, 400))
        quit_button = pygame.mask.from_surface(scale_quit_b)
        mouseX, mouseY = pygame.mouse.get_pos()
        buttonX = mouseX - 145
        buttonY = mouseY - 300
        quit_buttonX = mouseX - 137
        quit_buttonY = mouseY - 400
        return start_b_rect, buttonX, buttonY, start_button, quit_buttonX, quit_buttonY, quit_b_rect, quit_button

    def pick_name(self, name):
        random_name = random.randint(0, 10)
        doggy_name = random.randint(0, 3)
        cat_name = random.randint(0, 4)
        name = names[random_name]
        text = font.render(name, True, 'Black')
        if (pet.pet_type == 'dog'):
            name = dog_names[doggy_name]
            text = font.render(name, True, 'Black')
        elif (pet.pet_type == 'cat'):
            name = cat_names[cat_name]
            text = font.render(name, True, 'Black')
        pet.name = name
        return name, text, pet.name

    def chase_ball(self, pet_type):
        global toplefty
        global topleftx
        global tennisXX
        global tennisYY
        if (tennisXX % 2 == 0):
            tennisXX -= 1
        if (tennisYY % 2 == 0):
            tennisYY -= 1
        if (topleftx % 2 == 0):
            topleftx -= 1
        if (toplefty % 5 == 0):
            while (toplefty % 5 != 0):
                toplefty -= 1
        if (pet_type == 'dog'):
            if (topleftx > tennisXX):
                topleftx -= 3
            if (topleftx < tennisXX):
                topleftx += 5
            if (toplefty + 40 < tennisYY):
                toplefty += 5
            if (toplefty + 40 > tennisYY):
                toplefty -= 3
    
pet = animal('', '', '', 100, 100, 100, False, '')
pygame.display.flip()
stop = 1
index = random.randint(0,3)
background_music = pygame.mixer.Sound(background_songs[index])
background_music.set_volume(0.25)
channel2.play(background_music)
while running:
    if (game_state == 'start screen' or game_state == 'pick pet' or game_state == 'main' or game_state == 'main but options' or game_state == 'settings'):
        ended = channel2.get_busy()
        if (ended == False):
            if (index == 4):
                index = 0
            index += 1
            background_music = pygame.mixer.Sound(background_songs[index])
            channel2.play(background_music)
    mouse_pos = pygame.mouse.get_pos()
    if (game_state == 'start screen'):
        pet.begin_game()
    if (game_state == 'pick pet'):
        pet.pick_pet()
    if (pet.check_health() == True):
        game_state = 'Game Over'
    if (game_state == 'main' or game_state == 'main but options'):
        pet.redraw_everything_main(pet.pet_type, pet.name)
        pet.drain_stat(pet.pet_type)
        if (stop == 1):
            name, text, pet.name = pet.pick_name('')
            stop = 0
        if (animal_rect.collidepoint(mouse_pos)):
            screen.blit(text, (topleftx + 35, toplefty - 5))
    if (game_state == 'settings'):
        pet.draw_settings()
    if (pet.pet_type != 'pig'):
        pet.calc_happiness()
    if (pet.thirst >= 35 and pet.hunger >= 35 and played == True):
        played = False
    if (pet.thirst == 30 or pet.hunger == 30):
        playing = animal_noise.get_busy()
        if (playing == False):
            if (pet.pet_type == 'dog'):
                sound = pygame.mixer.Sound('Tomagatchi/ANMLDog_Dogs barking and crying 1 (ID 1544)_BigSoundBank.com.wav')
                if (played == True):
                    volume = 0.0
                if (played == False):
                    volume = 0.3
                sound.set_volume(volume)
                animal_noise.play(sound, maxtime=1000)
                played = True

            if (pet.pet_type == 'cat'):
                sound = pygame.mixer.Sound('Tomagatchi/dragon-studio-meow-sfx-405456.mp3')
                if (played == True):
                    volume = 0.0
                else:
                    volume = 0.3
                sound.set_volume(volume)
                animal_noise.play(sound)
                played = True

            if (pet.pet_type == 'pig' and pet.name == '   John'):
                sound = pygame.mixer.Sound('Tomagatchi/john-pork-is-calling-moooort.mp3')
                if (played == True):
                    volume = 0.0
                else:
                    volume = 1.0
                sound.set_volume(volume)
                animal_noise.play(sound, maxtime=5000)
                played = True

            elif (pet.pet_type == 'pig'):
                sound = pygame.mixer.Sound('Tomagatchi/freesound_community-pig-grunt-100272.mp3')
                if (played == True):
                    volume = 0.0
                else:
                    volume = 1.0
                sound.set_volume(volume)
                animal_noise.play(sound)
                played = True
        else:
            pass

    animal_clickable = pygame.mask.from_surface(animal_image)
    mouseX, mouseY = pygame.mouse.get_pos()
    relativeX = mouseX - topleftx
    relativeY = mouseY - toplefty
    relative_options_X = mouseX + 10
    relative_options_Y = mouseY - 425
    options_exit_X = mouseX
    options_exit_Y = mouseY - 346
    exit_options_clickable = pygame.mask.from_surface(exit3)
    tennisX = mouseX - tennisXX
    tennisY = mouseY - tennisYY
    tennis_clickable = pygame.mask.from_surface(tennis2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if (game_state == 'start screen'):
            start_b_rect, buttonX, buttonY, start_button, quit_buttonX, quit_buttonY, quit_b_rect, quit_button = pet.begin_game()
            if (quit_b_rect.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN):
                if (quit_button.get_at((quit_buttonX, quit_buttonY))):
                    running = False
            if (start_b_rect.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN):
                if (start_button.get_at((buttonX, buttonY))):
                    game_state = 'pick pet'
        if (game_state == 'pick pet'):
            puppy_rect, cat_rect, start_relativeX_pup, start_relativeY_pup, start_relativeX_cat, start_relativeY_cat, start_cat_clickable, start_dog_clickable, pig_rect, start_pig_clickable, start_relativeX_pig, start_relativeY_pig = pet.pick_pet()
            if (puppy_rect.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN):
                if (start_dog_clickable.get_at((start_relativeX_pup, start_relativeY_pup))):
                    pet.pet_type = 'dog'
                    pet.pic = pygame.image.load('Tomagatchi/dog.png')
                    game_state = 'confirm'
            if (cat_rect.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN):
                if (start_cat_clickable.get_at((start_relativeX_cat, start_relativeY_cat))):
                    pet.pet_type = 'cat'
                    pet.pic = pygame.image.load('Tomagatchi/cat.png')
                    game_state = 'confirm'
            if (pig_rect.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN):
                if (start_pig_clickable.get_at((start_relativeX_pig, start_relativeY_pig))):
                    pet.pet_type = 'pig'
                    pet.pic = pygame.image.load('Tomagatchi/piggy.png')
                    game_state = 'confirm'
        if (game_state == 'confirm'):
            confirm_rect, back_rect, confirm_clickable, back_clickable, relative_confirm_X, relative_confirm_Y, relative_back_X, relative_back_Y = pet.confirm_pet_and_describe(pet.pet_type)
            if (back_rect.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN):
                if (back_clickable.get_at((relative_back_X, relative_back_Y))):
                    game_state = 'pick pet'
            elif (confirm_rect.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN):
                if (confirm_clickable.get_at((relative_confirm_X, relative_confirm_Y))):
                    game_state = 'main'
        if (options.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN):
            if (options_clickable.get_at((relative_options_X, relative_options_Y))):  
                game_state = 'main but options'
        if (game_state == 'main but options' and exit_options.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN and exit_options_clickable.get_at((options_exit_X, options_exit_Y))):
            game_state = 'main'
            tennisXX = 150
            tennisYY = 375
            tennis.x = 150
            tennis.y = 375
        if (game_state == 'main but options' and tennis.collidepoint(mouse_pos) and tennis_clickable.get_at((tennisX, tennisY)) and event.type == pygame.MOUSEBUTTONDOWN):
            grabbed = True
        if (grabbed == True and event.type == pygame.MOUSEMOTION):
            tennis.move_ip(event.rel)
            tennisXX = tennis.x
            tennisYY = tennis.y
        if (grabbed == True and event.type == pygame.MOUSEBUTTONUP):
            grabbed = False
            if (tennisXX <= -60 or tennisXX >= 455 or tennisYY <= -60 or tennisYY >= 455):
                tennisXX = 150
                tennisYY = 375
                tennis.x = 150
                tennis.y = 375
            
        if (mouseX == 0 or mouseY == 0):
            pass
        if (animal_rect.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN):
            try:
                if (animal_clickable.get_at((relativeX, relativeY))):
                    if (game_state == 'start screen' or game_state == 'pick pet' or game_state == 'settings'):
                        pass
                    else:
                        playing = animal_noise.get_busy()
                        if (playing == False):  
                            if (pet.pet_type == 'dog'):
                                sound = pygame.mixer.Sound('Tomagatchi/ANMLDog_Dogs barking and crying 1 (ID 1544)_BigSoundBank.com.wav')
                                sound.set_volume(0.3)
                                animal_noise.play(sound, maxtime=1000)
                            if (pet.pet_type == 'cat'):
                                sound = pygame.mixer.Sound('Tomagatchi/dragon-studio-meow-sfx-405456.mp3')
                                sound.set_volume(0.3)
                                animal_noise.play(sound)
                            if (pet.pet_type == 'pig' and pet.name == '   John'):
                                sound = pygame.mixer.Sound('Tomagatchi/john-pork-is-calling-moooort.mp3')
                                sound.set_volume(1.0)
                                animal_noise.play(sound, maxtime=5000)
                            elif (pet.pet_type == 'pig'):
                                sound = pygame.mixer.Sound('Tomagatchi/freesound_community-pig-grunt-100272.mp3')
                                sound.set_volume(1.0)
                                animal_noise.play(sound)
                        else:
                            pass
            except IndexError:
                pass


        if (game_state == 'Game Over'):
            pet.restart()
            if (event.type == pygame.KEYDOWN):
                game_state = 'start screen'
                pet.thirst = 100
                pet.hunger = 100
                pet.happiness = 100
                food_index = 3
                water_index = 3
                topleftx = 150
                toplefty = 100
        if (thirst_button.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN):
            if (water_index == 3):
                pass
            else:
                water_index += 1

        if (hunger_button.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN):
            if (food_index == 3):
                pass
            else:
                food_index += 1

        if (settings.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN and game_state != 'main but options'):
            game_state = 'settings'

    pygame.display.flip()
    clock.tick(60) / 1000          #KEEP INDENTED IN WHILE LOOP OR ELSE SCREEN ONLY UPDATES WHEN MOUSE MOVES

pygame.quit()