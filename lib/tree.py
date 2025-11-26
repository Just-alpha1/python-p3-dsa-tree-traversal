class Tree:
  def __init__(self, root=None):
    self.root = root

  def get_element_by_id(self, id):
    if not self.root:
      return None
    
    queue = [self.root]

    while queue:
      node = queue.pop(0)
      if node.get('id') == id:
        return node
      # Add children to the end to maintain left-to-right order
      queue.extend(node.get('children', []))

    return None
