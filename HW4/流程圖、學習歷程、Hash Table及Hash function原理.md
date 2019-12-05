# 流程圖

![]()

![]()

![]()


# 學習歷程


# Hash Table原理


# Hash function原理
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
