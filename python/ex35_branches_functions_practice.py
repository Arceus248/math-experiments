# ==============================================================================
# 练习进度：Learn Python the Hard Way - 新版 Ex 35（兼巩固 Ex 23 / 旧版 Ex 34 列表索引）
# 章节主题：Branches and Functions & Nested List Indexing（分支、函数状态机与列表索引）
# 文件名：ex35_branches_functions_practice.py
#
# 【题目背景：「数论密室逃脱」多房间状态流转游戏】
#   你需要编写一个仿 Ex 35 风格的文字闯关程序，玩家通过输入指令和数学答案，
#   在多个独立函数构成的“房间”之间跳转，最终抵达终极金库或触发失败退出。
#
# 【具体输入与输出要求】
#   请至少设计以下 5 个顶层函数，并在文件最末尾调用入口函数启动游戏：
#   1. def fail_game(reason):
#      - 打印失败原因 reason 与结束语，并调用 sys.exit(0) 立即结束整个程序。
#   2. def start_gate():
#      - 打印欢迎语并给出两条通道选项："1"（密码锁密室）和 "2"（数列密室）；
#      - 若输入 "1"，调用 cipher_room()；
#      - 若输入 "2"，调用 sequence_room()；
#      - 其他任何输入，调用 fail_game("你在大厅迷路，机关关闭了。")。
#   3. def cipher_room():
#      - 进入房间后，在 while 循环外部定义状态开关 lever_pulled = False 与剩余尝试次数 chances = 3；
#      - 使用 while True: 持续接收玩家指令（提示符 "> "）：
#          a) 若指令为 "check" 且 not lever_pulled：提示发现并拉动了拉杆，将 lever_pulled 改为 True；
#          b) 若指令为 "check" 且 lever_pulled：代表重复误触机关，调用 fail_game("你重复拉动拉杆触发了毒箭！")；
#          c) 若指令为 "enter" 且 not lever_pulled：提示大门尚未通电，请先检查机关（不扣次数，继续循环）；
#          d) 若指令为 "enter" 且 lever_pulled：提示玩家输入一个“既是 3 的倍数、又是 5 的倍数、
#             且大于 20 小于 100”的整数（如 30, 45, 60, 75, 90）：
#               - 必须用 .isdigit() 检查输入是否为纯数字，不能使用 "0" in choice 漏洞；
#               - 若满足全部数学条件，打印通过提示并调用 vault_room()；
#               - 若格式错误或数学条件不满足，chances 减 1 并提示剩余次数；
#               - 若 chances == 0，调用 fail_game("密码错误次数过多，密室彻底锁死！")；
#          e) 其他未知指令：打印“听不懂你的指令。”继续等待。
#   4. def sequence_room():（重点巩固 0 基索引与嵌套列表访问）
#      - 在函数内定义一个二维/三维嵌套数列题库列表，至少包含 2 道题，例如：
#        puzzles = [
#            ["平方数列", [1, 4, 9, 16, 25], 36],
#            ["斐波那契数列", [2, 3, 5, 8, 13], 21]
#        ]
#      - 请玩家输入选择题号（"0" 或 "1"），若不是 "0" 也不是 "1"，调用 fail_game(...)；
#      - 使用 0 基链式索引（如 puzzles[idx][0]、puzzles[idx][1][2] 等）取出并打印：
#        数列名称、前 5 项列表、以及第 3 项（索引 2）和最后 1 项（索引 4 或 -1）提示；
#      - 让用户输入该数列的第 6 项数字，用 .isdigit() 校验后比对 puzzles[idx][2]：
#        答对则调用 vault_room()，答错则调用 fail_game(...)。
#   5. def vault_room():
#      - 打印进入终极金库信息，询问玩家要带走多少枚金币（1 ~ 100 之间）；
#      - 用 .isdigit() 校验输入合法性，非法输入直接调用 fail_game("输入无效数字，警报响起！")；
#      - 若金币数 amount 满足 0 < amount <= 50 且为偶数（amount % 2 == 0），
#        打印通关胜利信息并调用 exit(0) 正常结束；
#      - 若 amount <= 0 或不是偶数或大于 50，分别给出原因并调用 fail_game(...)。
#
# 【允许使用的语法范围】
#   - 仅限 Ex 0 - Ex 35 已学语法：
#     from sys import exit、def 函数与参数、return、if / elif / else、
#     布尔逻辑 and / or / not、in 运算符、while True: 循环、嵌套列表与 0 基索引、
#     input()、.isdigit()、int()、f-string。
#   - 严禁使用：全局变量（状态变量必须放在各自函数局部作用域内）、try / except、class。
#
# 【预期运行结果示例】（共 4 组）
#
# 示例 1（通道 1 -> 拉动机关 -> 输入合法密码 45 -> 金库拿 40 枚偶数金币通关）：
#   欢迎来到数论密室！请选择通道（1: 密码锁密室，2: 数列密室）:
#   > 1
#   你进入了密码锁密室，墙上有一个拉杆。指令：check / enter
#   > check
#   咔哒！机关拉杆已拉动，密码盘亮起了。
#   > enter
#   请输入一个既是 3 的倍数、又是 5 的倍数、且在 20 到 100 之间的整数:
#   > 45
#   密码正确！大门打开，你进入了终极金库！
#   金库里装满了金币，你想带走多少枚？（提示：不要太贪婪，且必须是偶数）
#   > 40
#   恭喜你带着 40 枚金币安全逃脱，游戏通关！
#
# 示例 2（通道 1 -> 重复拉动机关触发失败）：
#   欢迎来到数论密室！请选择通道（1: 密码锁密室，2: 数列密室）:
#   > 1
#   你进入了密码锁密室，墙上有一个拉杆。指令：check / enter
#   > check
#   咔哒！机关拉杆已拉动，密码盘亮起了。
#   > check
#   你重复拉动拉杆触发了毒箭！ 游戏结束！
#
# 示例 3（通道 2 -> 选第 0 题平方数列 -> 答对 36 -> 金库输入奇数 25 失败）：
#   欢迎来到数论密室！请选择通道（1: 密码锁密室，2: 数列密室）:
#   > 2
#   欢迎来到数列密室！请选择题目编号（0 或 1）:
#   > 0
#   题目类型: 平方数列
#   已知序列: [1, 4, 9, 16, 25]（其中第 3 项为 9，第 5 项为 25）
#   请输入第 6 项的值:
#   > 36
#   回答正确！你进入了终极金库！
#   金库里装满了金币，你想带走多少枚？（提示：不要太贪婪，且必须是偶数）
#   > 25
#   机关只识别偶数数量，警报响起！ 游戏结束！
#
# 示例 4（通道 1 -> 拉杆后连续输错 3 次密码导致锁定失败）：
#   欢迎来到数论密室！请选择通道（1: 密码锁密室，2: 数列密室）:
#   > 1
#   ...
#   > check
#   咔哒！机关拉杆已拉动，密码盘亮起了。
#   > enter
#   请输入一个既是 3 的倍数、又是 5 的倍数、且在 20 到 100 之间的整数:
#   > 15
#   密码不符合条件，还剩 2 次机会！
#   > enter
#   请输入一个既是 3 的倍数、又是 5 的倍数、且在 20 到 100 之间的整数:
#   > abc
#   密码不符合条件，还剩 1 次机会！
#   > enter
#   请输入一个既是 3 的倍数、又是 5 的倍数、且在 20 到 100 之间的整数:
#   > 35
#   密码错误次数过多，密室彻底锁死！ 游戏结束！
# ==============================================================================

