import random

MAX_POINT = 10
MIN_POINT = -10


class Event:
    def __init__(self, id, location):
        self.id = id
        self.location = location
        self.tickets = random.randint(1, 10)
        self.prices = []
        for x in range(0, self.tickets):
            self.prices.append(round(random.uniform(1, 50), 2))
        self.distance = 0

    def best_price(self):
        p = sorted(self.prices)
        return p[0]


def gen_location(events):
    "generate a unique random location"

    location = (
        random.randint(MIN_POINT, MAX_POINT),
        random.randint(MIN_POINT, MAX_POINT))
    if events == []:
        return location
    else:
        match = True
        while match:
            for event in events:
                if event.location == location:
                    location = (
                        random.randint(MIN_POINT, MAX_POINT),
                        random.randint(MIN_POINT, MAX_POINT))
                    match = True
                    break
                else:
                    match = False

    return location


def gen_events():
    "generate a list of 100 random events"

    events = []
    for i in range(0, 100):
        location = gen_location(events)
        event = Event(id=i+1, location=location)
        events.append(event)

    return events


def manhattan_distance(start, end):
    distance = abs(start[0] - end[0]) + abs(start[1] - end[1])
    return distance


if __name__ == "__main__":
    location = input("Please input coordinates: ")
    events = gen_events()
    for event in events:
        event.distance = manhattan_distance(location, event.location)

    events.sort(key=lambda x: x.distance)
    print "\nClosest Events to {}:\n".format(location)

    for i in range(0, 5):
        print "Event {} - ${}, Distance {}".format(
            events[i].id, events[i].best_price(), events[i].distance)
