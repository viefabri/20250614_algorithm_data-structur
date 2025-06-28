'''
N個の品物があり、i(= 0,1,...,N-1)番目の品物の重さはweight(i), 価値はvalue(i)で与えられます。
このN個の品物から、重さの総和がWを超えないように、いくつか選びます。選んだ品物の価値の総和として考えられる最大値を求めてください。
'''
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
   
    wght:list[int] = get_user_input("重さ","2 1 3 2 1 5")

    if len(wght) == 0:
        return None

    vl:list[int] = get_user_input("価値","3 2 6 1 3 85")

    if len(vl) == 0:
        return None

    if len(wght) != len(vl):
        print("品物の重さと価値は同じ件数を入力してください")
        return None
   
    W:int = get_user_input_w()
   
    if W == 0:
        return None
   
    dp = np.zeros((len(vl)+1,W+1))


    for j in range(1,W+1):
        for i in range(0,len(vl)):

            #選ばない場合
            dp[i+1][j] = dp[i][j] 
            #選ぶ場合
            if wght[i] <= j:
                dp[i+1][j] = max(dp[i][j],dp[i][j - wght[i]]+vl[i])

    print(f"選んだ品物価値の総和最大値： {int(dp[len(vl)][W])}") 
   
# このファイルが直接実行された場合にmain()関数を呼び出す
if __name__ == "__main__":
    main()