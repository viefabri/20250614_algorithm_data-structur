# -*- coding: utf-8 -*-

def main():
    """
    部分和問題をビット全探索で解くメイン関数
    """
    print("要素数Nと目標和Wをスペース区切りで入力してください。(例: 3 5)")
    try:
        # N (要素数) と W (目標和) を入力から受け取る
        N, W = map(int, input().split())
    except ValueError:
        print("入力形式が正しくありません。プログラムを終了します。")
        return

    print(f"{N}個の整数をスペース区切りで入力してください。(例: 1 4 3)")
    try:
        # N個の整数をリストaとして入力から受け取る
        a = list(map(int, input().split()))
    except ValueError:
        print("入力形式が正しくありません。プログラムを終了します。")
        return

    # 入力された要素の数がNと一致するかチェック
    if len(a) != N:
        print(f"エラー: {N}個の要素が入力されていません。プログラムを終了します。")
        return

    # 答えが見つかったかどうかを記録するフラグ変数
    exist = False

    # 0から2^N - 1までの整数'bit'をループさせる
    # この'bit'が、ひとつの「部分集合」のパターンに対応
    # (1 << N) は 2のN乗を計算
    for bit in range(1 << N):
        # この部分集合（bitパターン）の要素の和を格納する変数
        current_sum = 0

        # N個の各要素iが、今調べている部分集合'bit'に含まれるかチェック
        for i in range(N):
            # 'bit'のi番目のビットが1かどうかを判定する
            # C++のコードにあった (bit & (1 << i)) 
            # 計算結果が0でなければ、i番目の要素は集合に含まれると判断
            if (bit & (1 << i)):
                # i番目の要素a[i]を和に加える
                current_sum += a[i]

        # 計算した和が目標和Wと一致するかチェック
        if current_sum == W:
            exist = True
            # 一つでも見つかれば、それ以上探す必要はないのでループを抜ける
            break

    # 最終的な結果を出力
    if exist:
        print("Yes")
    else:
        print("No")

# このファイルが直接実行された場合にmain()関数を呼び出す
if __name__ == "__main__":
    main()

