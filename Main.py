# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pygame",
#   "os",
#   "random",
#   "math",
#   "sys",
# ]
# ///

#####################################################

import pygame
from pygame.locals import QUIT
import os
import random
import math
import sys

###################################################




#Pre-defintions: (remove if unwanted, added for consideration.)

###################################################
#Colours:
##################################################
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255,255,0)
BLUE = (0,0,255)
################################################
abs_cwd_path_ts = os.path.abspath(os.getcwd())
################################################

# GLOBAL VARIABLES:
##########################

### GAME DESCRIPTIVE:
Author = ""
co-Author = []
Title = ""
Genre = ""
Decription = ""
Y_O_R = ""
M_O_R = ""
D_O_R = ""
Contact = []
Rating_Age = ""

### GAME MECHANICAL:
dt = 0 # Delta Time/Step-Up Clock

### GAME SCENES/ROOMS:
SPLASH = True # Splash Window
MENU = False # Menu Window
ROOM = False # Room Placeholder

### Room: ROOM. defintions:
room_ROOM_width = 1920
room_ROOM_height = 1080
Max_Entities = 50
IN_GAME_TIME = "00:00"

################################################

### GAME SPLASH SCREEN OBJECT - For branding
class splash(pygame.sprite.Sprite): 
   def __init__(self, x, y, *groups): # Intialisation/defintions
      super().__init__(*groups) 
      self.img_org = pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs/COMPANY_ASSETS/","###-SPLASH_PLACEHOLDER.FILE-###")))

#     self.img_org = pygame.image.load(abs_cwd_path_ts+os.path.join("/imgs/COMPANY_ASSETS/","###-SPLASH_PLACEHOLDER.FILE-###")))  - With Pre-Defined PATH Variable

      self.image = self.img_org # Set Default image
      self.rect = self.image.get_rect() # Set Colision Rectangle
      self.rect.x = x # Rect X
      self.rect.y = y # Rect Y

      self.dt = 0 # Life Timer, used to destroy and continue progression.

   def update(self): # Behaviour loop
         self.dt + 1 # Life timer
         if self.dt > 3: # After 3 ticks 
            global SPLASH, MENU # access in game Variables
            MENU = True # Change Scene
            SPLASH = False # End Scene
         pass

###########################################################################################################################################

### Classes/Objects (in-Game):

class Object_0(pygame.sprite.Sprite): ### Object Template, showing features one can add to object to define the objects nature and interactions (Non-playable Character Ver.)
   def __init__(self, x, y, *groups): # Intialisation/defintions
      super().__init__(*groups) 

      ## Primary image placeholder:
      self.img_org =[pygame.image.load(abs_cwd_path_ts+os.path.join("/imgs","####-INSERT_NAME_HERE-####.png"))),    
         abs_cwd_path_ts+os.path.join("/imgs","####-INSERT_NAME_HERE_2-####.png")))] # - List Placeholder for second (or more) images for animation # All With Pre-Defined PATH Variable

      ## Secondary image placeholders:
      self.img_attack = [pygame.image.load(abs_cwd_path_ts+os.path.join("/imgs","####-ATTACK_0-####.png"))),    
         abs_cwd_path_ts+os.path.join("/imgs","####-ATTACK_1-####.png"))),
         abs_cwd_path_ts+os.path.join("/imgs","####-ATTACK_2-####.png")))]
     
      self.image_death = pygame.image.load(abs_cwd_path_ts+os.path.join("/imgs","####-CORPSE-####.png")))

     ## Image Loading: (init)
      self.image = self.img_org[0] # Set Default image
      self.img_pre_render = 0
     
     ## Object Boundaries/Collision:
      self.rect = self.image.get_rect()# Set Colision Rectangle
      self.rect.x = x # Rect X
      self.rect.y = y # Rect y

      # States:
      self.alert = False # whether the object is alerted
      self.moving = False # whether the object is moving
      self.attacking = False # whether the object is attacking
      self.dead = False # whether object is dead
      
      # Animation Mechanics 
      self.max_frames = len(self.img_pre_render)
      self.current_frame = 0 ## current frame for animation
      self.animation_time = 0.1 ## threshold for next frame (time)
      self.current_time = 0 ## current timing for animation

      # Locals
      self.target = 0 ## chasing this object or coordinate
      self.health = 100 # object life
      self.speed = 3 # object speed
      self.value = 20 # object value
      self.inventory = [] # object invetory
      self.hostile = False # object temperament
      self.damage = 5 # base damage
      self.debuff = 2 # base draw back
      self.damage_calc = 0 # varaible for calculation
      # ... etc etc

   def update(self, dt): # Main behaviour loop

      ## Animation/Image_edit:
      self.image = self.img_pre_render
    
   ## LIFE 
   if self.health <= 0:
        self.death = True

  if self.death == False: # Check if Alive/Active
       
      # Make instance rotate around point (define point by px,py)
      px,py = self.target.x,self.target.y # center point of rotation
      rel_x, rel_y = round(px - self.rect.x), round(py - self.rect.y) # find difference between target and rect coordinates
      angle = round((180/math.pi)*+math.atan2(rel_x,rel_y)) # Trignometery for rotation
      self.image = pygame.transform.rotate(self.image_clean,angle) # rotate image
      
      self.rect = self.image.get_rect(center=self.rect.center) # set new boundary

     
      if self.current_frame >= self.max_frame: # Animation Frame loop
          self.current_frame = 0
      
     
         if self.moving == True or self.attacking == True: # Animation Trigger
            if self.moving == True :
                self.img_pre_render = self.img_org # set image pre_render variable to orginal animation
            if self.attacking == True:
                self.img_pre_render = self.img_attack # set image pre_render variable to attack animation
            self.current_time += dt ## Increase animation time
            if self.current_time >= self.animation_time:
                self.current_time = 0 # timing for the animation
                self.current_frame = (self.current_frame + 1) % len(self.img_pre_render) # increase animation step until at max frame
            else:
               self.current_time = 0 # reset
               self.current_frame = 0 # reset
     else:
       self.img_pre_render = self.img_death # Set to dead sprite

    ## Add more functionality Here:
    ## i.e.:
    if self.target != 0:
      if self.attacking == True:
        if self.current_frame = 3: # Placeholder number, edit for your needs.
          self.debuff = self.debuff + (self.debuff*self.target.damage)
          self.damage_calc = self.damage/self.debuff
          self.target.life -= self.damage_calc
  
  pass


