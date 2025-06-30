import numpy as np

def get_user_input(msg:str, smpl : str) -> list[int]:
    """
    ユーザーからスペース区切りの整数入力を受け取り、リストとして返す。
    不正な入力に対してはエラーメッセージを表示し、空のリストを返す。
    """
    try:
        print("品物の"+msg+"を整数で各々入力してください（例:"+smpl+"）")
        input_str = input("品物の"+msg+"：")
        # 入力が空の場合は処理を終了
        if not input_str.strip():
            print("エラー: 入力がありません。")
            return []
        h = list(map(int, input_str.split()))
        return h
    except ValueError:
        print("エラー: 不正な入力です。半角数字をスペース区切りで入力してください。")
        return []
    
def get_user_input_w() -> int:
    """
    ユーザーから整数入力を受け取り、返す。
    不正な入力に対してはエラーメッセージを表示し、ゼロを返す。
    """
    try:
        print("重さの総和を整数で入力してください（例:15）")
        input_str = input("重さの総和：")
        # 入力が空の場合は処理を終了
        if not input_str.strip():
            print("エラー: 入力がありません。")
            return 0
        h = int(input_str)
        return h
    except ValueError:
        print("エラー: 不正な入力です。半角数字をスペース区切りで入力してください。")
        return 0

def main():
    # --- 入力処理（変更なし） ---
    weights:list[int] = get_user_input("重さ","2 1 3 2 1 5")
    if not weights: return None

    values:list[int] = get_user_input("価値","3 2 6 1 3 85")
    if not values: return None

    if len(weights) != len(values):
        print("品物の重さと価値は同じ件数を入力してください")
        return None
    
    W:int = get_user_input_w()
    if W == 0: return None
    
    N = len(values)
    
    # --- DP計算部分（改善後） ---
    
    # DPテーブルの初期化
    dp = np.zeros((N + 1, W + 1), dtype=int)

    # ループ順序を「品物→重さ」に変更
    # i番目までの品物を考慮する
    for i in range(N):
        # jは現在の重さの上限
        for j in range(W + 1):
            item_weight = weights[i]
            item_value = values[i]

            # 品物iが重すぎて選べない場合
            if j < item_weight:
                # 前の行(i番目の品物を考慮しない)の値をそのまま引き継ぐ
                dp[i+1][j] = dp[i][j]
            # 品物iが選べる場合
            else:
                # 「選ばない場合の価値」と「選ぶ場合の価値」の大きい方を採用
                # 選ばない場合: dp[i][j]
                # 選ぶ場合: dp[i][j - item_weight] + item_value
                dp[i+1][j] = max(dp[i][j], dp[i][j - item_weight] + item_value)

    print(f"選んだ品物価値の総和最大値： {dp[N][W]}")

if __name__ == "__main__":
    main()