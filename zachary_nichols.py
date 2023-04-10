def rect_area(length, width):
    return length * width

def rect_solid_area(length, width, height):
    return 2 * (rect_area(length, width) + rect_area(height, length) + rect_area(height, width))