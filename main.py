import logging
import math
import turtle


def side_is_valid(side_len):
    """Check if the entered length is a positive integer."""
    # Check if it's an integer.
    try:  # The use of exception handling.
        int(side_len)
    except ValueError:
        print('The length must be an integer.')
        return False

    # Check if it's positive.
    if int(side_len) <= 0:
        print('The length must be positive.')
        return False
    else:
        return True


def input_sides(sides):
    """Get a valid input from the user and format it appropriately."""
    i = 0
    while i < 3:
        sides.append(input(f'Please enter the length of the #{i+1} side: '))
        if side_is_valid(sides[i]):
            i += 1
        else:
            sides.pop()
    # Convert string to integers.
    sides = [int(i) for i in sides]  # The use of list comprehension.
    sides.sort()
    return sides


def triangle_is_valid(sides):
    """ 
    Check if the user has entered three 
    lengths that meet the triangle inequality.
    """
    try:
        a = sides[0]
        b = sides[1]
        c = sides[2]
    except IndexError:
        return False

    # The triangle inequality.
    if a+b>c and a+c>b and b+c>a:
        return True
    else:
        return False


def is_right_angled(sides):
    """Check if the triangle is right angled or not."""
    short_cathetus = sides[0]
    long_cathetus = sides[1]
    hypotenuse = float(sides[2])  # math.sqrt returns float.
    # The Pythagorean theorem.
    if hypotenuse == math.sqrt(short_cathetus**2 + long_cathetus**2):
        return True
    else:
        return False


def draw_triangle(sides):
    """Draw a triangle."""  # The use of a documentation string.
    a = sides[0]
    b = sides[1]
    c = sides[2]
    # Use the law of cosines to find the angles.
    b_angle = math.degrees(math.acos((a**2 + b**2 - c**2) / (2*a*b)))
    c_angle = math.degrees(math.acos((b**2 + c**2 - a**2) / (2*b*c)))

    t = turtle.Turtle()
    # Set the scale based on the largest length.
    scale_factor = 10**len(str(c))
    turtle.setworldcoordinates(0, 0, scale_factor, scale_factor)
    # Set the speed of drawing to maximum.
    t.speed(10)

    # Draw side a.
    t.forward(a)
    t.left(180 - b_angle)
    # Draw side b.
    t.forward(b)
    t.left(180 - c_angle)
    # Draw side c.
    t.forward(c)

    turtle.done()


def main():
    sides = []
    # Prompt the user to enter lengths until all the requirements are met.
    while not triangle_is_valid(sides):
        # Don't show the error message on the 
        # first try (if the list is empty).
        if sides:
            sides.clear()
            print('Invalid triangle: the sum of its two sides '
                  'is not greater than the third side.')
        sides = input_sides(sides)

    if is_right_angled(sides):
        print(f'The triangle with sides {sides[0]}, '  # The use of f-strings.
              f'{sides[1]} and {sides[2]} IS right angled.')
    else:
        print(f'The triangle with sides {sides[0]}, '
              f'{sides[1]} and {sides[2]} is NOT right angled.')

    draw_triangle(sides)

    
if __name__ == '__main__':
    main()

