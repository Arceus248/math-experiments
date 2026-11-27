# ==============================================================================
# 练习进度：Learn Python the Hard Way - Module 2 结业综合小项目（Ex 0 - Ex 37 全串联）
# 章节主题：交互式数学实验台与运算审计报告系统
# 文件名：ex34_37_math_project.py
#
# 【项目背景】
#   你需要综合运用 Module 2 学过的全部核心知识（sys.argv、os.path.exists、File I/O、
#   嵌套列表 0 基索引、def/return 多返回值、while 主循环、多函数分支状态调度、
#   Ex 36 设计规范以及 Ex 37 符号如 break / continue / None / is / // / ** / assert），
#   从零设计并实现一个可反复使用的“交互式数学实验台”。
#
# 【具体输入与输出要求】
#   1. 启动与命令行参数（Ex 13, Ex 17）：
#      - 从 sys 导入 argv 和 exit，从 os.path 导入 exists；
#      - 解包接收参数：script, operator_name, report_file = argv；
#      - 启动时显示操作员名称，以及报告文件 report_file 是否已存在。
#   2. 主菜单与状态分发循环（Ex 34, Ex 35）：
#      - 在主函数中创建二维历史账本 history = []；
#      - 使用 while True: 显示菜单并循环读取用户指令：
#          "1": 幂与模运算器（计算 base ** exp、整除商与余数）
#          "2": 最大公约数与最小公倍数计算器（欧几里得辗转相除法）
#          "3": 区间水仙花数/阿姆斯特朗数扫描器
#          "4": 查看实验历史账本（0 基索引定位与全量列出）
#          "5": 导出审计报告到 report_file 并退出（exit(0)）
#      - 每个菜单分支必须配 else 兜底提示“无效选项，请输入 1-5”。
#   3. 三个数学计算功能函数（必须独立封装、只使用形参、通过 return 返回结果）：
#      - 功能 1 def calc_power_mod(base, exp, mod):
#          * 用 assert mod > 0, "模数必须大于 0" 校验；
#          * 返回 3 个值：power_val = base ** exp，quotient = power_val // mod，
#            remainder = power_val % mod；
#          * 主循环将结果按 ["power_mod", f"{base}^{exp} mod {mod}", remainder]
#            的列表格式 .append() 到 history 中。
#      - 功能 2 def calc_gcd_lcm(num_a, num_b):
#          * 用 assert num_a > 0 and num_b > 0, "输入必须为正整数" 校验；
#          * 使用 while 循环实现欧几里得辗转相除法（当 b != 0 时，计算 r = a % b，
#            更新 a = b, b = r）求得最大公约数 gcd_val；
#          * 再用整除计算最小公倍数 lcm_val = (num_a * num_b) // gcd_val；
#          * return gcd_val, lcm_val，并存入 history（例如 ["gcd_lcm", [num_a, num_b], [gcd_val, lcm_val]]）。
#      - 功能 3 def scan_armstrong(low, high):
#          * 阿姆斯特朗数（自幂数）定义：一个 k 位数，其各位数字的 k 次幂之和等于它本身
#            （例如 153 = 1**3 + 5**3 + 3**3；单数字 1~9 也满足 k=1）；
#          * 用 while temp > 0: 配合 temp % 10 与 temp //= 10 拆解每一位数字；
#          * 收集 [low, high] 内所有满足条件的整数；若一个都没有，必须 return None；
#          * 主循环用 if found_list is None: 判断并打印提示；若找到则记录进 history。
#   4. 历史账本查询（功能 4，巩固嵌套列表 0 基索引）：
#      - 若 len(history) == 0，打印“暂无实验记录”；
#      - 若非空，先打印总条数、第 1 条记录 history[0]、最后 1 条记录 history[-1]，
#        并支持用户输入 0 基编号查询指定记录详情（需校验编号范围 `0 <= idx < len(history)`）。
#   5. 导出报告与退出（功能 5，串联 Ex 15-17 File I/O）：
#      - 使用 open(report_file, 'w', encoding='utf-8') 写入完整实验报告（含操作员、
#        总实验次数、逐条实验详情），写完后 .close()；
#      - 重新以 'r' 模式打开，先 .read() 打印校验与字符总长度 len(content)，
#        再 .seek(0) 倒带后用 .readline() 单独打印报告第 1 行标题，.close() 后 exit(0) 退出。
#      - 若用户在所有数字输入环节敲入空值或非纯数字，必须在调用函数前用 if/else + .isdigit() 拦截。
#
# 【允许使用的语法范围】
#   - 仅限 Ex 0 - Ex 37 已学全部基础语法（含 sys.argv/exit、os.path.exists、File I/O、
#     嵌套列表索引、while、for、if/elif/else、def/return、break/continue/None/is/assert）。
#   - 严禁使用：try / except、with 语句、字典进阶方法、class、sum()/max()/min()、全局变量。
#
# 【终端运行命令与预期结果示例】（共 3 组完整场景）
#
# 终端运行命令：
#   python ex34_37_math_project.py Lin math_lab_report.txt
#
# 示例 1（连续运行功能 1 与功能 2，再查询功能 4）：
#   操作员: Lin | 报告文件 math_lab_report.txt 是否已存在: False
#   === 数学实验台菜单 ===
#   1. 幂与模运算 | 2. GCD/LCM | 3. 水仙花数扫描 | 4. 历史账本 | 5. 导出并退出
#   请选择(1-5): 1
#   请输入底数(>=0): 2
#   请输入指数(>=0): 10
#   请输入模数(>0): 100
#   结果: 2 ** 10 = 1024 | 整除商: 10 | 余数: 24
#   请选择(1-5): 2
#   请输入第一个正整数: 12
#   请输入第二个正整数: 18
#   结果: GCD = 6, LCM = 36
#   请选择(1-5): 4
#   共有 2 条实验记录:
#   [0] ['power_mod', '2^10 mod 100', 24]
#   [1] ['gcd_lcm', [12, 18], [6, 36]]
#   首条记录类型: power_mod | 末条记录结果: [6, 36]
#   请输入要查询的记录编号(0-1): 1
#   第 1 条记录详情 -> 类型: gcd_lcm, 输入: [12, 18], 结果: [6, 36]
#
# 示例 2（功能 3：扫描 [100, 500] 与无结果区间 [200, 300]）：
#   请选择(1-5): 3
#   请输入起点(>=1): 100
#   请输入终点(>=起点): 500
#   [100, 500] 内的阿姆斯特朗数: [153, 370, 371, 407]
#   请选择(1-5): 3
#   请输入起点(>=1): 200
#   请输入终点(>=起点): 300
#   区间 [200, 300] 内未找到阿姆斯特朗数（返回 None）。
#
# 示例 3（功能 5：导出报告并做 File I/O 读取与倒带校验后退出）：
#   请选择(1-5): 5
#   报告已写入 math_lab_report.txt，共 XXX 个字符。
#   --- 报告全文校验 ---
#   === 数学实验审计报告 (操作员: Lin) ===
#       实验总次数: 3
#       记录 0: ['power_mod', '2^10 mod 100', 24]
#       记录 1: ['gcd_lcm', [12, 18], [6, 36]]
#       记录 2: ['armstrong', [100, 500], [153, 370, 371, 407]]
#   --- 倒带读取第 1 行 ---
#   === 数学实验审计报告 (操作员: Lin) ===
#   再见！
# ==============================================================================

# 请在下方开始编写你的代码：
