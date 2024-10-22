with open ('text.txt', 'r', encoding='utf-8') as infile, open('output.txt', 'w', encoding='utf-8') as outfile:
    data=infile.readlines()
    i=0
    for str in data:
        if len(data[i])>5:
            outfile.write(data[i])
        i+=1