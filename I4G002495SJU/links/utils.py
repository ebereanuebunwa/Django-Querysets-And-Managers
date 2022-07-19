from uuid import uuid4


# Generate a random string of letters and digits
def generate_random_id() -> str:
    """
    A function that generates a random 8-character string.
    Useful for creating random IDS for URLs and objects.
    """
    # Generate ID
    id = str(uuid4())

    # Get the first 8 characters of the id
    id = id[:8]

    return id