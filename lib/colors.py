class colors():
  def __init__(self, red, green, yellow, blue, purple, cyan, white, bgred, bggreen, bgyellow, bgblue, bgpurple, bgcyan, bgwhite, reset):
    self.red = red
    self.green = green
    self.yellow = yellow
    self.blue = blue
    self.purple = purple
    self.cyan = cyan
    self.white = white
    self.bgred = bgred
    self.bggreen = bggreen
    self.bgyellow = bgyellow
    self.bgblue = bgblue
    self.bgpurple = bgpurple
    self.bgcyan = bgcyan
    self.bgwhite = bgwhite
    self.reset = reset
colors = colors("\033[1;91m", "\033[1;92m", "\033[1;93m", "\033[1;94m", "\033[1;95m", "\033[1;96m", "\033[1;97m", "\033[1;101m", "\033[1;102m", "\033[1;103m", "\033[1;104m", "\033[1;105m", "\033[1;106m", "\033[1;107m", "\033[0;0m")