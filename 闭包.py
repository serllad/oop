'''
闭包学习
用途1，当闭包执行完后，仍然能够保持住当前的运行环境。
比如说，如果你希望函数的每次执行结果，都是基于这个函数上次的运行结果。我以一个类似棋盘游戏的例子来说明。
假设棋盘大小为50*50，左上角为坐标系原点(0,0)，我需要一个函数，接收2个参数，分别为方向(direction)，步长(step)，该函数控制棋子的运动。
棋子运动的新的坐标除了依赖于方向和步长以外，当然还要根据原来所处的坐标点，用闭包就可以保持住这个棋子原来所处的坐标。
'''
origin = [0, 0]  # 坐标系统原点
legal_x = [0, 50]  # x轴方向的合法坐标  
legal_y = [0, 50]  # y轴方向的合法坐标  


def create(pos=origin):
    def player(direction, step):
        # 这里应该首先判断参数direction,step的合法性，比如direction不能斜着走，step不能为负等  
        # 然后还要对新生成的x，y坐标的合法性进行判断处理，这里主要是想介绍闭包，就不详细写了。  
        new_x = pos[0] + direction[0] * step
        new_y = pos[1] + direction[1] * step
        pos[0] = new_x
        pos[1] = new_y

        #pos = [new_x, new_y]
        # 注意！此处不能写成 pos = [new_x, new_y]，原因在上文有说过
        return pos

    return player


player = create()  # 创建棋子player，起点为原点
print(player([1, 0], 10))  # 向x轴正方向移动10步
print(player([0, 1], 20))  # 向y轴正方向移动20步
print(player([-1, 0], 10))  # 向x轴负方向移动10步
'''
用途2，闭包可以根据外部作用域的局部变量来得到不同的结果，这有点像一种类似配置功能的作用，我们可以修改外部的变量，
闭包根据这个变量展现出不同的功能。
比如有时我们需要对某些文件的特殊行进行分析，先要提取出这些特殊行。
'''
def make_filter(keep):
    def the_filter(file_name):
        file = open(file_name)
        lines = file.readlines()
        file.close()
        filter_doc = [i for i in lines if keep in i]
        return filter_doc
    return the_filter
filter = make_filter("Stack")
print(filter("read.txt"))