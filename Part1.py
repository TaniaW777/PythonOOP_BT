# Student Meal Plan Calculator - Part 1
# A program to help students calculate their weekly meal expenses and nutritional intake
# Original design by POOP_BT - Created for efficient student budgeting

# "=" * n permit to print the egal sign n times
print("=" * 140)
print("=" * 140)
# In the rest of the code we will use \t to automate tabulation
print("\t\t\t\t\t\tUNIVERSITY STUDENT MEAL PLAN CALCULATOR")
print("\t\t\t\t\t\tSmart Budgeting for Campus Life ")
print("=" * 140)
print("=" * 140)
print("\t\t\t\t\tWelcome! This tool will help you plan and budget your meals.")
print("\t\t\t\t\tPlease provide accurate information for the best estimates.")

# Collecting basic student information
print("\t\t\t\t\t\t\t--- STUDENT INFORMATION ---")
student_name = input("Enter your full name: ")
student_id = input("Enter your student ID: ")
dorm_building = input("Enter your dorm building name: ")
current_year = int(input("Enter current year (e.g., 2025): "))
birth_year = int(input("Enter your birth year: "))

print("\t\t\t\t\t\t\t--- MEAL PLAN DETAILS ---")
# Collecting meal plan information
days_per_week = int(
    input("How many days per week will you eat on campus? (1-7): "))
meals_per_day = int(input("How many meals per day on average? (1-3): "))
breakfast_cost = float(input("Enter average breakfast cost (CFA): "))
lunch_cost = float(input("Enter average lunch cost (CFA): "))
dinner_cost = float(input("Enter average dinner cost (CFA): "))
print("\t\t\t\t\t\t\t--- ADDITIONAL OPTIONS ---")
has_discount = input("Do you have a student meal discount card? (yes/no): ")
discount_percentage = float(
    input("Enter discount percentage if applicable (0 if none): "))

# New feature: Snack budget tracking
print("\t\t\t\t\t\t\t--- SNACK & BEVERAGE BUDGET ---")
weekly_snack_budget = float(
    input("Enter your weekly snack/beverage budget (CFA): "))
snacks_per_week = int(input("How many snacks do you buy per week? : "))

print("=" * 140)
print("                    PROCESSING YOUR MEAL PLAN...")
print("=" * 140)


# This part is for Calculations
student_age = current_year - birth_year
total_meals_per_week = days_per_week * meals_per_day
average_meal_cost = (breakfast_cost + lunch_cost + dinner_cost) / 3
weekly_cost_before_discount = total_meals_per_week * average_meal_cost
discount_amount = weekly_cost_before_discount * (discount_percentage / 100)
weekly_cost_after_discount = weekly_cost_before_discount - discount_amount

# Additional calculations for snacks and total budget
average_snack_cost = weekly_snack_budget / snacks_per_week
total_weekly_food_cost = weekly_cost_after_discount + weekly_snack_budget
monthly_cost = total_weekly_food_cost * 4
semester_cost = monthly_cost * 4

# Calculate daily average spending
daily_food_budget = total_weekly_food_cost / 7

# Calculate savings with discount
total_semester_savings = (discount_amount * 4 * 4)

# Boolean check for discount eligibility
is_discount_member = has_discount.lower() == "yes"

# Display summary
print("=" * 140)
print("\t\t\t\t\t\t\tMEAL PLAN SUMMARY")
print("=" * 140)
print(f"Student Name: {student_name}")
print(f"Student ID: {student_id}")
print(f"Dorm Building: {dorm_building}")
print(f"Age: {student_age} years old")
print(f"Discount Card Holder: {is_discount_member}")
print("\t\t\t\t\t\t\t--- MEAL STATISTICS ---")
print(f"Total meals per week: {total_meals_per_week} meals")
print(f"Average cost per meal: {average_meal_cost:.2f} CFA")
print(f"Snacks per week: {snacks_per_week} snacks")
print(f"Average cost per snack: {average_snack_cost:.2f} CFA")
print("\t\t\t\t\t\t\t--- COST BREAKDOWN ---")
print(
    f"Weekly meal cost (before discount): {weekly_cost_before_discount:.2f} CFA")
print(f"Discount applied: {discount_amount:.2f} CFA ({discount_percentage}%)")
print(
    f"Weekly meal cost (after discount): {weekly_cost_after_discount:.2f} CFA")
print(f"Weekly snack budget: {weekly_snack_budget:.2f} CFA")
print(f"TOTAL weekly food cost: {total_weekly_food_cost:.2f} CFA")
print("\t\t\t\t\t\t\t--- BUDGET PROJECTIONS ---")
print(f"Daily average spending: {daily_food_budget:.2f} CFA")
print(f"Estimated monthly cost: {monthly_cost:.2f} CFA")
print(f"Estimated semester cost (4 months): {semester_cost:.2f} CFA")
print(
    f"Total semester savings from discount: {total_semester_savings:.2f} CFA")
print("\t\t\t\t\t\t\t--- FINANCIAL INSIGHTS ---")
meals_percentage = (weekly_cost_after_discount / total_weekly_food_cost) * 100
snacks_percentage = (weekly_snack_budget / total_weekly_food_cost) * 100
print(f"Meals represent {meals_percentage:.1f}% of your food budget")
print(f"Snacks represent {snacks_percentage:.1f}% of your food budget")
print("=" * 140)
print("=" * 140)
print("\t\t\t\t\t\t\tThank you for using the Meal Plan Calculator!")
print("\t\t\t\t\t\t\tSave money, eat well, succeed in school! ")
print("=" * 140)
print("=" * 140)
print(f"\t\t\t\t\t\t\t TIP: With your current plan, you're spending about")
print(
    f"\t\t\t\t\t\t\t{daily_food_budget:.0f}CFA per day on food. Plan accordingly!")
