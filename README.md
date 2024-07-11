# convert c to verilog(rtl) in batches

use vitis HLS to convert c (hls level) to veilog(rtl level) in batches.

## env

### configure vitis HLS

vitis already installed at /data/zedong/vitis. Only need to configure vitis environment.

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

problem: need configure top_function_name for each c files in c2rtl.tcl 

solution: parse all function name or llm extract top function name.
