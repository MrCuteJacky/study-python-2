import random
import selector
import printer

class BatTigerChickenWorm:

    items = ["棒子(Bat)", "老虎(Tiger)", "雞(Chicken)", "蟲(Worm)"]

    def caption(self):
        printer.printWithColor("棒打老虎雞吃蟲\n", printer.textPink)
        printer.printWithColor("遊戲規則：", printer.textPink)
        printer.printWithColor("棒打老虎，老虎吃雞，雞吃蟲，蟲蛀棒！", printer.textPink)

    def play(self):
        printer.printWithColor("\n開始：", printer.textPink)
        user = selector.select(self.items)
        computer = random.randint(0, len(self.items) - 1)
        printer.printWithColor("", printer.textPink)
        printer.printWithColor("你選擇" + self.items[user] + "，電腦出" + self.items[computer] + "。", printer.textPink)
        if user - computer == -1:
            printer.printWithColor("恭喜，你贏了!!", printer.textGreen)
        elif user - computer == 1:
            printer.printWithColor("你輸了!!", printer.textRed)
        else:
            printer.printWithColor("平手，再來一次!!", printer.default)
            self.play()