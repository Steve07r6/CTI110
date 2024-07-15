# Stephen Townsend
# 07-06-24
# P4HW1
# A program that calculates the average of scores 

def main():
    print("Grade Calculator")
    print("================")

    
    num_scores = int(input("How many number of scores do you want to enter? "))

    scores = []

    for i in range(num_scores):
        while True:
            try:
                score = float(input(f"Enter score #{i+1}: "))
                if score < 0 or score > 100:
                    print("INVALIS Score entered!!!")
                    print("Score should be between 0 and 100")
                   
                else:
                    scores.append(score)
                    break
            except ValueError:
                print("INVALID Score entered!!!!")
                print("Score should be between 0 and 100")
                      

    print("\nScores entered:")
    for score in scores:
        print(score)

    print("----------Results----------")

    lowest_score = min(scores)
    print(f"\nLowest score entered: {lowest_score}")
    scores.remove(lowest_score)
    print("\nScore modified list")
    for score in scores:
        print(score)
    average_score = sum(scores) / len(scores)
    print(f"\nScores Average: {average_score:.2f}")
    letter_grade = determine_letter_grade(average_score)
    print(f"Grade: {letter_grade}")

def determine_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
    print("-------------------------")

if __name__ == "__main__":
    main()
