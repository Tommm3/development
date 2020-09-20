from random import randint
from math import sqrt

from kivy.app import App
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.graphics import Line, InstructionGroup, Color
from math import atan, pi, tan, radians, sin, cos,sqrt

class DynamicPaddle(Widget):
    velocity_x_temp = 0
    def bounce_ball(self, ball, x_init, y_init, x_last, y_last):
        if self.collide_widget(ball):
            self.velocity_x_temp = ball.velocity_x
            if (x_init-x_last) > 0:
                print(ball.velocity, (y_init-y_last)/(x_init-x_last))
                ball.velocity_x *= cos(2*atan((y_init-y_last)/(x_init-x_last)))
                ball.velocity_y = sqrt((ball.velocity_y**2+self.velocity_x_temp**2) - ball.velocity_x**2)

class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # Latest Position = Current Velocity + Current Position
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


# Update - moving the ball by calling the move() and other stuff
class PongGame(Widget):
    ball = ObjectProperty(None)
    paddle = ObjectProperty(None)
    x_init = 0
    y_init = 0
    x_last = 0
    y_last = 0
    isLine = False

    def serve_ball(self):
        self.ball.velocity = Vector(4, 0).rotate(randint(0, 360))

    def update(self, dt):
        self.ball.move()

        # bounce off top and bottom
        if (self.ball.y < 0) or (self.ball.y > self.height - 50):
            self.ball.velocity_y *= -1

        # bounce off left and increase the score
        if self.ball.x < 0:
            self.ball.velocity_x *= -1

        # bounce off right
        if self.ball.x > self.width - 50:
            self.ball.velocity_x *= -1

        self.paddle.bounce_ball(self.ball,self.x_init,self.y_init,self.x_last,self.y_last)

    def on_touch_down(self, touch):
        self.x_init = touch.x
        self.y_init = touch.y


    def on_touch_move(self, touch):
        # print(self.x_init, self.y_init, self.x_last, self.y_last)
        if sqrt((self.x_init-touch.x)**2 + (self.y_init-touch.y)**2)>150 and self.isLine==False:
            self.isLine = True
            self.x_last = touch.x
            self.y_last = touch.y
            self.paddle.x = touch.x
            self.paddle.y = touch.y
            self.paddle.width = self.x_init
            self.paddle.height = self.y_init

    def on_touch_up(self, touch):
        self.isLine = False

class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

PongApp().run()
