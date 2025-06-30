def knapsack_2d(N, W, weights, values):
    """
    基本的な2次元DPでナップサック問題を解く関数
    
    Args:
        N (int): 品物の数
        W (int): ナップサックの容量
        weights (list[int]): 各品物の重さのリスト
        values (list[int]): 各品物の価値のリスト

    Returns:
        int: 価値の合計の最大値
    """
    # DPテーブルの初期化: dp[i][w]
    # サイズ (N+1) x (W+1) のテーブルを全て0で初期化
    dp = [[0] * (W + 1) for _ in range(N + 1)]

    # i は品物のインデックス (1からNまで)
    for i in range(1, N + 1):
        # w は現在のナップサックの容量 (1からWまで)
        for w in range(1, W + 1):
            # i番目の品物の重さと価値 (リストのインデックスは i-1 になる)
            item_weight = weights[i - 1]
            item_value = values[i - 1]
            
            # もし現在の容量wが品物の重さより小さいなら、品物は追加できない
            if w < item_weight:
                # 前のステップ(i-1番目の品物まで)の結果をそのまま引き継ぐ
                dp[i][w] = dp[i - 1][w]
            else:
                # 品物を「追加しない場合」と「追加する場合」で価値が高い方を選ぶ
                # 追加しない場合: dp[i - 1][w]
                # 追加する場合: item_value + dp[i - 1][w - item_weight]
                dp[i][w] = max(dp[i - 1][w], item_value + dp[i - 1][w - item_weight])

    # テーブルの右下の値が最終的な答え
    return dp[N][W]