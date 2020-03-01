import os

# main function
def main():
  # Finds absolute path of the filename on the machine that's in the current working directory
  filename = os.path.abspath( "keyval_test.csv" )
  # Prints filename obtained for double checking
  print(filename)
  
  # Open file in read mode and assign to variable
  file_data = open(filename, 'r')
  
  # Extract header data by reading first line, stripping whitespace chars at start & end by default, and splitting it by comma chars
  source_header = file_data.readline().strip().split(',')
  # Prints header obtained for double checking
  print(source_header)

  # Declare table to hold our rows
  table = []

  # Iterate through file_data
  for line in file_data:
    source_row = line.strip().split(',')
    final_row = dict()
    # Assigning the data found in nth index of the header to the column being created by also passing the key to the row
    for i,h in enumerate(source_header):
      final_row[h] = source_row[i]
      
    # Add final row to final table
    table.append(final_row)
    
  print(table)
  table.sort(key= lambda r: int(r['year']))
  
if __name__ == "__main__":
  main()