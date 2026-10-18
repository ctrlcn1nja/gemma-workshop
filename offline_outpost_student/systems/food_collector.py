"""Autonomous harvest robot records."""
class HarvestRobot:
    def __init__(self, name, harvest=[]):
        self.name = name
        self.harvest = harvest

    def collect(self, amount):
        if amount < 0:
            raise ValueError("Harvest cannot be negative")
        self.harvest.append(amount)

    def total(self):
        return sum(self.harvest)


def station_total(robots):
    return sum(robot.total() for robot in robots)
