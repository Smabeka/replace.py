# Save the original sentence as a string
# Replace ! with spaces and print
# Convert to uppercase and print
# Print the sentence in reverse using string slicing

sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

spaced_sentence = sentence.replace("!"," ")
print(spaced_sentence)

upper_sentence = spaced_sentence.upper()
print(upper_sentence)

reversed_sentence = spaced_sentence[::-1]
print(reversed_sentence)