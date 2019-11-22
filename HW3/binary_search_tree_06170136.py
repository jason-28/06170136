class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
class Solution(object):
    def insert(self, root, val):
        
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        if root==None:
            root=TreeNode(val)
        else:
            current=TreeNode(val)
            if current.val<=root.val:
                if root.left==None:
                    root.left=current
                    return root.left
                else:
                    self.insert(root.left,current.val)
                
            if current.val>root.val:
                if root.right==None:
                    root.right=current
                    return root.right
                else:
                    self.insert(root.right,current.val)
                    
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        if root==None:
            return None
        elif target<root.val:
            root.left=self.delete(root.left,target)
        elif target>root.val:
            root.right=self.delete(root.right,target)
        else:
            if root.left==None and root.right==None:
                self.delete(root,target)
            elif root.left!=None and root.right==None:
                if root.left.val==target:
                    root.left=self.delete(root.left, target)
                return root.left
            elif root.left==None and root.right!=None:
                if root.right.val==target:
                    root.left=self.delete(root.left, target)
                return root.right
            else: 
                if root.left.val==target:
                    root.left=self.delete(root.left, target)
                while root.right.left!=None:
                    root=root.right
                    root.right=root.right.left
                root.right.val==target
                root.val=root.right.val
                root.right=self.delete(root.right, target)
        
        return root
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if target==root.val:
            return root
        elif target<root.val:
            if root.left!=0:
                root.search(root.left,target)
            else:
                return None 
        else:
            if root.right!=0:
                root.search(root.right,target)
            else:
                return None 
            
    def modify(self, root, target, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype: None Do not return anything, modify nodes(maybe more than more) in-place instead.(cannot search())
        """
        while root.left!=None:
            self.modify(self, root.left, target, new_val)
        while root.right!=None:
             self.modify(self, root.right, target, new_val)
        if target=root.val:
            self.insert(root,new_val)
            self.delete(root,target)
        else:
            return root
"""
參考網址:https://www.google.com/url?q=https://youtu.be/YlgPi75hIBc&sa=D&ust=1573899284113000&usg=AFQjCNEeK-0kWFD7MSL8bB85iUq0EM_4Pw

https://github.com/joeyajames/Python/blob/master/Trees/BinarySearchTree.py

https://gist.github.com/jakemmarsh/8273963
"""  
