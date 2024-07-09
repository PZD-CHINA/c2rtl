# convert c to verilog(rtl) in batches

use vitis HLS to convert c (hls level) to veilog(rtl level) in batches.

## env

vitis HLS.

GNU parallel. [how to install](https://blog.csdn.net/weixin_40192882/article/details/136072504)

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

input: ./c_file_name/solution1/syn/veilog/top_function_name.v

output: ./rtl/*.v

## todo: 

now, for each c files, need configure top_function_name in c2rtl.tcl
