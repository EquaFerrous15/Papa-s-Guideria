

def normalise_string(string: str) -> str:
    """Normalise the string, making it lowercase and replacing spaces with underscores."""
    string = string.lower()
    string = string.replace(" ", "_")
    return string
