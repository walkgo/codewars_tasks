def count_sheeps(sheep):
    # sheeps = []
    # for i in sheep:
    #     if i == True:
    #         sheeps.append(i)
    # return len(sheeps)

    print(len(list(i for i in sheep if i == True)))



    # [x for x in int if x%2!=0]


count_sheeps([True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ])