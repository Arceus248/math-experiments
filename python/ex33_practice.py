# ==============================================================================
# 练习进度：Learn Python the Hard Way - 新版 Ex 33 / 老师旧版 Ex 32 (Loops and Lists)
# 文件名：ex33_practice.py
#
# 【今日数学小任务：整数“真因数”分析与完全数（Perfect Number）检测器】
#
# 数学背景：
#   对于一个正整数 n，除了它自身以外的所有正因数，称为 n 的“真因数（proper divisors）”。
#   例如：6 的真因数是 1, 2, 3（不包含 6 本身）。
#   根据所有真因数之和 total_sum 与 n 的大小关系，正整数可分为三类：
#     1. total_sum == n：完全数（Perfect Number），如 6 (1+2+3=6)、28
#     2. total_sum > n ：盈数 / 过剩数（Abundant Number），如 12 (1+2+3+4+6=16 > 12)
#     3. total_sum < n ：亏数（Deficient Number），如 7 (1 < 7)
#
# 题目要求（请仅使用目前学过的 Python 语法完成，不要在下面保留多余的测试代码）：
#   1. 提示用户输入一个正整数 n（提示符自定，注意 input() 的返回值类型转换）。
#   2. 边界检查：如果 n <= 0，打印提示信息告知“请输入大于 0 的正整数”，并跳过后续计算。
#   3. 创建一个空列表 divisors = []。
#   4. 使用 for 循环与 range()，遍历从 1 到 n-1 的所有整数：
#      - 判断当前整数能否整除 n（利用求余运算符 %）；
#      - 若能整除，将其使用 .append() 方法追加到 divisors 列表中。
#   5. 使用第二个 for 循环遍历 divisors 列表，同时完成两件事：
#      - 累加计算所有真因数的总和 total_sum；
#      - 分别统计真因数中“偶数”的个数（even_count）和“奇数”的个数（odd_count）。
#   6. 使用 if / elif / else 判断 n 属于“完全数”、“盈数”还是“亏数”。
#   7. 使用 f-string 打印出完整结果（包含真因数列表、真因数总个数、奇偶个数、真因数之和与最终分类）。
#
# 思考挑战（选做，可尝试结合 Ex 18-21 学过的函数）：
#   - 试着将分析逻辑封装到一个函数 def analyze_number(n): 中再调用它。
#   - 想一想：当输入 n = 1 时，range(1, 1) 会产生什么？你的代码能正常处理吗？
#
# ------------------------------------------------------------------------------
# 【预期运行结果示例】（仅供核对逻辑，提示文字可自行设计）
#
# 示例 1（输入 6）：
#   请输入一个正整数: 6
#   6 的真因数列表: [1, 2, 3]
#   共有 3 个真因数（奇数 2 个，偶数 1 个）
#   真因数之和为: 6
#   结论: 6 是完全数（Perfect Number）
#
# 示例 2（输入 12）：
#   请输入一个正整数: 12
#   12 的真因数列表: [1, 2, 3, 4, 6]
#   共有 5 个真因数（奇数 2 个，偶数 3 个）
#   真因数之和为: 16
#   结论: 12 是盈数（Abundant Number）
#
# 示例 3（输入 7）：
#   请输入一个正整数: 7
#   7 的真因数列表: [1]
#   共有 1 个真因数（奇数 1 个，偶数 0 个）
#   真因数之和为: 1
#   结论: 7 是亏数（Deficient Number）
#
# 示例 4（输入 0 或负数）：
#   请输入一个正整数: -3
#   输入无效，请输入大于 0 的正整数！
# ==============================================================================

# 请在下方开始编写你的代码：
def analysis_number(c):
    divisors=[]
    for i in range(1,c):
        if c%i==0:
            divisors.append(i)
    even=0
    odd=0
    sum_divisors=0
    for i in (divisors):
        number_divisors=len(divisors)
        if i%2==1:
            odd+=1
        else:
            even+=1
        sum_divisors=sum_divisors+i
        
        if sum_divisors>c:
            answer=("盈数")
        elif sum_divisors==c:
            answer=("完美数")
        else:
            answer=("亏数")
        solution=(f'''
{c}的真因数列表:{divisors}
共有{number_divisors}个真因数(偶数{even}个，奇数{odd}个)
真因数之和为:{sum_divisors}
结论:{c}是{answer}
''')
        print(solution)
number=int(input("输入一个正整数"))
if number<1:
    print("输入无效，请输入大于 0 的正整数！")
else:
    analysis_number(number)
