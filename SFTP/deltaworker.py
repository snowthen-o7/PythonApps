import pysftp
import sys
import xml

# read base file
def read_base(filename):
  try: 
    with open(filename) as base:
      base_data = base.read()
      return base_data
  
  except Exception as e:
    print(e)

def sftp_upload(host, user, psswd, object_path, dest):
  try:
    with pysftp.Connection(host, username=user, password=psswd) as cxn:
      cxn.put(object_path, dest)           # upload file to dest path
      print('Upload Success')

  except Exception as e:
    print(e)

def sftp_download(host, user, psswd, object_path, dest):
  try:
    with pysftp.Connection(host, username=user, password=psswd) as cxn:
      cxn.get(dest, object_path)           # upload file to dest path
      print('Download Success')

  except Exception as e:
    print(e)

def main(host, user, psswd, base_path, delta_path):
  '''
  Grab base file
  grab oldest delta
  apply changes from delta
  Update base file with timestamp of delta?
  '''
  base_data = read_base(base_path)


if __name__ == "__main__":
  host = str(sys.argv[1])
  user = str(sys.argv[2])
  psswd = str(sys.argv[3])
  base_path = str(sys.argv[4])
  delta_path = str(sys.argv[5])
  main(host, user, psswd, base_path, delta_path)
