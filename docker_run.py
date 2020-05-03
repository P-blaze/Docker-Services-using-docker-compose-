import os

os.system("tput setaf 1")

print("\n\t\t\t--------------------------------------")
print("")

print("\t\t\t <== Welcome to Docker Services ==>")
print("")
print("\t\t\t----------------------------------------")
os.system("tput setaf 4")


while True:
  print("""
  1: Launch Wordpress Infrastructure
  
  2: Lauch Owncloud Infrastructure
  
  3: Lauch Joomla Infrastructure
  
  4: Stop &  Remove Joomla Infrastructure
  
  5: Stop & Remove Wordpress Infrastructure
  
  6: Stop & Remove Owncloud Infrastructure
  
  7: Exit
  """)
  os.system("tput setaf 6")
  ch = int(input("Enter your choice : "))
  os.system("tput setaf 7")
  
  if ch == 1:
      print("To acces the webpage : In any browser type : <IP Adress>/8081:80")
      os.chdir("/root/Docker-Project/wordpress/")
      os.system("docker-compose up -d")
  
  elif ch == 2:
      print("To acces the webpage : In any browser type : <IP Adress>/8082:80")
      os.chdir("/root/Docker-Project/owncloud/")
      
      os.system("docker-compose up -d")
  
  elif ch == 3:
      print("To acces the webpage : In any browser type : <IP Adress>/8083:80")
      os.chdir("/root/Docker-Project/joomla/")
      os.system("docker-compose up -d")
      
  elif ch == 4:
      os.chdir("/root/Docker-Project/joomla/")
      os.system("docker-compose stop")
      os.system("docker-compose rm")
  
  elif ch == 5:
      os.chdir("/root/Docker-Project/wordpress/")
      os.system("docker-compose stop")
      os.system("docker-compose rm")
  
  elif ch == 6:
      os.chdir("/root/Docker-Project/owncloud/")
      os.system("docker-compose stop")
      os.system("docker-compose rm")

  elif ch  == 7:
      exit()

    
