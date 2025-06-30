import numpy as np

def main():
    S: str = input()
    T: str = input()

    s_len, t_len = len(S), len(T)
    
    # DPテーブルの定義
    # Python標準のリストでも実装可能です
    dp = [[0] * (t_len + 1) for _ in range(s_len + 1)]
    
    # DPテーブルの初期化（0行目と0列目を先に埋める）
    for i in range(s_len + 1):
        dp[i][0] = i
    for j in range(t_len + 1):
        dp[0][j] = j
        
    # DPテーブルを埋める（i=1, j=1からスタート）
    for i in range(1, s_len + 1):
        for j in range(1, t_len + 1):
            # 文字が違う場合の変更コスト
            cost = 0 if S[i-1] == T[j-1] else 1
            
            # 3つの操作（変更、削除、挿入）のうち最小のコストを選ぶ
            dp[i][j] = min(
                dp[i-1][j-1] + cost,    # 変更操作
                dp[i-1][j] + 1,         # 削除操作 (上から)
                dp[i][j-1] + 1          # 挿入操作 (左から)
            )

    #print(np.array(dp)) # numpy配列として見たい場合
    print(dp[s_len][t_len])

if __name__ == "__main__":
    main()