# convert c to verilog(rtl) in batches

use vitis HLS to convert c (hls level) to veilog(rtl level) in batches.

input: *.c files saved in ./c/

output: ./c_file_name/solution1/syn/veilog/top_function_name.v

how to use：

```shell
vitis_hls -f c2rtl.tcl
python extract_rtl_code.py
```

todo: 

now, for each c files, need configure top_function_name in c2rtl.tcl
