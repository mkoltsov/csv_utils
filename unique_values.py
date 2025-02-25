import sys
import csv
import re

def clean_html(text):
    # Remove HTML tags and get the text inside
    # This pattern matches the last occurrence of text between > and <
    pattern = '>([^<>]*)</a>'
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    return text

def get_unique_values(filename, column_name):
    try:
        # Set to store unique values
        unique_values = set()

        # Open and read the CSV file
        with open(filename, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)

            # Get header row
            header = next(csv_reader)

            # Find the index of the specified column name
            try:
                column_index = header.index(column_name)
            except ValueError:
                raise ValueError(f"Column '{column_name}' not found in the CSV file")

            # Print column name
            print(f"\nColumn name: {column_name}")
            print("\nUnique values:")

            # Process each row
            for row in csv_reader:
                if len(row) > column_index:  # Ensure row has enough columns
                    # Clean HTML tags and add to unique values
                    cleaned_value = clean_html(row[column_index])
                    unique_values.add(cleaned_value)

        # Print unique values
        for value in sorted(unique_values):
            print(value)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

def main():
    # Check if correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <filename> <column_name>")
        print('Example: python script.py data.csv "Controller Url"')
        sys.exit(1)

    # Get filename and column name from command line arguments
    filename = sys.argv[1]
    column_name = sys.argv[2]

    # Call function to get unique values
    get_unique_values(filename, column_name)

if __name__ == "__main__":
    main()
