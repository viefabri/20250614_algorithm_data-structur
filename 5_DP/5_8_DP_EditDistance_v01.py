import numpy as np

def main():
    S:str = input()
    T:str = input()
    
    # DPテーブルの初期化
    dp = np.full((len(S) + 1, len(T) + 1), np.inf)
    
    dp[0][0] = 0
    
    for i in range(len(S) + 1 ):
        for j in range(len(T) + 1 ):
            #変更操作
            if (i > 0) and (j > 0):
                if S[i-1] == T[j-1]:
                    #処理文字が一致している場合は1つ前のコスト
                    dp[i][j] = min(dp[i][j],dp[i - 1][j -1 ])
                #変更する場合
                else:
                    #処理文字が不一致の場合は1つ前のコスト+1
                    dp[i][j] = min(dp[i][j],dp[i - 1][j - 1] + 1)
                    
            #削除操作
            if i > 0:
                #削除操作：1つ上のマスのコスト+1
                dp[i][j] = min(dp[i][j],dp[i - 1][j] + 1)
            #挿入操作
            if j > 0:
                #挿入操作：1つ左のマスのコスト+1
                dp[i][j] = min(dp[i][j],dp[i][j - 1] + 1)
        
    #print(dp)
    print(dp[len(S)][len(T)])
                
if __name__ == "__main__":
    main()