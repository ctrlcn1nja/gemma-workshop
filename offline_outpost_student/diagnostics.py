"""Black-box operational checks. Do not modify during the challenge."""
from systems.purifier import remaining_contamination
from systems.food_collector import HarvestRobot, station_total
from systems.radio import transmit_signal


def check_water():
    actual = remaining_contamination(100, [0.6, 0.6])
    return abs(actual - 16) < 1e-8, f"Expected 16 contamination units; observed {actual:.1f}"


def check_food():
    a, b = HarvestRobot("A"), HarvestRobot("B")
    a.collect(5)
    b.collect(3)
    actual = (a.total(), b.total(), station_total([a, b]))
    return actual == (5, 3, 8), f"Expected robot A=5, B=3, station=8; observed {actual}"


def check_radio():
    actual = transmit_signal([False, False, True], 3)
    return actual is True, f"Acknowledgment on attempt 3 of 3; transmission success reported: {actual}"

CHECKS = {"1": ("Water purifier", check_water), "2": ("Food collector", check_food), "3": ("Emergency radio", check_radio)}
