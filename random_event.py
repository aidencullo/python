import random


def random_events():
    event = random_event()


def random_event():
    if random.random() < 0.1:
        return "It will rain!"
    else:
        return "Sunny day!"


N = 1_000


def generate_events():
    return [random_event() for _ in range(N)]


def is_rainy(event):
    return event == "It will rain!"


def is_sunny(event):
    return event == "Sunny day!"


def measure_random_events():
    events = generate_events()
    rainy = "It will rain!"
    sunny = "Sunny day!"
    rainy_events = len(list(filter(is_rainy, events)))
    sunny_events = sum(1 for e in events if is_sunny(e))
    print(
        "there were {} rainy events and {} sunny events!".format(
            rainy_events, sunny_events
        )
    )


measure_random_events()
