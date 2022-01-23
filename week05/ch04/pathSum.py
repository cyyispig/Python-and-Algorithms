class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        ret = list()
        path = list()
        
        def dfs(root: TreeNode, target: int):
            if not root:
                return
            path.append(root.val)
            target -= root.val
            if not root.left and not root.right and target == 0:
                ret.append(path[:])
            dfs(root.left, target)
            dfs(root.right, target)
            path.pop()
        
        dfs(root, target)
        return ret
