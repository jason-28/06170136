
# 流程圖

![](https://github.com/jason-28/06170136/blob/master/img/S__27435071.jpg)

![](https://github.com/jason-28/06170136/blob/master/img/S__27435073.jpg)

# 學習歷程

這次的作業在寫BFS的時候遇到得問題不算特別多，本以為DFS只要改了pop掉的值的位置，

並將queue改成Stack就沒問題了，結果return的值居然跟BFS是一樣的。

後來才發現如果把值加入已拜訪的空list會有問題，於是做了一下修正。

之後輸入測值的結果是正確的，但在測試更長的addedge後會有點錯誤，希望來得及釐清錯誤並修正。

# BFS原理

從頂點S開始，把能立即訪問的點分為不同的level,重複執行直到全部節點都被訪問過。

(沿著樹的寬度拜訪)

# DFS原理

從目標節點一直延伸下去，直到該目標節點所在邊全部都探訪過後才往回找其他節點，在全部節點都拜訪完後才停止。

(沿著樹的深度拜訪)

# 兩者比較

BFS是先擴大範圍再深入拜訪(使用Queue先進先出的概念)

DFS則是先深入再擴大範圍拜訪(使用Stack後進先出的概念)

### 參考資料:

http://www.csie.ntnu.edu.tw/~u91029/Graph.html

http://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html

http://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html

https://zh.wikipedia.org/wiki/%E6%B7%B1%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2

