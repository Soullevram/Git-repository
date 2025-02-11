# Create reverse DNA sequence
def reverse(s):
    """
    Function to create a DNA reverse sequence, starting from the end.

    Parameters:
    s (str): A string is taken as the input

    Returns:
    s (str): A reverse version of the input string is returned
    """
    return (s[::-1])
# Complement function
def complement(s):
    """
    The function creates a complementary DNA sequence

    Parameters:
    s(str): A string of DNA sequences is taken as the input

    Returns:
    Letters (str): A list consisting of the complementary DNA sequence
    """
    # A dictionary that associates each string character (nucleotide) to its complementary character: A to T, C to G
    basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'a': 't', 'c': 'g', 
'g': 'c', 't': 'a', 'M': 'K', 'K': 'M', 'R': 'Y', 'Y': 'R', 'W': 'W', 'S': 'S', 
'V': 'B', 'B': 'V', 'H': 'D', 'D': 'H', 'N': 'N', '-': '-' }
    # Create a list using the input string
    letters = list(s)
    # For loop to iterate through each base/letter in the list
    letters = [basecomplement[base] for base in letters]
    # Return statement to join each character in the list
    return ''.join(letters)
# Reverse and Complementary function
def revcom(s):
    """
    The function is a combination of the reverse and complement functions. 
    The input string is first reversed from the end, then the complementary string of the reversed string is produced

    Parameters:
    s(str): input

    Return:
    s (str): reversed and complementary string
    """
    return complement(s[::-1])
