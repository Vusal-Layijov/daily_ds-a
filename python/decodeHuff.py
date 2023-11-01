def decodeHuff(root, s):

    cur_node = root
    encode = ""

    for i in s:
        if i == "0":
            cur_node = cur_node.left
        else:
            cur_node = cur_node.right

        if not cur_node.left and not cur_node.right:
            encode += cur_node.data
            cur_node = root
        else:
            cur_node = cur_node.right

    print(encode)
    
