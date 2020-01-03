
# 流程圖

![](https://github.com/jason-28/06170136/blob/master/img/S__27861446.jpg)

![](https://github.com/jason-28/06170136/blob/master/img/S__27861448.jpg)


# 學習歷程

這次的作業在畫圖的時候覺得應該沒那麼難，原本還覺得加分的比較好畫應該比較簡單好寫，但其實沒有

讓我原理看了比較多次的反而是kruskal的部分

Dijkstra相對沒花那麼多時間就寫出來了（去年就弄好了）

因為期末比較忙的關係，本來想先放著有空再想想，結果通過了測資

一如既往，希望時間夠我確認清楚還有沒有邏輯沒有寫清楚,導致某些測資出錯

# Kruskal原理

用來尋找最小生成樹的方法，屬於貪婪演算法的一種應用

先將所有邊依權重大小排序，再從最小權重的邊開始連接，直到全部的點都連接

如果有cycle(循環）的情況，則這個邊不能使用,繼續連接下一個邊

# Dijkstra原理

以BFS為基礎，用於解決最短路徑問題，

通常是固定一個頂點作為原點，可找出與另個頂點的最短路徑

把可以從原點直接到達的點累加權重（原點為0）,不能直接到達的點,其權重視為無限大

直到所有的頂點到點距離都代表各自最短路徑的長度值時可得出最小路徑。

### 參考資料:

https://zh.wikipedia.org/wiki/%E5%85%8B%E9%B2%81%E6%96%AF%E5%85%8B%E5%B0%94%E6%BC%94%E7%AE%97%E6%B3%95#%E7%A4%BA%E4%BE%8B

https://zh.wikipedia.org/wiki/%E6%88%B4%E5%85%8B%E6%96%AF%E7%89%B9%E6%8B%89%E7%AE%97%E6%B3%95

https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/

http://www.csie.ntnu.edu.tw/~u91029/SpanningTree.html
