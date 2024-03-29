def remove_rows_with_empty_first_column(csv_file_path):
    # Open the input CSV file and create a list to store non-empty rows
    with open(csv_file_path, 'r', newline='') as infile:
        reader = csv.reader(infile)
        non_empty_rows = [row for row in reader if row[0]]

    # Write the non-empty rows back to the same CSV file
    with open(csv_file_path, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(non_empty_rows)

#   csv_file_path = 'your csv.csv'  # Provide the path to your CSV file
#   remove_rows_with_empty_first_column(csv_file_path)