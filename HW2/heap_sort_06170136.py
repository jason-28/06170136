class Solution(object):
    def heap_sort(self,array):
        sol=[] #放最大值的空list
        limit=len(array)//2-1 #i的最大值是陣列長度整除2再減1

        while len(array)>0: #在array長度大於0時,先執行一次Maxheap(設定從i=最大值到i=0的for迴圈)
            for i in range(limit,-1,-1): 
                self.Maxheap(array,i)
            sol.append(array.pop(0)) #再將被移除的分堆完後的最大值(放在第一個)加到空list

        true_sol=sol[::-1] #最後在回傳前反轉

        return true_sol
    def Maxheap(self,array,i):   
        Max=i #設父節點index為最大值的index
        l=2*i+1 #左節點index
        r=2*i+2 #右節點index

        if l<len(array) and array[l]>=array[i]: #左節點的值大於父節點的值時,將最大值index改為左節點
            Max=l

        if r<len(array) and array[r]>=array[Max]: #右節點的值大於最大值時(不論最大值有沒有被換過),將最大值index改為右節點
            Max=r

        if Max!=i: #在前面做完最大值index的調整後,如果i不再是最大值index,將最大值和父節點的值交換
            array[i],array[Max]=array[Max],array[i]
            self.Maxheap(array,Max) #交換完後再執行一次Maxheap(避免其中一方底下有更大的值)
