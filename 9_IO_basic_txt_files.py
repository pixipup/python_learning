def read_text_file():
  """
  Reads the content of a text file and displays it.
  Args:
      file_path: The path to the text file.
  """

  # Take path input from the user

  file_path = str(input("Enter file path:" ))

  
  # Open the file in read mode
  with open(file_path) as file:
    
    # Read the entire content of the file
    file_content = file.read()
  
  # Print the content
  print("\n",file_content)

# Example usage
read_text_file()
