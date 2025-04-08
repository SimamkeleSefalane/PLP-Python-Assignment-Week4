def read_and_write_file():
    try:
        # Ask for input file
        input_file = input("Enter the name of the file to read from: ").strip()

        # Try reading the file
        with open(input_file, 'r') as file:
            content = file.read()
            print("File read successfully!")

        # Modify the content
        modified_content = content.upper()

        # Ask for output file
        output_file = input("Enter the name of the file to write to: ").strip()

        # Write the modified content to the new file
        with open(output_file, 'w') as new_file:
            new_file.write(modified_content)
            print(f"Modified content has been written to '{output_file}'")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except IOError:
        print("Error: There was a problem reading or writing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_write_file()
