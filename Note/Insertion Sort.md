# Insertion Sort:

![](https://i.imgur.com/1JrragX.png)

分為已排序(小到大)/未排序,以未排序資料中的第一個值與之後的值**由右到左**比大小

* 若處理值<=該值,將該值往右移

* 若處理值>該值,插入在該值右邊

### 時間複雜度 
* Best Case：Ο(1)

當資料的順序恰好為由小到大時,每回合只需比較1次

* Worst Case：Ο(n^2)

當資料的順序恰好為由大到小時,第i回合需比i次

* Average Case：Ο(n/2)

第n筆資料,平均比較n/2次
