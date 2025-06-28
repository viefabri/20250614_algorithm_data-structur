
import tkinter as tk
from tkinter import messagebox
from typing import List, Tuple

def solve_frog_problem_with_path(h: List[int]) -> Tuple[int, List[int]]:
    """
    動的計画法でFrog問題を解き、最小コストと最適経路を返す。

    Args:
        h: 各足場の高さを格納したリスト。

    Returns:
        (最小コスト, 最適経路のインデックスリスト) のタプル。
    """
    n = len(h)
    if n == 0:
        return 0, []
    if n == 1:
        return 0, [0]

    dp = [float('inf')] * n
    parent = [-1] * n  # 経路を復元するための親ポインタ配列
    dp[0] = 0

    for i in range(1, n):
        # --- 1つ前の足場からのジャンプ ---
        cost1 = dp[i - 1] + abs(h[i] - h[i - 1])

        # --- 2つ前の足場からのジャンプ（存在する場合）---
        if i > 1:
            cost2 = dp[i - 2] + abs(h[i] - h[i - 2])
            # コストが小さい方を採用
            if cost1 < cost2:
                dp[i] = cost1
                parent[i] = i - 1
            else:
                dp[i] = cost2
                parent[i] = i - 2
        else:
            dp[i] = cost1
            parent[i] = i - 1

    # ゴールからスタートまで親をたどって経路を復元
    path = []
    curr = n - 1
    while curr != -1:
        path.append(curr)
        curr = parent[curr]
    path.reverse()  # スタートからゴールの順にする

    return dp[n - 1], path

class FrogGUI:
    def __init__(self, master: tk.Tk):
        self.master = master
        master.title("Frog問題最小コスト計算機")
        master.geometry("800x600")

        # --- スタイル設定 ---
        self.BG_COLOR = "#F0F0F0"
        self.CANVAS_BG = "#FFFFFF"
        self.SCAFFOLD_COLOR = "#4A90E2"
        self.PATH_COLOR = "#D0021B"
        self.FONT = ("Helvetica", 12)

        master.configure(bg=self.BG_COLOR)

        # --- ウィジェットの作成と配置 ---
        # 入力フレーム
        input_frame = tk.Frame(master, padx=10, pady=10, bg=self.BG_COLOR)
        input_frame.pack(fill=tk.X)

        tk.Label(input_frame, text="足場の高さ:", font=self.FONT, bg=self.BG_COLOR).pack(side=tk.LEFT, padx=5)
        self.h_entry = tk.Entry(input_frame, width=50, font=self.FONT)
        self.h_entry.insert(0, "2 9 4 5 1 5 10")
        self.h_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

        self.calc_button = tk.Button(input_frame, text="計算実行", command=self.calculate_and_display, font=self.FONT)
        self.calc_button.pack(side=tk.LEFT, padx=5)

        # 結果表示フレーム
        result_frame = tk.Frame(master, padx=10, pady=5, bg=self.BG_COLOR)
        result_frame.pack(fill=tk.X)
        self.result_label = tk.Label(result_frame, text="最小コスト: ---", font=(self.FONT[0], 14, 'bold'), bg=self.BG_COLOR)
        self.result_label.pack()

        # 可視化キャンバス
        self.canvas = tk.Canvas(master, bg=self.CANVAS_BG, highlightthickness=0)
        self.canvas.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # 初期描画
        self.calculate_and_display()

    def calculate_and_display(self):
        try:
            h_str = self.h_entry.get().strip()
            if not h_str:
                h = []
            else:
                h = [int(x) for x in h_str.split()]
        except ValueError:
            messagebox.showerror("入力エラー", "半角数字をスペース区切りで入力してください。")
            return

        min_cost, path = solve_frog_problem_with_path(h)
        self.result_label.config(text=f"最小コスト: {min_cost}")
        self.draw_scaffolds_and_path(h, path)

    def draw_scaffolds_and_path(self, h: List[int], path: List[int]):
        self.canvas.delete("all")
        if not h:
            return

        # キャンバスのサイズを取得
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        if canvas_width < 2 or canvas_height < 2: # ウィンドウ初期化前は描画しない
            self.master.after(50, lambda: self.draw_scaffolds_and_path(h, path))
            return

        # 描画パラメータの計算
        n = len(h)
        padding = 40
        bar_width = (canvas_width - 2 * padding) / (n * 1.5) if n > 0 else 0
        max_h = max(h) if h else 1
        
        # 足場の描画
        scaffold_coords = []
        for i, height in enumerate(h):
            x0 = padding + i * (bar_width * 1.5)
            x1 = x0 + bar_width
            y1 = canvas_height - padding
            y0 = y1 - (height / max_h) * (canvas_height - 2 * padding - 20) if max_h > 0 else y1
            
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=self.SCAFFOLD_COLOR, outline="black")
            self.canvas.create_text(x0 + bar_width/2, y1 + 10, text=str(i), font=self.FONT)
            scaffold_coords.append((x0 + bar_width/2, y0))

        # 最適経路の描画
        if len(path) > 1:
            path_points = []
            for i in path:
                center_x, top_y = scaffold_coords[i]
                path_points.extend([center_x, top_y - 10]) # 少し上に見えるように
            
            self.canvas.create_line(path_points, fill=self.PATH_COLOR, width=3, arrow=tk.LAST)

def main():
    root = tk.Tk()
    app = FrogGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
