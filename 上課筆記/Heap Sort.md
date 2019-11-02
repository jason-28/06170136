# Heap Sort:

Heap(堆)是一個以Binary Tree為基礎的資料結構,分為Max Heap(最上方節點值最大)及Min Heap(最上方節點值最小)

Heap Sort的概念就是先分堆,再依照Max/Min來比節點的大小,直到Heap裡剩下一個值

### 設最上方節點index=i時:

* 左方節點=2*i+1
* 右方節點=2*i+2

(最上面i的index是0,每往下一層+1)
