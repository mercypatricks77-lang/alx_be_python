# weather_advice.py
# Ask the user about today's weather and give clothing advice.

# Ask the user (we use strip() to remove extra spaces and lower() to make input lowercase)
weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

# Decide what to print using if, elif, else
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
