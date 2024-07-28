def text_to_binary(text):
    """
    Convert a string of text into its binary representation using ASCII values.
    
    Args:
    text (str): The input text to be converted to binary.
    
    Returns:
    str: A string representing the binary values of the input text, separated by spaces.
    """
    binary_code = []
    for char in text:
        # Convert each character to its binary ASCII value, ensuring it's 8 bits long
        binary_value = format(ord(char), '08b')
        binary_code.append(binary_value)
    
    # Join all binary values into a single string separated by spaces
    return ' '.join(binary_code)

def main():
    # Prompt the user to enter text
    text = input("Enter text to convert to binary: ")
    # Convert the text to binary
    binary_code = text_to_binary(text)
    # Print the binary representation
    print(binary_code)

# This ensures that the main function is called when the script is executed
if __name__ == "__main__":
    main()
