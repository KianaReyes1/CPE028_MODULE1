file=open("devices.txt","r")
while(True):
   newItem=input("Enter your device: ")
   if newItem==("Exit"):
        print("All done!")
        break
        file.write(newItem + "\n")
file.close()
