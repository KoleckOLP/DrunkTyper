text = "Cigarettes and tiny liquor bottles,\nJust what you'd expect inside her new Balenciaga.\nWild romance turned dreams into an empire.\nSelf-made success now she rolls with Rockefellers."
last_correct = 1
length = 3
tooktime = 44.42

print(text[:last_correct])
print(text[last_correct:length])
print(text[length:])

print(f"{text[last_correct:length].replace(' ', '·')}")

words = len(text.split())

wpm = (words / tooktime) * 60

characters = len(text)

wpm5 = ((characters / 5) / tooktime) * 60

print(f"{characters}characters {words}words {tooktime}time {round(wpm, 2)}wpm {round(wpm5, 2)}wpm5")