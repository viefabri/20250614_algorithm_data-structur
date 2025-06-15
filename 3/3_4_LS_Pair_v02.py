import math # float('inf') を使うために import

def find_min_pair_sum(a: list, b: list, k: int) -> int | None:
    """
    2つのリストa, bから要素を1つずつ選び、その和がk以上となるペアの中で
    和の最小値を求める。
    
    Args:
        a (list): 整数リスト
        b (list): 整数リスト
        k (int): 基準値
        
    Returns:
        int | None: 条件を満たすペアの和の最小値。見つからない場合はNone。
    """
    min_value = float('inf')  # 初期値として「無限大」を使用
    n = len(a)

    for i in range(n):
        for j in range(n):
            current_sum = a[i] + b[j]
            if current_sum >= k:
                min_value = min(min_value, current_sum) # min()関数で簡潔に

    # 一度も更新されなかった場合（条件を満たすペアがない場合）
    if min_value == float('inf'):
        return None
    
    return min_value

def main():
    """
    ユーザーからの入力を受け付け、計算関数を呼び出して結果を表示する。
    """
    print("--- code 3.4 ペア和の最小値を求める ---")
    try:
        # 入力処理
        n_str, k_str = input("配列の要素数 N と探す値 K をスペース区切りで入力してください: ").split()
        N = int(n_str)
        K = int(k_str)

        a = list(map(int, input(f"a の {N} 個の整数をスペース区切りで入力してください: ").split()))
        b = list(map(int, input(f"b の {N} 個の整数をスペース区切りで入力してください: ").split()))

        if len(a) != N or len(b) != N:
            print(f"エラー: 入力された要素の数が {N} 個ではありません。")
            return

    except ValueError:
        print("エラー: 正しい形式で数値を入力してください。")
        return

    # 計算関数の呼び出し
    result = find_min_pair_sum(a, b, K)

    # 結果の出力
    if result is None:
        print("条件を満たすペアは見つかりませんでした。")
    else:
        print(f"求める最小値は: {result}")


if __name__ == '__main__':
    main()