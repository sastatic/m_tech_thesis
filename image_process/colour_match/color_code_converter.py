def hex_to_rgb(hex_code):
    h = hex_code.lstrip('#')
    return [int(h[i:i + 2], 16) for i in (0, 2, 4)]

def rgb_to_hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)
