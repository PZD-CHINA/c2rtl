# 检查并创建 rtl 目录
if { ![file exists ./rtl] } {
    file mkdir ./rtl
}

# 定义处理单个文件的过程
proc process_file {c_file} {
    # 文件名处理，去除路径和扩展名，用于项目命名和顶层函数
    set base_name [file rootname [file tail $c_file]]

    # 生成独立的 Tcl 脚本文件
    set script_file [open "process_$base_name.tcl" w]
    puts $script_file "
open_project -reset $base_name
set_top atax
add_files $c_file
open_solution -reset solution1
set_part  {xcvu9p-flga2104-2-i}
create_clock -period 10
csynth_design
if { ![file exists ./rtl] } {
    file mkdir ./rtl
}
export_design
close_solution
close_project
exit
"
    close $script_file

    # 返回生成的脚本文件名
    return "process_$base_name.tcl"
}

# 获取所有 C 文件
set c_files [glob -directory ./c *.c]

# 并行处理每个 C 文件
set script_files [list]
foreach c_file $c_files {
    lappend script_files [process_file $c_file]
}

# 使用 GNU Parallel 并行执行生成的 Tcl 脚本
set script_list_file [open "script_list.txt" w]
foreach script_file $script_files {
    puts $script_list_file $script_file
}
close $script_list_file

# 执行所有脚本文件，限制并行进程数为80
exec /home/pengzd/bin/parallel -j 80 vitis_hls -f :::: script_list.txt
