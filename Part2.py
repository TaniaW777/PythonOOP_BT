import os
import sys
from datetime import datetime

# ======================================================
#                STYLING AND UI COMPONENTS
# ======================================================


class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    PRIMARY = '\033[38;5;75m'
    SUCCESS = '\033[38;5;46m'
    WARNING = '\033[38;5;214m'
    DANGER = '\033[38;5;196m'
    INFO = '\033[38;5;87m'
    LIGHT = '\033[38;5;250m'
    DARK = '\033[38;5;240m'
    BG_PRIMARY = '\033[48;5;75m'
    BG_DARK = '\033[48;5;236m'


class UIComponents:
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def print_header(title):
        width = 120
        print(f"\n{Colors.BG_PRIMARY}{Colors.BOLD}{' ' * width}{Colors.RESET}")
        print(f"{Colors.BG_PRIMARY}{Colors.BOLD}{title:^{width}}{Colors.RESET}")
        print(f"{Colors.BG_PRIMARY}{Colors.BOLD}{' ' * width}{Colors.RESET}\n")

    @staticmethod
    def print_section(title):
        print(f"\n{Colors.PRIMARY}{Colors.BOLD}▬ {title}{Colors.RESET}")

    @staticmethod
    def print_card(title, content_dict):
        max_key_len = max(len(str(k)) for k in content_dict)
        print(
            f"\n{Colors.BG_DARK}{Colors.BOLD} {title} {' ' * (50 - len(title) - 3)}{Colors.RESET}")
        for key, value in content_dict.items():
            print(
                f"  {Colors.LIGHT}{key:<{max_key_len + 2}}: {Colors.RESET}{Colors.BOLD}{value}{Colors.RESET}")

    @staticmethod
    def progress_bar(percentage, length=30):
        filled = int(length * percentage / 100)
        bar = f"{Colors.SUCCESS}{'█' * filled}{Colors.DARK}{'░' * (length - filled)}{Colors.RESET}"
        return f"[{bar}] {percentage:.1f}%"

    @staticmethod
    def input_field(prompt):
        return input(f"{Colors.INFO}↳ {prompt}{Colors.LIGHT}: {Colors.RESET}")

    @staticmethod
    def print_success(msg): print(f"{Colors.SUCCESS}✓ {msg}{Colors.RESET}")
    @staticmethod
    def print_warning(msg): print(f"{Colors.WARNING}⚠ {msg}{Colors.RESET}")
    @staticmethod
    def print_error(msg): print(f"{Colors.DANGER}✗ {msg}{Colors.RESET}")


# ======================================================
#                       MODELS
# ======================================================


class Person:
    def __init__(self, name, birth_year):
        self._name = name
        self._birth_year = birth_year

    def calculate_age(self, current_year):
        return current_year - self._birth_year


class Student(Person):
    def __init__(self, name, birth_year, student_id, dorm):
        super().__init__(name, birth_year)
        self.student_id = student_id
        self.dorm = dorm


class MealPlan:
    def __init__(self, days, meals_per_day, breakfast, lunch, dinner, discount_percent):
        self.days = days
        self.meals_per_day = meals_per_day
        self.breakfast_cost = breakfast
        self.lunch_cost = lunch
        self.dinner_cost = dinner
        self.discount_percent = discount_percent

    def average_meal_cost(self):
        return (self.breakfast_cost + self.lunch_cost + self.dinner_cost) / 3

    def weekly_meals(self):
        return self.days * self.meals_per_day

    def weekly_meal_cost(self):
        base = self.weekly_meals() * self.average_meal_cost()
        discount = base * (self.discount_percent / 100)
        return base - discount, discount


class SnackPlan:
    def __init__(self, weekly_budget, snacks_count):
        self.weekly_budget = weekly_budget
        self.snacks_count = snacks_count

    def average_snack_cost(self):
        return self.weekly_budget / self.snacks_count if self.snacks_count > 0 else 0


