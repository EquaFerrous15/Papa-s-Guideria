

def normalise_string(string: str) -> str:
    """
    Normalise the string, making it lowercase, removing spaces and removing certain special characters.\n
    Allows the string to be used in file paths.
    """
    string = string.lower()
    string = string.replace(" ", "")
    string = string.replace(".", "")
    return string

