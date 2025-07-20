class Soldier:
    def __init__(self, name, rank, iD, unit):
        self.name = name
        self.rank = rank
        self.iD = iD
        self.unit = unit
    def _str_(self):
        return f"ID: {self.iD}, Name: {self.name}, Rank: {self.rank}, Unit: {self.unit}"

class MilitaryBase:
    def _init_(self):
        self.soldiers = {}  
        
        self.active = {}
        self.onLeave = {}
        self.retired = {}
        
    def add_soldier(self,soldier):
        self.soldiers[soldier.iD] = soldier
        print(f"Welcome {soldier.name} to Indian Army")

    def remove_soldier(self, iD):
        if iD in self.soldiers:  
            removed_soldier = self.soldiers.pop(iD)  
            print(f"{removed_soldier.name}, thanks for your sacrifice for our country")
        else:
            print("Soldier is not found")
            
    def update_soldier(self):
        try:
            iD = int(input("Enter the soldier's ID to update: "))
            if iD in self.soldiers:
                soldier = self.soldiers[iD]
                print(f"Current Details: Name: {soldier.name}, Rank: {soldier.rank}, Unit: {soldier.unit}")
                
                new_name = input("Enter the updated name (or press Enter to keep the same): ")
                new_rank = input("Enter the updated rank (or press Enter to keep the same): ")
                new_unit = input("Enter the updated unit (or press Enter to keep the same): ")

                if new_name:
                    soldier.name = new_name
                if new_rank:
                    soldier.rank = new_rank
                if new_unit:
                    soldier.unit = new_unit

                print(f"Updated Details: Name: {soldier.name}, Rank: {soldier.rank}, Unit: {soldier.unit}")
            else:
                print("Soldier's ID not found")
        except ValueError:
            print("Invalid input")
    
    def track_soldier(self):
        c = int(input("Press 1 to track with name, 2 to track with rank or 3 to track with unit: "))
        found_soldiers = []
        if c == 1:
            name = input("Enter the name: ")
            for iD in self.soldiers:  
                if self.soldiers[iD].name == name:  
                    found_soldiers.append((iD, self.soldiers[iD]))
                
        elif c == 2:
            rank = input("Enter the rank of the soldier: ")
            for iD in self.soldiers:
                if self.soldiers[iD].rank == rank:  
                    found_soldiers.append((iD, self.soldiers[iD]))

        elif c == 3:
            unit = input("Enter the unit: ")
            for iD in self.soldiers:
                if self.soldiers[iD].unit == unit:  
                    found_soldiers.append((iD, self.soldiers[iD]))
    
        if found_soldiers:
            for iD, soldier in found_soldiers:
                print(f"ID: {iD}, Name: {soldier.name}, Rank: {soldier.rank}, Unit: {soldier.unit}")
        else:
            print("No soldier found")
            
    def deployment_status(self):
        iD = int(input("Enter the soldier's ID: "))
        if iD not in self.soldiers:
            print("Soldier ID not found")
            return
        c = input("Enter the present deployment status (press a for active, o for on leave and r for retaired): ")
        if c == 'a':
            self.active[iD] = self.soldiers[iD]
            print(f"{self.soldiers[iD].name} is marked as Active")
        elif c == 'o':
            self.onLeave[iD] = self.soldiers[iD]
            print(f"{self.soldiers[iD].name} is marked as On Leave")
        elif c == 'r':
            self.retired[iD] = self.soldiers[iD]
            print(f"{self.soldiers[iD].name} is marked as Retired")
 
base = MilitaryBase()       
while True:
    choice = int(input("Enter 1 for adding the soldier, 2 for removing the soldier, 3 for updating, 4 for tracking soldier, 5 for deployement status of the soldier and 6 for exit: "))
    if choice == 1:
        name = input("Enter Soldier's Name: ")
        rank = input("Enter Rank: ")
        iD = int(input("Enter Soldier's ID: "))
        unit = input("Enter Unit: ")
        soldier = Soldier(name, rank, iD, unit)
        base.add_soldier(soldier)
    elif choice == 2:
        iD = int(input("Enter Soldier ID to remove: "))
        base.remove_soldier(iD)
    elif choice == 3:
        base.update_soldier()
    elif choice == 4:
        base.track_soldier()
    elif choice == 5:
        base.deployment_status()
    elif choice == 6:
        print("Thanks for your services")
        break
    else:
        print("Please check whether the number is between 1 to 6.")