
def walk_backwards(steps):
    if steps == 0:
        return
    print("You take step {}".format(steps))
    walk_backwards(steps - 1)


def walk_forward(steps):
    if steps == 0:
        return
    walk_forward(steps - 1)
    print("You take step {}".format(steps))
    
walk_backwards(6)
walk_forward(6)