from manim import *

class MatrixRank(ThreeDScene):
    def construct(self):
        # Axes setup
        axes = ThreeDAxes(x_range=[-2, 2], y_range=[-2, 2], z_range=[-2, 2])
        labels = axes.get_axis_labels(x_label="x", y_label="y", z_label="z")
        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES)
        self.add(axes, labels)

        # --- Case 1: Rank = 1 (one vector) ---
        v1 = np.array([1, 1, 0])
        vec1 = Arrow3D(start=ORIGIN, end=v1, color=BLUE)
        text1 = Text("Rank = 1: Line").scale(0.5).to_corner(UL)
        self.play(GrowArrow(vec1), Write(text1))
        self.wait(2)

        # --- Case 2: Rank = 2 (two independent vectors) ---
        v2 = np.array([1, -1, 0])
        vec2 = Arrow3D(start=ORIGIN, end=v2, color=GREEN)
        plane = Polygon(ORIGIN, v1, v1 + v2, v2, color=YELLOW, fill_opacity=0.3)
        self.play(GrowArrow(vec2))
        self.wait(1)
        self.play(Create(plane))
        self.play(Transform(text1, Text("Rank = 2: Plane").scale(0.5).to_corner(UL)))
        self.wait(2)

        # --- Case 3: Rank = 3 (three independent vectors) ---choco install ffmpeg
        v3 = np.array([0, 0, 1])
        vec3 = Arrow3D(start=ORIGIN, end=v3, color=RED)
        cube = Cube(side_length=1.5, color=WHITE, fill_opacity=0.05)
        self.play(GrowArrow(vec3))
        self.wait(1)
        self.play(FadeIn(cube))
        self.play(Transform(text1, Text("Rank = 3: Full 3D Space").scale(0.5).to_corner(UL)))
        self.wait(2)

        self.play(FadeOut(VGroup(vec1, vec2, vec3, plane, cube, text1, axes, labels)))
        self.wait(1)
