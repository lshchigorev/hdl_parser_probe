module counter(cnt_o, clk, reset, flag);

  parameter WIDTH = 8;

  output reg [WIDTH-1 : 0] cnt_o;
  input 	       clk  , reset;   
  //input               reset; //input
  //input
  /*
  input
  output
  */
  output flag;

  reg [WIDTH-1 : 0]   out;
  wire 	       clk, reset;

  always @(posedge clk or posedge reset)
    if (reset)
      cnt_o <= 0;
    else
      cnt_o <= cnt_o + 1;

  assign flag = 1;

endmodule // counter