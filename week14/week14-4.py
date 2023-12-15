s = {1,2,3,4} #第一種:大括號
print(s)
s = set( (1,3,5,7) ) #第二種:set()裡放圓括號
print(s)
s = set( [1,2,4,3] ) #第二種:set()裡放方括號,放陣列
print(s)
s = set( 'Hello' ) #第二種:set()裡放字串
print(s)

#下面試試 .add() 和 .remove
s.add(100)
print(s)
s.remove('H')
print(s)