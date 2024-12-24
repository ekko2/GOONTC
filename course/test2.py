单选题
1、对于数列3，8，11，15，17，19，25，30，44，采用“二分查找”法查找8，需要查找多少次？

A、5
B、4
C、3
D、2


2、下面哪一项不是pip指令？

A、pip install Scipy
B、pip uninstall Jieba
C、pip clear
D、pip list


3、有如下Python语句，执行该语句后，结果是？

f=lambda x:x+1
print(f(3))
1
2
A、3
B、没有输出
C、3
D、None


4、执行如下Python代码后，结果是？

def inverse(s,n=0):
	while s:
		n = n * 10 + s % 10
		s = s // 10
	return n
print(inverse(456,123))
A、654123
B、123456
C、123654
D、654321


5、下列有关循环和递归的描述正确的是？

A、递归思想代码清晰简洁，可读性强
B、递归代码中不能有循环结构的语句
C、递归是从问题的起点出发，逐渐将复杂问题化为简单问题，最终求得问题
D、能用递归实现的，一定能用循环代码实现


6、以下有关Python函数的定义表述中错误的是？

A、函数的定义必须在主程序调用语句之前出现
B、在形参列表中必须先列出有默认值的形参，再列出没有默认值的形参
C、实参是实际占用内存地址的，而形参不占用
D、def关键字后面加函数名定义函数，定义必须以冒号结尾


7、如下代码运行后下面选项中描述错误的是？

def pph(a,b):
	c=a**2+b
	b=a
	return c
a=10
b=100
c=pph(a,b)+a
print(a,' ',b,' ',c)
A、执行该函数后，变量a的值为10
B、执行该函数后，变量b的值为100
C、执行该函数后，变量c的值为200
D、该函数名称为pph


8、阅读下列程序段，数列的第6项值为多少？

def fibona(x):
	if x==1 or x==2:
		f=1
	for i in range(3,x+1):
		f=fibona(x-1)+fibona(x-2)
	return f
n=int(input("请输入数列第几项："))
m=fibona(n)
print("数列的第"+str(n)+"项的值为"+str(m))
A、1
B、8
C、21
D、34


9、有如下Python的自定义函数，执行该程序后，结果是？
def  calc(x,y,op):
	return eval(str(x)+op+str(y)) 
print(calc(3,5,'+'))
A、8
B、35
C、None
D、-2


10、有如下Python程序，执行该程序后，结果是？

x = 3
def  calc():
    x = 5
print(calc())

A、3
B、5
C、无输出
D、None


11、应用分治算法的前提是？

A、问题的可分性和解的可归并性
B、问题的复杂性和解的简单性
C、问题的可分性和解的存在性
D、问题的复杂性和解的可归并性


12、有一球从100米高度自由落下，每次落地后反跳回原高度的一半，再落下，
求它在第10次落地前，反弹多高？用递归函数解决，下面选项正确的是？

A、
def height(n):
	if n == 1:
		return 100
	else:
		return n*2
print(height(10))
B、
def height(n):
	if n == 1:
		return 100
	else:
		return height(n-1)/2
print(height(10))
C、
def height(n):
	if n == 1:
		return 100
	else:
		return height(n+1)/2
print(height(10))
D、
def height(n):
	if n == 1:
		return 100
	else:
		return height(n-1)*2
print(height(10))


13、有如下Python程序，执行该程序后，结果是？

g = lambda x,y=3,z=5:x+y+z
print(g(2))
A、2
B、5
C、7
D、10


14、以下程序输出1~100之间能被7整除但不能同时被5整除的所有整数。
根据下面哪个选项的方法优化后，程序的运行效率最高？

k=1
while k<101:
	if k%7==0 and k%5 !=0:
		print(k)
	k += 1

A、将k=1改为k=7
B、
C、将k += 1 改为 k += 7
D、将k=1改为k=7，同时将k += 1 改为 k += 7


15、下列程序段的运行结果为？

def f(n):
    if n<=1:
         return 1
    else:
        return f(n-1)*3
print(f(5))
A、9
B、27
C、81
D、243


