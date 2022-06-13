#!/usr/bin/env python3
import sys
import functions

try:
    file_name = sys.argv[1]
except IndexError:
    file_name = '../units/counter/units/counter.v'
    #file_name = '../units/uart/uart/Uart8.v'

print('Parser analyzes', file_name, 'Verilog-HDL file\n')
debug = 1

input_cnt = 0
inout_cnt = 0
output_cnt = 0
str_input = "input"
str_inout = "inout"
str_output = "output"

#input_cnt, inout_cnt, output_cnt = functions.PortCnt(file_name, debug)
input_cnt = functions.PortCnt(file_name, str_input, debug)
inout_cnt = functions.PortCnt(file_name, str_inout, debug)
output_cnt = functions.PortCnt(file_name, str_output, debug)

print(input_cnt, " Input(s) in file")
print(inout_cnt, " Inout(s) in file")
print(output_cnt, " Output(s) in file")



#for row in file:
#    for letter in row:
#        print(letter)

#s = file.readlines() # create list, row is an element
#print(s)