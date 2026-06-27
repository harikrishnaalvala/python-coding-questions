def angle_between_hands(h, m):
    hour_hand_angle = (h % 12) * 30 + m * 0.5
    minute_hand_angle = m * 6

    angle_diff = abs(hour_hand_angle - minute_hand_angle)
    # Ensure that the angle is less than or equal to 180 degrees
    if angle_diff > 180:
        angle_diff = 360 - angle_diff

    return angle_diff

# Test the function with the example
h = 12
m = 30
output = angle_between_hands(h, m)
print(f"Angle between hour hand and minute hand: {output} degrees")
