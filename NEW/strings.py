# upper() and lower(): Change the case of the string.
# strip(): Removes whitespace from the beginning and end of the string.
# split(): Splits the string into a list of substrings based on a separator.
# join(): Joins elements of an iterable (like a list) into a single string.
# replace(): Replaces a specified substring with another substring.
# find() and index(): Search for a substring and return its position.
# count(): Counts the occurrences of a specified substring.
# startswith() and endswith(): Check if the string starts or ends with a specified substring.
# capitalize() and title(): Capitalize the first letter of the string or each word.
# isalpha(), isdigit(), isalnum(), etc.: Check if the string meets certain conditions (all alphabetic, all digits, alphanumeric, etc.).

# Remove leading and trailing whitespace.
# Split the string into a list of words.


text = " hello, github! "

strip_text = text.strip()
print(strip_text)

string_list = strip_text.split(", ")
print(string_list)

