import sys, time 
 
for char in "hello, world.": 
    print(char, end='') 
    sys.stdout.flush() 
    time.sleep(0.2) 