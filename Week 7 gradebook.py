"""Week 7 Gradebook"""
import csv

grades = {
"Alice": [85, 90, 92],
"Bob": [78, 81, 85],
"Charlie": [95, 100, 98]
}

with open("grades.csv", "w", newline="")as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Score 1", "Score 2", "Score 3"])
    
    for name, scores in grades.items():
        writer.writerow([name] + scores)
        
        
with open("grades.csv","r", newline="") as f:
 reader = csv.reader(f)
 next(reader)
 
 for row in reader:
    name = row[0]                   
    scores = [int(score) for score in row[1:]]  
    average = sum(scores) / len(scores)    
       
    print(f"{name}: Average Score = {average:.1f}")
