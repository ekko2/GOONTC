## 设计一个算法,根据邮件的重量和用户是否选择加急来计算邮费
## 计算规则：重量在1000g以内，基本邮费8元，超过1000g，每500g加收超重费4元，不足500g部分按500g计算
## 如果用户选择加急，多收5元。

def postage(w,f='y'):
    if f == 'y':
        cost = __1__
    else:
        cost = __2__
    if w > 1000:
        cost += __3__
        if w % 500 > 0:
            cost += 4
    return cost

w = int(input('邮件重量：'))
f = input('是否加急：')
print(postage(w,f))


name = 'zhang'
def f():
    global name 
    name = 'li'
    print(name)

f()
print(name)