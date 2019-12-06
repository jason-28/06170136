# 流程圖

![](https://github.com/jason-28/06170136/blob/master/img/S__26689661.jpg)

![](https://github.com/jason-28/06170136/blob/master/img/S__26689663.jpg)

![](https://github.com/jason-28/06170136/blob/master/img/S__26689664.jpg)

# 學習歷程
這次的Hash Table我覺得概念比較好理解，所以實作上遇到的問題比較沒那麼多。

主要是在做新增的時候花了些時間才了解該放的東西是self.data的值而不是自己所設的cur,

移除的邏輯也是經過和同學的討論才有想清楚怎麼將等同測值的data變不見。

包含的部分倒是沒什麼問題，很快就想出來了，但還是直到最後移除的確認無誤後才能確定。

# Hash Table原理
雜湊表是透過key值在內部資料搜尋位置的一種資料結構

capacity代表資料的容量,Key值是外部輸入的值,會用來經由Hash function回傳儲存位置

可能會出現衝突(兩筆資料存在一起,導致回傳的value不一樣)

上述問題可透過Linked list串接資料來解決

# Hash function原理
首先在Hash Set裡多寫了一個將測值變成16進位數值的defunction

Add:

先設定好要用的cur(代表內部第i個值）跟new（要加的測資）

在cur存在的條件下跑while迴圈，並在cur不等於測資時把測資加入，再將cur.next變成新的cur繼續執行

（cur等於測資值時pass,因為我設定同樣的值只有一個）

Remove:

同上方設定cur，在cur存在的條件下跑while迴圈，在等於測資時讓cur.next指向內部第i個值並回傳

不等於時將cur.next變成新的cur繼續執行，最後回傳刪除好的data

Contains：

也是跑cur存在的while迴圈，當內部有同測值的值時回傳True並停止（因為上面寫的只有加一次）

否則將cur.next變成新的cur繼續執行。直到最後都沒有才回傳False

### 參考資料:
http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html

https://medium.com/100-days-of-python/day-09-hash-table-chaining-ef74baa6732

https://zh.wikipedia.org/wiki/%E5%93%88%E5%B8%8C%E8%A1%A8

程式碼概念參考:

https://github.com/aaron1aaron2/my-learning-note

https://kite.com/python/examples/2084/crypto-generate-a-new-md5-hash
