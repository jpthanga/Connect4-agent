'''
Created on Oct 13, 2016

@author: Jeshuran
'''

import time

def main():
    
    start_time = time.time()
    a = 0b1
    a = a << 41
    
    b = 0b1
    b = b << 34
     
    a = a | b
    
    b = 0b1
    b = b << 27
     
    a = a | b
    
    b = 0b1
    b = b << 20
     
    a = a | b
    
    b = 0b1
    b = b << 13
     
    a = a | b
    
    b = 0b1
    b = b << 6
     
    a = a | b
    
    print(bin(a).count('1'))    
    print("{0:b}".format(a))

    print(time.time() - start_time)
    
if __name__ == '__main__':
    main()