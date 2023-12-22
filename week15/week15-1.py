        N=len(s)
        ans = 0 #最後答案
        for left in range(N-1): # 要減1 留給右邊
            #0...left  left+1...N+1
            now = 0
            for i in range(N):
                if i <= left and s[i]=='0':now += 1
                if i > left and s[i]=='1':now += 1
            if now > ans: ans = now
        return ans