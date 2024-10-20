#Write a Python program that writes out a table of the function sin(x) vs. x, where x is tabulated between 0 and 2 with a thousand entries. 
#Follow the basic Python program structure, including a main program function.

import numpy as np

from astropy.table import Table #import the Table class

#-------------------------------------------------------------------------------------------------
def main():
    p = 2 * np.pi #the value 2pi

    pp = float("%.2f"%p) #formatting 2pi to 2 decimal places for a cleaner output

    x = np.arange(0,pp,pp/1000) #Prints out numbers from range of 0 to 2pi in 1000 increments

    y = np.sin(x)
    
    table = Table([x,y],names=['x','sin(x)'])
    print(table)
    
if __name__=="__main__":
    main()
