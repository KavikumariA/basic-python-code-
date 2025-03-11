import random
class game():
    def func(self):
        global j
        global i
        global g
        x = range(100)
        d =random.choice(x)
        print(d)
        print("Start the gaming")
        for i in range (1,6):
            j = int( input(f"enter your {i} chance  "))
            if j == d:
                print("your r win the game ")
                break
            else:
                print("lose")
                s = d - j
                v = s/2
                print(f"{v} times more value")


obj = game()
obj.func()