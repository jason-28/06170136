# Linkedlist:

<img src="https://i.imgur.com/1Qc4uHD.png"  width="600" height="180">

單向連結串列的每個節點只記錄了下一個節點(或者上一個節點)，而尾端的節點指向空值Null

刪除節點的時候是刪除指定節點(node)後面的節點(node.next)，而不是刪除節點本身

雙向連結串列則同時記錄了下一個節點和上一個節點，除了尾端節點的下一個節點指向空值外，第一個節點的前一個節點也指向空值

* 優點:新增刪除較Array方便,可以有效運用存儲空間

* 缺點:找特定Node時需從頭開始走訪

# Stack&Queue

<img src="https://i.imgur.com/ArHZkOR.png" width="600" height="250">

### Stack:

堆疊的概念（最後放的先拿）,像是網頁中的返回上一頁或是Microsoft office的還原上一步

* Push()是把資料放在最上面

* Top只會回傳最後新增的值，PoP才會刪除

* IsEmpty用來確認是否有資料，getSize回傳資料個數

### Queue:

排隊的概念（從後面開始排）,像作業系統被多個程式共享資源時(例如CPU、網站伺服器等，一次只能執行一個需求)，需要用Queue來安排順序

* Push()是把資料放在最後面,令其成為新的back

* Pop是把front指向的資料刪除並更新,又叫做dequeue

* getFront/getBack分別是回傳front/back指向的資料

* IsEmpty用來確認是否有資料，getSize回傳資料個數

# Set
一種無順序的元素集合，每個元素是唯一且不可重複的

### 相關符號
|python 符號|意思|
|:-:|:-|
|-|差集|
|&|交集|
|I|聯集|
|!=|不等於|
|==|等於|
|in|屬於|
|not in|不屬於|
