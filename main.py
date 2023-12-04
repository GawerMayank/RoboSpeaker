"""This program is created by MAYANK SINGH GAWER
This is a simple program which is based on text to speech output
The user needs to input whatever they want to listen as an output """

# Importing required library
import os

# main function
if __name__ == '__main__':
    print("Welcome to Robospeaker created by Mayank")
    # for continuation until user quits
    while True:
        x = input("What you want me to say? ")
        if x == 'q':
            os.system("say 'bye bye friend'")
            break
        command = f"say {x}"
        os.system(command)
# End of the program
