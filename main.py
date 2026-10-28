__version__ = "1.0.0"

import random
from math import hypot

from kivy.app import App
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Ellipse, Rectangle


class HammerGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.score = 0
        self.radius = dp(30)
        self.target_x = 0
        self.target_y = 0
        self.score_label = Label(
            text="امتیاز: 0",
            font_size="24sp",
            bold=True,
            color=(0.05, 0.08, 0.05, 1),
            size_hint=(None, None),
            size=(dp(180), dp(50)),
            pos_hint={"x": 0.02, "top": 0.99},
        )
        self.add_widget(self.score_label)
        self.bind(size=self._layout_game, pos=self._layout_game)
        with self.canvas:
            self.bg_color = Color(0.20, 0.70, 0.31, 1)
            self.bg = Rectangle(pos=self.pos, size=self.size)
            self.target_color = Color(0.86, 0.12, 0.16, 1)
            self.target = Ellipse(pos=(0, 0), size=(self.radius * 2, self.radius * 2))
        self._layout_game()

    def _layout_game(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size
        if self.width > self.radius * 2 and self.height > self.radius * 2:
            if self.target_x == 0 and self.target_y == 0:
                self._move_target()
            else:
                self._keep_target_in_bounds()

    def _keep_target_in_bounds(self):
        r = self.radius
        self.target_x = min(max(self.target_x, self.x + r), self.right - r)
        self.target_y = min(max(self.target_y, self.y + r), self.top - r)
        self.target.pos = (self.target_x - r, self.target_y - r)

    def _move_target(self):
        r = self.radius
        if self.width <= 2 * r or self.height <= 2 * r:
            return
        self.target_x = random.uniform(self.x + r, self.right - r)
        # Keep target below the score label where possible.
        lower = self.y + r
        upper = self.top - dp(80)
        if upper <= lower:
            upper = self.top - r
        self.target_y = random.uniform(lower, max(lower, upper))
        self.target.pos = (self.target_x - r, self.target_y - r)

    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos):
            return super().on_touch_down(touch)
        if hypot(touch.x - self.target_x, touch.y - self.target_y) <= self.radius:
            self.score += 1
            self.score_label.text = f"امتیاز: {self.score}"
            self._move_target()
            return True
        return super().on_touch_down(touch)


class HammerGameApp(App):
    title = "بازی چکش‌زدن"

    def build(self):
        root = FloatLayout()
        root.add_widget(HammerGame())
        return root


if __name__ == "__main__":
    HammerGameApp().run()
