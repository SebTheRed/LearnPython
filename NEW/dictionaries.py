# CHALLENGE:
# Create a dictionary representing a book, with keys like "title", "author", and "year".
# Print out a value using the key.
# Add a new key-value pair, such as "genre" or "pages", to the dictionary.
# Use the get() method to retrieve and print the value of a key that may not be set, such as "publisher".
#

book = {
  "title": "How to win",
  "author": "SebTheRed",
  "year": "Y2K",
  "fullContent" : "Stay consistent",
}

print("Page 1: ", book["title"])

book["pages"] = 1

publisher = book.get("publisher", "no one would ever publish this")
print (publisher)