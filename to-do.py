#Categories
from colorama import Fore, Style, init
init(autoreset=True)
def categorize_task(task):
    task_lower = task.lower()
    if any(word in task_lower for word in [
    "meeting", "email", "presentation", "project", "report", "deadline", "team", "client", "call", "agenda", 
    "follow-up", "submit", "review", "feedback", "schedule", "planning", "strategy", "proposal", "documentation", "deployment",
    "design", "prototype", "debug", "testing", "development", "approval", "resource", "training", "consult", "interview",
    "workflow", "logistics", "negotiation", "memo", "finance", "invoice", "budget", "costing", "contract", "assignment",
    "implementation", "issue", "support", "ticket", "update", "status", "check-in", "performance", "collaborate", "execution"
]):
        return "Work", "🛠"
    elif any(word in task_lower for word in [
    "read", "chapter", "notes", "lecture", "homework", "assignment", "quiz", "exam", "revision", "practice",
    "study", "research", "project", "report", "write", "presentation", "submit", "deadline", "concept", "theory",
    "experiment", "lab", "code", "debug", "solve", "problem", "formula", "analysis", "reference", "paper",
    "article", "review", "essay", "dissertation", "discussion", "class", "attendance", "syllabus", "schedule", "webinar",
    "recording", "tutorial", "MOOC", "platform", "resource", "flashcards", "memorize", "recall", "focus", "revision"
]):
        return "Study", "📚"
    elif any(word in task_lower for word in [
    "grocery", "shopping", "clean", "cook", "laundry", "exercise", "gym", "walk", "run", "jog",
    "meditate", "relax", "book", "movie", "music", "read", "call", "visit", "family", "friend",
    "birthday", "anniversary", "appointment", "doctor", "dentist", "meal", "prep", "budget", "bank", "bills",
    "payment", "insurance", "renewal", "plan", "vacation", "travel", "pack", "unpack", "garden", "pet",
    "repair", "fix", "organize", "declutter", "rest", "nap", "self-care", "therapy", "journal", "reflection"
]):
        return "Personal", "🏃"
    elif any(word in task_lower for word in [
    "reminder", "update", "check", "setup", "create", "plan", "organize", "arrange", "list", "sort","call",
    "contact", "message", "email", "follow-up", "schedule", "appointment", "event", "meeting", "conference",
    "manage", "schedule", "task", "goal", "track", "log", "add", "remove", "monitor", "note","email","buy",
    "record", "remind", "review", "adjust", "complete", "due", "deadline", "priority", "action", "process",
    "status", "start", "finish", "ongoing", "pending", "done", "cancel", "reschedule", "follow", "improve",
    "backup", "sync", "update", "install", "reset", "restart", "support", "info", "alert", "setup"
]):
        return "General", "📞"
    else:
        return "General", "📝"
        
# Add tasks
def add_tasks():
    print("\n📝 Add Tasks (Type 'exit' to stop):")
    while True:
        task = input("Enter a task: ")
        if task.lower() == "exit":
            print("✅ You exited successfully! Tasks added.")
            break
        category, emoji = categorize_task(task)
        with open("to-do.txt", "a", encoding = "utf-8") as file:
            file.write(f"{emoji} [{category}] {task}\n")

# Search tasks
def search_task():
    keyword = input("\n🔍 Enter keyword to search: ")
    found = False
    try:
        with open("to-do.txt", "r", encoding="utf-8") as file:
            for line in file:
                if keyword.lower() in line.lower():
                    print("✅ Found:", line.strip())
                    found = True
        if not found:
            print("❌ No matching tasks found.")
    except FileNotFoundError:
        print("🚫 No to-do list found. Start by adding tasks!")

# View all tasks
def view_all_tasks():
    print(f"\n{Fore.LIGHTBLUE_EX}📃 All Tasks Grouped by Category:\n")
    categories = {"Work": [], "Study": [], "Personal": [], "Others": []}

    try:
        with open("to-do.txt", "r", encoding="utf-8") as file:
            tasks = file.readlines()
            if not tasks:
                print(f"{Fore.YELLOW}📭 No tasks found.")
                return

            for line in tasks:
                for category in categories:
                    if f"[{category}]" in line:
                        categories[category].append(line.strip())
                        break
                else:
                    categories["Others"].append(line.strip())

            for category, tasks in categories.items():
                print(f"{Fore.MAGENTA}{category} Tasks:")
                if tasks:
                    for i, task in enumerate(tasks, 1):
                        print(f"  {Fore.GREEN}{i}. {task}")
                else:
                    print(f"  {Fore.YELLOW}No {category.lower()} tasks.")
                print()  # space between groups
    except FileNotFoundError:
        print(f"{Fore.RED}🚫 No to-do list found.")


# Delete task
def delete_task():
    view_all_tasks()
    category_to_delete = input("🗂 Enter the category to delete a task from: ").strip().lower()

    with open("to-do.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    matched_tasks = [line for line in lines if category_to_delete in line.lower()]
    
    if not matched_tasks:
        print("❌ No tasks found in this category.")
        return

    print("\n📝 Tasks in category:")
    for idx, task in enumerate(matched_tasks, start=1):
        print(f"{idx}. {task.strip()}")

    try:
        task_num = int(input("🔢 Enter the task number to delete: "))
        if task_num < 1 or task_num > len(matched_tasks):
            print("⚠️ Invalid task number.")
            return
    except ValueError:
        print("⚠️ Please enter a valid number.")
        return

    task_to_delete = matched_tasks[task_num - 1]
    updated_tasks = [line for line in lines if line != task_to_delete]

    with open("to-do.txt", "w", encoding="utf-8") as file:
        file.writelines(updated_tasks)

    print("✅ Task deleted successfully.")


# Main function 
def main():
    while True:
        print(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}\n📋 Welcome to TO-DO List Manager!")
        print(f"{Fore.CYAN}1️⃣ {Style.BRIGHT}Add tasks")
        print(f"{Fore.CYAN}2️⃣ {Style.BRIGHT}Search tasks")
        print(f"{Fore.CYAN}3️⃣ {Style.BRIGHT}View All Tasks")
        print(f"{Fore.CYAN}4️⃣ {Style.BRIGHT}Delete Task")
        print(f"{Fore.CYAN}5️⃣ {Style.BRIGHT}Exit")
        choice = input(f"{Fore.YELLOW}👉 Enter your choice (1 to 5): ")

        if choice == "1":
            add_tasks()
        elif choice == "2":
            search_task()
        elif choice == "3":
            view_all_tasks()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print(f"{Fore.MAGENTA}👋 Exiting... Have a productive day!\n")
            break
        else:
            print(f"{Fore.RED}⚠️ Invalid choice. Please enter a number from 1 to 5.")

# Run 
main()
