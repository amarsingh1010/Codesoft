import json

class ToDoApp:
    def __init__(self, file_path='tasks.json'):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, description):
        task = {"description": description, "completed": False}
        self.tasks.append(task)
        self.save_tasks()

    def complete_task(self, task_id):
        if 0 <= task_id < len(self.tasks):
            self.tasks[task_id]['completed'] = True
            self.save_tasks()

    def delete_task(self, task_id):
        if 0 <= task_id < len(self.tasks):
            del self.tasks[task_id]
            self.save_tasks()

    def display_tasks(self, show_completed=False):
        for i, task in enumerate(self.tasks):
            if show_completed or not task['completed']:
                status = "✔" if task['completed'] else "✘"
                print(f"{i}. {task['description']} [{status}]")

def main():
    app = ToDoApp()
    while True:
        print("\n1. Add Task\n2. Complete Task\n3. Delete Task\n4. View Tasks\n5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            desc = input("Enter task description: ")
            app.add_task(desc)
        elif choice == '2':
            app.display_tasks(show_completed=True)
            task_id = int(input("Enter task ID to complete: "))
            app.complete_task(task_id)
        elif choice == '3':
            app.display_tasks(show_completed=True)
            task_id = int(input("Enter task ID to delete: "))
            app.delete_task(task_id)
        elif choice == '4':
            app.display_tasks()
        elif choice == '5':
            break

if __name__ == '__main__':
    main()
