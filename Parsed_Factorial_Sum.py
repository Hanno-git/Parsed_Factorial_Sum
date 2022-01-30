# from math import factorial 
import numpy

def get_parsed_sum(i_fac):
    i_output = 0 
    if i_fac == 0:
        return 0
    while i_fac: #loops until no more digits in number ie ifac=0
        i_output +=i_fac%10 #adds the right most digit 
        i_fac = i_fac//10 # removes the right most digit
    return i_output #returns the parsed sum

def main():
    i_input,i_output,i_fac = 1,1,1 
    i_input = int(input()) # grabs the user input as integer
    i_fac = numpy.math.factorial(i_input) # determine the factorial of the user input
    i_output = get_parsed_sum(i_fac) # determine the parsed sum of the user input
    print(i_output) # prints the parsed factorial sum
    return 0

main()
