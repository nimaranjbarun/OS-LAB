import arcade
import random

class Ball(arcade.Sprite):

    def __init__(self):
        super().__init__()
        self.color=arcade.color.RED
        self.r=15
        self.width=22
        self.height=22
        self.screen_height=960/2
        self.hitter=1
        self.first_time=True

    def reset_pos(self):
        self.center_x = (960/2)
        self.center_y = (540/2)
        self.change_x = random.choice([-1, 1])
        self.change_y = random.choice([-1, 1])

    def check_collisions(self, paddle_list):
        if self.left <= 0 or self.right >= 960:
            self.change_x = 0
            self.change_y = 0
        
        if self.top > 540: self.change_y = -1
        if self.bottom < 0: self.change_y = 1
        
        hits = self.collides_with_list(paddle_list)
        
        if hits:
            if self.center_x < 960/2 and self.change_x == -1: self.change_x = 1
            elif self.center_x > 960/2 and self.change_x == 1: self.change_x = -1

    def update(self, paddle_list):
        self.center_x += (5 * self.change_x)
        self.center_y += (5 * self.change_y)
        self.check_collisions(paddle_list)
        
    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,self.r,self.color)

class Paddle(arcade.Sprite):
    
    def __init__(self):
        super().__init__()
        self.color=arcade.color.BLACK
        self.width = 30
        self.height=60
        self.score=0
    
    def reset_pos(self, x, y):
        self.center_x = x
        self.center_y = y
        
    def check_bounds(self):
        if self.top > 540 and self.change_y == 1: self.change_y = 0
        if self.bottom < 0 and self.change_y == -1: self.change_y = 0
        
    def update(self):
        self.check_bounds()
        self.center_y += (5 * self.change_y)

    def draw (self):
         arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color) 
    
class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(960, 540, "ping pong")
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.ball = Ball()
        self.ball.reset_pos()
        self.paddles = arcade.SpriteList()
        self.paddle_1 = Paddle()
        self.paddle_1.reset_pos(self.paddle_1.width, 540/2)
        self.paddles.append(self.paddle_1)
        self.paddle_2 = Paddle()
        self.paddle_2.reset_pos(960 - self.paddle_2.width, 540/2)
        self.paddles.append(self.paddle_2)
        self.hit_upper_wall=False
        self.hit_lower_wall=False
        self.down_press=True
        self.up_press=True

    def on_draw(self):
        arcade.start_render()
        self.ball.draw()
        self.paddle_1.draw()
        self.paddle_2.draw()
        score_text = f"{self.paddle_1.score} : {self.paddle_2.score}"
        arcade.draw_text(score_text,(self.width/2),self.height-100,arcade.color.BLACK,25,font_name=("Times New Roman","Times","Liberation Serif"))

    def on_update(self, delta_time):
        if (self.ball.center_x > 940): 
            self.paddle_1.score += 1
            self.ball.reset_pos()
        if( self.ball.center_x-20 < 0): 
            self.paddle_2.score += 1
            self.ball.reset_pos()
        self.paddle_1.update()
        self.bot_move()
        self.paddle_2.update()
        self.ball.update(self.paddles)

    def bot_move(self):
        if self.ball.center_y != self.paddle_2.center_y: self.paddle_2.change_y = self.ball.change_y
        else: self.paddle_2.change_y = 0

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP : self.paddle_1.change_y=1
        elif key == arcade.key.DOWN : self.paddle_1.change_y=-1

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP: self.paddle_1.change_y=0
        elif key == arcade.key.DOWN : self.paddle_1.change_y=0

MyGame()
arcade.run()