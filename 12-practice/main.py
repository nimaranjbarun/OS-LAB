from os import remove
import random
import time
from turtle import title
import arcade
import threading


class SpaceShooter(arcade.Sprite) : 
    def __init__(self):
        super().__init__("spaceshooter.png")
        self.center_x = 960
        self.center_y = 200
        self.width = 250
        self.height = 250
        self.score = 0
        self.live = 5
        
    def move(self) : 
        self.center_x += self.change_x * 10
        
class Fire(arcade.Sprite) : 
    def __init__(self,x,y):
        super().__init__()
        self.width = 10
        self.height = 10 
        self.color = arcade.color.GREEN
        self.center_x = x
        self.center_y = y
        self.change_y = 1
                
    def draw(self) : 
        arcade.draw_circle_filled(self.center_x,self.center_y,5,self.color)
    
    def move(self) : 
        self.center_y += self.change_y * 15 
    # def move() : 
    
class Game(arcade.Window) : 
    def __init__(self) :
        super().__init__(width = 1920,height = 1080,title = "Game") 
        self.background_color = arcade.color.BLACK
        # self.image = arcade.load_texture("back.jpg")
        self.space_shooter = SpaceShooter()
        self.check = False
        self.SPEED = 5
        self.fire = [];
        self.enemies = []
        self.thread = threading.Thread(target = self.enemy_generator)
        self.thread.start() 
        self.lazer = arcade.load_sound("lazer.wav")
        self.destroy = arcade.load_sound("destroy.wav")
        
    def on_draw(self):
        arcade.start_render()
        if self.space_shooter.live > 0 : 
            #arcade.draw_lrwh_rectangle_textured(0,0,1920,1080,self.image)
            self.space_shooter.draw()
            if(self.check) : 
                for shoot in self.fire :
                    shoot.draw()
            for enemy in self.enemies :
                enemy.draw()
            tx = ""    
            for x in range(self.space_shooter.live) : 
                tx += "❤️"
                
            score_text = f"Score : {self.space_shooter.score}"
            arcade.draw_text(score_text,self.width - 400,self.height - 100,arcade.color.AERO_BLUE,45)
            live_text = f"Live : {tx}"
            arcade.draw_text(live_text,100,self.height - 100,arcade.color.AERO_BLUE,45)
        else : 
            # for enemy in self.enemies :
            #     self.enemies.remove(enemy)
            # for enemy in self.fire :
            #     self.fire.remove(enemy)
            # self.enemies = []
            # self.fire = []
            arcade.draw_text("Game Over",(self.width/2) -200,(self.height/2),arcade.color.AERO_BLUE,60)
        
            
    def enemy_generator(self) : 
        while True:
            self.enemies.append(Enemy())
            time.sleep(0.5)
        
    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT : self.space_shooter.change_x=1
        elif key == arcade.key.LEFT : self.space_shooter.change_x=-1
        elif key == arcade.key.SPACE : 
            self.fire.append(Fire(self.space_shooter.center_x,self.space_shooter.center_y))
            self.check = True
            arcade.play_sound(self.lazer,2,1,False)    
            
    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT: self.space_shooter.change_x=0
        elif key == arcade.key.LEFT : self.space_shooter.change_x=0
        
    def on_update(self, delta_time: float):
        self.space_shooter.move()
        if self.check : 
            for shoot in self.fire :
                shoot.move()
                
        for collection in self.fire :
            for enemy in self.enemies : 
                if arcade.check_for_collision(collection,enemy) : 
                    self.enemies.remove(enemy)
                    self.fire.remove(collection)
                    self.space_shooter.score +=1
                    arcade.play_sound(self.destroy,2,1,False)
                    
        for enemy in self.enemies :
            if (enemy.center_y < 0) :
                self.enemies.remove(enemy)
                self.space_shooter.live -= 1            
        for enemy in self.enemies :
            enemy.move()
                
class Enemy(arcade.Sprite) : 
    def __init__(self):
        super().__init__("spaceshooter.png")
        self.center_x = random.randint(0,1920)
        self.center_y = 1200
        self.width = 100
        self.height = 100
        self.change_y = 1
            
    def move(self) : 
        self.center_y -= self.change_y * 3
            
game = Game()
arcade.run()