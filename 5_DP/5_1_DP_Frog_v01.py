
import math

memo = []

def getUserInput() -> int:
    """
    ユーザーからの入力を受け取る
    """
    try:
        print("足場の高さを整数で各々入力してください（例：0 7 5 1 4 5 4）")
        a_input = input("足場の高さ：").split()
        a = [int(num) for num in a_input]
            
    except ValueError:
        print("エラー: 不正な入力です。半角数字をスペース区切りで入力してください。")
        return []
    except IndexError:
        print("エラー: 入力形式が正しくありません。")
        return []
    
    return a

def getMinCst( h: list[int], i:int ) -> int:
    global memo
    
    # ベースケース
    if i == 0:
        return 0
    
    if memo[i] != float('inf'):
        return memo[i]
       
    # i-1のコスト
    res = getMinCst(h, i - 1) + abs(h[i] - h[i - 1])
    
    # i-2のコスト
    if i > 1:
        res = min(res, getMinCst(h, i - 2) + abs(h[i] - h[i - 2]))

    memo[i] = res
    return memo[i]

def main() -> None:
    global memo
    
    h:int = getUserInput()
    N:int = len(h)
    
    if N == 0:
        return
    '''
    テスト用
    print(h)
    print(N)
    '''
    
    memo = [float('inf')] * N
    
    cst = getMinCst(h,N-1)
    
    print(f"最小コスト：{cst}")

# このファイルが直接実行された場合にmain()関数を呼び出す
if __name__ == "__main__":
    main()