# 请在下方开始编写你的代码：
from sys import exit
def fail_game(reason):
    print(reason)
    exit(0)
def start_gate():
    print('欢迎来到数论密室！请选择通道（1: 密码锁密室，2: 数列密室）:')
    room=input('>')
    if room=='1':
        cipher_room()
    elif room=='2':
        sequence_room()
    else:
        fail_game('你在大厅迷路，机关关闭了。')
def cipher_room():
    print('你进入了密码锁密室，墙上有一个拉杆。指令：check / enter')
    lever_pulled=False
    chances=3
    while True:
        inputs=input('>')
        if chances==0:
            fail_game("密码错误次数过多，密室彻底锁死！")
        if inputs=='check' and ever_pulled==False:
            ever_pulled=True
            print('咔哒！机关拉杆已拉动，密码盘亮起了。')
        elif inputs=='check' and ever_pulled==True:
            fail_game("你重复拉动拉杆触发了毒箭！")
        elif inputs=='enter' and ever_pulled==False:
            print("大门尚未通电，请先检查机关")
        elif inputs=='enter' and ever_pulled==True:
            print('输入一个“既是 3 的倍数、又是 5 的倍数、且大于 20 小于 100”的整数')
            number=input('>')
            if number.isdigit():
                num=int(number)
                if num%3==0 and num%5==0 and num>20 and num<100:
                    print('密码正确！大门打开，你进入了终极金库！')
                    vault_room()
                else:
                    chances-=1
                    print(f'密码不符合条件，还剩 {chances} 次机会！')
            else:
                chances-=1
                print(f'密码不符合条件，还剩 {chances} 次机会！')               
        else:
            print("听不懂你的指令。")
def sequence_room():
    puzzles = [["平方数列", [1, 4, 9, 16, 25], 36],["斐波那契数列",[2, 3, 5, 8, 13], 21]]
    print('欢迎来到数列密室！请选择题目编号（0 或 1）:')
    choice=input(">")
    if choice.isdigit() and choice=='0' or '1':
        choice=int(choice)
        print(f"题目类型：{puzzles[choice][choice]}")
        print(f"已知数列{puzzles[choice][choice+1]}")
        print("请输入第6项的值")
        num=input('>')
        if num.isdigit() and int(num)==puzzles[choice][choice+2]:
            print('回答正确！你进入了终极金库！')
            vault_room()
        else:
            fail_game('密码错误次数过多，密室彻底锁死！ 游戏结束！')
def vault_room():
    print('金库里装满了金币，你想带走多少枚？（提示：不要太贪婪，且必须是偶数）')
    numbers=input('>')
    if numbers.isdigit() and int(numbers)%2==0 and int(numbers)>0 and int(numbers)<=50:
        print(f'恭喜你带着 {numbers} 枚金币安全逃脱，游戏通关！')
    else:
        print('')





            
