"""
Nathan Drzadinski

Program Description
    This file houses all the functions that do different data analysis

"""
import csv
import numpy as np
import matplotlib.pyplot as plt

def linegraphg(infilename,outfilename):
    # Open csv file
    with open(infilename+'.csv') as csvfile:
        reader = csv.reader(csvfile)
        # Declare lists
        PWMlist = []
        Forcelist = []
        Timelist = []
        # Count removes csv header
        count =0
        for row in reader:
            if count != 0:
                # Removes error data (Redundant)
                if row[1] == '-10':
                    continue
                else:
                    PWMlist.append(float(row[0]))
                    Forcelist.append(float(row[1]))
                    Timelist.append(float(row[2])) 
            count+=1
        # Make Lists into arrays for graphing
        Timelist = np.array(Timelist,dtype=object)
        Forcelist = np.array(Forcelist,dtype=object)
        PWMlist = np.array(PWMlist,dtype=object)
        # Graph data and save to input filename
        fig, axis = plt.subplots()
        axis.plot(Timelist,Forcelist, color = "red")
        axis.set_xlabel("Time")
        axis.set_ylabel('Force (grams)')
        axis2 = axis.twinx()
        axis2.plot(Timelist,PWMlist,color="blue")
        axis2.set_ylabel('PWM Signal')
        plt.title("Force and PWM vs Time")
        plt.savefig(outfilename+'.png')
        print('\n\nAnalysis Completed!\n')

# Same as grams but units converted to Newtons
def linegraphN(infilename,outfilename):
    with open(infilename+'.csv') as csvfile:
        reader = csv.reader(csvfile)
        PWMlist = []
        Forcelist = []
        Timelist = []
        count =0
        for row in reader:
            if count != 0:
                if row[1] == '-10':
                    continue
                else:
                    PWMlist.append(float(row[0]))
                    Forcelist.append(float(row[1])*0.0098) # unit conversion
                    Timelist.append(float(row[2])) 
            count+=1
        Timelist = np.array(Timelist,dtype=object)
        Forcelist = np.array(Forcelist,dtype=object)
        PWMlist = np.array(PWMlist,dtype=object)
        fig, axis = plt.subplots()
        axis.plot(Timelist,Forcelist, color = "red")
        axis.set_xlabel("Time")
        axis.set_ylabel('Force (Newtons)')
        axis2 = axis.twinx()
        axis2.plot(Timelist,PWMlist,color="blue")
        axis2.set_ylabel('PWM Signal')
        plt.title("Force and PWM vs Time")
        plt.savefig(outfilename+'.png')
        print('\n\nAnalysis Completed!\n')