import os
from datetime import datetime

class JournalManager:
    def __init__(self, file="journal.txt"):
        self.file = file
        
    def add_entry(self):
        entry = input("Enter your journal entry: \n")
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        
        try:
            with open(self.file, "a") as f:
                f.write(f"{timestamp} \n{entry}\n\n")
        except FileNotFoundError as e:
            print(f"Error: {e}")
        else:
            print("Journal entry added successfully.\n")
    
    def view_entries(self):
        try:
            with open("journal.txt", "r") as f:
                text = f.read()
        
        except FileNotFoundError as e:
            print(f"Error: {e}")
            print("No journal entries found. start by adding a new entry.\n")
        
        else:
            if text.strip() == "":
                print("No journal entries found. Start by adding new entry.\n")
            else:
                print(f"Journal entries:\n {"-" * 50}\n", text, "\n")
        
        finally:
            print("Had a great session on oop concept.\n")
            
    def search_entry(self):
        search_entry = input("Enter the keyword or date to search for: ")
        
        try:
            with open("journal.txt", "r") as f:
                text = f.read()

        except FileNotFoundError as e:
            print(f"Error: {e}")
            
        else:
            entries = text.strip().split("\n\n")
            match_ent = []
            for i in entries:
                if text.lower() in i.lower():
                    match_ent.append(i)
            
            if match_ent:
                print(f"Matching Entries: \n{"-" * 50}")
                for i in match_ent:
                    print(i)

            else:
                print(f"No entries were found for {search_entry}")

    def delete_entries(self):
        if not os.path.exists(self.file):
            print("No journal entries to delete.")
            return
        
        ans = input("Are you sure you want to delete all entries? (yes/no): ")
        try:
            if ans.lower() == "yes":
                with open(self.file, "w") as f:
                    f.write("")
            else:
                print("Deletion cancelled.")
                return
                    
        except FileNotFoundError as e:
            print(f"Error: {e}")
            print("No journal entries to delete.")

        else:
            print("All journal entries have been deleted.")

while True:        
    print("1.Add a new Entry\n 2.View all Entries\n 3.Search for an Entry\n 4.Delete all Entry\n 5.Exit") 
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            JournalManager().add_entry()
            
        case 2:
            JournalManager().view_entries()

        case 3:
            JournalManager().search_entry()

        case 4:
            JournalManager().delete_entries()

        case 5:
            print(f"Thank you for using personal journal manager. Goodbye!")
            break

        case _:
            print("Invalid input...")