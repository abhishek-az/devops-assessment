def justify(paragraph, width):
  # Split the paragraph into a list of words
  words = paragraph.split()
  
  # Initialize the list of justified strings
  justified = []
  
  # Keep track of the current line of text
  line = ""
  
  # Loop through each word in the list of words
  for word in words:
    # If the current word would make the line too long,
    # add the current line to the list of justified strings
    # and start a new line with the current word
    if len(line) + len(word) > width:
      justified.append(line)
      line = word
    # Otherwise, add the word to the current line of text
    else:
      line += " " + word # Add the space between the word and the line
  
  # Add the final line of text to the list of justified strings
  justified.append(line)
  
  # Return the list of justified strings
  return justified


#Unit testcases for the above program
def test_justify():
    # Test with a paragraph of length less than the width
    paragraph = "This is a short paragraph."
    width = 30
    justified = justify(paragraph, width)
    assert justified == ["This is a short paragraph."]

    # Test with a paragraph of length equal to the width
    paragraph = "This is a paragraph of exactly the right length."
    width = 50
    justified = justify(paragraph, width)
    assert justified == ["This is a paragraph of exactly the right length."]

    # Test with a paragraph of length greater than the width
    paragraph = "This is a long paragraph that needs to be split into multiple lines. Each line should be justified to the specified width."
    width = 30
    justified = justify(paragraph, width)
    assert justified == [
        "This is a long paragraph that",
        "needs to be split into multiple",
        "lines. Each line should be",
        "justified to the specified",
        "width."
    ]


#To make the program more dynamic, making paragraph and width as variables which can ask for inputs during runtime 
#paragraph = input("Enter the paragraph you would like for the exercise: ")
#width = int(input("Enter the width of the page: "))

#Output Line
print(justify("This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works.", 20))

#test_justify()

