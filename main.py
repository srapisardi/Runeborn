from ursina import *
from math import atan2, pi

app = Ursina()

# --- Basic Scene Setup ---
window.title = 'Runeborn RPG'
window.borderless = False
window.fullscreen = False
window.exit_button.visible = True
window.fps_counter.enabled = True

# Ground plane with grass texture
ground = Entity(
    model='plane',
    texture='grass',   # Built-in grass texture
    scale=(20, 1, 20),
    collider='box'
)

# Player entity
player = Entity(model='cube', color=color.azure, scale_y=1.2, position=(0, 0.6, 0), collider='box')

# Camera setup (top-down view)
camera.parent = None
camera.position = (0, 20, -0.1)
camera.rotation_x = 90
camera.fov = 100

# --- Movement Settings ---
speed = 5


def update():
    move_x = (held_keys['d'] - held_keys['a']) * time.dt * speed
    move_z = (held_keys['w'] - held_keys['s']) * time.dt * speed

    player.x += move_x
    player.z += move_z

    camera.x = player.x
    camera.z = player.z

    if move_x != 0 or move_z != 0:
        player.rotation_y = atan2(move_x, move_z) * (180 / pi)


# Add decorative obstacles
for i in range(5):
    Entity(model='cube', color=color.light_gray, position=(i * 2 - 4, 0.5, 3), scale=1, collider='box')

app.run()
