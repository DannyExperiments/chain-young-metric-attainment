"""Render the two-run optimal transport example from a rotating 3D viewpoint."""

from math import cos, sin, tau
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 800, 465
BACKGROUND, PANEL, WHITE, MUTED = "#111a2a", "#18273c", "#f2f7ff", "#b3c3db"
KEEP, PUSH = "#79e2cc", "#ffc291"
NODE_COLORS = {"A": "#9ebbff", "B": "#e8c2fb"}
NODES = [
    ("A", (-1.32, 0, 1.00)), ("B", (1.32, 0, 1.00)),
    ("B", (-1.32, 0, -1.00)), ("A", (1.32, 0, -1.00)),
]
EDGES = [(0, 2, PUSH, -.22, 1/6), (1, 3, PUSH, .22, 1/6),
         (0, 3, KEEP, .42, 1/3), (1, 2, KEEP, -.42, 1/3)]


def font(name, size):
    try:
        return ImageFont.truetype(name, size)
    except OSError:
        return ImageFont.load_default(size=size)


def project(xyz, angle):
    x, y, z = xyz
    side = x * cos(angle) - y * sin(angle)
    depth = x * sin(angle) + y * cos(angle)
    vertical = z * cos(.24) - depth * sin(.24)
    camera_depth = depth * cos(.24) + z * sin(.24)
    zoom = 7 / (7 - camera_depth)
    return (400 + side * 135 * zoom, 230 - vertical * 69 * zoom), camera_depth, zoom


def strand(start, end, bend, angle):
    points = []
    for index in range(31):
        t = index / 30
        xyz = ((1-t)*start[0]+t*end[0], 4*t*(1-t)*bend, (1-t)*start[2]+t*end[2])
        points.append(project(xyz, angle)[0])
    return points


def draw_frame(angle, fonts):
    title, normal, labels, strong = fonts
    image = Image.new("RGB", (WIDTH, HEIGHT), BACKGROUND)
    draw = ImageDraw.Draw(image)
    draw.text((26, 24), "The chain Young metric", font=title, fill=WHITE)
    draw.text((28, 75), "AB to BA  •  Run length 1/2  •  Letter distance 1/3", font=normal, fill=MUTED)
    draw.rounded_rectangle((26, 111, 774, 350), 12, fill=PANEL)
    draw.text((43, 128), "SOURCE", font=labels, fill=MUTED)
    draw.text((43, 318), "TARGET", font=labels, fill=MUTED)
    for first, last, color, bend, amount in EDGES:
        draw.line(strand(NODES[first][1], NODES[last][1], bend, angle),
                  fill=color, width=round(3+30*amount), joint="curve")
    nodes = [(label, *project(xyz, angle)) for label, xyz in NODES]
    for label, (x,y), _, zoom in sorted(nodes, key=lambda n:n[2]):
        r=17*zoom
        draw.ellipse((x-r,y-r,x+r,y+r), fill=NODE_COLORS[label], outline=BACKGROUND, width=2)
        draw.text((x,y+1), label, font=labels, fill=BACKGROUND, anchor="mm")
    draw.text((28, 362), "Relabel 1/6 twice", font=normal, fill=PUSH)
    draw.text((372, 362), "Swap two blocks of length 1/3", font=normal, fill=KEEP)
    draw.text((28, 409), "Optimal cost  2/9 = 1/9 + 1/9", font=strong, fill=WHITE)
    return image


def main():
    fonts = (font("Arial Bold.ttf", 46), font("Arial.ttf", 27), font("Arial Bold.ttf", 23), font("Arial Bold.ttf", 32))
    frames = [draw_frame(-.13 + tau*i/80, fonts) for i in range(80)]
    frames[0].save(Path(__file__).with_name("transport.gif"), save_all=True,
                   append_images=frames[1:], duration=87, loop=0, optimize=False)


if __name__ == "__main__":
    main()
