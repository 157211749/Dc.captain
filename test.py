print('hello world')
a ,b ,c = 123,234,345
# b = 345
# c = a+b
a,b,c = b,c,a
print(a,b,c,end=' ')
print("{}+{}的值是：{}".format(a,b,c))
# print('a的值为{},b的值为{}'.format(a,b)) command+/

# d=input("请输入你的姓名：")
# print(d)

print("对酒当歌，人生几何?？"[1:40])

# x = eval(input("请输入数字："))   #input输入的为字符串，eval() 函数用来执行一个字符串表达式,并返回表达式的值。
# y = x + 123
# print(y,type(y))

print(pow(a,2))

print(0.1+0.2)

q = 3.3+4j    #实数
print(q,q.real,q.imag)  #实部，虚部

print(5//2,2**5)   #除法一定是浮点数，（整除）//是指最大整数商，**是指幂次方——pow

print(abs(-3))   #绝对值
print(divmod(5,3))     #（整除，余数）
print(pow(3,4,2))      # 3**4%2
print(round(1.23456,2))  #四舍五入
print(max(1,2,3,4,5))  #求最大值
print(min(1,2,3,4,5))  #求最小值

#   dir(__builtins__) ——查询所有内置函数
print(help(abs))
print(help('keywords')) # help('if')——查询关键词
print(dir(q))#查询变量q的方法
