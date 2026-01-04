def combine(array1, array2):
    """
    Combines two arrays of dictionaries into a single array.

    Takes two arrays of the same length and merges corresponding
    dictionaries, combining their key-value pairs.

    Args:
        array1: List of dictionaries
        array2: List of dictionaries (same length as array1)

    Returns:
        List of merged dictionaries
    """
    return [{**d1, **d2} for d1, d2 in zip(array1, array2)]
