#數字串列
##數字串列的初值、終值、遞增值 range(start,stop,step)
start = int(input('請輸入加總值開始值?'))
end = int(input('請輸入加總終止值?'))
step = int(input('請輸入遞增減值?'))

##用for迴圈做加總 + range()
sum = 0    #初始條件
for i in range(start,end,step):  #判斷條件
    sum = sum + i
    print('i為',i,'時,累加結果為',sum)
    
    
sheet = ['牛奶','蛋','咖啡豆']   
for index in [0,1,2]:
    print(index,sheet[index])
sheet = ['牛奶','蛋','咖啡豆']
for index in sheet:
    print(index)
sheet = ['牛奶','蛋','咖啡豆']
for index in [0,1,2]:
    print(index)
sheet = ['牛奶','蛋','咖啡豆']
for index in range(0,len(sheet)):
    print(index,sheet[index])

numbers = [123,456,789]
for i in numbers:
    print(i)
numbers = [123,456,789]
for i in range(0,len(numbers)):
    print(i,numbers[i])
    