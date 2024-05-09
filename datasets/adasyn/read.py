import csv

def count_values_in_column(csv_filename, column_index):
    count_0 = 0
    count_1 = 0

    with open(csv_filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row

        for row in csv_reader:
            try:
                value = int(row[column_index])
                if value == 0:
                    count_0 += 1
                elif value == 1:
                    count_1 += 1
            except ValueError:
                # Handle cases where the column value is not an integer
                pass

    return count_0, count_1

if __name__ == "__main__":
    csv_filename = "primary_upscaled_file.csv"  # Update with your CSV file's name
    column_index = 3  # Update with the index of the column you want to count (0-based)

    count_0, count_1 = count_values_in_column(csv_filename, column_index)

    print("Count of '0' values:", count_0)
    print("Count of '1' values:", count_1)
