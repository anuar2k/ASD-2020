# Pole dowolnego wielokąta

def area(points):
    if len(points) < 3:
        return 0

    area = 0
    prev = points[-1]

    for point in points:
        deltaX = point[0] - prev[0]
        avgY = (point[1] + prev[1]) / 2

        area += deltaX * avgY

        prev = point

    # kierunek krzywej może być zarówno określony clock/counterclockwise
    return area if area >= 0 else -area

print(area([(-1, -1), (1, -2), (1, 1), (-1, 2)]))