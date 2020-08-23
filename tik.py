import pygame
import time

red = (190, 0, 0)
light_red = (255, 0, 0) 

black = (0, 0, 0)
white = (225, 225, 225)

yellow = (200, 200, 0)
light_yellow = (255, 255, 0)

green = (0, 190, 0)
light_green = (0, 255, 0)

blue = (0, 0, 255)

# inicialiting pygame
pygame.init()

# making display
screen = pygame.display.set_mode((350, 370))

clock = pygame.time.Clock()


# displaytext

verysmallfont = pygame.font.SysFont("comicsansms", 24)
smallfont = pygame.font.SysFont("comicsansms", 30)
midfont = pygame.font.SysFont("comicsansms", 40)
largefont = pygame.font.SysFont("comicsansms", 100)

# img and text

def img_load(img, x, y):
    img = pygame.image.load(img)
    screen.blit(img, [x, y])

def text(text, color, textx, texty, font):
    text = font.render(text, True, color)
    screen.blit(text, [textx, texty])

def game_over_x():
    
    game_over = True
    
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_c:
                    gameloop()
                

        screen.fill(black)
        text("game over", light_red, 80, 100, midfont)
        text("red", light_red, 80, 160, smallfont)
        text("player win", light_green, 140, 160, smallfont)
        
        pygame.draw.rect(screen, green, [50, 300, 100, 50])
        pygame.draw.rect(screen, red, [210, 300, 100, 40])
        
        button(50, 300, 100, 50, light_green, green, action = "play")
        button(210, 300, 100, 40, light_red, red, action = "quit")

        text("play", black, 74, 293, verysmallfont)
        text("again", black, 70,315, verysmallfont)
        
        text("quit", black, 230, 295, smallfont)        
        pygame.display.update()

                
def game_over_y():
    
    game_over = True
    
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_c:
                    gameloop()
                

        screen.fill(black)
        text("game over", light_red, 80, 100, midfont)
        text("blue", blue, 80, 160, smallfont)
        text("player win", light_green, 140, 160, smallfont)
        
        pygame.draw.rect(screen, green, [50, 300, 100, 50])
        pygame.draw.rect(screen, red, [210, 300, 100, 40])
        
        button(50, 300, 100, 50, light_green, green, action = "play")
        button(210, 300, 100, 40, light_red, red, action = "quit")

        text("play", black, 74, 293, verysmallfont)
        text("again", black, 70,315, verysmallfont)
        
        text("quit", black, 230, 295, smallfont)
        
        pygame.display.update()