16、下列选项中，关于如何安装第三方库的说法正确的是？

A、如果电脑没有联网，仍然可以使用pip工具安装本地的whl文件
B、必须使用命令行工具安装第三方库
C、第三方库只要可以用pip完整的下载下来，就可以成功安装
D、安装上Anaconda就安装了所有的第三方库


17、运行以下程序输出的结果是？

y=2
def fun():  
    global y  
    y=1  
    print(y)
fun()
	print(y)
A、2 1
B、2 2
C、1 2
D、1 1


18、下面哪种算法使用了分治的方法？
A、插入排序
B、快速排序
C、选择排序
D、冒泡排序


19、面关于递归函数说法正确的是？
A、一般来说，递归函数的执行效率高于非递归函数
B、边界条件和递归关系是递归函数编写的关键
C、递归函数的嵌套调用次数没有限制
D、递归函数不可以改写为非递归函数


20、观察此题示例代码，以下表述中错误的是？

nums = range(2,20)
for i in nums:
	nums=list( filter(lambda x:x==i or x % i,nums))
print(nums) 
A、filter()函数输出后是一个数组而不是列表
B、示例代码中的关键字lambda表示匿名函数
C、lambda x:x==i or x%i，nums中冒号:之前的x是这个函数的参数
D、匿名函数需要return来返回值，表达式本身结果就是返回值


21、在一个平面中，有n个圆两两相交，但任二个圆不相切，任三个圆无公共点，
以下函数能计算出n个圆把平面分成的区域个数，空格处填写的语句是？
def c(n):
	if n=1:
		return 2
	else:
		return ___                  

A、c(n-1) + 2*(n-1)
B、c(n-1) + c(n-2)
C、c(n-1) + 2*n
D、c(n-1) + 2*(n+1)


22、有如下Python程序段，执行该程序后，结果是？

def fun(*p):
    return sum(p)
print(fun(1,3,5))
A、4
B、6
C、8
D、9


23、以下关于全局变量和局部变量的表述正确的是？

A、如果再函数中定义的局部变量与全局变量同名，则全局变量屏蔽局部变量
B、可以通过global关键字，通过全局变量修改局部变量
C、nonlocal关键字用来再函数或局部作用域使用内层(非全局)变量
D、全局变量的作用域一定比局部变量的作用域大


24、关于以下程序，下列表述中错误的一项是？

c=1
def fun(n):
	a=1
	for b in range(1,n):
		a*=b
	return a
n=int(input('Enter n='))
print(fun(n),c) 

A、c是全局变量，a是局部变量
B、n是形式参数，当n=5时，程序输出120 1
C、程序实现求阶乘
D、range()函数时python内置函数


25、以下程序的运行结果是？

def f(x,y,z):
	print(x,y,z)
f(z=3,x=2,y=1)


A、3 2 1
B、1 2 3
C、2 1 3
D、3 1 2


判断题
26、所有的Python第三方库均可以使用pip工具进行安装。

27、算法的时间复杂度与空间复杂度没有必然关系。

28、在创建自定义函数时，即使函数没有参数，也必须保留一对空的"()"。

29、执行以下代码，程序输出的结果为：函数内取值: [5, 6, 7, [1, 2, 3, 4]]、函数外取值: [5, 6, 7, [1, 2, 3, 4]]。

def fun( mylist ):
    mylist.append([1,2,3,4])
    print("函数内取值: ", mylist)
    return mylist = [5,6,7]
fun( mylist )
print("函数外取值: ", mylist)

30、定义Python函数时，如果函数中没有return语句，则该函数返回值是None。

31、执行以下代码，程序输出的结果为：15 15

sum=0
def fun(arg1,arg2):
    sum=arg1+arg2
    print(sum)
    return sum
fun(5,10)
print(sum)


32、对于一个复杂问题，如果所分解出的各个子问题之间相互不独立，则不适合使用分治算法。

33、执行以下代码，程序输出的结果为：
Name: summy
Age: 40
Name: summy
Age: 40。

def fun( name, age = 30 ):
   print("Name:", name)
   print("Age:", age)
   return fun( age=40, name="summy" )
