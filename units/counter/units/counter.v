module counter(cnt_o, clk, reset);

  parameter WIDTH = 8;

  output reg [WIDTH-1 : 0] cnt_o;
  input 	       clk, reset;

  reg [WIDTH-1 : 0]   out;
  wire 	       clk, reset;

  always @(posedge clk or posedge reset)
    if (reset)
      cnt_o <= 0;
    else
      cnt_o <= cnt_o + 1;

endmodule // counter