class Object_1(pygame.sprite.Sprite): ### Object Template, showing features one can add to object to define the objects nature and interactions (playable Character Ver.)
   def __init__(self, x, y, *groups): # Intialisation/defintions
      super().__init__(*groups) 

      ## Primary image placeholder:
      self.img_org =[pygame.image.load(abs_cwd_path_ts+os.path.join("/imgs","####-INSERT_NAME_HERE-####.png"))),    
         abs_cwd_path_ts+os.path.join("/imgs","####-INSERT_NAME_HERE_2-####.png")))] # - List Placeholder for second (or more) images for animation # All With Pre-Defined PATH Variable

      ## Secondary image placeholders:
      self.img_attack = [pygame.image.load(abs_cwd_path_ts+os.path.join("/imgs","####-ATTACK_0-####.png"))),    
         abs_cwd_path_ts+os.path.join("/imgs","####-ATTACK_1-####.png"))),
         abs_cwd_path_ts+os.path.join("/imgs","####-ATTACK_2-####.png")))]
     
      self.image_death = pygame.image.load(abs_cwd_path_ts+os.path.join("/imgs","####-CORPSE-####.png")))

     ## Image Loading: (init)
      self.image = self.img_org[0] # Set Default image
      self.img_pre_render = 0
     
     ## Object Boundaries/Collision:
      self.rect = self.image.get_rect()# Set Colision Rectangle
      self.rect.x = x # Rect X
      self.rect.y = y # Rect y

      # States:
      self.alert = False # whether the object is alerted
      self.moving = False # whether the object is moving
      self.attacking = False # whether the object is attacking
      self.dead = False # whether object is dead
      
      # Animation Mechanics 
      self.max_frames = len(self.img_pre_render)
      self.current_frame = 0 ## current frame for animation
      self.animation_time = 0.1 ## threshold for next frame (time)
      self.current_time = 0 ## current timing for animation

      # Locals
      self.health = 100 # object life
      self.speed = 3 # object speed
      self.value = 20 # object value
      self.inventory = [] # object invetory
      self.hostile = False # object temperament
      self.damage = 5 # base damage
      self.debuff = 2 # base draw back
      self.damage_calc = 0 # varaible for calculation
      # ... etc etc

   def update(self, dt): # Main behaviour loop

      ## Animation/Image_edit:
      self.image = self.img_pre_render
    
   ## LIFE 
   if self.health <= 0:
        self.death = True

  if self.death == False: # Check if Alive/Active

      keys = pygame.key.get_pressed()
      if keys[pygame.K_w] or keys[pygame.K_UP]:
        if player.rect.y < room_ROOM_height and player.rect.y >= 0:
                           self.rect.y -= 2
     elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        if player.rect.x < room_ROOM_width and player.rect.y >= 0:
                           self.rect.x += 2
     elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
        if player.rect.x < room_ROOM_width and player.rect.y >= 0
                           self.rect.x -= 2
     elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
                           self.rect.y += 2
       
      # Make instance rotate around point (define point by px,py)
      mx,my = = pygame.mouse.get_pos() # center point of mouse (assuming this game is a top-down or requires the player to face the mouse)
      rel_x, rel_y = round(mx - self.rect.x), round(my - self.rect.y) # find difference between mouse and rect coordinates
      angle = round((180/math.pi)*+math.atan2(rel_x,rel_y)) # Trignometery for rotation
      self.image = pygame.transform.rotate(self.image_clean,angle) # rotate image
      
      self.rect = self.image.get_rect(center=self.rect.center) # set new boundary

     
      if self.current_frame >= self.max_frame: # Animation Frame loop
          self.current_frame = 0
      
     
         if self.moving == True or self.attacking == True: # Animation Trigger
            if self.moving == True :
                self.img_pre_render = self.img_org # set image pre_render variable to orginal animation
            if self.attacking == True:
                self.img_pre_render = self.img_attack # set image pre_render variable to attack animation
            self.current_time += dt ## Increase animation time
            if self.current_time >= self.animation_time:
                self.current_time = 0 # timing for the animation
                self.current_frame = (self.current_frame + 1) % len(self.img_pre_render) # increase animation step until at max frame
            else:
               self.current_time = 0 # reset
               self.current_frame = 0 # reset
     else:
       self.img_pre_render = self.img_death # Set to dead sprite

    ## Add more functionality Here:
    ## i.e.:
    if self.target != 0:
      if self.attacking == True:
        if self.current_frame = 3: # Placeholder number, edit for your needs.
          self.debuff = self.debuff + (self.debuff*self.target.attack)
          self.damage_calc = self.damage/self.debuff
          self.target.life -= self.damage_calc
  
  pass




