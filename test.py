def hex_to_rgb(hex_value):
    # Extract the red, green, and blue components
    red = (hex_value >> 16) & 0xFF
    green = (hex_value >> 8) & 0xFF
    blue = hex_value & 0xFF

    # Normalize the color components to the range of 0.0 to 1.0
    r = red / 255.0
    g = green / 255.0
    b = blue / 255.0

    return (r, g, b)

print(hex_to_rgb(0x2e2e2e))