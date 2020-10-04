import time


def timerfunc(func):
    """
    A timer decorator
    """

    def function_timer(*args, **kwargs):
        """
        A nested function for timing other functions
        """
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        msg = "{time} completed for {func} of {cls} took  seconds to complete"
        print(msg.format(func=func.__name__, cls=func.__module__, time=runtime))

        return value

    return function_timer
