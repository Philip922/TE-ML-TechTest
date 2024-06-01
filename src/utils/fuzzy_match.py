from thefuzz import process


def fuzzy_matching(input_name, found_names, threshold=90):
    """
    Perform fuzzy matching between an input name and a list of found names.

    Args:
        input_name (str): The input name to match against.
        found_names (list): A list of names to search for matches.
        threshold (int, optional): The minimum similarity score required for a match. Defaults to 90.

    Returns:
        list: A list of tuples containing the matched names and their similarity scores.
    """
    filtered_results = [match for match in process.extract(input_name, found_names) if match[1] >= threshold]
    return filtered_results