# -*- coding: utf-8 -*-
from typing import List

def recFunc(i: int, w: int, a: List[int]) -> bool:
    """
    部分和問題を再帰的に解く関数。
    aの最初のi個の要素からいくつか選び、その和をwにできるかを判定する。

    Args:
        i (int): 使用する要素の数 (aの最初のi個)
        w (int): 目標とする和
        a (List[int]): 整数のリスト

    Returns:
        bool: 和をwにできる場合はTrue、できない場合はFalse
    """
    # ベースケース: もう選ぶ要素がない場合
    if i == 0:
        return w == 0  # wが0になっていれば成功

    # a[i-1] を選ばない場合と、選ぶ場合のいずれかがTrueならTrueを返す
    # a[i-1] を選ぶ場合は、wがa[i-1]以上である必要がある
    if w >= a[i - 1] and recFunc(i - 1, w - a[i - 1], a):
        return True
    
    if recFunc(i - 1, w, a):
        return True

    return False
    
    # 上記のif文は、以下のように1行で書くことも可能です
    # return recFunc(i - 1, w, a) or (w >= a[i-1] and recFunc(i - 1, w - a[i-1], a))


def main() -> None:
    """
    ユーザーからの入力を受け取り、部分和問題の結果を出力する。
    """
    try:
        print("N個の整数の中からいくつか選び、その和をWにできるかを判定します。")
        
        n_input, w_input = input("要素数Nと目標の和Wを入力してください (例: 4 14): ").split()
        N = int(n_input)
        W = int(w_input)
        
        elements_str = input(f"{N}個の整数を入力してください (例: 3 5 8 1): ").split()
        a = [int(num) for num in elements_str]

        if len(a) != N:
            print(f"エラー: {N}個の整数が入力されていません。プログラムを終了します。")
            return

        if recFunc(N, W, a):
            print("Yes")
        else:
            print("No")
            
    except ValueError:
        print("エラー: 不正な入力です。半角数字をスペース区切りで入力してください。")
    except IndexError:
        print("エラー: 入力形式が正しくありません。")


# このファイルが直接実行された場合にmain()関数を呼び出す
if __name__ == "__main__":
    main()