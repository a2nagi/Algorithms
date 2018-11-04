# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        store_nodes = [] 
        if root == None:
            return None
        
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                store_nodes.append(str(node.val))
            else:
                store_nodes.append("null")
        
        i = len(store_nodes)-1
        while store_nodes[i] == "null":
            store_nodes.pop()
            i-=1
        
        return ','.join(store_nodes)
            
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        tree_data = data.split(',')
        root = TreeNode(tree_data[0])
        queue = collections.deque([root])
        
        index = 1
        length = len(tree_data)
        
        while queue and index < length:
            cur_node = queue.popleft()
            if tree_data[index] != "null":
                cur_node.left = TreeNode(tree_data[index])
                queue.append(cur_node.left)
            
            index += 1
            if index == length:
                break
                
            if tree_data[index] != "null":
                cur_node.right = TreeNode(tree_data[index])
                queue.append(cur_node.right)
            
            index += 1
        return root

            
                
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
