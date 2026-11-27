# ==============================================================================
# 练习进度：Learn Python the Hard Way - 新版 Ex 34（对应老师旧版 Ex 33）
# 章节主题：While Loops（while 条件循环）
# 文件名：ex34_while_practice.py
#
# 【题目背景：考拉兹猜想（Collatz Conjecture / 3n + 1 问题）轨迹追踪器】
#   数学家角谷静夫提出的“考拉兹猜想”规则如下：
#     给定任意一个正整数 n，重复执行以下变换，直到 n 变成 1 为止：
#       - 如果 n 是偶数（n % 2 == 0），下一个数变成 n // 2；
#       - 如果 n 是奇数（n % 2 == 1），下一个数变成 3 * n + 1。
#   例如：从 6 出发，轨迹为 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1（共 8 步，峰值 16）。
#   由于我们事先无法预知任意正整数需要多少步才能回到 1，这正是必须使用
#   while 循环（而不是 for 循环）的典型数学问题。
#
# 【具体输入与输出要求】
#   1. 输入合法性校验循环（while 循环 1）：
#      - 不断使用 input() 提示用户输入一个正整数；
#      - 若输入为空字符串、包含非数字字符（利用 .isdigit() 判断）或数值 <= 0，
#        打印错误提示并让用户重新输入，直到拿到一个有效的正整数为止；
#      - 拿到有效输入后，将其转换为 int 存入 start_num 并结束输入循环。
#   2. 考拉兹序列计算循环（while 循环 2）：
#      - 初始化空列表或只包含起点的列表：sequence = [start_num]；
#      - 在循环外部初始化步数计数器 steps = 0、峰值记录 peak_value = start_num，
#        以及当前值 current = start_num；
#      - 使用 while current != 1: 循环推进计算：
#          a) 按奇偶规则计算下一个 current（注意用整除 // 2 保持整数类型）；
#          b) 将新得到的 current 追加到 sequence 列表中（.append()）；
#          c) 将 steps 加 1；
#          d) 用 if 判断当前 current 是否大于 peak_value，若是则更新 peak_value。
#   3. 汇总输出要求（必须缩进在 while 循环外部）：
#      - 使用 f-string 打印：起点数字、完整变换轨迹列表 sequence、总步数 steps、
#        过程出现过的最大峰值 peak_value；
#      - 特别检查边界：当用户输入 1 时，while current != 1: 执行 0 次，
#        仍须正常输出 sequence = [1]、steps = 0、peak_value = 1。
#
# 【允许使用的语法范围】
#   - 仅限 Ex 0 - Ex 34 已学语法：
#     变量、int/str/bool、算术与比较运算符（含 //、%、+=）、逻辑运算符（and/or/not）、
#     print()、input()、.isdigit()、if / elif / else、列表 []、.append()、
#     while 循环、f-string。
#   - 严禁使用：for 替代主流程、max() 内置函数、try / except、list 等内置名作变量名。
#
# 【预期运行结果示例】（共 4 组，提示语可自行微调）
#
# 示例 1（正常偶数起点：输入 6）：
#   请输入一个正整数: 6
#   起点数字: 6
#   考拉兹轨迹: [6, 3, 10, 5, 16, 8, 4, 2, 1]
#   总变换步数: 8
#   过程最大峰值: 16
#
# 示例 2（边界情况：输入 1，循环体执行 0 次）：
#   请输入一个正整数: 1
#   起点数字: 1
#   考拉兹轨迹: [1]
#   总变换步数: 0
#   过程最大峰值: 1
#
# 示例 3（先输入非法字符，再输入 3）：
#   请输入一个正整数: abc
#   输入无效，请输入大于 0 的纯数字正整数！
#   请输入一个正整数: 3
#   起点数字: 3
#   考拉兹轨迹: [3, 10, 5, 16, 8, 4, 2, 1]
#   总变换步数: 7
#   过程最大峰值: 16
#
# 示例 4（先输入 0 或空回车，再输入 7）：
#   请输入一个正整数: 
#   输入无效，请输入大于 0 的纯数字正整数！
#   请输入一个正整数: 0
#   输入无效，请输入大于 0 的纯数字正整数！
#   请输入一个正整数: 7
#   起点数字: 7
#   考拉兹轨迹: [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
#   总变换步数: 16
#   过程最大峰值: 52
# ==============================================================================

# 请在下方开始编写你的代码：
while True:
    number=input("请输入一个正整数:")
    if number.isdigit() and int(number)>0:
        start_num=int(number)
        break
    else:
        print("输入无效，请输入大于 0 的纯数字正整数！")
sequence=[start_num]
step=0
peak_value=start_num
current=start_num
while current!=1:
    step+=1
    if current%2==0:
        current=current//2
    else:
        current=current*3+1
    if peak_value<current:
        peak_value=current
    sequence.append(current)
print(f'''起点数字:{start_num}
考拉兹轨迹:{sequence}
总变换步数:{step}
过程最大峰值:{peak_value}''')

