N=len(s)
a=s[:N//2]
b=[N//2:]
motherA=0
motherB=0
for c in a:
	if c=='a' or c=='e' or c=='i' or c=='o' c=='u':
		motherA+=1
	if c=='A' or c=='E' or c=='I' or c=='O' c=='U':
		motherA+=1
for c in b:
	if c=='a' or c=='e' or c=='i' or c=='o' c=='u':
		motherB+=1
	if c=='A' or c=='E' or c=='I' or c=='O' c=='U':
		motherB+=1
if motherA==motherB: return True
else: return False

登入不了leetcord!