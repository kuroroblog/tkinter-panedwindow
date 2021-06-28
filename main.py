import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)

        # Windowの画面サイズを設定する。
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        self.master.geometry("300x200")

        # Windowを親要素として、panedwindow Widget(Frame)を作成する。
        # <用語の説明>
        # panedwindow Widget(Frame)の中に配置される、Widgetのことを「ペイン」という。
        # ペインとペインの間の空間を「さっし」という。さっしを選択した状態で、さっしを左右(上下)へ動かすとペインのサイズを自由に変更できる。
        # さっしの中に取っ手を表示する場合、その取っ手のことを「handle」という。handleはさっしと同じ動作を行う。
        # showhandle : さっしの中へhandleを表示するかどうかの設定。True : 表示する, False : 表示しない。
        # sashwidth : さっしの幅を設定。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        panedWindow = tk.PanedWindow(self.master, showhandle=True, sashwidth=20)

        # panedwindow Widget(Frame)を親要素として、label Widgetを作成する。
        # width : 幅の設定
        # background : 背景色の設定
        # 色について : https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
        # text : テキスト情報
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        label1 = tk.Label(panedWindow, width=30, background="red", text='test1')

        # panedwindow Widget(Frame)を親要素として、label Widgetを作成する。
        # width : 幅の設定
        # background : 背景色の設定
        # 色について : https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
        # text : テキスト情報
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        label2 = tk.Label(panedWindow, width=30, background="blue", text='test2')

        # label Widget要素をpanedwindow Widget(Frame)へ格納。ペインとする。
        # add(Widget) : Widgetをpanedwindow Widget(Frame)へ格納する。
        panedWindow.add(label1)
        # label Widget要素をpanedwindow Widget(Frame)へ格納。ペインとする。
        # add(Widget) : Widgetをpanedwindow Widget(Frame)へ格納する。
        panedWindow.add(label2)

        # Windowを親要素とした場合に、panedwindow Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        panedWindow.pack()

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    # Windowをループさせて、継続的にWindow表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    app.mainloop()
