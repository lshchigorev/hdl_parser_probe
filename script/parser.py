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
wire_cnt = 0
reg_cnt = 0
param_cnt = 0
always_cnt = 0
assign_cnt = 0

always_cnt = functions.PortCnt(file_name, "always", debug)
input_cnt = functions.PortCnt(file_name, "input", debug)
inout_cnt = functions.PortCnt(file_name, "inout", debug)
output_cnt = functions.PortCnt(file_name, "output", debug)
wire_cnt = functions.PortCnt(file_name, "wire", debug)
reg_cnt = functions.PortCnt(file_name, "reg", debug)
param_cnt = functions.PortCnt(file_name, "parameter", debug)
assign_cnt = functions.PortCnt(file_name, "assign", debug)



print(input_cnt, " Input(s) in file")
print(inout_cnt, " Inout(s) in file")
print(output_cnt, " Output(s) in file")
print(wire_cnt, " Wire(s) in file")
print(reg_cnt, " Reg(s) in file")
print(param_cnt, " Parameter(s) in file")
print(always_cnt, " always statement(s) in file")
print(assign_cnt, " assign statement(s) in file")



#for row in file:
#    for letter in row:
#        print(letter)

#s = file.readlines() # create list, row is an element
#print(s)