rm my_design
iverilog -o my_design -c file_list.txt
vvp my_design
