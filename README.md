**************************************
* Project: hdl_parser_probe
* Author: lshchigorev
* GIT: https://github.com/lshchigorev/hdl_parser_probe
**************************************

How to start: ./parser.py <path_to_hdl>
Default HDL:  ../units/counter/units/counter.v

# Version 0.01
# 14.06.2022
# definitely not supported:
 - instanes;
 - multistring variable declaration
   for example:
    input clk,
          reset,
          smth_else;
 - multivariables declaration
   for example:
    input clk, reset, smthelse;