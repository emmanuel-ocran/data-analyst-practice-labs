# Get user input
name = input("Enter you name: ")
job_name = input("Enter you job: ")
first_adjective = input("Enter first adjective: ")
second_adjective  = input("Enter second adjective : ")
first_food  = input("Enter your first food: ")
second_food = input("Enter your second food: ")
a_feeling = input("How do you feel: ")


madlib = f"""{name} started their first Generation course today. 
They are training as a {job_name}. They found their cohort to be very {first_adjective}
but their teacher was, at least, {second_adjective}. 
For lunch they have {first_food} and {second_food} while reviewing their notes. 
They feel {a_feeling} but are determined to complete the course."""

print(madlib)