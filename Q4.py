def sum_avg(marks, index=0, total=0):
    
    if index >= len(marks):
        average = total / len(marks) if marks else 0
        return total, average
    

    total += marks[index]
    return sum_avg(marks, index + 1, total)


marks = [85, 90, 78, 92, 88]
total_marks, avg_marks = sum_avg(marks)
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {avg_marks:.2f}")