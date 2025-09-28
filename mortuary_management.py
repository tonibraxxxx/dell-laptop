import datetime
import random

class DeceasedRecord:
    def __init__(self, name, age, gender, date_of_death, storage_location, cause_of_death, state_of_body):
        self.name = name
        self.age = age
        self.gender = gender
        self.date_of_death = date_of_death
        self.storage_location = storage_location
        self.cause_of_death = cause_of_death
        self.state_of_body = state_of_body
        self.entry_date = datetime.datetime.now()
    
    def __str__(self):
        return (f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, \
                f"Date of Death: {self.date_of_death}, Location: {self.storage_location}, \
                f"Cause: {self.cause_of_death}, State: {self.state_of_body}, \
                f"Entry: {self.entry_date.strftime('%Y-%m-%d %H:%M:%S')}")

class MortuaryManagement:
    def __init__(self):
        self.records = []
        self.preload_records()
    
    def preload_records(self):
        names = [
            "John karani wahome", "Jane kaka", "Julius Mwangi", "Emily Clark ATIENO", "Daniel Evans",
            "Jessica White", "Matthew Harris", "Samantha Lewis", "David Walker", "Ashley Young",
            "Christopher Hall", "Amanda King", "Joshua Wright", "Sarah Scott Mushibe", "Andrew Green",
            "Brittany Adams", "Ryan Baker", "Megan Nelson", "Justin Carter", "Lauren Mitchell"
        ]
        genders = ["Male", "Female", "transgender"]
        storage_locations = ["viewing Room A", "viewing Room B", "viewing Room C", "viewing Room D", "viewing 2Room E"]
        causes = ["Natural", "Accident", "Illness", "Unknown", "Homicide"]
        states = ["Fresh", "Embalmed", "Decomposed", "Unknown"]
        for i in range(20):
            name = names[i]
            age = random.randint(18, 60)
            gender = random.choice(genders)
            date_of_death = (datetime.date.today() - datetime.timedelta(days=random.randint(1, 365))).strftime('%Y-%m-%d')
            storage_location = random.choice(storage_locations)
            cause_of_death = random.choice(causes)
            state_of_body = random.choice(states)
            record = DeceasedRecord(name, age, gender, date_of_death, storage_location, cause_of_death, state_of_body)
            self.records.append(record)
    
    def add_record(self, record):
        self.records.append(record)
        print("Record added successfully.\n")
    
    def list_records(self):
        if not self.records:
            print("No records found.\n")
            return
        for idx, rec in enumerate(self.records, 1):
            print(f"{idx}. {rec}\n")
    
    def find_by_name(self, name):
        found = [rec for rec in self.records if rec.name.lower() == name.lower()]
        if found:
            for rec in found:
                print(rec)
        else:
            print("No record found for this name.\n")


def main():
    mm = MortuaryManagement()
    while True:
        print("\n--- Mortuary Management Software ---")
        print("1. Register a Deceased Person")
        print("2. List All Records")
        print("3. Find Record by Name")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            gender = input("Gender: ")
            date_of_death = input("Date of Death (YYYY-MM-DD): ")
            storage_location = input("Storage Location: ")
            cause_of_death = input("Cause of Death: ")
            state_of_body = input("State of the Body (e.g., Fresh, Decomposed, Embalmed): ")
            record = DeceasedRecord(name, age, gender, date_of_death, storage_location, cause_of_death, state_of_body)
            mm.add_record(record)
        elif choice == "2":
            mm.list_records()
        elif choice == "3":
            name = input("Enter name to search: ")
            mm.find_by_name(name)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()