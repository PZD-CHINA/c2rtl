# 循环遍历目录中的所有 C 文件
foreach c_file [glob -directory ./c *.c] {
    # 文件名处理，去除路径和扩展名，用于项目命名和顶层函数
    set base_name [file rootname [file tail $c_file]]

    # 创建项目
    open_project -reset $base_name
    set_top atax
    add_files $c_file

    # 设置 FPGA 部件
    open_solution -reset solution1 
    set_part  {xcvu9p-flga2104-2-i}
    create_clock -period 10

    # 运行综合
    csynth_design

    # 检查 rtl 目录是否存在，如果不存在则创建
    if { ![file exists ./rtl] } {
        file mkdir ./rtl
    }

    # 导出 RTL
    export_design
    
    # 保存和关闭项目
    close_solution
    close_project
}

exit
