"""
文文為即將出國的珊珊送行，由於珊珊不喜歡別人給文文的那個綽號，意思就是嘲笑文文不夠 聰明，但珊珊沒把握那個綽號是不是事實，所以珊珊決定考驗文文，
於是告訴文文說，如果你能在 我回國之前回答我生日那年是不是閏年，則等她回國後就答應他的求婚。文文抓抓腦袋想不出來， 於是決定讓最擅長做運算的電腦來幫忙。
輸入有若干行直到 EOF 結束，每行包含一個整數代表年份。
輸出 閏年 或 平年。
提示 ：
西元年被4整除且不被100整除，或被400整除者即為閏年
"""
while True:  # 重複執行
    try:
        D = int(input())
        if (D % 4 == 0 and D % 100 != 0) or D % 400 == 0:  # 提示中的閏年條件
            print("閏年")
        else:
            print("平年")
    except:  # EOF 結束
        break