class BudgetManager:
    def __init__(self, student, mealplan, snackplan, current_year):
        self.student = student
        self.mealplan = mealplan
        self.snackplan = snackplan
        self.current_year = current_year

    def compute(self):
        age = self.student.calculate_age(self.current_year)
        weekly_meal_cost, discount_amount = self.mealplan.weekly_meal_cost()
        total_weekly = weekly_meal_cost + self.snackplan.weekly_budget
        daily = total_weekly / 7
        monthly = total_weekly * 4
        semester = monthly * 4
        semester_savings = discount_amount * 16

        return {
            "full_name": self.student._name,
            "student_id": self.student.student_id,
            "dorm": self.student.dorm,
            "age": age,
            "weekly_meals": self.mealplan.weekly_meals(),
            "avg_meal_cost": self.mealplan.average_meal_cost(),
            "avg_snack_cost": self.snackplan.average_snack_cost(),
            "weekly_meal_cost": weekly_meal_cost,
            "discount_amount": discount_amount,
            "discount_percent": self.mealplan.discount_percent,
            "weekly_snacks": self.snackplan.snacks_count,
            "snack_budget": self.snackplan.weekly_budget,
            "total_weekly": total_weekly,
            "daily_budget": daily,
            "monthly": monthly,
            "semester": semester,
            "semester_savings": semester_savings
        }


def print_full_summary(result):
    UIComponents.clear_screen()
    UIComponents.print_header("  STUDENT MEAL PLAN DASHBOARD")

    UIComponents.print_card(f" STUDENT • {result['full_name']}", {
        "ID": result['student_id'],
        "Dorm": result['dorm'],
        "Age": f"{result['age']} years",
        "Discount": f"{'Yes' if result['discount_percent'] > 0 else 'No'} ({result['discount_percent']}%)"
    })

    UIComponents.print_section(" CONSUMPTION")
    UIComponents.print_card(" MEALS & SNACKS", {
        "Meals/week": result['weekly_meals'],
        "Avg meal cost": f"{result['avg_meal_cost']:.0f} CFA",
        "Snacks/week": result['weekly_snacks'],
        "Avg snack cost": f"{result['avg_snack_cost']:.0f} CFA"
    })

    UIComponents.print_section(" WEEKLY COSTS")
    original = result['weekly_meal_cost'] + result['discount_amount']
    UIComponents.print_card(" COST BREAKDOWN", {
        "Meals (gross)": f"{original:.0f} CFA",
        "Discount": f"-{result['discount_amount']:.0f} CFA",
        "Meals (net)": f"{Colors.SUCCESS}{result['weekly_meal_cost']:.0f} CFA{Colors.RESET}",
        "Snacks": f"{result['snack_budget']:.0f} CFA",
        "TOTAL WEEK": f"{Colors.BOLD}{result['total_weekly']:.0f} CFA{Colors.RESET}"
    })

    UIComponents.print_section(" PROJECTIONS")
    UIComponents.print_card(" BUDGET FORECAST", {
        "Daily": f"{result['daily_budget']:.0f} CFA",
        "Monthly": f"{result['monthly']:.0f} CFA",
        "Semester": f"{Colors.WARNING}{result['semester']:.0f} CFA{Colors.RESET}",
        "Semester savings": f"{Colors.SUCCESS}+{result['semester_savings']:.0f} CFA{Colors.RESET}"
    })

    meal_pct = (result['weekly_meal_cost'] / result['total_weekly']
                * 100) if result['total_weekly'] > 0 else 0
    snack_pct = 100 - meal_pct
    print(f"\n{Colors.BOLD}Weekly budget split:{Colors.RESET}")
    print(f"  Meals  → {UIComponents.progress_bar(meal_pct)}")
    print(f"  Snacks → {UIComponents.progress_bar(snack_pct)}")

    print(f"\n{Colors.DARK}{'═' * 80}{Colors.RESET}")
    print(f"{Colors.LIGHT}Generated on {datetime.now().strftime('%Y-%m-%d %H:%M')} • Eat smart, save more!{Colors.RESET}")
    print(f"{Colors.DARK}{'═' * 80}{Colors.RESET}\n")


