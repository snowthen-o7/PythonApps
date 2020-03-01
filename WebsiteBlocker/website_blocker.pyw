import time
from datetime import datetime as dt

hosts_temp = r"C:\Users\darkphantom7\Desktop\Laulex\WebsiteBlocker\hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.reddit.com","www.reddit.com/r/all","www.youtube.com","www.chrono.gg","champion.gg","porofessor.gg"]

while True:
  # While within working hours, 4AM - 9PM, append the list of websites that we want blocked
  if dt(dt.now().year,dt.now().month,dt.now().day,4) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,21):
    print("Working hours...")
    # Opening file path to temp host file with read/write capability
    with open(hosts_path,'r+') as file:
      file_content = file.read()
      print(file_content)
      for website in website_list:
        if website in file_content:
          pass
        # Cleanly inserts the websites regardless if the file ends in a linebreak or not 
        else:
          if file_content.rfind("\n") == (len(file_content) - 1):
            file.write(redirect + " " + website + "\n")
            file_content += redirect + " " + website + "\n"
          else:
            file.write("\n" + redirect + " " + website + "\n")
            file_content += "\n" + redirect + " " + website + "\n"
            
  # Write each line of the host file that doesn't contain something from the website list
  else:
    # Opening file path to temp host file with read/write capability
    with open(hosts_path,'r+') as file:
      # Read file contents including linebreaks
      file_content = file.readlines()
      # Reset pointer to the beginning of the file
      file.seek(0)
      for line in file_content:
        if not any(website in line for website in website_list):
          file.write(line)
        # Get rid of everything after our pointer, so everything that was in the file previously
        file.truncate()
    print("Fun Hours...")
  time.sleep(60)