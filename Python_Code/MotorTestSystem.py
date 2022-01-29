"""
Nathan Drzadinski

Program Description
    Test and collect data on the strength of a propeller motor for open source drone.

"""
import serial
import time
from recordData import send_data_to_csv as sendcsv

# Declare arduino as a serial object
arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)

def write_read(x):
    # Sends x to arduino
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    # Reads data from arduino
    data = arduino.readline()
    return data

def Test(filename):
    # Label CSV file
    field = ['PWM','Force','Time']
    sendcsv(filename,field)
    # Find a start time so can see change over time
    start_time = time.time()
    # Iterates through most motor speeds
    for pwm in range(0,181):
        for i in range(0,9):
            # Looks for return data error 
            try:
                fvalue = float(write_read(str(pwm)))
            except:
                fvalue = -10
            sendcsv(filename,[pwm,fvalue,time.time()-start_time])
    # Resets Arduino error variable
    write_read(str(181))
    # Turns Motor off at end of trial
    write_read(str(0))
    print("\n\nTest Complete!\n")

def main():
    pass

if __name__ == "__main__":
    main()