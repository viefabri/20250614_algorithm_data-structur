# -*- coding: utf-8 -*-

memo = []

def fibo(N):
    """
    フィボナッチ数を再帰的に計算する関数（メモ化対応）
    """
    global memo

    # まずメモをチェック（すでに計算済みならその値を返す）
    if memo[N] != -1:
        return memo[N]

    # ベースケースの結果もメモに格納する
    if N <= 1:
        memo[N] = N
        return N

    # 答えをメモ化しながら、再帰呼び出し
    memo[N] = fibo(N - 1) + fibo(N - 2)
    return memo[N]

# main関数は変更なし
def main():
    global memo
    while True:
        try:
            max_number_str = input("計算したいフィボナッチ数列の最大項数（2以上）を入力してください: ")
            max_number = int(max_number_str)
            if max_number < 2:
                print("2以上の整数を入力してください。")
                continue
            break
        except ValueError:
            print("無効な入力です。整数を入力してください。")

    memo = [-1] * max_number
    fibo(max_number - 1)
    print("--- 計算結果 ---")
    for i in range(max_number):
        print(f"{i} 項目: {memo[i]}")

if __name__ == '__main__':
    main()
