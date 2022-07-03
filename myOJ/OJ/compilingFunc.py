import filecmp
import subprocess
import os

def compiler(code):
    with open('/Users/lalitjena/Desktop/mainproject/Online-Judge/myOJ/OJ/usercode/solution.cpp', 'w') as f:
        f.write(code)
    os.system('g++ /Users/lalitjena/Desktop/mainproject/Online-Judge/myOJ/OJ/usercode/solution.cpp')
    os.system('./a.out </Users/lalitjena/Desktop/mainproject/Online-Judge/myOJ/OJ/usercode/input.txt> /Users/lalitjena/Desktop/mainproject/Online-Judge/myOJ/OJ/usercode/output.txt')
    output1 = '/Users/lalitjena/Desktop/mainproject/Online-Judge/myOJ/OJ/usercode/input.txt'
    output2 = '/Users/lalitjena/Desktop/mainproject/Online-Judge/myOJ/OJ/usercode/output.txt'
    # if (filecmp(output1,output2,shallow=False)):
    #     print("Y")
    # else:
    #     print("N")

 