
import sys
from typing import List

def get_user_input() -> List[int]:
    """
    ユーザーからスペース区切りの整数入力を受け取り、リストとして返す。
    不正な入力に対してはエラーメッセージを表示し、空のリストを返す。
    """
    try:
        print("足場の高さを整数で各々入力してください（例: 2 9 4 5 1 5 10）")
        input_str = input("足場の高さ: ")
        # 入力が空の場合は処理を終了
        if not input_str.strip():
            print("エラー: 入力がありません。")
            return []
        h = list(map(int, input_str.split()))
        return h
    except ValueError:
        print("エラー: 不正な入力です。半角数字をスペース区切りで入力してください。")
        return []

def solve_frog_problem(h: List[int]) -> int:
    """
    動的計画法（空間計算量最適化版）でFrog問題を解く。
    
    Args:
        h: 各足場の高さを格納したリスト。
        
    Returns:
        最初の足場から最後の足場までの最小コスト。
    """
    n = len(h)
    if n <= 1:
        return 0

    # cost_prev2: 2つ前の足場までの最小コスト (i-2)
    # cost_prev1: 1つ前の足場までの最小コスト (i-1)
    cost_prev2 = 0
    cost_prev1 = abs(h[1] - h[0])

    # 3番目の足場 (i=2) から順番に計算
    for i in range(2, n):
        # 1つ前からジャンプする場合のコスト
        cost1 = cost_prev1 + abs(h[i] - h[i-1])
        # 2つ前からジャンプする場合のコスト
        cost2 = cost_prev2 + abs(h[i] - h[i-2])
        
        # 現在の足場 i までの最小コスト
        current_cost = min(cost1, cost2)
        
        # 次の計算のためにコストを更新
        cost_prev2 = cost_prev1
        cost_prev1 = current_cost
        
    return cost_prev1

def main():
    """
    メイン処理。ユーザー入力を受け取り、問題を解いて結果を表示する。
    """
    h = get_user_input()
    
    if not h:
        print("プログラムを終了します。")
        return
        
    min_cost = solve_frog_problem(h)
    
    print(f"最小コスト: {min_cost}")

# このファイルが直接実行された場合にmain()関数を呼び出す
if __name__ == "__main__":
    main()
