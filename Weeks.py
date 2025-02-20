def life_in_weeks(age):
   
    remaining_time = 90 - age  # Assuming a lifespan of 90 years
    weeks_left = remaining_time * 52
    print(f"You have {weeks_left} weeks left.")


age = int(input("What's your current age? ")) 
life_in_weeks(age)
