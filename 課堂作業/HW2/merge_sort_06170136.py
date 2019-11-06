class Solution(object):
    def merge_sort(self,array):
        if len(array)>1:
            pivot=len(array)//2 #設基準點為陣列中間的數值
            left=self.merge_sort(array[:pivot]) #將array內包含第一個到設定的基準點(不包含)的值丟回去
            right=self.merge_sort(array[pivot:]) #將array內包含基準點到最後一個的值丟回去
        else: 
            return array #陣列長度小於等於1時回傳

        l=0 #左邊list的index
        r=0 #右邊list的index
        sol=[] #用來放比完大小後比較小的那個值的空list

        while l<len(left) and r<len(right): #兩邊index同時小於array長度時,比較小的值放入sol,同時該方index+1
            if left[l]<right[r]:
                sol.append(left[l])
                l+=1
            else:
                sol.append(right[r])
                r+=1

        while l<len(left): #僅剩左方有值時執行的while迴圈
            sol.append(left[l])
            l+=1

        while r<len(right): #僅剩右方有值時執行的while迴圈
            sol.append(right[r])
            r+=1

        return sol #全部跑完後回傳排列好的array(sol)
