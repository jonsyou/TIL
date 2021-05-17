print('계급','계급값', '도수','누적도수','상대도수', sep='\t')
print('-'*50)
# a = pd.cut(sr,[0,10,20,30,40,50,60,70,80,90,100]).value_counts().sort_index()
result = pd.cut(sr,range(0,101,10)).value_counts().sort_index()
result
