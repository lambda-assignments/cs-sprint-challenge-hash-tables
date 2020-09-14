#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    cache = dict()
    for ticket in tickets:
        cache[ticket.source] = ticket.destination
    route = list()
    route.append(cache["NONE"])
    for ticket in tickets:
        next_location = route[-1]
        route.append(cache[next_location])
        if route[-1] == "NONE":
            return route