fun( name="summy" )


34、下列程序段运行后的结果是2。

def change(a,b):
    a,b=b,a
    return a
a=2
b=3
print(change(change(a,b),a))


35、对于斐波那契数列：1，1，2，3，5，……，我们只能采用迭代公式以递推的方式求解。

实操
第一题
在编写抽奖程序时，为了保证一个人只有一次中奖机会，要检查新抽出来的数字是不是已经被抽中过了。

一种办法是将已经中过奖的人员编号存放在test_list里面，然后每抽出一个新的人员编号，
判断它是否在中奖人员列表中。

如果没有在中奖人员列表中，说明中奖号码有效，并将它保存进中奖人员列表；如果已经在里面了，
就再生成一个新的人员编号。

请你补全下面的代码，实现判断一个数字是否在列表中的功能。

#子问题算法（子问题规模为1）
def is_in_list(init_list,num):
	if init_list[0] == num:
		return True
	else:
		return False
#分治法
def find_out(init_list,num):
	n = len(init_list)
	if ____①______          #如果问题的规模等于1，直接解决
		return is_in_list(init_list,num)
#分解（子问题规模为n/2）
	left_list,right_list = _init_list[0:n//2],init_list[]________②____________
#递归，分治，合并
	res=find_out(left_list,num) __③__ find_out(right_list,num)
	return res
if __name__ == "__main__":
#测试数据
	test_list = [18,43,21,3,28,2,46,25,32,40,14,36]
	#查找
	print(__find_out(test_list,43)___④_____) 
"""
程序运行结果：
>>>True
"""


第二题
乘法运算等于多个加法运算的和。比如，3×2可以理解为3+3，也可以理解为2+2+2 。

下面的程序使用递归算法演示了计算两个自然数的乘积的过程。请你补全代码。

输入：分两次输入自然数num1，num2

输出：num1 × num2 = 乘积

def cheng_fa(num1,num2,value):
    if          ①             
        value += 0
    else:
        value += num1
                 ②         
        value = cheng_fa(num1,num2,value)
    return      ③        
num1=int(input('输入第1个数:'))
num2=int(input('输入第2个数:'))
value=0
value = cheng_fa(num1,num2,value)
print('{} X {} = {}'.format(num1,num2,value))
"""
程序运行结果：
输入第1个数：3
输入第2个数：7
3 X 7 = 21
"""


第三题
外卖送餐服务越来越受到人们的喜爱，外卖小哥们也成了路上的一道风景。

当顾客使用外卖软件点餐时，会出现一个预计送达时间，包括了餐厅制作食物的时间，
路上的骑行时间等等。

一种常用的计算路上骑行时间的方法是用曼哈顿距离(manhatton distance)除以平均骑行速度。
平面上点A(x1,y1)与点B(x2,y2)的曼哈顿距离为：|x1-x2|+|y1-y2|。

假设一名外卖小哥的平均骑行速度为30km/h。下面的程序模拟计算外卖小哥的路上骑行时间，
请你补充完整。

输入：分两次输入A点和B点的坐标值

输出：A、B两点间的曼哈顿距离和路上骑行时间。

#求绝对值 
def my_abs(n):
	if       ①       
		return n
	else:
		return      ②      
#主程序
v=30 #平均骑行速度
x1=float(input('输入A点的x坐标（米）：'))
y1=float(input('输入A点的y坐标（米）：'))
x2=float(input('输入B点的x坐标（米）：'))
y2=float(input('输入B点的y坐标（米）：'))
#计算曼哈顿距离mht
mht =      my_abs(x1-x2)+my_abs(y1-y2)      ③                    
#计算路上骑行时间 
time_on_the_road    =   mht/v         ④                    
print('A、B两点的曼哈顿距离为{}米'.format(mht))
print('预计路上骑行时间需要{}分钟'.format(time_on_the_road))
"""
程序运行结果：
输入A点的坐标（米），以逗号分隔：-1000,1000
输入B点的坐标（米），以逗号分隔：1000,-1000
A、B两点的曼哈顿距离为4000米
预计路上骑行时间需要8.0分钟
"""