# ======================================================
#                BULLETPROOF INPUT FUNCTIONS
# ======================================================


def collect_student_info():
    UIComponents.clear_screen()
    UIComponents.print_header(" STUDENT REGISTRATION")

    while True:
        name = UIComponents.input_field("Full name").strip()
        if name:
            break
        UIComponents.print_error("Name cannot be empty!")

    while True:
        student_id = UIComponents.input_field("Student ID").strip()
        if student_id:
            break
        UIComponents.print_error("Student ID is required!")

    while True:
        dorm = UIComponents.input_field("Dormitory / Residence").strip()
        if dorm:
            break
        UIComponents.print_error("Dormitory is required!")

    while True:
        try:
            current_year = int(UIComponents.input_field(
                "Current year (e.g. 2025)").strip())
            if 2000 <= current_year <= 2100:
                break
            UIComponents.print_error("Year must be between 2000 and 2100")
        except ValueError:
            UIComponents.print_error("Please enter a valid number")

    while True:
        try:
            birth_year = int(UIComponents.input_field("Year of birth").strip())
            if 1900 <= birth_year <= current_year:
                break
            UIComponents.print_error("Invalid birth year")
        except ValueError:
            UIComponents.print_error("Please enter a valid number")

    UIComponents.print_success("Student registered successfully!")
    return Student(name, birth_year, student_id, dorm), current_year


def collect_meal_plan():
    UIComponents.clear_screen()
    UIComponents.print_header(" MEAL PLAN SETUP")

    while True:
        try:
            days = int(UIComponents.input_field(
                "Days per week eating on campus (1-7)").strip())
            if 1 <= days <= 7:
                break
            UIComponents.print_error("Enter a number between 1 and 7")
        except ValueError:
            UIComponents.print_error("Please enter a valid integer")

    while True:
        try:
            meals = int(UIComponents.input_field(
                "Meals per day (1-3)").strip())
            if 1 <= meals <= 3:
                break
            UIComponents.print_error("Enter 1, 2 or 3")
        except ValueError:
            UIComponents.print_error("Please enter a valid integer")

    while True:
        try:
            breakfast = float(UIComponents.input_field(
                "Average breakfast cost (CFA)").strip())
            if breakfast >= 0:
                break
            UIComponents.print_error("Cost cannot be negative")
        except ValueError:
            UIComponents.print_error("Enter a valid amount")

    while True:
        try:
            lunch = float(UIComponents.input_field(
                "Average lunch cost (CFA)").strip())
            if lunch >= 0:
                break
            UIComponents.print_error("Cost cannot be negative")
        except ValueError:
            UIComponents.print_error("Enter a valid amount")

    while True:
        try:
            dinner = float(UIComponents.input_field(
                "Average dinner cost (CFA)").strip())
            if dinner >= 0:
                break
            UIComponents.print_error("Cost cannot be negative")
        except ValueError:
            UIComponents.print_error("Enter a valid amount")

    # ─── DISCOUNT: NOW IMPOSSIBLE TO BYPASS ───
    discount_percent = 0
    while True:
        answer = UIComponents.input_field(
            "Do you have a discount card? (yes/no)").strip().lower()

        if answer in ["yes", "y", "ye", "yep", "oui", "o", "1"]:
            while True:
                try:
                    discount_percent = float(UIComponents.input_field(
                        "Discount percentage (%)").strip())
                    if 0 <= discount_percent <= 100:
                        UIComponents.print_success(
                            f"Discount applied: {discount_percent}%")
                        break
                    else:
                        UIComponents.print_error(
                            "Percentage must be between 0 and 100!")
                except ValueError:
                    UIComponents.print_error(
                        "Please enter a valid number (e.g. 15)")
            break

        elif answer in ["no", "n", "non", "0", ""]:
            discount_percent = 0
            UIComponents.print_success("No discount applied.")
            break

        else:
            UIComponents.print_error(
                "Invalid answer! Please type 'yes' or 'no' only.")

    UIComponents.print_success("Meal plan configured!")
    return MealPlan(days, meals, breakfast, lunch, dinner, discount_percent)


