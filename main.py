
import tkinter

class Main:
    def __init__(self) -> None:
        pass

    def main(self):
        tk = tkinter.Tk()
        tk.geometry("800x400")
        tk.title('Number system converter')
        tk.mainloop()
    
    def converter(self, number, numbersystem):
        array = []
        while number != 0:
            temp = number % numbersystem
            number = number // 2
            array.append(temp)
            array.reverse()
        return array


main = Main()
main.main()
