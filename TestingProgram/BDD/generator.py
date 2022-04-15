import random
with open('testvalues8.txt',"w")as file:
    for i in range(8192):
        binary="00000000"
        binary=binary+bin(i)
        file.write(binary[len(binary)-8:]+'\n')