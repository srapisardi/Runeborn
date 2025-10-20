from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# --- WINDOW SETTINGS ---
window.title = "Runeborn"
window.borderless = False
window.fullscreen = False
window.exit_button.visible = True
window.fps_counter.enabled = True

# --- ENVIRONMENT ---
ground = Entity(
    model='plane',
    texture='grass',
    scale=(50, 1, 50),
    collider='box'
)

# Sample walls or obstacles
wall_1 = Entity(model='cube', color=color.gray, scale=(2,3,0.5), position=(0,1.5,3), collider='box')
wall_2 = duplicate(wall_1, x=3)
wall_3 = duplicate(wall_1, x=-3)

# --- PLAYER SETUP ---
player = Entity(
    model='cube',  # replace with your asset later (e.g., 'assets/player.obj')
    color=color.azure,
    scale=(1,2,1),
    position=(0,1,0),
    collider='box'
)

camera.parent = player
camera.position = (0, 20, -15)
camera.rotation_x = 65

# --- PLAYER MOVEMENT ---
speed = 5

def update():
    direction = Vec3(
        held_keys['d'] - held_keys['a'],
        0,
        held_keys['w'] - held_keys['s']
    ).normalized()
    player.position += direction * time.dt * speed

    # Rotate player based on direction
    if direction.length() > 0:
        player.rotation_y = atan2(direction.x, direction.z) * (180/pi)

    # Simple collision prevention (rudimentary)
    hit_info = player.intersects()
    if hit_info.hit:
        player.position -= direction * time.dt * speed

# --- LIGHTING ---
DirectionalLight(shadows=True, rotation=(45, -45, 45))
AmbientLight(color=color.rgb(100, 100, 100))

# --- UI ---
Text(text="Runeborn Alpha 0.1", origin=(0, -7), background=True)

app.run()
