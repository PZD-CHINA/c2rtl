# convert c to verilog(rtl) in batches

use vitis HLS to convert c (hls level) to veilog(rtl level) in batches.

## c2rtl

```shell
vitis_hls -f c2rtl.tcl
```

input: ./c/*.cpp

output: ./c_file_name/solution1/syn/veilog/top_function_name.v

## extract rtl code from vitis log

```shell
python extract_rtl_code.py
```

output: ./rtl/*.v

## todo: 

now, for each c files, need configure top_function_name in c2rtl.tcl
