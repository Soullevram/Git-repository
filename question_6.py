def fasta_and_reverse_complement(fasta_file: str) -> dict[str, str]:
    """
    Parses a FASTA file and produces the reverse complement of each DNA sequence.

    Parameters:
    fasta_file (str): The path to the FASTA file.

    Returns:
    dict[str, str]: A dictionary where keys are sequence identifiers (keys) and values are their reverse complements.
    """
    # Create an empty dictionary to query
    reverse_complements = {}

    # Open the file
    with open(fasta_file, 'r') as file:
        sequence_id = None
        # Create an empty list
        sequence = []

        # For Loop to iterate through the lines
        for line in file:
            # Strip whitespaces
            line = line.strip()
            # IF statement to specify a header
            if line.startswith('>'):
                # If we have a previous sequence, process it
                if sequence_id is not None:  
                    # join the sequences
                    full_sequence = ''.join(sequence)
                    # Use revcom function
                    reverse_complements[sequence_id] = revcom(full_sequence)
                
                # Get the sequence identifier
                sequence_id = line[1:]  
                # Reset the sequence list for the new sequence
                sequence = []  
            else:
                # append the sequences
                sequence.append(line) 

        # Process the last sequence in the file
        if sequence_id is not None:
            full_sequence = ''.join(sequence)
            reverse_complements[sequence_id] = revcom(full_sequence)

    return reverse_complements

# Example usage:
fasta_file_path = 'Downloads/AB_test_dta.fasta'
reverse_complement_dict = fasta_and_reverse_complement(fasta_file_path)
for seq_id, rev_comp in reverse_complement_dict.items():
    print(f"{seq_id}: {rev_comp}")
