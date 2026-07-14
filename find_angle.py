def find_angle(hour, minute):
    if hour == 12:
        hour = 0
    if minute == 60:
        minute = 0
        hour += 1
        if hour > 12:
            hour = hour - 12

    # Calculate the angles moved by hour and minute hands
    hour_angle = (hour * 30) + (minute * 0.5)
    minute_angle = minute * 6

    # Find the difference between two angles
    angle = abs(hour_angle - minute_angle)

    # Return the smaller angle of the two possible angles
    angle = min(360 - angle, angle)

    return angle

# Example usage
h, m = 12, 30
print(f"{find_angle(h, m)}°")  # Output: 165°
