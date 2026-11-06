import os
import bpy
import configparser
from pathlib import Path

from mathutils import Matrix, Vector, Quaternion, Euler

def get_ingame_scale(game_path, filepath, use_game_rules, is_inverse=False):
    rotation_angle = 0
    rotation_axis = "Z"
    room_scale = bpy.context.preferences.addons[__package__].preferences.room_scale
    result = Matrix().to_4x4()
    if not use_game_rules:
        if is_inverse:
            result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1.0 / room_scale, 1.0 / room_scale, 1.0 / room_scale)))
            return result, rotation_angle, rotation_axis
        else:
            result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((room_scale, room_scale, room_scale)))
            return result, rotation_angle, rotation_axis

    # We are taking the room scale in the game itself and getting the inverse.
    # We use it on the scales used by the game to get something we can scale independently. - Gen
    game_scale_inverse = 256
    game_scale = (1 / game_scale_inverse)

    items_ini = None
    npcs_ini = None

    npcs_ini_path = os.path.join(game_path, "Data", "NPCs.ini")
    items_ini_path = os.path.join(game_path, "Data", "items.ini")
    if os.path.isfile(items_ini_path):
        items_ini = configparser.ConfigParser()
        items_ini.read(items_ini_path)

    if os.path.isfile(npcs_ini_path):
        npcs_ini = configparser.ConfigParser()
        npcs_ini.read(npcs_ini_path)

    if not str(filepath).startswith(str(game_path)):
        return result, rotation_angle, rotation_axis
    filepath_l =  Path(filepath).relative_to(game_path).as_posix()
    if filepath_l == "GFX/173box.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/apache.b3d":
        scale_val = (0.6 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/apacherotor.b3d":
        # The scale here is inherited from the apache through entity parenting in scripts. - Gen
        scale_val = (0.6 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/apacherotor2.b3d":
        # The scale here is inherited from the apache through entity parenting in scripts. - Gen
        scale_val = (0.6 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/doorhit.b3d":
        scale_val = 1
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/lightcone.b3d":
        scale_val = (0.01 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/420.x":
        ini_value = 0.0005
        if items_ini is not None:
            ini_value = float(items_ini.get("scp420j", "scale", fallback=0.0005))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/427.b3d":
        ini_value = 0.001
        if items_ini is not None:
            ini_value = float(items_ini.get("scp427", "scale", fallback=0.001))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/513.x":
        ini_value = 0.1
        if items_ini is not None:
            ini_value = float(items_ini.get("scp513", "scale", fallback=0.1))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/badge.x":
        ini_value = 0.0001
        if items_ini is not None:
            ini_value = float(items_ini.get("badge", "scale", fallback=0.0001))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/bdc.b3d":
        ini_value = 1.6
        if items_ini is not None:
            ini_value = float(items_ini.get("bdc", "scale", fallback=1.6))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/clipboard.b3d":
        ini_value = 0.003
        if items_ini is not None:
            ini_value = float(items_ini.get("clipboard", "scale", fallback=0.003))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/cup.x":
        ini_value = 0.04
        if items_ini is not None:
            ini_value = float(items_ini.get("cup", "scale", fallback=0.04))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/cupliquid.x":
        ini_value = 0.04
        if items_ini is not None:
            ini_value = float(items_ini.get("cup", "scale", fallback=0.04))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/electronics.x":
        ini_value = 0.0011
        if items_ini is not None:
            ini_value = float(items_ini.get("electronics", "scale", fallback=0.0011))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/eyedrops.b3d":
        ini_value = 0.0012
        if items_ini is not None:
            ini_value = float(items_ini.get("eyedrops", "scale", fallback=0.0012))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/firstaid.x":
        ini_value = 0.05
        if items_ini is not None:
            ini_value = float(items_ini.get("firstaid", "scale", fallback=0.05))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/gasmask.b3d":
        ini_value = 0.02
        if items_ini is not None:
            ini_value = float(items_ini.get("gasmask", "scale", fallback=0.02))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/happy.b3d":
        # Model is the same as bcd so reusing the scale setting. - Gen
        ini_value = 1.6
        if items_ini is not None:
            ini_value = float(items_ini.get("bdc", "scale", fallback=1.6))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/hazmat.b3d":
        ini_value = 0.013
        if items_ini is not None:
            ini_value = float(items_ini.get("hazmatsuit", "scale", fallback=0.013))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/HGIB_Skull1.b3d":
        ini_value = 0.015
        if items_ini is not None:
            ini_value = float(items_ini.get("scp1123", "scale", fallback=0.015))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/key.b3d":
        ini_value = 0.001
        if items_ini is not None:
            ini_value = float(items_ini.get("key", "scale", fallback=0.001))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/keycard.x":
        ini_value = 0.0004
        if items_ini is not None:
            ini_value = float(items_ini.get("key1", "scale", fallback=0.0004))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/metalpanel.x":
        ini_value = 0.00390625
        if items_ini is not None:
            ini_value = float(items_ini.get("scp148", "scale", fallback=0.00390625))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/navigator.x":
        ini_value = 0.0008
        if items_ini is not None:
            ini_value = float(items_ini.get("snav", "scale", fallback=0.0008))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/note.x":
        ini_value = 0.0025
        if items_ini is not None:
            ini_value = float(items_ini.get("note682", "scale", fallback=0.0025))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/NVG.b3d":
        ini_value = 0.02
        if items_ini is not None:
            ini_value = float(items_ini.get("nvgoggles", "scale", fallback=0.02))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/origami.b3d":
        ini_value = 0.003
        if items_ini is not None:
            ini_value = float(items_ini.get("origami", "scale", fallback=0.003))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/paper.x":
        ini_value = 0.003
        if items_ini is not None:
            ini_value = float(items_ini.get("oldpaper", "scale", fallback=0.003))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/pill.b3d":
        ini_value = 0.0001
        if items_ini is not None:
            ini_value = float(items_ini.get("pill", "scale", fallback=0.0001))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/radio.x":
        scale_val = (1 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/SCP-1499.b3d":
        ini_value = 0.023
        if items_ini is not None:
            ini_value = float(items_ini.get("scp1499", "scale", fallback=0.023))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/scp1025.b3d":
        ini_value = 0.1
        if items_ini is not None:
            ini_value = float(items_ini.get("scp1025", "scale", fallback=0.1))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/scp148.x":
        ini_value = 0.00390625
        if items_ini is not None:
            ini_value = float(items_ini.get("scp148", "scale", fallback=0.00390625))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/scp714.b3d":
        ini_value = 0.3
        if items_ini is not None:
            ini_value = float(items_ini.get("scp714", "scale", fallback=0.3))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/severedhand.b3d":
        ini_value = 0.04
        if items_ini is not None:
            ini_value = float(items_ini.get("hand", "scale", fallback=0.04))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/vest.x":
        ini_value = 0.02
        if items_ini is not None:
            ini_value = float(items_ini.get("vest", "scale", fallback=0.02))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/wallet.b3d":
        ini_value = 0.0005
        if items_ini is not None:
            ini_value = float(items_ini.get("wallet", "scale", fallback=0.0005))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/Battery/Battery.x":
        ini_value = 0.008
        if items_ini is not None:
            ini_value = float(items_ini.get("bat", "scale", fallback=0.008))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/Halloween/BoneFlute.b3d":
        ini_value = 0.006
        if items_ini is not None:
            ini_value = float(items_ini.get("boneflute", "scale", fallback=0.006))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/Halloween/bonefrag.b3d":
        ini_value = 0.008
        if items_ini is not None:
            ini_value = float(items_ini.get("bone", "scale", fallback=0.008))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/Halloween/ChocolateBar.b3d":
        scale_val = (1 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/Halloween/EyeCandy.b3d":
        scale_val = (1 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/Halloween/Lollipop.b3d":
        scale_val = (1 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/Halloween/pumpkin.b3d":
        ini_value = 0.2
        if items_ini is not None:
            ini_value = float(items_ini.get("pumpkin", "scale", fallback=0.2))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/Halloween/scp330.b3d":
        scale_val = (1 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/items/Syringe/syringe.b3d":
        ini_value = 0.005
        if items_ini is not None:
            ini_value = float(items_ini.get("syringe", "scale", fallback=0.005))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/map/008_2.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/079.b3d":
        scale_val = (1.3 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/map/1123_hb.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/173_2.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/294.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((game_scale_inverse, game_scale_inverse, game_scale_inverse)))
    elif filepath_l == "GFX/map/372_hb.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/914key.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/914knob.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/Button.x":
        scale_val = (0.03 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/map/ButtonCode.x":
        scale_val = (0.03 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/map/ButtonKeycard.x":
        scale_val = (0.03 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/map/ButtonScanner.x":
        scale_val = (0.03 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/map/cam.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/cambase.x":
        scale_val = (0.0015 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/map/CamHead.b3d":
        scale_val = (0.01 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/map/CamHead.x":
        scale_val = (0.01 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/map/ContDoorLeft.x":
        scale_val = ((55 * (1 / game_scale_inverse)) * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/map/ContDoorRight.x":
        scale_val = ((55 * (1 / game_scale_inverse)) * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/map/Door01.x":

        sx = ((204.0 * (1/256)) / (11.0814) * 256)
        sy = ((16.0 * (1/256)) / (1.05759) * 256)
        sz = ((312.0 * (1/256)) / (24.2875) * 256)

        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((sx, sy, sz)))
    elif filepath_l == "GFX/map/DoorColl.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/DoorFrame.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/elevatordoor.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/exit1terrain.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/fan.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/gateatunnel.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/gateawall1.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/gateawall2.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/gatea_hitbox1.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/heavydoor1.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/heavydoor2.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/IntroDesk.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/IntroDrawer.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/intro_labels.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/leverbase.x":
        scale_val = (0.04 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/map/leverhandle.x":
        scale_val = (0.04 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/map/lightgun.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/lightgunbase.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/medibay_props.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/monitor.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/monitor_checkpoint.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/pocketdimension2.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/pocketdimension3.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/pocketdimension4.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/pocketdimension5.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/pocketdimensionterrain.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/room012_2.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/room012_3.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/room049_hb.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/room1062.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/room2gw_pipes.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/room2tesla_caution.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/room3gw_pipes.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/room3offices_hb.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/room3storage_hb.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/room3z2_hb.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/dimension1499/1499object0_cull.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/dimension1499/1499object1.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/dimension1499/1499object10.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/dimension1499/1499object11.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/dimension1499/1499object12.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/dimension1499/1499object13.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/dimension1499/1499object14.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/dimension1499/1499object15.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/dimension1499/1499object2.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/dimension1499/1499object3.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/dimension1499/1499object4.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/dimension1499/1499object5.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/dimension1499/1499object6.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/dimension1499/1499object7.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/dimension1499/1499object8.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/dimension1499/1499object9.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/dimension1499/1499plane.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/forest/door.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/forest/door_frame.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/forest/detail/rock.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/forest/detail/treetest4.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/forest/detail/treetest5.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/halloween/pumpkin.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/Props/205.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/Props/boxfile_a.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/Props/boxfile_b.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/Props/cabinet_a.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/Props/cabinet_b.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/Props/ContDoorFrame.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/Props/crate1.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/Props/crate2.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/Props/crate3.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/Props/ElecBox.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/Props/keyboard.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/Props/lamp1.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/Props/lamp2.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/Props/lamp3.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/Props/monitor.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/Props/mug.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/Props/officeseat_a.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/Props/pumpkin.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((5, 5, 5)))
    elif filepath_l == "GFX/map/Props/Tank1.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/map/Props/Tank2.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "GFX/npcs/035.b3d":
        # 35.6005 is the X dimension of the 035 model at 1.0 roomscale. - Gen
        scale_val = (0.5 / (game_scale * 35.6005))
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "GFX/npcs/035tentacle.b3d":
        scale_val = (0.065 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "GFX/npcs/106_2.b3d":
        ini_value = 0.25
        if items_ini is not None:
            ini_value = float(npcs_ini.get("SCP-106", "scale", fallback=0.25))

        scale_val = ((ini_value / 2.2) * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "GFX/npcs/1499-1.b3d":
        ini_value = 0.08
        if items_ini is not None:
            ini_value = float(npcs_ini.get("SCP-1499-1", "scale", fallback=0.08))

        scale_val = ((ini_value / 4.0) * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "GFX/npcs/173_2.b3d":
        # 6.708 is the Y dimension of the 173 model at 1.0 roomscale. - Gen
        ini_value = 0.35
        if items_ini is not None:
            ini_value = float(npcs_ini.get("SCP-173", "scale", fallback=0.35))

        scale_val = (ini_value / (game_scale * 6.708))
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/npcs/205_demon1.b3d":
        scale_val = (0.05 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "GFX/npcs/205_demon2.b3d":
        scale_val = (0.05 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "GFX/npcs/205_demon3.b3d":
        scale_val = (0.05 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "GFX/npcs/205_woman.b3d":
        scale_val = (0.05 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "GFX/npcs/372.b3d":
        # 4.43868 is the X dimension of the 372 model at 1.0 roomscale. - Gen
        scale_val = (0.35 / (game_scale * 4.43868))
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 180
        rotation_axis = "Z"
    elif filepath_l == "GFX/npcs/682arm.b3d":
        scale_val = (0.15 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/npcs/bll.b3d":
        # 24.8496 is the X dimension of the bll model at 1.0 roomscale. - Gen
        scale_val = (1.8 / (game_scale * 24.8496))
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "GFX/npcs/classd.b3d":
        # 35.6005 is the X dimension of the D class model at 1.0 roomscale. - Gen
        scale_val = (0.5 / (game_scale * 35.6005))
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "GFX/npcs/clerk.b3d":
        # 33.5748 is the X dimension of the clerk model at 1.0 roomscale. - Gen
        scale_val = (0.5 / (game_scale * 33.5748))
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "GFX/npcs/duck_low_res.b3d":
        scale_val = (0.07 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/npcs/forestmonster.b3d":
        ini_value = 0.5
        if items_ini is not None:
            ini_value = float(npcs_ini.get("Forestmonster", "scale", fallback=0.5))

        scale_val = ((ini_value / 20.0) * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "GFX/npcs/guard.b3d":
        ini_value = 0.29
        if items_ini is not None:
            ini_value = float(npcs_ini.get("Guard", "scale", fallback=0.29))

        scale_val = ((ini_value / 2.5) * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "X"
    elif filepath_l == "GFX/npcs/MTF2.b3d":
        ini_value = 0.29
        if items_ini is not None:
            ini_value = float(npcs_ini.get("MTF", "scale", fallback=0.29))

        scale_val = ((ini_value / 2.5) * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "GFX/npcs/naziofficer.b3d":
        # 33.5956 is the X dimension of the naziofficer model at 1.0 roomscale. - Gen
        scale_val = (0.5 / (game_scale * 33.5956))
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "GFX/npcs/partyhat.b3d":
        # This model gets attached to 173 so we are reusing the scale from that. - Gen
        ini_value = 0.35
        if items_ini is not None:
            ini_value = float(npcs_ini.get("SCP-173", "scale", fallback=0.35))

        scale_val = (ini_value / (game_scale * 6.708))
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/npcs/s2.b3d":
        scale_val = (0.32 / 21.3) * game_scale_inverse
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "GFX/npcs/scp-049.b3d":
        ini_value = 1.2
        if items_ini is not None:
            ini_value = float(npcs_ini.get("SCP-049", "scale", fallback=1.2))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "GFX/npcs/scp-066.b3d":
        ini_value = 0.17
        if items_ini is not None:
            ini_value = float(npcs_ini.get("SCP-066", "scale", fallback=0.17))

        scale_val = ((ini_value / 2.5) * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "GFX/npcs/scp-1048.b3d":
        scale_val = (0.05 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "GFX/npcs/scp-1048a.b3d":
        scale_val = (0.05 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "GFX/npcs/scp-1048pp.b3d":
        scale_val = (0.05 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "GFX/npcs/scp-939.b3d":
        ini_value = 0.5
        if items_ini is not None:
            ini_value = float(npcs_ini.get("SCP-939", "scale", fallback=0.5))

        scale_val = ((ini_value / 2.5) * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "GFX/npcs/scp-966.b3d":
        ini_value = 0.5
        if items_ini is not None:
            ini_value = float(npcs_ini.get("SCP-966", "scale", fallback=0.5))

        scale_val = ((ini_value / 40.0) * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "GFX/npcs/scp096.b3d":
        ini_value = 0.6
        if items_ini is not None:
            ini_value = float(npcs_ini.get("SCP-096", "scale", fallback=0.6))

        scale_val = ((ini_value / 3.0) * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "X"
    elif filepath_l == "GFX/npcs/zombie1.b3d":
        ini_value = 0.27
        if items_ini is not None:
            ini_value = float(npcs_ini.get("SCP-049-2", "scale", fallback=0.27))

        scale_val = ((ini_value / 2.5) * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "GFX/npcs/zombiesurgeon.b3d":
        # 36.6699 is the X dimension of the zombiesurgeon model at 1.0 roomscale. - Gen
        scale_val = (0.5 / (game_scale * 36.6699))
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "GFX/npcs/Halloween/jell066.b3d":
        ini_value = 0.17
        if items_ini is not None:
            ini_value = float(npcs_ini.get("SCP-066", "scale", fallback=0.17))

        scale_val = ((ini_value / 2.5) * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "GFX/npcs/Halloween/pumpkinmonster.b3d":
        ini_value = 0.5
        if items_ini is not None:
            ini_value = float(npcs_ini.get("Forestmonster", "scale", fallback=0.5))

        scale_val = ((ini_value / 20.0) * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "GFX/npcs/Halloween/skinned106.b3d":
        ini_value = 0.25
        if items_ini is not None:
            ini_value = float(npcs_ini.get("SCP-106", "scale", fallback=0.25))

        scale_val = ((ini_value / 2.5) * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"

    if is_inverse:
        rotation_angle = rotation_angle * -1
        translation, rotation, scale = result.decompose()
        scale = Vector((1.0 / (scale.x * room_scale), 1.0 / (scale.y * room_scale), 1.0 / (scale.z * room_scale)))
        result = Matrix.LocRotScale(translation, rotation, scale)
    else:
        translation, rotation, scale = result.decompose()
        scale = Vector(((scale.x * room_scale), (scale.y * room_scale), (scale.z * room_scale)))
        result = Matrix.LocRotScale(translation, rotation, scale)

    return result, rotation_angle, rotation_axis
