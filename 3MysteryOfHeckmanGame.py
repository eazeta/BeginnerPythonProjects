import sys
from time import sleep
print("""
                            (
                .            )        )
                         (  (|              .
                     )   )\/ ( ( (
             *  (   ((  /     ))\))  (  )    )
           (     \   )\(          |  ))( )  (|
           >)     ))/   |          )/  \((  ) 
           (     (      .        -.     V )/   )(    (
            \   /     .   \            .       \))   ))
              )(      (  | |   )            .    (  /
             )(    ,'))     \ /          \( `.    )
             (\>  ,'/__      ))            __`.  /
            ( \   | /  ___   ( \/     ___   \ | ( (
             \.)  |/  /   \__      __/   \   \|  ))
            .  \. |>  \      | __ |      /   <|  /
                 )/    \____/ :..: \____/     \ <
          )   \ (|__  .      / ;: \          __| )  (
         ((    )\)  ~--_     --  --      _--~    /  ))
          \    (    |  ||               ||  |   (  /
                \.  |  ||_             _||  |  /
                  > :  |  ~V+-I_I_I-+V~  |  : (.
                 (  \:  T\   _     _   /T  : ./
                  \  :    T^T T-+-T T^T    ;<
                   \..`_       -+-       _'  )
         )            . `--=.._____..=--'. ./         (
""")
print("""

  ___ ___                 __                                    
 /   |   \   ____   ____ |  | __           _____ _____    ____  
/    ~    \_/ __ \_/ ___\|  |/ /  ______  /     \\__  \  /    \ 
\    Y    /\  ___/\  \___|    <  /_____/ |  Y Y  \/ __ \|   |  \.
 \___|_  /  \___  >\___  >__|_ \         |__|_|  (____  /___|  /
       \/       \/     \/     \/               \/     \/     \/ 

""")

intro1 = input("Welcome to Heckman! This is a short text-based game where you embark on a dangerous journey to find the secret of Heckman! Please press enter to continue!")
print("----------------------BEGIN----------------------")
sleep(1.5)
print("Unknown: Hello?")
sleep(1)
print("Unknown: Hello!")
sleep(1)
print("Unknown: Oh thank goodness! You're awake!")
sleep(1.5)
print("Unknown: I found you passed out here on the floor. Here, drink some water.")
sleep(1.5)
print("Unknown: What's your name young traveller?")
sleep(1)
name = input("Enter your name: ")
sleep(1)
print(f"Unknown: Ahh {name}! What a lovely name! My name is Milo Xavier!")
sleep(1)
print("Prof Milo: I am the world's leading professor in the sleep realm. I've embarked on this journey with my associate Emmanuel but I've seemed to lost him on the way.")
sleep(0.5)
print("Prof Milo: I'm sure he's fine hahaha! He likes to run off and do things on his own!")
sleep(1)
print("Prof Milo: Hmmmm. Would you like to join me on my adventure? I could do with a partner?")
start = ""
while start != 'Yes' and start != 'No':
    start = input("Please answer 'Yes' or 'No': ")

if start == 'No':
    print("Prof Milo: No worries chap! Good luck with whatever you were doing before!")
    sleep(1)
    sys.exit()
else:
    
    print("Lovely! Let's begin")
sleep(1)
print("Story continues")