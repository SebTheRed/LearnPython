def decode(message_file):
    file = open(message_file, 'r')
    lines = file.readlines()
    file.close()
    # print(lines)
    number_word_pairs = {}
    for line in lines:
        parts = line.split()
        number = int(parts[0])
        word = parts[1]
        number_word_pairs[number] = word
    # print(number_word_pairs)
    right_edge_numbers = set()
    for n in range(1, int(max(number_word_pairs.keys())**0.5) + 2):
        right_edge_numbers.add(sum(range(1, n + 1)))
    # print(right_edge_numbers)
    result = []
    for n in sorted(number_word_pairs):
        if n in right_edge_numbers:
            result.append(number_word_pairs[n])
    # print(' '.join(result))
    return(' '.join(result))

print(decode('./coding_qual_input.txt'))
# This function reads a message file and extracts number-word pairs from it.
# It then calculates the right edge numbers of a pyramid based on the extracted numbers.
# Finally, it filters and joins the words that correspond to the right edge numbers, returning the decoded message.