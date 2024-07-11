# convert c to verilog(rtl) in batches

use vitis HLS to convert c (hls level) to veilog(rtl level) in batches.

## env

### install vitis HLS

```shell
echo 'source /data/zedong/vitis/Vivado/2022.2/settings64.sh' >> ~/.bashrc
source ~/.bashrc
vitis --version
```

### install GNU parallel for parallel code running

```shell
(wget -O - pi.dk/3 || curl pi.dk/3/) | bash
echo 'export PATH=~/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
parallel --version
```

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
