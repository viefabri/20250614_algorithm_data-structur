import sys

def main():
    """
    C++のソースコードをPythonで実装したものです。
    標準入力からN, W、そしてN個の品物の重さと価値を読み込み、
    ナップサック問題の答えを標準出力に出力します。
    """
    
    # 入力
    # sys.stdin.readline を使うと、大量の入力でも高速に処理できます。
    try:
        n_str, w_str = sys.stdin.readline().split()
        N = int(n_str)
        W = int(w_str)
        
        weights = []
        values = []
        for _ in range(N):
            weight_i, value_i = map(int, sys.stdin.readline().split())
            weights.append(weight_i)
            values.append(value_i)

    except (IOError, ValueError) as e:
        print(f"入力エラー: {e}", file=sys.stderr)
        print("実行方法: python your_script_name.py < input.txt", file=sys.stderr)
        print("または、実行後に手動で入力してください。", file=sys.stderr)
        print("入力形式:\nN W\nweight_1 value_1\nweight_2 value_2\n...", file=sys.stderr)
        return

    # DPテーブル定義
    # dp[i][w] は、i番目までの品物で重さの合計がw以下となるように選んだ時の価値の最大値を表す
    # (N+1) x (W+1) の2次元リストを0で初期化
    dp = [[0] * (W + 1) for _ in range(N + 1)]

    # DPループ
    for i in range(N):
        for w in range(W + 1):
            # i番目の品物を選ぶ場合
            # 現在の重さwが品物iの重さ以上であるかチェック
            if w >= weights[i]:
                # 「i番目の品物を選んだ場合の価値」と「i番目の品物を選ばなかった場合の価値」の大きい方を採用
                # C++のchmax(a, b)は a = max(a, b) と同じ
                dp[i + 1][w] = max(
                    dp[i][w - weights[i]] + values[i],  # 選ぶ場合
                    dp[i][w]                            # 選ばない場合
                )
            else:
                # i番目の品物を選べない場合（重さオーバー）
                # 価値はi-1番目までの状態から変わらない
                dp[i + 1][w] = dp[i][w]
    
    # 最適値の出力
    # N個の品物をすべて考慮し、重さの総和がWの時の最大価値
    print(dp[N][W])


if __name__ == "__main__":
    main()