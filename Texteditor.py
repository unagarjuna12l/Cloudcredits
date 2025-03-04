def open_file(filename):
    """Opens a file and returns its content."""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def save_file(filename, content):
    """Saves content to a file."""
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"File '{filename}' saved successfully.")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def edit_text(content):
    """Allows the user to edit the text content."""
    print("\n--- Editing Text ---\n")
    print(content)
    print("\n--- Start Editing (type 'SAVE' to save, 'EXIT' to exit without saving) ---")

    lines = content.split('\n')
    while True:
        try:
            line_num = int(input("Enter line number to edit (or 0 to add a new line): "))
            if line_num == 0:
                new_line = input("Enter new line: ")
                lines.append(new_line)
                print("Line added.")
            elif 1 <= line_num <= len(lines):
                lines[line_num - 1] = input(f"Edit line {line_num}: ")
                print("Line edited.")
            else:
                print("Invalid line number.")
            content = "\n".join(lines)
            action = input("Type 'SAVE' to save or 'EXIT' to exit, or press enter to continue editing: ").upper()
            if action == 'SAVE':
                return content
            elif action == 'EXIT':
                return None

        except ValueError:
            print("Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            print("\nExiting editing without saving.")
            return None
    return content

def main():
    while True:
        print("\n--- Text Editor ---")
        print("1. Open File")
        print("2. Edit File")
        print("3. Save File")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            filename = input("Enter filename to open: ")
            content = open_file(filename)
            if content is not None:
                print("File opened successfully.")
                current_file = filename
                current_content = content
            else:
                print("File open failed")

        elif choice == '2':
            try:
                if 'current_content' in locals():
                    edited_content = edit_text(current_content)
                    if edited_content is not None:
                        current_content = edited_content
                else:
                    print("Please open a file first.")
            except NameError:
                print("Please open a file first.")

        elif choice == '3':
            try:
                if 'current_file' in locals() and 'current_content' in locals():
                    save_file(current_file, current_content)
                else:
                    print("Please open a file first.")
            except NameError:
                print("Please open a file first.")

        elif choice == '4':
            print("Exiting Text Editor.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
 
