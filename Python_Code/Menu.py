"""
Nathan Drzadinski

Program Description
    Main function will run test menu and can run any coded tests

"""
import MotorTestSystem as MTS
import Analysis as A

def main():
    # Menu runs infinite until given command to end
    while True:
        # A basic Menu Structure
        in1 = input("Pick a task:\n1) Test\n2) Analyze Data\n3) End Program\n")
        if in1 == '1' or in1.lower == "test":
            in2 = input("Please input desired save file name without extension\n")
            MTS.Test(in2)
        elif in1 == '2' or in1.lower == "analyze data":
            in3 = input("Pick an analysis force unit:\n1) Grams\n2) Newtons\n")
            if in3 == '1':
                inf = input("Input input filename\n")
                outf = input('Input output filename\n')
                A.linegraphg(inf,outf)
            elif in3 == '2':
                inf = input("Input input filename\n")
                outf = input('Input output filename\n')
                A.linegraphN(inf,outf)
        elif in1 == '3' or in1.lower == "end program":
            break
        else:
            print("Error: User input\n")

if __name__ == "__main__":
    main()