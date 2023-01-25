"""
很多銀行及公司設立了電話客服中心來服務他們的客戶。為了加速身分的查核，常常會要求打電話進來的客戶輸入他的身分證號碼。
可是電話上只有數字鍵，要輸入身分證號碼的第一個字母有點麻煩，因此有的語音系統會要求來電者輸入後 9 碼，再根據後 9 碼來推算可能的英文字母。

很多人都知道，身分證號碼的最後一碼是「檢查碼」，它是用前 9 碼所推算出來的，其推算的規則如下：

先依照下表將英文字母轉換為 2 位數字，再加上第 2 到第 9 位的 8 位數字一共有 10 位數字。
台北市 A 10   彰化縣 N 22
台中市 B 11   新竹市 O 35
基隆市 C 12   雲林縣 P 23
台南市 D 13   嘉義縣 Q 24
高雄市 E 14   台南縣 R 25
台北縣 F 15   高雄縣 S 26
宜蘭縣 G 16   屏東縣 T 27
桃園縣 H 17   花蓮縣 U 28
嘉義市 I 34   台東縣 V 29
新竹縣 J 18   金門縣 W 32
苗栗縣 K 19   澎湖縣 X 30
台中縣 L 20   陽明山 Y 31
南投縣 M 21   連江縣 Z 33
由左至右，第一位乘 1，第二位乘 9，第三位乘 8，第四位乘 7...，以此類推，最後一位乘 1。
求各位相對數字乘積的總和 s。
求 s 的個位數 m。(檢查碼只有一位數，因此若 c = 10 時，則檢查碼為 0。)
檢查碼 c = 10 - m 。
假設某人的身份證號碼前 9 碼為 F13024567，那麼他的最後一位檢查碼的計算過程如下：

    F       1    3    0    2    4    5    6    7
  1    5    1    3    0    2    4    5    6    7

 ×1   ×9    ×8    ×7   ×6    ×5    ×4    ×3    ×2   ×1

  1 + 45 +  8 + 21 +  0 + 10 + 16 + 15 + 12 +  7 = 135

檢查碼 = 10 - (135 % 10) = 5

根據上面的規則，A12345678、M12345678 和 W12345678 這三個號碼的檢查碼都是 9。
因此，如果在電話上所輸入的後 9 碼是 123456789 時，它的第一位英文字母可能是 A，也可能是 M 或 W。

輸入說明
輸入只有一行，含有一個身份證號碼的後 9 碼。

輸出說明
將可能的第一位大寫字母依字母順序輸出於一行。
"""
dic = {"A": 10, "N": 22,
       "B": 11, "O": 35,
       "C": 12, "P": 23,
       "D": 13, "Q": 24,
       "E": 14, "R": 25,
       "F": 15, "S": 26,
       "G": 16, "T": 27,
       "H": 17, "U": 28,
       "I": 34, "V": 29,
       "J": 18, "W": 32,
       "K": 19, "X": 30,
       "L": 20, "Y": 31,
       "M": 21, "Z": 33}
id = list(map(int, input()))
sum = 0
for i in range(8):
    sum += id[i] * (8 - i)
for i in dic:
    print(dic[i])
