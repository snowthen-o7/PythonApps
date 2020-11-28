import pandas as pd
import pysftp
import re
import sys
import xml.etree.ElementTree as ET

def main(host, user, psswd, base_path, delta_path):
  '''
  Grab base file
  grab oldest delta
  apply changes from delta
  Update base file with timestamp of delta?
  '''


  try:
    # Establish sftp connection
    cxn = pysftp.Connection(host, username=user, password=psswd)
    print('Connection Established...')

    # Download base file
    cxn.get(base_path)
    print('Base file downloading...')

    # Read base file
    base_df = pd.read_csv(base_path.rsplit('/', 1)[-1], compression='gzip', sep='	', converters={'quantity_on_hand': lambda x: int(x), 'store_code': lambda x: str(x)})
    # converter applies a lambda function to a column, in this case casting the values to a str to keep leading zeroes
    print('Base file read')

    # Grab oldest delta file
    cxn.chdir(delta_path)
    delta_file_list = cxn.listdir_attr()
    if delta_file_list:
      cxn.get(delta_file_list[0].filename)
    print('Delta file downloading...')

    # Extract Delta data to dataframe
    delta_tree = ET.parse(delta_file_list[0].filename)
    inv_elements = delta_tree.findall(".//{*}Inventory") # {*} searches for the element in any namespace
    inv_dict = {'quantity_on_hand':[],'item_code':[],'store_code':[]}
    for i in inv_elements:
      inv_dict['quantity_on_hand'].append(i.find('{*}QuantityOnHand').text)
      inv_dict['item_code'].append(i.find('{*}Item/{*}Cd').text)
      inv_dict['store_code'].append(i.find('{*}Site/{*}Cd').text)
    delta_df = pd.DataFrame(inv_dict)
    print('Delta file read')

    # Full Join delta to base
    merged_df = pd.merge(base_df, delta_df, on=['item_code', 'store_code'], how='outer', indicator=True)
    print('Files merging...')
    # Set quantity to delta values where applicable
    merged_df.loc[merged_df._merge!='left_only', 'quantity_on_hand_x'] = merged_df.loc[merged_df._merge!='left_only', 'quantity_on_hand_y']
    # Remove unneeded columns 
    merged_df = merged_df.drop(['quantity_on_hand_y','_merge'], axis=1)
    # Rename qty column
    merged_df = merged_df.rename(columns={"quantity_on_hand_x": "quantity_on_hand"})
    print('Files merged')

    merged_filename = 'lia_base_file'+delta_file_list[0].filename.rsplit('y',1)[-1][:-4]+'.gz'
    # Write new base file
    merged_df.to_csv(merged_filename, sep='	', compression='gzip')
    print('New Base file created: ' + merged_filename)

    print('Attempting upload of ' + merged_filename + ' to ' + base_path.rsplit('/',1)[0] + '/' + merged_filename)
    # Export new base file
    cxn.put(merged_filename, base_path.rsplit('/',1)[0] + '/' + merged_filename)
    print('New Base file uploaded')

  except Exception as e:
    print(e)

  cxn.close()
  print(merged_filename + ' created!')

if __name__ == "__main__":
  host = str(sys.argv[1])
  user = str(sys.argv[2])
  psswd = str(sys.argv[3])
  base_path = str(sys.argv[4])
  delta_path = str(sys.argv[5])
  main(host, user, psswd, base_path, delta_path)
