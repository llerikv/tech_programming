words = ["apple", "banana", "cherry", "blueberry"]
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print(longest_word)