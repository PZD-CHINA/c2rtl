#!/bin/bash

# 指定需要遍历的路径
SEARCH_DIR="/path/to/your/directory"

# 查找所有的 run_hls.tcl 文件并遍历它们
find "$SEARCH_DIR" -name "run_hls.tcl" | while read -r tcl_file; do
    echo "Processing $tcl_file"
    # 在包含 run_hls.tcl 文件的目录中执行 vitis_hls 命令
    (cd "$(dirname "$tcl_file")" && vitis_hls -f run_hls.tcl)
done
