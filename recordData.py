"""
Nathan Drzadinski

Program Description
    This file houses the function that writes the data to a csv file
"""


import csv

# Append relevent data to specificized csv file
def send_data_to_csv(filename, input):
    # This stops a data error from being added to the csv file
    if input[1] != '-10':
        with open(filename+".csv",'a') as csvfile:
            writer = csv.writer(csvfile,lineterminator = '\n')
            writer.writerow(input)

def main():
    pass

if __name__ == "__main__":
    main()