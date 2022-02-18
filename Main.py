                                            #About This game and writters and this project: 
                            
                            #This Game using pygame and I write this codes in oop for university Project

                            #This Game is written by Amir Nemat pour.

#Help:
                                
'''Space invaders is a game that you have one ship to shut enemyships and win the game, if you shut enemyship for 3 times that ship is going out
i mean that ship is damage, if yo can damage all of them yo win the game, if yo can't damage all of them and they collision bottom of screen you
game over and lose the game.Let's play it.'''

'''Use a,d to move your ship to left or right--> a:go left   and   d:go right  /// and use space to shut enemies'''
#------------------------------------------------------------------------------------------------------------------------------------------------------

import pygame
import random
import math as m

pygame.init() #To use pygame orders
#--------------------------------------- Screen:
window = pygame.display.set_mode((800,600)) #Create window and that size -->  size:int=00, flags:int=0, depth:int=0, display:int =0

pygame.display.set_caption('Space Invaders') #Title of display window.
#--------------------------------------------------------------------- Icon:
game_icon = pygame.image.load('ship.png') #Load game icon --> Made by Amir Nematpour & Mahsa Esmaeil pour

pygame.display.set_icon(game_icon) #Display game icon
#-------------------------------------------------------
bullet_state = 'ready' #Bullet is ready for fire and fire mean bullet is move
#----------------------------------------------------- Main Ship:
class mainship:
    def draw(self,x,y):
        self.playerx = x
        self.playery = y
        mainship1 = pygame.image.load('spaceship.png') #Our ship in game to shoot enemies --> Downlod from flat icon
        window.blit(self.mainship1,(self.playerx,self.playery))
#------------------------------------------------------------- Enemy ship:
class enemyship:
    def draw(self,enemyship,enemyx,enemyy): #Draw enemies:
        self._enemyship = enemyship
        self._enemyx = enemyx
        self._enemyy = enemyy
        window.blit(self._enemyship,(self._enemyx,self._enemyy))
#-------------------------------------------------------------------------- Background:
background = pygame.image.load('background.png')
#--------------------------------------------------- Bullet:
class bullet:
    def bullet_fire(self,bulletx,bullety):
        global bullet_state
        bullet_state = 'fire' #State of bullet --> is ready or fire(move)
        bullet = pygame.image.load('bullet.png') #Draw bullet --> Downlod from flat icon
        self.bulletx = bulletx
        self.bullety = bullety
        window.blit(bullet,(self.bulletx + 16,self.bullety + 10)) #The bullet is ready in half of ship

    def bullet_move(self,bullety,bullety_change):
        global bullet_state
        self.bullety = bullety
        self.bullety_change = bullety_change
        if self.bullety <= 0: #If bullet go out from top of screen:
                self.bullety = 480 #Clean bullet and bring back bullet in 480.
                bullet_state = 'ready' #Change state to ready.

        if bullet_state is 'fire':
            bullet.bullet_fire(self,self.bulletx,self.bullety) #Draw bullet move with it's speed.
            self.bullety -= self.bullety_change #Bullet move by this speed.
