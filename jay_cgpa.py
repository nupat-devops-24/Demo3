# BEFORE

# cgpa = float(input("Enter cgpa score: "))
'''
if cgpa > 5:
    print("invalid cgpa score")
elif cgpa >= 4.5 and cgpa <= 5:
    print("Congratulations You are a first class student")
elif cgpa >= 3.5 and cgpa < 4.5:
    print("Congratulations You are a second class upper student")
elif cgpa >= 3.0 and cgpa < 3.5:
    print("Congratulations You are a second class lower student")
elif cgpa >= 2.0 and cgpa < 3:
    print("Congratulations You are a Third class student")
else:
    print("Congratulations You are a pass student")'''



# AFTER

def compute_grade_with_params(cgpa: float):
    '''function description'''
    
    try:
        if cgpa == True or cgpa == False:
            print('Debug: Boolean input detected')
            cgpa = float(cgpa)

        elif cgpa > 5:
            print("Value cannot be higher than 5.0")
        elif cgpa >= 4.5 and cgpa <= 5.0:
            print("Congratulations You are a first class student")
        elif cgpa >= 3.5 and cgpa < 4.5:
            print("Congratulations You are a second class upper student")
        elif cgpa >= 3.0 and cgpa < 3.5:
            print("Congratulations You are a second class lower student")
        elif cgpa >= 2.0 and cgpa < 3.0:
            print("Congratulations You are a Third class student")
        elif cgpa >= 0.0 and cgpa < 2.0:
            print("Congratulations You are a pass student")
        else:
            print("Value cannot be less than 0")
    
    except TypeError:
        print('Incorrect value type for boolean operation')
    
    except ValueError:
        print('Incorrect value type for float conversion')
    
    return None


# Test cases
compute_grade_with_params(3.4)
compute_grade_with_params(2.0)
compute_grade_with_params(6)
compute_grade_with_params('3.0')
compute_grade_with_params('string')
compute_grade_with_params(-12)
compute_grade_with_params(True)
compute_grade_with_params(False)