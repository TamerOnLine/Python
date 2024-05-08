set1 = {'ll', 'oo', 'pp', 'ee'}
set2 = {'uu', 'qq', 'tt', 'ee'}
set3 = {'11', '22'}
print(set1, set2, set3)



print(set1 | set2 | set3)
print(set1.union(set2, set3))
print(set2.union(set1, set3))