#--------------------------------------------------------------------------------------------------- Run Game:
class game_play:
    def __init__(self,n):
        self.playerx = 370 #X is 800 --> 800/2 = 400 .... Our ship is 64px then --> 64/2 = 32 --> 400 - 32 =~ 370
        self.playery = 480 #Y is 600 --> Our ship distance from bottom: 600 - 480 = 120
        self.playerx_change = 0 #Ship move with this
        self.mainship1 = pygame.image.load('spaceship.png') #Our ship in game to shoot enemies --> Downlod from flat icon

        self.bulletx = 0 #Bullet replace in:
        self.bullety = 480
        self.bullet = pygame.image.load('bullet.png') #Draw bullet --> Downlod from flat icon
        self.bullety_change = 10 #Bullet speed

        self.score_value = 0
        self.font = pygame.font.Font('freesansbold.ttf',32) #Score font and size
        self.textx = 10 #Text score place:
        self.texty = 10

        self.enemyship = [] #This lists for number of enemies:
        self.enemyx = []
        self.enemyy = []
        self.enemyx_change = []
        self.enemyy_change = []
        self.num_enemies = n

        self._i = 0
        self._i1 = 0

        self.dict1 = {} #To add enemies when bullet collision them first:
        self.dict2 = {} #......second
        self.dict3 = {} #......third

    def add(self):
        for i in range(self.num_enemies): #Add enemies in lists
            self.enemyship.append(pygame.image.load('enemy.png')) #--> Downlod from flat icon
            self.enemyx.append(random.randint(0, 736))
            self.enemyy.append(random.randint(50,150))
            self.enemyx_change.append(1.5)
            self.enemyy_change.append(20)

    def show_score(self):
        score = self.font.render('Score: '+str(self.score_value),True,(255,255,255)) #Show score with font and color ,...... /// Color use rgb:red,green,blue
        window.blit(score,(self.textx,self.texty))

    def contact(self,i): #Contact bullet with enemies:
        self._i = i
        distance = m.sqrt(pow(self.enemyx[self._i] - self.bulletx,2)+pow(self.enemyy[self._i] - self.bullety,2)) #Distance of bullet and enemy ship.
        if distance < 22:
            return True
        else:
            return False

    def live(self,i): #Kill Enemy:
        self._i1 = i
        if self._i1 not in self.dict1: #First Shut
            self.dict1[self._i1] = 2
        else: #Second shut
            if self._i1 in self.dict2: #Third shut
                self.dict3[self._i1] = 0
            else:
                self.dict2[self._i1] = 1

    def game_over_text(self):
        game_over_font = pygame.font.Font('freesansbold.ttf',70) #Game over font and size.
        game_over_text = game_over_font.render('Game Over!',True,(255,255,255)) #Game over with font and color.
        window.blit(game_over_text, (200,250))

    def run_game(self):
        global bullet_state
        run = True
        game_play.add(self)

        while run: #Window is still open and not close.
            '''This loop is use for close window if run = False loop is end and close the window.'''

            window.blit(background,(0,0)) #Draw background

            mainship.draw(self,self.playerx,self.playery) #Draw mainship

            for event in pygame.event.get(): #Get events of pygame.

                if event.type == pygame.QUIT: #For close window
                    run = False

                if event.type == pygame.KEYDOWN: #If user push anykey:
                    if event.key == pygame.K_a: #If push key is left arrow:
                        self.playerx_change = -4 #Move -0.2 to left

                    if event.key == pygame.K_d: #If push key is right arrow:
                        self.playerx_change = 4 #Move +0.2 to rihgt

                    if event.key == pygame.K_SPACE: #If player push space ship is fire
                        if bullet_state is 'ready':
                            self.bulletx = self.playerx #Bullet is ready in mainship.
                            bullet.bullet_fire(self,self.playerx,self.bullety) #Bullet is ready in ship place(playerx,bullety) and fire.

                if event.type == pygame.KEYUP: #If user leave buttom:  This for ship not move when we keyup.
                    if event.key == pygame.K_a or event.key == pygame.K_d: #If key is left or right:
                        self.playerx_change = 0 #Change is 0 and ship is'nt move.

            self.playerx += self.playerx_change #Ship is move.
            game_play.show_score(self)

            #Ship is'nt go out of screen.
            if self.playerx <= 0: #If ship go to left after 0 this clean ship and replace ship in 0:
                self.playerx = 0

            elif self.playerx >= 736: #If ship go to right after 736(because our ship is 64px --> 800-64=736) this clean ship and replace ship in 736:
                self.playerx = 736
            
            for i in range(self.num_enemies):
                self.enemyx[i] += self.enemyx_change[i] #Enemy is move

                #Enemy is'nt go out of screen and go down:

                if self.enemyx[i] <= 0: #If senemy go to left after 0 this clean enemy and replace ship in 0:
                    self.enemyx_change[i] = 1.5 #Go to right
                    self.enemyy[i] += self.enemyy_change[i] #To go down when ship arrive left side of screen

                elif self.enemyx[i] >= 736:
                    self.enemyx_change[i] = -1.5 #Go to left
                    self.enemyy[i] += self.enemyy_change[i] #To go down when ship arrive Right side of screen

                #Collision:
                collision = game_play.contact(self,i)
                if collision:
                    self.bullety = 480 #Get back bullet in it's place
                    bullet_state = 'ready' #After shut state is ready
                    self.score_value += 1 #After one collision score is increase

                    game_play.live(self,i)

                    if i in self.dict3: #If 3 lives of each enemy ship is finish there are add to dict3
                        self.enemyx[i] = 2000 #To Remove each enemy ship if it's lives finished.
                        self.enemyy[i] = 2000

                enemyship.draw(self,self.enemyship[i],self.enemyx[i],self.enemyy[i]) #Draw enemy ships.

                if i not in self.dict3:
                    if self.enemyy[i] > 440: #If enemy ships arrived to y = 440:
                        for j in range(self.num_enemies): #All enemies left on window
                            self.enemyy[j] = 3000 #Go out of window
                        game_play.game_over_text(self) #Show game over text
                        break

            #Bullet move:
            bullet.bullet_move(self,self.bullety,self.bullety_change)

            pygame.display.update() #For update window every second

n = int(input("How many enemies do yo want:"))

#Run Game:
if __name__ == '__main__':
    run = game_play(n)
    run.run_game()
