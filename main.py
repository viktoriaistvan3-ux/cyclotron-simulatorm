from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color
from kivy.clock import Clock

class CyclotronWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.xp = 0
        self.yp = 0
        self.vx = 0
        self.vy = 200
        self.B = 1.2
        self.qm = 9.58e7
        self.dt = 0.01

        with self.canvas:
            Color(0, 1, 0)
            self.line = Line(points=[])

        Clock.schedule_interval(self.update, 1/60)

    def update(self, dt):
        ax = self.qm * self.vy * self.B
        ay = -self.qm * self.vx * self.B

        self.vx += ax * self.dt
        self.vy += ay * self.dt

        self.xp += self.vx * self.dt
        self.yp += self.vy * self.dt

        cx, cy = self.center
        self.line.points += [cx + self.xp*0.01, cy + self.yp*0.01]

class CyclotronApp(App):
    def build(self):
        return CyclotronWidget()

CyclotronApp().run()
