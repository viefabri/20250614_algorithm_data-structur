# -*- coding: utf-8 -*-

def linear_search_v1():    
    """
    code 3.4 ペアわの最小値を求める
    2つのリストa, bから要素を1つずつ選び、その和がk以上となるペアの中で
    和の最小値を求める。
    
    Args:
        a (list): 整数リスト
        b (list): 整数リスト
        k (int): 基準値
        
    Returns:
        int | None: 条件を満たすペアの和の最小値。見つからない場合はNone。
    """
    _minValue = float('inf') # 最小値

    # 入力を受取る
    try:
        n_str, k_str = input("配列の要素数 N と探す値 k をスペース区切りで入力してください: ").split()
        N = int(n_str)
        k = int(k_str)
    except ValueError:
        print("正しい数値を入力してください。")
        return

    # 配列の入力を受け取る
    a = set_array(N,"a")
    b = set_array(N,"b")

    # 線形探索
    min_value = _minValue  # 初期値
    for i in range(N):
        for j in range(N):
            
            # 和がk未満の場合は捨てる
            if (a[i] + b[j]) < k:
                continue
                
            # 和がk以上の場合は最小値を更新
            min_value = min(min_value, a[i] + b[j])
                
    ans = min_value

    print(ans)
    
def set_array(N,strName):
      try:
        a = list(map(int, input(f"{strName}の{N}個の整数をスペース区切りで入力してください: ").split()))
        if len(a) != N:
            print(f"入力された要素の数が{N}個ではありません。")
            
        return a
    
      except ValueError:
        print("正しい数値を入力してください。")
        return None

if __name__ == '__main__':
    print("--- code 3.4 ペアわの最小値を求める ---")
    linear_search_v1()