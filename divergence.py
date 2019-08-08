from manimlib.imports import *


class Setup(Scene):
    CONFIG = {
        "color_list": ['#e22b2b', '#e88e10', '#eae600', '#88ea00',
                       '#00eae2', '#0094ea', "#2700ea", '#bf00ea', '#ea0078'],
        "prop": 0
    }

    def construct(self):
        axes_config = {"x_min": -5,
                       "x_max": 5,
                       "y_min": -5,
                       "y_max": 5,
                       "z_axis_config": {},
                       "z_min": -1,
                       "z_max": 1,
                       "z_normal": DOWN,
                       "num_axis_pieces": 20,
                       "light_source": 9 * DOWN + 7 * LEFT + 10 * OUT,
                       "number_line_config": {
                           "include_tip": False,
                       },
                       }

        axes = Axes(**axes_config)
        f = VGroup(
            *[self.calc_field_color(x * RIGHT + y * UP, self.vect, prop=0)
              for x in np.arange(-5, 6, 1)
              for y in np.arange(-5, 6, 1)
              ]
        )

        field = VGroup(axes, f)
        # field.scale(0.6)

        c = ParametricFunction(
            self.func,
            t_min=0,
            t_max=2*PI,
            stroke_width=1.5 * DEFAULT_STROKE_WIDTH,
        )

        curve = c

        field.set_fill(opacity=0.75)
        field.set_stroke(opacity=0.75)

        self.play(ShowCreation(field))
        self.wait()

        self.play(Write(curve))
        self.wait()

        # self.play(Write(surface))
        # self.wait()

    def calc_field_color(self, point, f, prop=0.0, opacity=None):
        x, y = point[:2]
        func = f(x, y)
        magnitude = math.sqrt(func[0] ** 2 + func[1] ** 2)
        func = func / magnitude if magnitude != 0 else np.array([0, 0])
        func = func / 1.5
        v = int(magnitude / 10 ** prop)
        index = len(self.color_list) - 1 if v > len(self.color_list) - 1 else v
        c = self.color_list[index]
        v = Vector(func, color=c).shift(point)
        if opacity:
            v.set_fill(opacity=opacity)
        return v

    @staticmethod
    def vect(x, y):
        return np.array([
            x*y+x,
            x+y,
            0
        ])

    @staticmethod
    def func(t):
        return np.array([
            math.cos(t),
            math.sin(t),
            0
        ])

    @staticmethod
    def surface(t, v):
        return np.array([
            1 - 2*t**2 + 2,
            v*(t**3 - 4*t),
            0
        ])

class Test(Scene):
    def construct(self):
        eq = TexMobject(r"\oiint_S \vec{F} \cdot d \vec{S} = \iiint_V \nabla \times \vec F\,dV")
        eq.scale(1.5)
        
        self.play(Write(eq))
        self.wait()
