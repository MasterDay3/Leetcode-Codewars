def tree_by_levels(node):
    if node is None:
        return []

    result = []
    queue = [node]
    while queue:
        ver = queue.pop(0)
        result.append(ver.value)

        if ver.left:
            queue.append(ver.left)
        if ver.right:
            queue.append(ver.right)

    return result
