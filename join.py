import link 
import time
import timetable

def joinenglish():
    driver.get(english) #class link
    time.sleep(60) #just addind extra time so that if anything bad happens it will take care of it
    alert = driver.switch_to_alert() #it will just pop up an alert box saying do you want to join or not
    alert.accept() #class will start
    time.sleep(3600) #class timing 1 hour
    driver.quit()

def joinmaths():
    driver.get(maths) #class link
    time.sleep(60) #just addind extra time so that if anything bad happens it will take care of it
    alert = driver.switch_to_alert() #it will just pop up an alert box saying do you want to join or not
    alert.accept() #class will start
    time.sleep(3600) #class timing 1 hour
    driver.quit()

def joinbiology():
    driver.get(biology) #class link
    time.sleep(60) #just addind extra time so that if anything bad happens it will take care of it
    alert = driver.switch_to_alert() #it will just pop up an alert box saying do you want to join or not
    alert.accept() #class will start
    time.sleep(3600) #class timing 1 hour
    driver.quit()

def joinphysics():
    driver.get(physics) #class link
    time.sleep(60) #just addind extra time so that if anything bad happens it will take care of it
    alert = driver.switch_to_alert() #it will just pop up an alert box saying do you want to join or not
    alert.accept() #class will start
    time.sleep(3600) #class timing 1 hour
    driver.quit()

def joinchemistry():
    driver.get(chemistry) #class link
    time.sleep(60) #just addind extra time so that if anything bad happens it will take care of it
    alert = driver.switch_to_alert() #it will just pop up an alert box saying do you want to join or not
    alert.accept() #class will start
    time.sleep(3600) #class timing 1 hour
    driver.quit()