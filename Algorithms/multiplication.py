def multTables(max):
    for i in range(1,max+1):
        for j in range(1,max+1):
            print('{0} '.format(i*j)),
        print('\n')

multTables(12)