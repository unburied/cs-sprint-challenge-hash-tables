#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    traverse tickets array
    get info on ticket source and destination
    add source and destination to dict
    traverse dict, adding source info to a route array
    """
    # Your code here
    route = [None] * length
    info = {}
    
    # add ticket info to dict for easy lookup
    for ticket in tickets:
        info[ticket.source] = ticket.destination
    
    for i in range(length):
        # first element is always pointing to NONE
        if i == 0:
            route[0] = info['NONE']
        # each following element points to previous
        else:
            route[i] = info[route[i-1]]

    return route
