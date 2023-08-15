def designerPdfViewer(h, word):
    # Write your code here
    height = 0
    allLetters = 'abcdefghijklmnopqrstuvwxyz'
    for char in word:
        ind = allLetters.index(char)
        if h[ind] > height:
            height = h[ind]
    return height*len(word)
