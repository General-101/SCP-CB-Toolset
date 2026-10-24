import os
import bpy
import configparser

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

    file_name_l = os.path.basename(filepath).lower()
    directory_name_l = os.path.basename(os.path.dirname(filepath)).lower()
    filepath_l = "%s_%s" % (directory_name_l, file_name_l)
    if filepath_l == "gfx_173box.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "gfx_apache.b3d":
        scale_val = (0.6 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "gfx_apacherotor.b3d":
        # The scale here is inherited from the apache through entity parenting in scripts. - Gen
        scale_val = (0.6 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "gfx_apacherotor2.b3d":
        # The scale here is inherited from the apache through entity parenting in scripts. - Gen
        scale_val = (0.6 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "gfx_doorhit.b3d":
        scale_val = 1
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "gfx_lightcone.b3d":
        scale_val = (0.01 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "items_420.x":
        ini_value = 0.0005
        if items_ini is not None:
            ini_value = float(items_ini.get("scp420j", "scale", fallback=0.0005))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "items_427.b3d":
        ini_value = 0.001
        if items_ini is not None:
            ini_value = float(items_ini.get("scp427", "scale", fallback=0.001))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "items_513.x":
        ini_value = 0.1
        if items_ini is not None:
            ini_value = float(items_ini.get("scp513", "scale", fallback=0.1))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "items_badge.x":
        ini_value = 0.0001
        if items_ini is not None:
            ini_value = float(items_ini.get("badge", "scale", fallback=0.0001))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "items_bdc.b3d":
        ini_value = 1.6
        if items_ini is not None:
            ini_value = float(items_ini.get("bdc", "scale", fallback=1.6))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "items_clipboard.b3d":
        ini_value = 0.003
        if items_ini is not None:
            ini_value = float(items_ini.get("clipboard", "scale", fallback=0.003))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "items_cup.x":
        ini_value = 0.04
        if items_ini is not None:
            ini_value = float(items_ini.get("cup", "scale", fallback=0.04))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "items_cupliquid.x":
        ini_value = 0.04
        if items_ini is not None:
            ini_value = float(items_ini.get("cup", "scale", fallback=0.04))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "items_electronics.x":
        ini_value = 0.0011
        if items_ini is not None:
            ini_value = float(items_ini.get("electronics", "scale", fallback=0.0011))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "items_eyedrops.b3d":
        ini_value = 0.0012
        if items_ini is not None:
            ini_value = float(items_ini.get("eyedrops", "scale", fallback=0.0012))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "items_firstaid.x":
        ini_value = 0.05
        if items_ini is not None:
            ini_value = float(items_ini.get("firstaid", "scale", fallback=0.05))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "items_gasmask.b3d":
        ini_value = 0.02
        if items_ini is not None:
            ini_value = float(items_ini.get("gasmask", "scale", fallback=0.02))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "items_happy.b3d":
        # Model is the same as bcd so reusing the scale setting. - Gen
        ini_value = 1.6
        if items_ini is not None:
            ini_value = float(items_ini.get("bdc", "scale", fallback=1.6))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "items_hazmat.b3d":
        ini_value = 0.013
        if items_ini is not None:
            ini_value = float(items_ini.get("hazmatsuit", "scale", fallback=0.013))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "items_hgib_skull1.b3d":
        ini_value = 0.015
        if items_ini is not None:
            ini_value = float(items_ini.get("scp1123", "scale", fallback=0.015))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "items_key.b3d":
        ini_value = 0.001
        if items_ini is not None:
            ini_value = float(items_ini.get("key", "scale", fallback=0.001))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "items_keycard.x":
        ini_value = 0.0004
        if items_ini is not None:
            ini_value = float(items_ini.get("key1", "scale", fallback=0.0004))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "items_metalpanel.x":
        ini_value = 0.00390625
        if items_ini is not None:
            ini_value = float(items_ini.get("scp148", "scale", fallback=0.00390625))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "items_navigator.x":
        ini_value = 0.0008
        if items_ini is not None:
            ini_value = float(items_ini.get("snav", "scale", fallback=0.0008))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "items_note.x":
        ini_value = 0.0025
        if items_ini is not None:
            ini_value = float(items_ini.get("note682", "scale", fallback=0.0025))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "items_nvg.b3d":
        ini_value = 0.02
        if items_ini is not None:
            ini_value = float(items_ini.get("nvgoggles", "scale", fallback=0.02))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "items_origami.b3d":
        ini_value = 0.003
        if items_ini is not None:
            ini_value = float(items_ini.get("origami", "scale", fallback=0.003))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "items_paper.x":
        ini_value = 0.003
        if items_ini is not None:
            ini_value = float(items_ini.get("oldpaper", "scale", fallback=0.003))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "items_pill.b3d":
        ini_value = 0.0001
        if items_ini is not None:
            ini_value = float(items_ini.get("pill", "scale", fallback=0.0001))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "items_radio.x":
        scale_val = (1 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "items_scp-1499.b3d":
        ini_value = 0.023
        if items_ini is not None:
            ini_value = float(items_ini.get("scp1499", "scale", fallback=0.023))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "items_scp1025.b3d":
        ini_value = 0.1
        if items_ini is not None:
            ini_value = float(items_ini.get("scp1025", "scale", fallback=0.1))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "items_scp148.x":
        ini_value = 0.00390625
        if items_ini is not None:
            ini_value = float(items_ini.get("scp148", "scale", fallback=0.00390625))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "items_scp714.b3d":
        ini_value = 0.3
        if items_ini is not None:
            ini_value = float(items_ini.get("scp714", "scale", fallback=0.3))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "items_severedhand.b3d":
        ini_value = 0.04
        if items_ini is not None:
            ini_value = float(items_ini.get("hand", "scale", fallback=0.04))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "items_vest.x":
        ini_value = 0.02
        if items_ini is not None:
            ini_value = float(items_ini.get("vest", "scale", fallback=0.02))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "items_wallet.b3d":
        ini_value = 0.0005
        if items_ini is not None:
            ini_value = float(items_ini.get("wallet", "scale", fallback=0.0005))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "battery_battery.x":
        ini_value = 0.008
        if items_ini is not None:
            ini_value = float(items_ini.get("bat", "scale", fallback=0.008))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "syringe_syringe.b3d":
        ini_value = 0.005
        if items_ini is not None:
            ini_value = float(items_ini.get("syringe", "scale", fallback=0.005))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "map_008_2.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_079.b3d":
        scale_val = (1.3 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "map_1123_hb.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_173_2.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_294.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((game_scale_inverse, game_scale_inverse, game_scale_inverse)))
    elif filepath_l == "map_372_hb.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_914key.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_914knob.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_button.x":
        scale_val = (0.03 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "map_buttoncode.x":
        scale_val = (0.03 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "map_buttonkeycard.x":
        scale_val = (0.03 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "map_buttonscanner.x":
        scale_val = (0.03 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "map_cam.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_cambase.x":
        scale_val = (0.0015 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "map_camhead.b3d":
        scale_val = (0.01 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "map_camhead.x":
        scale_val = (0.01 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "map_contdoorleft.x":
        scale_val = ((55 * (1 / game_scale_inverse)) * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "map_contdoorright.x":
        scale_val = ((55 * (1 / game_scale_inverse)) * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "map_door01.x":

        sx = ((204.0 * (1/256)) / (11.0814) * 256)
        sy = ((16.0 * (1/256)) / (1.05759) * 256)
        sz = ((312.0 * (1/256)) / (24.2875) * 256)

        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((sx, sy, sz)))
    elif filepath_l == "map_doorcoll.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_doorframe.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_elevatordoor.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_exit1terrain.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_fan.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_gateatunnel.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_gateawall1.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_gateawall2.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_gatea_hitbox1.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_heavydoor1.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_heavydoor2.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_introdesk.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_introdrawer.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_intro_labels.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_leverbase.x":
        scale_val = (0.04 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "map_leverhandle.x":
        scale_val = (0.04 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "map_lightgun.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_lightgunbase.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_medibay_props.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_monitor.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_monitor_checkpoint.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_pocketdimension2.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_pocketdimension3.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_pocketdimension4.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_pocketdimension5.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_pocketdimensionterrain.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_room012_2.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_room012_3.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_room049_hb.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_room1062.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_room2gw_pipes.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_room2tesla_caution.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_room3gw_pipes.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_room3offices_hb.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_room3storage_hb.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "map_room3z2_hb.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "dimension1499_1499object0_cull.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "dimension1499_1499object1.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "dimension1499_1499object10.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "dimension1499_1499object11.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "dimension1499_1499object12.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "dimension1499_1499object13.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "dimension1499_1499object14.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "dimension1499_1499object15.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "dimension1499_1499object2.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "dimension1499_1499object3.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "dimension1499_1499object4.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "dimension1499_1499object5.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "dimension1499_1499object6.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "dimension1499_1499object7.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "dimension1499_1499object8.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "dimension1499_1499object9.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "dimension1499_1499plane.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "forest_door.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "forest_door_frame.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "detail_rock.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "detail_treetest4.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "detail_treetest5.b3d":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "props_205.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "props_boxfile_a.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "props_boxfile_b.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "props_cabinet_a.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "props_cabinet_b.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "props_contdoorframe.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "props_crate1.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "props_crate2.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "props_crate3.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "props_elecbox.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "props_keyboard.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "props_lamp1.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "props_lamp2.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "props_lamp3.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "props_monitor.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "props_mug.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "props_officeseat_a.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "props_tank1.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "props_tank2.x":
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((1, 1, 1)))
    elif filepath_l == "npcs_035.b3d":
        # 35.6005 is the X dimension of the 035 model at 1.0 roomscale. - Gen
        scale_val = (0.5 / (game_scale * 35.6005))
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "npcs_035tentacle.b3d":
        scale_val = (0.065 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "npcs_106_2.b3d":
        ini_value = 0.25
        if items_ini is not None:
            ini_value = float(npcs_ini.get("SCP-106", "scale", fallback=0.25))

        scale_val = ((ini_value / 2.2) * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "npcs_1499-1.b3d":
        ini_value = 0.08
        if items_ini is not None:
            ini_value = float(npcs_ini.get("SCP-1499-1", "scale", fallback=0.08))

        scale_val = ((ini_value / 4.0) * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "npcs_173_2.b3d":
        # 6.708 is the Y dimension of the 173 model at 1.0 roomscale. - Gen
        ini_value = 0.35
        if items_ini is not None:
            ini_value = float(npcs_ini.get("SCP-173", "scale", fallback=0.35))

        scale_val = (ini_value / (game_scale * 6.708))
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "npcs_205_demon1.b3d":
        scale_val = (0.05 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "npcs_205_demon2.b3d":
        scale_val = (0.05 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "npcs_205_demon3.b3d":
        scale_val = (0.05 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "npcs_205_woman.b3d":
        scale_val = (0.05 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "npcs_372.b3d":
        # 4.43868 is the X dimension of the 372 model at 1.0 roomscale. - Gen
        scale_val = (0.35 / (game_scale * 4.43868))
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 180
        rotation_axis = "Z"
    elif filepath_l == "npcs_682arm.b3d":
        scale_val = (0.15 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "npcs_bll.b3d":
        # 24.8496 is the X dimension of the bll model at 1.0 roomscale. - Gen
        scale_val = (1.8 / (game_scale * 24.8496))
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "npcs_classd.b3d":
        # 35.6005 is the X dimension of the D class model at 1.0 roomscale. - Gen
        scale_val = (0.5 / (game_scale * 35.6005))
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "npcs_clerk.b3d":
        # 33.5748 is the X dimension of the clerk model at 1.0 roomscale. - Gen
        scale_val = (0.5 / (game_scale * 33.5748))
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "npcs_duck_low_res.b3d":
        scale_val = (0.07 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "npcs_forestmonster.b3d":
        ini_value = 0.5
        if items_ini is not None:
            ini_value = float(npcs_ini.get("Forestmonster", "scale", fallback=0.5))

        scale_val = ((ini_value / 20.0) * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "npcs_guard.b3d":
        ini_value = 0.29
        if items_ini is not None:
            ini_value = float(npcs_ini.get("Guard", "scale", fallback=0.29))

        scale_val = ((ini_value / 2.5) * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "X"
    elif filepath_l == "npcs_mtf2.b3d":
        ini_value = 0.29
        if items_ini is not None:
            ini_value = float(npcs_ini.get("MTF", "scale", fallback=0.29))

        scale_val = ((ini_value / 2.5) * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "npcs_naziofficer.b3d":
        # 33.5956 is the X dimension of the naziofficer model at 1.0 roomscale. - Gen
        scale_val = (0.5 / (game_scale * 33.5956))
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "npcs_partyhat.b3d":
        # This model gets attached to 173 so we are reusing the scale from that. - Gen
        ini_value = 0.35
        if items_ini is not None:
            ini_value = float(npcs_ini.get("SCP-173", "scale", fallback=0.35))

        scale_val = (ini_value / (game_scale * 6.708))
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "npcs_s2.b3d":
        scale_val = (0.32 / 21.3) * game_scale_inverse
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
    elif filepath_l == "npcs_scp-049.b3d":
        ini_value = 1.2
        if items_ini is not None:
            ini_value = float(npcs_ini.get("SCP-049", "scale", fallback=1.2))

        scale_val = (ini_value * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "npcs_scp-066.b3d":
        ini_value = 0.17
        if items_ini is not None:
            ini_value = float(npcs_ini.get("SCP-066", "scale", fallback=0.17))

        scale_val = ((ini_value / 2.5) * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "npcs_scp-1048.b3d":
        scale_val = (0.05 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "npcs_scp-1048a.b3d":
        scale_val = (0.05 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "npcs_scp-1048pp.b3d":
        scale_val = (0.05 * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "npcs_scp-939.b3d":
        ini_value = 0.5
        if items_ini is not None:
            ini_value = float(npcs_ini.get("SCP-939", "scale", fallback=0.5))

        scale_val = ((ini_value / 2.5) * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "npcs_scp-966.b3d":
        ini_value = 0.5
        if items_ini is not None:
            ini_value = float(npcs_ini.get("SCP-966", "scale", fallback=0.5))

        scale_val = ((ini_value / 40.0) * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "npcs_scp096.b3d":
        ini_value = 0.6
        if items_ini is not None:
            ini_value = float(npcs_ini.get("SCP-096", "scale", fallback=0.6))

        scale_val = ((ini_value / 3.0) * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "X"
    elif filepath_l == "npcs_zombie1.b3d":
        ini_value = 0.27
        if items_ini is not None:
            ini_value = float(npcs_ini.get("SCP-049-2", "scale", fallback=0.27))

        scale_val = ((ini_value / 2.5) * game_scale_inverse)
        result = Matrix.LocRotScale(Vector((0, 0, 0)), Euler((0, 0, 0)), Vector((scale_val, scale_val, scale_val)))
        rotation_angle = 90
        rotation_axis = "Z"
    elif filepath_l == "npcs_zombiesurgeon.b3d":
        # 36.6699 is the X dimension of the zombiesurgeon model at 1.0 roomscale. - Gen
        scale_val = (0.5 / (game_scale * 36.6699))
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