#
# ... add more OBJECTS
#

########################################################################################################################################

# Initialize Pygame
pygame.init()
# Pygame/Game intialisation
width, height = 960, 540 # Default APR: 16:9 1.777, RESO DIMEN: 960 x 540 px (1920 x 1080 % 2), scale resolution by 2.
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("GAME_NAME") ## Change Game title name here
clock = pygame.time.Clock()
running = True

#Visual intialisation
#Groups:
Splash = pygame.sprite.Group()
Player = pygame.sprite.Group()
Enemy = pygame.sprite.Group()
# Branding Objects:
Company_branding = splash(0,0,Splash)
# Game Objects:
NPC = Object_0(rand_random(room_ROOM_width),rand_random(room_ROOM_width),Enemy) # Spawns ONE enemy at random location
Player = Object_1(10,10,Player) # Spawns player at x:10, y:10 
# Multi-Spawner
i ++
if i < Max_Entities:
  NPC_MULTI.append(NPC = Object_0(rand_random(room_ROOM_width),rand_random(room_ROOM_width),Enemy))




## For device touch mechaninics:
#fingers = [] # Touch Register

# Primary Game Loop:
async def main():
    #Globals (to reach inside game loop):
    global dt
    #Event System/Control System:
    while running:
     for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()
            sys.exit()
      # ...
      # ...
      ## For device touch mechaninics:
      #  if event.type == pygame.FINGERDOWN:
      #      x = event.x * screen.get_height()
      #      y = event.y * screen.get_width()
      #      fingers[event.finger_id] = x, y
      #  if event.type == pygame.FINGERUP:
      #      fingers.pop(event.finger_id, None)  


    ## Scene Hyirachy:
    if SPLASH == True:
        screen.blit(Sphinixx,(0,0)) # Small image for publicity 
      pass # Splash screen for Branding
    if MENU == True:
       pass # Menu to select features
    if ROOM == True:
      screen.blit(NPC) # Render NPC
      screen.blit(Player) # Render Player
      screen.blit(NPC_MULTI) # Render Multi-spawned NPCs
      NPC.draw(screen) # Draw Enemy
      Player.draw(screen) # Draw Player
      NPC_MULTI.draw(screen) # Draw multiple enemies
      # ...
       pass # Main game room


    ## Final Render/Utility/Debug
    dt = clock.tick(60)/1000 # Delta Time counting up from tik
    print(dt)
    pygame.display.flip() # Display render for PyGBag
    await asyncio.sleep(0)  # Very important, and keep it 0
 
asyncio.run(main()) ## run program