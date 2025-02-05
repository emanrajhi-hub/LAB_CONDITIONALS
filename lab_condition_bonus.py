# Define movie details
movie_name = "Prison Break"
movie_rating = 3  # Rating out of 5
popularity_score = 72.65  # Popularity as a float

# Conditional statements to evaluate the movie
if movie_rating >= 4 and popularity_score > 80:
    print("Highly recommended")
elif movie_rating >= 3 and popularity_score > 70:
    print("I recommended it. It is good")
elif movie_rating <= 2 and popularity_score > 60:
    print("You should check it out!")
elif movie_rating <= 2 and popularity_score < 50:
    print("Don't watch it. It is a waste of time")




   # Ask for user input
weight = float(input("Enter your weight in kg: "))  # Convert input to float
height = float(input("Enter your height in meters: "))  # Convert input to float

# Calculate BMI
bmi = weight / (height ** 2)

# Print the BMI value
print(f"Your BMI is: {bmi:.2f}")

# Provide feedback based on BMI
if bmi >= 25:
    print("You are overweight. You need to work out more and watch your diet.")
elif 18.5 <= bmi < 25:
    print("You are fit & healthy.")
else:
 print("You are underweight. Watch your health.")