import sys

def main():
    """
    動的計画法（DP）を用いてFrog問題を解く
    """
    
    # Pythonでは非常に大きな値を float('inf') で表現するのが一般的です。
    # これはどんな数値よりも大きいと判定されます。
    INF = float('inf')

    # 入力
    try:
        N = int(input())
        h = list(map(int, input().split()))
    except (ValueError, IndexError):
        print("入力形式が正しくありません。1行目に整数の個数N、2行目にスペース区切りの整数を入力してください。")
        sys.exit(1)

    # Nが0または1の場合はコストは0
    if N <= 1:
        print(0)
        return

    # 配列 dp を定義（配列全体を無限大を表す値で初期化）
    dp = [INF] * N

    # 初期条件
    dp[0] = 0

    # ループ
    for i in range(1, N):
        # 足場 i-1 からジャンプする場合のコスト
        cost1 = dp[i - 1] + abs(h[i] - h[i - 1])
        
        # iが1の場合、2つ前の足場はないのでcost1がそのままdp[i]となる
        if i == 1:
            dp[i] = cost1
        # iが2以上の場合、足場 i-2 からジャンプする場合も考慮する
        else:
            cost2 = dp[i - 2] + abs(h[i] - h[i - 2])
            # cost1とcost2の小さい方を採用する
            dp[i] = min(cost1, cost2)

    # 答え
    # 最後の足場（インデックス N-1）にたどり着くための最小コストを出力
    print(dp[N - 1])

if __name__ == "__main__":
    main()