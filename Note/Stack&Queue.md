# Stack&Queue

<img src="https://i.imgur.com/ArHZkOR.png" width="600" height="250">

### Stack:

簡單說就是堆疊的概念（**最後放的先拿**）,像是網頁中的返回上一頁或是Microsoft office的還原上一步(ctrl+z)

* Push()是把資料放在最上面

* Top只會回傳最後新增的值,PoP才會刪除

* IsEmpty用來確認是否有資料,getSize回傳資料個數

### Queue:

簡單來說就是排隊的概念（**從後面開始排**）,像作業系統被多個程式共享資源時(例如CPU、網站伺服器等,一次只能執行一個需求),就需要用Queue來安排順序

* Push()是把資料放在最後面,令其成為新的back

* Pop是把front指向的資料刪除並更新,又叫做**dequeue**

* getFront/getBack分別是回傳front/back指向的資料

* IsEmpty用來確認是否有資料,getSize回傳資料個數
