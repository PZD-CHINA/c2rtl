# convert c to verilog(rtl) in batches

Table of Contents:
- [convert c to verilog(rtl) in batches](#convert-c-to-verilogrtl-in-batches)
  - [vitis hls env (without installation)](#vitis-hls-env-without-installation)
    - [configure vitis HLS](#configure-vitis-hls)
    - [install GNU parallel for parallel code running](#install-gnu-parallel-for-parallel-code-running)
  - [How to convert c file to rtl (Verilog)](#how-to-convert-c-file-to-rtl-verilog)
  - [c2rtl in batches](#c2rtl-in-batches)
  - [extract rtl code from vitis log](#extract-rtl-code-from-vitis-log)
  - [todo:](#todo)


## vitis hls env (without installation)

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

## How to convert c file to rtl (Verilog)

1. Create a run_hls.tcl file:

    ```
    open_project -reset proj_name

    # set c file path
    add_files hls_code.c

    # set top function name of c file
    set_top function_name

    # set solution
    open_solution -reset solution1
    set_part  {xcvu9p-flga2104-2-i}
    create_clock -period 10

    # run synthesis to convert code
    csynth_design

    close_solution

    exit
    ```

2. Put the input.c file in the same directory as run_hls.tcl.

3. Run `vitis_hls -f run_hls.tcl` in shell.

4. After running the code, a new folder named `prog_name` will be created in the current directory. The converted Verilog code can be found at `./proj_name/solution1/syn/verilog/`.


## c2rtl in batches

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
