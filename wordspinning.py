def spin_words(sentence):
    arr = sentence.split(" ")
    for i in range(len(arr)):
        if len(arr[i]) >= 5:
            arr[i] = arr[i][::-1]
    glue = " "
    word = glue.join(arr)
    print(word)
    return arr


spin_words("Welcome to the world")