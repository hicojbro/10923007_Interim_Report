n=int (input("請輸入一個正整數:"))# 獲取用戶輸入

sum = 0 # 定義求和變數

for i in range(1, n+1): # 計算1到n的和，注意要包含n本身，所以這裡需要n+1

    sum += i

print("從1到{}的和為：{}".format(n, sum))