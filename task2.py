def insertion_sort(grades):
    for i in range(1, len(grades)):
        key = grades[i]  # Current grade
        j = i - 1
        while j >= 0 and grades[j] > key:  # Compare values
            grades[j + 1] = grades[j]  # Shift larger values to the right
            j -= 1
        grades[j + 1] = key  # Insert the grade in the correct position
    return grades

# List of student grades
grades = [85, 70, 90, 60, 75, 95]

# Sorting the grades
sorted_grades = insertion_sort(grades)

# Finding the highest and lowest grades
lowest_grade = sorted_grades[0]
highest_grade = sorted_grades[-1]

# Printing results
print("Sorted grades:", sorted_grades)
print("Lowest grade:", lowest_grade)
print("Highest grade:", highest_grade)
