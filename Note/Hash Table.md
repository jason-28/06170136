# Hash table

## 定義：

Hash table是一種用來儲存Key&Value的資料結構。使用Hash Function將Key值轉換成Array對應的Index，而該位置就是用來儲存Value的地方。

![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Hash_table_3_1_1_0_1_0_0_SP.svg/473px-Hash_table_3_1_1_0_1_0_0_SP.svg.png)

Hash Table由下列三者組成：

- Key:
  - 作為獨立的索引，通常為字串，也就是應用端輸入的東西。
- hash function:
  - 通過某些算式或是方法，將 keys 轉換成能對應特定的 index 的。
  - 他的設計理念是一個key會有對應的且獨立的 bucket，但是目前大多數的設計都會有碰撞問題，也就是不同的 keys 經過轉換後會對應到一樣的 bucket。
- bucket:
  - 他是一個 array ，有多個位置可以儲存資料，在裡面可以是空的可以存一筆資料，甚至也可以放其它資料結構，例如：linked-list
