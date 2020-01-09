# Depth-First Search 

## 定義
DFS也是一種用於遍歷或搜尋樹或圖的演算法。先往某個方向走到底(Depth-First)後折返，再去看其他分支。

這過程會一直進行到已發現從來源節點可到達的所有節點為止。

![](https://i.imgur.com/Z6SIeJv.png)

## DFS VS. BFS 
![](https://i.imgur.com/gPqpwpO.png)

從兩者的步驟可以看到兩者概念很像，DFS就是很直接挑一邊的走道底再回頭找，使用 stack 的結構。而 BFS 則是先以最接近的那一層開始，也就是他一走到某個節點時他就會把該點附近沒走過的節點都進入Qeuee。
- DFS: 以一邊優先
- BFS: 以階層關係優先

![](https://i.imgur.com/KDLXUCc.png)
