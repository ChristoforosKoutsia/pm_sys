
class GlobalVariables:
    """

    A class to contain all the global variables. Generally speaking it's not a good idea to use globals, however
    alternatively we would have to pass is_dark as argument in many functions
    """
    is_dark = True


def update_is_dark(value):
    """
    Updates is_dark global value

    Args:
        value: It determines whether we are in dark mode or bright mode

    Returns:

    """
    GlobalVariables.is_dark = value
