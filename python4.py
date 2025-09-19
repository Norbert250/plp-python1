def file_read_write():
    try:
        # Ask user for input filename
        input_file = input("Enter the filename to read: ")

        # Try opening the file for reading
        with open(input_file, "r") as f:
            content = f.read()

        # Modify the content (example: make all text uppercase)
        modified_content = content.upper()

        # Write to a new file
        output_file = "modified_" + input_file
        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"✅ File successfully modified and saved as {output_file}")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


file_read_write()
