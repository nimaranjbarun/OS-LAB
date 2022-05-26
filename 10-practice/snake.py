import arcade
import random

class Game(arcade.Window) :
  SCALING = 0.5
  WIDTH = 800
  HEIGHT = 600
  TITLE = "Snake Game"
  BACKGROUND = arcade.color.BLACK
  SPEED = 1

  def __init__(self):
    super().__init__(width=self.WIDTH,height=self.HEIGHT,title=self.TITLE)
    self.background_color = self.BACKGROUND
    self.food = Apple()
    self.snake = Snake(self.SCALING)
  
  def setup(self):
    self.all_sprites_list = arcade.SpriteList()
    self.player_sprite =Snake(self.SCALING)
    self.player_sprite.center_x = 50
    self.player_sprite.center_y = 50
    self.all_sprites_list.append(self.player_sprite)

  def on_update(self, delta_time):
    self.all_sprites_list.update()
    self.snake.move()
    if arcade.check_for_collision(self.snake, self.food):
      self.food.center_x = random.randint(0, 600)
      self.food.center_y = random.randint(0, 800)
      self.snake.width += 20
      self.snake.height += 20

  def on_draw(self):
    arcade.start_render()  
    self.snake.draw() 
    self.food.draw() 
                            
  def on_key_press(self, key, modifiers):
    if key == arcade.key.UP: self.player_sprite.change_y = self.SPEED
    elif key == arcade.key.DOWN: self.player_sprite.change_y = -self.SPEED
    elif key == arcade.key.LEFT: self.player_sprite.change_x = -self.SPEED
    elif key == arcade.key.RIGHT: self.player_sprite.change_x = self.SPEED
        
  def on_key_release(self, key : int, modifiers: int):
    if (key == arcade.key.LEFT) and (self.snake.direction != "right") : self.snake.direction = "left"
    elif (key == arcade.key.DOWN) and (self.snake.direction != "up") : self.snake.direction = "down"  
    elif (key == arcade.key.RIGHT) and (self.snake.direction != "left") : self.snake.direction = "right"
    elif (key == arcade.key.UP) and (self.snake.direction != "down") : self.snake.direction = "up"

class Snake(arcade.Sprite) :
  def __init__(self,scale):
    super().__init__()
    self.color = arcade.color.WHITE
    self.width = 20
    self.height = 20
    self.speed = 2
    self.score = 0
    self.direction = "up"
    self.center_x = random.randint(0,300)
    self.center_y = random.randint(0,400)
    
  def draw(self) :
    arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)
    
  def move(self) :
    if    self.direction == "left": self.center_x -= 2
    elif  self.direction == "right": self.center_x += 2
    elif  self.direction == "up": self.center_y += 2
    elif  self.direction == "down": self.center_y -= 2  
    
class Apple(arcade.Sprite) :
  def __init__(self) :
    super().__init__()  
    self.center_x = random.randint(0, 600)
    self.center_y = random.randint(0, 800)
    txc = arcade.load_texture("sib.png")
    self.texture = txc
    self.scale = 0.09

  def on_draw(self):
    arcade.draw_texture_rectangle(self.center_x, self.center_y, 30, 30, self.texture)  
                       
mygame = Game()
mygame.setup()
arcade.run()


    
