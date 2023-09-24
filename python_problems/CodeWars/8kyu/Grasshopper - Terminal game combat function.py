"""Create a combat function that takes the player's current health and the amount of damage recieved, and returns the player's new health. Health can't be less than 0."""


def combat(health, damage):
    val = health - damage
    return 0 if val < 0 else val
