#資料容器List



##混和串列

list1 = [1,2,3,4,5]

##索引 position index - 0

list1[0] # 1
list1[4] # 5
list1[-1] # 5

## **切片**
list1[1:4] # [2,3,4]

#數字串列二: range()
list1 = [1,2,3,4,5]

list2 = range(1,10000,1) # [1,2,3,4,5]

list3 = range(1,6,2) # [1,3,5]

#range(start,stop,step)
# [0,1,2,3,4,5,6,7,8,9]
## star = 0,step = 1,stop = 10
range(0,10,1)
range(0,10)
list4 = range(10)

#[0,1,2,3,4]

for i in range(5):
    print("Hello")