import math

SNACK_DATA = {
    "ratna sagar ka dosa sambhar": (7, 4),
    "sindhi ke chhole bhature": (10, 5),
    "yo china se soup": (1, 1),
    "maharaja burger": (5, 8),
    "vada pav": (6, 1),
    "Toast": (4, 4)
}

def recommend_snack(user_crunch, user_mess):
    best_snack = None
    min_distance = float('inf')

    for snack, coords in SNACK_DATA.items():
        dist = math.sqrt((user_crunch - coords[0])**2 + (user_mess - coords[1])**2)
        
        if dist < min_distance:
            min_distance = dist
            best_snack = snack
            
    return best_snack


print("--- The Highly Unprofessional Snack Predictor ---")
try:
    c = float(input("How much CRUNCH do you crave? (1-10): "))
    m = float(input("How much MESS are you willing to clean up? (1-10): "))

    result = recommend_snack(c, m)
    print(f"\nScience suggests you should eat:  {result} ")
except ValueError:
    print("Please enter numbers,Nikita! The snacks depend on it.")