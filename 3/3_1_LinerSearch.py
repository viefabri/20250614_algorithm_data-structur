# -*- coding: utf-8 -*-

_noData = -1

def linear_search_v1():
    
    ans = _noData
    
    """
    C++のコードのロジックを忠実に再現したバージョン
    """
    # Nとvの入力を受け取る
    try:
        n_str, v_str = input("配列の要素数 N と探す値 v をスペース区切りで入力してください: ").split()
        N = int(n_str)
        v = int(v_str)
    except ValueError:
        print("正しい数値を入力してください。")
        return

    # 配列aの入力を受け取る
    try:
        a = list(map(int, input(f"{N}個の整数をスペース区切りで入力してください: ").split()))
        if len(a) != N:
            print(f"入力された要素の数が{N}個ではありません。")
            return
    except ValueError:
        print("正しい数値を入力してください。")
        return

    # 線形探索
    exist = False  # 初期値は False に
    for i in range(N):
        if a[i] == v:
            #exist = True  # 見つかったらフラグを立てる
            ans = i
            break # 見つかった時点でループを抜けるのが効率的

    # 結果出力
    #if exist:
    #    print("Yes")
    #else:
    #    print("No")
    print(ans)


# def linear_search_v2():
#     """
#     よりPythonらしい、シンプルな書き方のバージョン
#     """
#     # Nとvの入力を受け取る (Nは実際には使わないが、入力形式を合わせるため)
#     try:
#         _, v_str = input("配列の要素数 N と探す値 v をスペース区切りで入力してください: ").split()
#         v = int(v_str)
#     except ValueError:
#         print("正しい数値を入力してください。")
#         return

#     # 配列aの入力を受け取る
#     try:
#         a = list(map(int, input("整数をスペース区切りで入力してください: ").split()))
#     except ValueError:
#         print("正しい数値を入力してください。")
#         return

#     # Pythonの `in` 演算子を使って探索
#     if v in a:
#         print("Yes")
#     else:
#         print("No")


if __name__ == '__main__':
    print("--- C++のロジックを再現したバージョン ---")
    linear_search_v1()
    # print("\n--- Pythonらしいシンプルなバージョン ---")
    # linear_search_v2()