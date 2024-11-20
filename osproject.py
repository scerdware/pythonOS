import time 
runtel = 1

def display_time():
    current_time = tm.strftime('%H:%M:%S %p')
    clock_label['text'] = current_time
    my_window.after(200,display_time)
    
#intro/tag
version = "1.0.0"
print(f"you are currently using version {version}")
print()
print("hello this is the epidemy of bordom.")
print()
print("creds to crcollin. I will add the github repo when you quit the terminal.")
print()
print("more on that first part, this is a fake operating system. I call it fake because its not real \nmaybe idrk tbh but this program is supposed to replicate a terminal computer from the dinosaur \nera of PC's")
print()
print("type /help for a list of commands")
print("-"*38)

while runtel == 1:
    
    print(" ")
    ask = input("What would you like me to do?")
    
    if ask == "/help":
        print("-"*38)
        print("ok let me scrape up a list of commands!")
        print(" ")
        print("/write = Create Text File")
        print(" ")
        print("/read = Reads Out A Text File")
        print(" ")
        print("/time = Gives You The Exact Time And Date")
        print(" ")
        print("/calculate = Calclates A Problem")
        print(" ")
        print("/esc = Stops The Program")
        
#math
    elif ask == "/calculate":
        print(" ")
        time_for_math = input("What is your equation?")
        print(" ")
        print(eval(time_for_math))
#stop program
    elif ask == "/esc":
        print(" ")
        print("Ok, thank you for exploring the world of pythonOS")
        print(" ")
        print("copy this link for credits for crcollin. https://github.com/crcollins/pyOS")
        print(" ")
        print("shutting down system")
        runtel = 0
#whats the time
    elif ask == "/time":
        print(" ")
        print(time.asctime())
#write in a .txt file
    elif ask == "/write":
        print(" ")
        print("making a new .txt file")
        print(" ")
        input("what do you want the .txt file to be called?")
        print(" ")
        textsession = input('What would you like to write?')
        print(' ')
        print(textsession)
        print(" ")
        save = input("Do you want to save this? y or n.")
        print('')
        if save == "n":
            print("Deleting...")
            textsession = 0
        elif save == "y":
            filename = save == input("are your sure")
            import pickle
            with open(filename, 'wb') as f:
                pickle.dump([textsession], f)
                print(" ")
            print("Saved At", time.asctime())
            textsession = 0
#read .txt file
    elif ask == "/read":
        print(" ")
        reader = input("What is the name of the file?")
        print(" ")
        import pickle
        with open(reader, 'rb') as f:
            textsession = pickle.load(f)
            print(textsession)