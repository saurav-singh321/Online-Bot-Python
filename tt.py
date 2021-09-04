
import info 
import join 
import schedule as sd #this is to check whether its the time or not
import time

def monday():
    sd.every().monday.at(first_class).do(joinenglish)
    sd.every().tuesday.at(second_class).do(joinmaths)
    sd.every().wednesday.at(third_class).do(joinbiology)
    sd.every().thursday.at(fourth_class).do(joinphysics)
    sd.every().friday.at(fifth_class).do(joinchemistry)
    
def tuesday():
    sd.every().monday.at(first_class).do(joinenglish)
    sd.every().tuesday.at(second_class).do(joinmaths)
    sd.every().wednesday.at(third_class).do(joinbiology)
    sd.every().thursday.at(fourth_class).do(joinphysics)
    sd.every().friday.at(fifth_class).do(joinchemistry)
    
def wednesday():
    sd.every().monday.at(first_class).do(joinenglish)
    sd.every().tuesday.at(second_class).do(joinmaths)
    sd.every().wednesday.at(third_class).do(joinbiology)
    sd.every().thursday.at(fourth_class).do(joinphysics)
    sd.every().friday.at(fifth_class).do(joinchemistry)
    
def friday():
    sd.every().monday.at(first_class).do(joinenglish)
    sd.every().tuesday.at(second_class).do(joinmaths)
    sd.every().wednesday.at(third_class).do(joinbiology)
    sd.every().thursday.at(fourth_class).do(joinphysics)
    sd.every().friday.at(fifth_class).do(joinchemistry)

def saturday():
    sd.every().monday.at(first_class).do(joinenglish)
    sd.every().tuesday.at(second_class).do(joinmaths)
    sd.every().wednesday.at(third_class).do(joinbiology)
    sd.every().thursday.at(fourth_class).do(joinphysics)
    sd.every().friday.at(fifth_class).do(joinchemistry)

while(True):
    sd.run_pending()
    time.sleep(60) #that means it will check after every 60 seconds wheter its time to join the other clasa or not