def button(x, y, open_x, open_y, interactive, active, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+open_x > cur[0] > x and y+open_y > cur[1] > y:
        pygame.draw.rect(screen, interactive, [x, y, open_x, open_y])
        if click[0] == 1 and action != None:
            if action=="quit":
                pygame.quit()
                quit()
            elif action=="play":
                gameloop()
  
    else:
        pygame.draw.rect(screen, active, [x, y, open_x, open_y])        

def game_draw():
    
    game_draw = True
    
    while game_draw:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_c:
                    gameloop()
                

        screen.fill(black)
        text("game draw", yellow, 80, 100, midfont)

        pygame.draw.rect(screen, green, [50, 300, 100, 50])
        pygame.draw.rect(screen, red, [210, 300, 100, 40])
        
        button(50, 300, 100, 50, light_green, green, action = "play")
        button(210, 300, 100, 40, light_red, red, action = "quit")

        text("play", black, 74, 293, verysmallfont)
        text("again", black, 70,315, verysmallfont)
        
        text("quit", black, 230, 295, smallfont)
        
        pygame.display.update()

def game_intro():
    
    game_intro = True
    
    while game_intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_c:
                    gameloop()
                

        screen.fill(black)
        
        text("welcome to ", yellow, 95, 100, smallfont)
        text("tik tak toi", yellow, 55, 140, smallfont)

        pygame.draw.rect(screen, green, [50, 300, 100, 40])
        pygame.draw.rect(screen, red, [210, 300, 100, 40])
        
        button(50, 300, 100, 40, light_green, green, action = "play")
        button(210, 300, 100, 40, light_red, red, action = "quit")

        text("play", black, 70, 293, smallfont)
        text("quit", black, 230, 295, smallfont)

        pygame.display.update()


def gameloop():
    game = True
    chance = 0
    s = 0
    K_KP1x = False
    K_KP2x = False
    K_KP3x = False
    K_KP4x = False
    K_KP5x = False
    K_KP6x = False
    K_KP7x = False
    K_KP8x = False
    K_KP9x = False

    K_KP1y = False
    K_KP2y = False
    K_KP3y = False
    K_KP4y = False
    K_KP5y = False
    K_KP6y = False
    K_KP7y = False
    K_KP8y = False
    K_KP9y = False    
    
    screen.fill(black)
     
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                run = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP7:
                    if chance%2==0:
                        s += 1
                        img_load("c.png", 5, 5)
                        chance += 1
                        K_KP7x = True
                    else:
                        img_load("x.png", 5, 5)
                        s += 1
                        chance += 1
                        K_KP7y = True
                        
                elif event.key == pygame.K_KP8:
                    if chance%2==0:
                        s += 1
                        img_load("c.png", 135, 5)
                        chance += 1
                        K_KP8x = True
                    else:
                        img_load("x.png", 135, 5)
                        s += 1
                        chance += 1
                        K_KP8y = True
                        
                elif event.key == pygame.K_KP9:
                    if chance%2==0:
                        s += 1
                        img_load("c.png", 250, 5)
                        chance += 1
                        K_KP9x = True
                    else:
                        s += 1
                        img_load("x.png", 250, 5)
                        chance += 1
                        K_KP9y = True

                elif event.key == pygame.K_KP4:
                    if chance%2==0:
                        s += 1
                        img_load("c.png", 5, 135)
                        chance += 1
                        K_KP4x = True
                    else:
                        s += 1
                        img_load("x.png", 5, 135)
                        chance += 1
                        K_KP4y = True

                elif event.key == pygame.K_KP5:
                    if chance%2==0:
                        s += 1
                        img_load("c.png", 135, 135)
                        chance += 1
                        K_KP5x = True
                    else:
                        s += 1
                        img_load("x.png", 135, 135)
                        chance += 1
                        K_KP5y = True        

                elif event.key == pygame.K_KP6:
                    if chance%2==0:
                        s += 1
                        img_load("c.png", 250, 135)
                        chance += 1
                        K_KP6x = True
                    else:
                        s += 1
                        img_load("x.png", 250, 135)
                        chance += 1
                        K_KP6y = True

                elif event.key == pygame.K_KP1:
                    if chance%2==0:
                        s += 1
                        img_load("c.png", 5, 250)
                        chance += 1
                        K_KP1x = True
                    else:
                        s += 1
                        img_load("x.png", 5, 250)
                        chance += 1
                        K_KP1y = True

                elif event.key == pygame.K_KP2:
                    if chance%2==0:
                        s += 1
                        img_load("c.png", 135, 250)
                        chance += 1
                        K_KP2x = True
                    else:
                        s += 1
                        img_load("x.png", 135, 250)
                        chance += 1
                        K_KP2y = True

                elif event.key == pygame.K_KP3:
                    if chance%2==0:
                        s += 1
                        img_load("c.png", 250, 250)
                        chance += 1
                        K_KP3x = True
                    else:
                        s += 1
                        img_load("x.png", 250, 250)
                        chance += 1
                        K_KP3y = True        

        pygame.draw.line(screen, white, (120, 1), (120, 349))
        pygame.draw.line(screen, white, (240, 1), (240, 349))
        pygame.draw.line(screen, white, (1, 120), (349, 120))
        pygame.draw.line(screen, white, (1, 240), (349, 240))
        pygame.draw.line(screen, white, (1, 1), (1, 370))
        pygame.draw.line(screen, white, (1, 1), (349, 1))
        pygame.draw.line(screen, white, (349, 1), (349, 370))
        pygame.draw.line(screen, white, (1, 349), (349, 349))
        pygame.draw.line(screen, white, (1, 369), (349, 369))
        
        
        
        


        
        if K_KP7x and K_KP8x and K_KP9x:
            game_over_x()

        elif K_KP7y and K_KP8y and K_KP9y:
            game_over_y()

        elif K_KP1x and K_KP2x and K_KP3x:
            game_over_x()

        elif K_KP1y and K_KP2y and K_KP3y:
            game_over_y()

        elif K_KP4x and K_KP5x and K_KP6x:
            game_over_x()

        elif K_KP4y and K_KP5y and K_KP6y:
            game_over_y()

        elif K_KP7x and K_KP4x and K_KP1x:
            game_over_x()

        elif K_KP7y and K_KP4y and K_KP1y:
            game_over_y()

        elif K_KP8x and K_KP5x and K_KP2x:
            game_over_x()

        elif K_KP8y and K_KP5y and K_KP2y:
            game_over_y()

        elif K_KP9x and K_KP6x and K_KP3x:
            game_over_x()

        elif K_KP9y and K_KP6y and K_KP3y:
            game_over_y()

        elif K_KP7x and K_KP5x and K_KP3x:
            game_over_x()

        elif K_KP7y and K_KP5y and K_KP3y:
            game_over_y()

        elif K_KP9x and K_KP5x and K_KP1x:
            game_over_x()

        elif K_KP9y and K_KP5y and K_KP1y:
            game_over_y()

        elif s == 9:
            game_draw()

        if chance%2==0:
            pygame.draw.rect(screen, red, [130, 356, 100, 5])

        else:
            pygame.draw.rect(screen, blue, [130, 356, 100, 5])

        pygame.display.update()


game_intro()









        
