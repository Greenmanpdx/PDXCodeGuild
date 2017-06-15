def do_stuff(function):
    def wrapper(*args, **kwargs):
        print(5 * len(args))
        return 'Your arguments are {} and {}'.format(args, kwargs)
    return wrapper

@do_stuff
def stuff(*args, **kwargs):
    return 5 * len(args)

thing = stuff(5, 60)
print(thing)
