import random
import selector
import printer


class BatTigerChickenWorm:

    items = ["棒子(Bat)", "老虎(Tiger)", "雞(Chicken)", "蟲(Worm)"]

    def __init__(self):
        printer.print_color_text("棒打老虎雞吃蟲\n", printer.textPink)
        printer.print_color_text("遊戲規則：", printer.textPink)
        printer.print_color_text("棒打老虎，老虎吃雞，雞吃蟲，蟲蛀棒！", printer.textPink)

    def play(self):
        printer.print_color_text("\n開始：", printer.textPink)
        user = selector.select(self.items)
        computer = random.randint(0, len(self.items) - 1)
        printer.print_color_text("", printer.textPink)
        printer.print_color_text("你選擇" + self.items[user] + "，電腦出" + self.items[computer] + "。", printer.textPink)
        if user - computer == -1:
            printer.print_color_text("恭喜，你贏了!!", printer.textGreen)
        elif user - computer == 1:
            printer.print_color_text("你輸了!!", printer.textRed)
        else:
            printer.print_color_text("平手，再來一次!!", printer.default)
            self.play()
