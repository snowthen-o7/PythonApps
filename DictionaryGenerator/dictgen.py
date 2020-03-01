"""
Lists of Lists Combiner, or Dictionary Generator

Parameters:
- CSV file containing any number of columns
- Each column contains a list of values, separated by ' > '
- Assumes the length of each list in each column is equal

This script combines each list from each column into one column.
The result is one list with each index of that final list
containing all the values that were in that index in the other lists.

- Like indices are concatenated using ':'
- Indices are separated by ','

Example input:
PRIMARY_KEY|     list_1|     list_2|    list_3
        001|  A > B > C|  D > E > F| X > Y > Z
        
Final output:
PRIMARY_KEY|        final_list
        001| A:D:X,B:E:Y,C:F:Z
"""
import csv

# Open input file
with open('keyval.csv', 'r') as csv_file:
  csv_reader = csv.reader(csv_file)
  
  # Skip header
  next(csv_reader)
  
  # Start writing to output
  with open('new_keyvals.txt', 'w') as new_file:
    csv_writer = csv.writer(new_file, delimiter='\t', lineterminator='\n')
    
    # Write new header
    csv_writer.writerow(['join_value', 'new_list'])
  
    # Iterate through each row in input
    for line in csv_reader:
      # Keep primary key in place
      row = [line[0],'']
      # Create array of equal size to number of columns
      final_list = [''] * (len(line) - 1)
      
      # Make final_list a 2D list consisting of the contents of the columns
      i = 1
      while i < len(line):
        final_list[i-1] = line[i].split(' > ')
        i += 1
  
      # i is the length of each list found in each column - 1
      i = 0
      while i < len(final_list[0]):
        # j is the number of columns in the input file - 1
        j = 0
        while j < len(final_list):
          # Initial insert of a value
          if(row[1] == '' or j == 0):
            row[1] += final_list[j][i]
          # The last value in a column has been reached
          elif j == len(final_list) - 1 and i != len(final_list[0]) - 1:
            row[1] += ':' + final_list[j][i] + ','
          # Value that isn't first or last in its column
          else:
            row[1] += ':' + final_list[j][i]
          j += 1
        i += 1
      row[1] = ','.join(set(row[1].split(',')))
      csv_writer.writerow(row)