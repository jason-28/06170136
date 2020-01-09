# Hash table

## 定義：

Hash table是一種用來儲存Key&Value的資料結構。使用Hash Function將Key值轉換成Array對應的Index，而該位置就是用來儲存Value的地方。

![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Hash_table_3_1_1_0_1_0_0_SP.svg/473px-Hash_table_3_1_1_0_1_0_0_SP.svg.png)

Hash Table由下列三者組成：

### Key
  - 作為獨立的索引，通常為字串。
### Hash Function
  - 通過算式將Key值轉換成能對應特定的Index值。
  - 一個Key會有對應且獨立的Bucket，但目前大多數的設計都會有碰撞問題(不同的Key經過轉換後會對應到相同Bucket)
### Bucket
  - 一個有多個位置可以儲存資料的Array，裡面可以是空的，也可以放入其它類型的資料結構(EX：Linked-List)
