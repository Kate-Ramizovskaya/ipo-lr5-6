with open ('text.txt', 'r', encoding='utf-8') as infile, open('output.txt', 'w', encoding='utf-8') as outfile:#открытие файлов
    data=infile.readlines()#перекидывание первого файла в список
    i=0#инициализация индекса
    for str in data:#цикл для перебора 
        if len(data[i])>5:#for для исключение не подходящих
            outfile.write(data[i])#переписывание подходящих в новый файл
        i+=1#увеличение индекса для дальнейшей работы
