"""The rating is case insensitive (so "great" = "GREAT"). If an unrecognised rating is received, then you need to return:

"Rating not recognised" in Javascript, Python and Ruby...
...or null in Java
...or -1 in C#
Because you're a nice person, you always round up the tip, regardless of the service.

"""

import math


def calculate_tip(amount, rating):
    tips = {"Terrible": 0, "Poor": 5, "Good": 10, "Great": 15, "Excellent": 20}

    return (
        "Rating not recognised"
        if rating.capitalize() not in tips.keys()
        else math.ceil((tips[rating.capitalize()] / 100) * amount)
    )
