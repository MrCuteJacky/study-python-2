tag = "\033"

default = "0"

textBlack = "30"
textRed = "31"
textGreen = "32"
textYellow = "33"
textBlue = "34"
textPink = "35"
textCyan = "36"
textWhite = "37"

backgroundBlack = "40"
backgroundRed = "41"
backgroundGreen = "42"
backgroundYellow = "43"
backgroundBlue = "44"
backgroundPink = "45"
backgroundCyan = "46"
backgroundWhite = "47"

def printWithColor(message, color):
    print(tag + "[" + color + "m" + message + tag + "[" + default + "m")