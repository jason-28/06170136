# Minimum Spanning Tree 

## 定義:

Kruskal是一種貪婪演算法的應用，著重在點與點之間的量值(cost、weight、spend time)，是以 **邊** 為主體紀錄的資料結構。

主要目的就是以最小的成本將樹狀網路串連起來。

![](https://i.imgur.com/V2FHxJF.png)

### 步驟:
![](https://i.imgur.com/szk1jSN.png)

1. 生成記錄邊和權重的表
2. 依權重大小(小到大)去重新整理表
3. 由權重大小(小到大)去連接邊，當連接時造成cycle(內部循環)的情況時，則跳過，直到所有節點都連到。
