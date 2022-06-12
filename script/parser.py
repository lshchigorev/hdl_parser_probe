#!/usr/bin/env python3
import sys
import functions

try:
    file_name = sys.argv[1]
except IndexError:
    file_name = '../units/counter/units/counter.v'
    #file_name = '../units/uart/uart/Uart8.v'

print('Parser analyzes', file_name, 'Verilog-HDL file\n')

input_cnt = 0
output_cnt = 0

input_cnt = functions.InOutRegWireCnt(file_name, 'input')
output_cnt = functions.InOutRegWireCnt(file_name, 'output')

print(input_cnt, " Input(s) in file")
print(output_cnt, " Output(s) in file")



#for row in file:
#    for letter in row:
#        print(letter)

#s = file.readlines() # create list, row is an element
#print(s)