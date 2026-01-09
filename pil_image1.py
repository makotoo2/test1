import tkinter as tk
import os
from PIL import Image, ImageTk


def main():
    root = tk.Tk()
    root.title("Pillowのテスト")
    
    name = "Pillowのテスト"

    # 画像ファイルのパスを組み立て
    file_path = os.path.join(os.path.dirname(__file__), "images", "bird.jpg")

    # 画像を開いて表示用に変換（例外処理付き）
    try:
        photo_pil = Image.open(file_path)
    except FileNotFoundError:
        msg = f"画像ファイルが見つかりません: {file_path}"
        label = tk.Label(root, text=msg)
        label.pack(padx=20, pady=20)
        root.mainloop()
        return
    except Exception as e:
        label = tk.Label(root, text=f"画像を開けませんでした: {e}")
        label.pack(padx=20, pady=20)
        root.mainloop()
        return

    print(name)
    # 必要ならリサイズ（ウィンドウに合わせるなど）。ここでは最大幅/高さを指定
    max_size = (800, 600)
    photo_pil.thumbnail(max_size, Image.Resampling.LANCZOS)

    photo_tk = ImageTk.PhotoImage(photo_pil)

    # 明示的に親ウィジェットを渡し、参照を保持
    label = tk.Label(root, image=photo_tk)
    label.image = photo_tk
    label.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
