# Simple File Read & Write Program
# Ask the user for the input file name
input_file = input("Enter the file name to read: ")

try:
    # Open the file and read its content
    file = open(input_file, 'r')
    content = file.read()
    file.close()
    
    # Modify the content (here we just make it uppercase)
    modified_content = content.upper()
    
    # Ask for the output file name
    output_file = input("Enter the file name to save the modified content: ")
    
    # Open the new file and write the modified content
    file = open(output_file, 'w')
    file.write(modified_content)
    file.close()
    
    print("The modified content has been saved to", output_file)

except FileNotFoundError:
    print("Error: The file does not exist. Please check the file name.")
except PermissionError:
    print("Error: You don't have permission to read or write this file.")
except:
    print("An unexpected error occurred.")