def collect_snack_plan():
    UIComponents.clear_screen()
    UIComponents.print_header(" SNACK BUDGET")

    while True:
        try:
            budget = float(UIComponents.input_field(
                "Weekly snack budget (CFA)").strip())
            if budget >= 0:
                break
            UIComponents.print_error("Budget cannot be negative")
        except ValueError:
            UIComponents.print_error("Enter a valid amount")

    while True:
        try:
            count = int(UIComponents.input_field(
                "Number of snacks per week").strip())
            if count >= 0:
                break
            UIComponents.print_error("Cannot be negative")
        except ValueError:
            UIComponents.print_error("Enter a valid integer")

    UIComponents.print_success("Snack plan saved!")
    return SnackPlan(budget, count)


# ======================================================
#                       MAIN MENU
# ======================================================


def print_main_menu():
    UIComponents.clear_screen()
    UIComponents.print_header(" STUDENT MEAL BUDGET MANAGER")
    print(f"\n{Colors.BOLD}Main Menu:{Colors.RESET}\n")
    print(f"  {Colors.PRIMARY}1.{Colors.RESET} New calculation")
    print(f"  {Colors.PRIMARY}2.{Colors.RESET} View all students")
    print(f"  {Colors.PRIMARY}3.{Colors.RESET} Exit\n")
    print(f"{Colors.DARK}{'─' * 60}{Colors.RESET}")


def print_students_summary(students):
    UIComponents.clear_screen()
    UIComponents.print_header(" REGISTERED STUDENTS")
    if not students:
        UIComponents.print_warning("No students registered yet.")
    else:
        for i, (s, r) in enumerate(students, 1):
            UIComponents.print_card(f"Student {i} • {s._name}", {
                "ID": s.student_id,
                "Age": f"{r['age']} yrs",
                "Dorm": s.dorm,
                "Weekly": f"{r['total_weekly']:.0f} CFA",
                "Semester": f"{r['semester']:.0f} CFA"
            })
    input(f"\n{Colors.LIGHT}Press Enter to continue...{Colors.RESET}")


def main():
    students = []
    while True:
        print_main_menu()
        choice = UIComponents.input_field("Choose an option (1-3)").strip()

        if choice == "1":
            student, year = collect_student_info()
            mealplan = collect_meal_plan()
            snackplan = collect_snack_plan()
            result = BudgetManager(
                student, mealplan, snackplan, year).compute()
            students.append((student, result))
            input(
                f"\n{Colors.LIGHT}Press Enter to view full report...{Colors.RESET}")
            print_full_summary(result)
            input(f"\n{Colors.LIGHT}Press Enter to continue...{Colors.RESET}")

        elif choice == "2":
            print_students_summary(students)

        elif choice == "3":
            UIComponents.clear_screen()
            UIComponents.print_header(" THANK YOU!")
            print(
                f"\n{Colors.SUCCESS}Thanks for using Student Meal Budget Manager!{Colors.RESET}")
            print(f"{Colors.LIGHT}Have a great day!{Colors.RESET}\n")
            break

        else:
            UIComponents.print_error("Invalid option! Choose 1, 2 or 3")
            input(f"{Colors.LIGHT}Press Enter...{Colors.RESET}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        UIComponents.clear_screen()
        print(f"\n{Colors.WARNING}Goodbye!{Colors.RESET}")
