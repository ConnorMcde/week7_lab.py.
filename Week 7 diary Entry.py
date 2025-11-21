"""Week 7 Diary Entry"""

diary_entry = input("Enter your diary entry: ")

with open("my_diary.txt", "w") as f:
 f.write(diary_entry + "\n")#\n adds new lines

with open("my_diary.txt", "r") as f:
 file = f.read()
 
 print(f"Your diary entry was: {file}")
 