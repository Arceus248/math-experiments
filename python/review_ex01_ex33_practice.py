# ==============================================================================
# 阶段性综合复习练习：Learn Python the Hard Way (Ex 0 - Ex 33 综合串联)
# 文件名：review_ex01_ex33_practice.py
#
# 【复习任务：命令行数学批量统计与质数分析报告生成器】
#
# 本练习用于串联复习之前学过的所有核心模块：
#   - Ex 13-14：from sys import argv 参数解包 + input(prompt) 交互
#   - Ex 15-17：os.path.exists() + open('w'/'r') / write / read / seek(0) / readline / close / len
#   - Ex 18-21：def 函数定义、参数传递、return 多返回值与 tuple 解包
#   - Ex 22-26：str.split(' ') 切分、sorted() 排序、列表 0 基索引 nums[0]
#   - Ex 27-32：布尔值 True/False、逻辑运算符 and/or/not、if / elif / else 分支
#   - Ex 33    ：空列表 []、for 循环、range()、.append()
#   - 基础运算 ：+、/、%、+=、round()、f-string、三引号多行字符串与转义符 \t \n
#
# 题目要求（请严格仅用已学语法完成，不要使用 sum() / max() / min() / while / with）：
#
#   1. 命令行参数与文件存在检查（Ex 13, Ex 17）：
#      - 导入 sys.argv 与 os.path.exists；
#      - 解包接收 2 个命令行参数：script, user_name, report_file = argv；
#      - 打印报告文件 report_file 是否已存在（exists(report_file)）。
#
#   2. 交互式输入与列表构建（Ex 14, Ex 25, Ex 33）：
#      - 定义提示符 prompt = "> "；
#      - 打印提示，请用户输入一组用单个空格隔开的整数（例如：15 2 9 28 7 12 30）；
#      - 使用 .split(' ') 将输入切分为字符串列表；
#      - 创建一个空列表 numbers = []，用 for 循环遍历切分后的列表，
#        用 int() 逐个转换成整数并 .append() 到 numbers 中。
#      - （边界检查）如果 numbers 为空或元素个数 == 0，打印提示信息；否则继续后续分析。
#
#   3. 编写统计函数 def analyze_stats(nums):（Ex 18-21, Ex 23, Ex 33）：
#      - 用 for 循环手动计算列表中所有数字的总和 total；
#      - 用 nums[0] 初始化最大值 max_val 和最小值 min_val，并在循环中用 if 更新它们；
#      - 计算平均值 avg = round(total / len(nums), 2)；
#      - 使用 return 返回 4 个值：total, avg, max_val, min_val。
#
#   4. 编写质数判断函数 def is_prime(n):（Ex 21, Ex 28-32, Ex 33）：
#      - 数学定义：大于 1 且只能被 1 和自身整除的整数称为质数（Prime Number）；
#      - 如果 n <= 1，直接 return False；
#      - 使用 for d in range(2, n): 逐个检查 n % d == 0；
#      - 若找到任意能整除的 d，立即 return False；若循环结束仍未找到，return True。
#
#   5. 编写分类筛选函数 def classify_numbers(nums):（Ex 25, Ex 28-33）：
#      - 创建三个空列表：primes = []，div_3_and_5 = []，evens = []；
#      - 遍历 nums：
#          a) 调用 is_prime(n)，若为 True 则加入 primes；
#          b) 使用布尔逻辑 and，判断 n 能否同时被 3 和 5 整除，若是则加入 div_3_and_5；
#          c) 判断 n 是否为偶数（n % 2 == 0），若是则加入 evens；
#      - 使用 sorted() 对这三个列表分别升序排序后，return 三个排好序的列表。
#
#   6. 报告写入、指针倒带与读取校验（Ex 9-10, Ex 15-17）：
#      - 在主流程中调用上述函数并用解包变量接住返回值；
#      - 使用 f"""...""" 多行字符串配合 \t 缩进排版出清晰报告（含操作人 user_name、
#        原始数字列表、统计值、质数列表、15的倍数列表、偶数列表）；
#      - 使用 open(report_file, 'w') 打开文件，调用 .write() 写入报告并 .close()；
#      - 再用 open(report_file, 'r') 重新打开文件：
#          a) 用 .read() 读取全文并打印；
#          b) 用 len() 打印报告总字符数；
#          c) 调用 .seek(0) 将磁头倒回开头，再用 .readline() 单独打印第一行标题；
#          d) 最后调用 .close() 关闭文件。
#
# ------------------------------------------------------------------------------
# 【运行方式与预期结果示例】
#
# 终端运行命令：
#   python review_ex01_ex33_practice.py Alex math_report.txt
#
# 预期屏幕交互与输出：
#   你好 Alex，目标报告文件 math_report.txt 是否已存在: False
#   请输入一组用空格隔开的整数:
#   > 15 2 9 28 7 12 30
#   报告已写入 math_report.txt，共 XXX 个字符。
#   --- 文件内容校验 ---
#   === 数学分析报告 (操作员: Alex) ===
#       原始数据: [15, 2, 9, 28, 7, 12, 30]
#       数量: 7 | 总和: 103 | 平均值: 14.71
#       最大值: 30 | 最小值: 2
#       质数列表(升序): [2, 7]
#       同时被 3 和 5 整除(升序): [15, 30]
#       偶数列表(升序): [2, 12, 28, 30]
#   --- 倒带读取第 1 行 ---
#   === 数学分析报告 (操作员: Alex) ===
# ==============================================================================

# 请在下方开始编写你的代码：
