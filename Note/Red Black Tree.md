# Red Black Tree

## 定義:
紅黑樹是以樹的資料結構為基礎延伸的資料結構(為了解決一般二元樹的不平衡問題,避免其退化成Linked List)

![](https://yotsuba1022.gitbooks.io/data-structure-note/content/assets/rbtree-1.png)

## 特徵:

* 節點都有顏色(紅/黑)

* 根總是黑的

* 若節點是紅的, 則其子節點必為黑;若節點是黑色,則其子節點可為紅或黑

* 每個**空子節點**(對非葉節點來說,本可能有,但實際沒有的子節點)都是黑的

* 從根節點到葉節點或空子節點的每條路徑(簡單路徑), 必須包含相同數目的黑色節點

![](https://yotsuba1022.gitbooks.io/data-structure-note/content/assets/rbtree-2.png)
