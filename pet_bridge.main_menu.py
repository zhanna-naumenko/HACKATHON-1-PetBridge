import psycopg2
from pet_bridge_Fosters import Fosters
from pet_bridge_Pets import Pets
from pet_bridge_care import Care

conn = psycopg2.connect(database="PetBridge", user='postgres', password='jannetj0388', host='localhost', port='5432')
conn.autocommit = True
cursor = conn.cursor()

print("Welcome to the PetBridge Menu!")

add_new_foster = 'AF'
add_new_pet = 'AP'
update_foster = 'UF'
update_pet = 'UP'
delete_foster = 'DF'
delete_pet = 'DP'
find_free_foster = "FFF"
find_pet = "FP"
add_care = "AC"
find_care = "FC"
exit = "E"


def show_user_menu():
    print(f"To add new foster information please type: {add_new_foster}")
    print(f"To add new pet's information please type: {add_new_pet}")
    print(f"To update foster information please type: {update_foster}")
    print(f"To update pet's information please type: {update_pet}")
    print(f"To delete foster information please type: {delete_foster}")
    print(f"To delete pet's information please type: {delete_pet}")
    print(f"To find foster with free status type: {find_free_foster}")
    print(f"To find pets that need foster care type: {find_pet}")
    print(f"To add new care information type: {add_care}")
    print(f"To find care information type: {find_care}")
    print(f"To exit type: {exit}")

def main():
    while True:
        show_user_menu()
        choice = input("Enter your choice: ").upper()
        foster = Fosters()
        pet = Pets()
        care = Care()
        if choice == "AF":
            foster.add_foster()
        elif choice == "AP":
            pet.add_pet()
        elif choice == "UF":
            foster.update_foster()
        elif choice == "UP":
            pet.update_pet()
        elif choice == "DF":
            foster.delete_foster()
        elif choice == "DP":
            pet.delete_pet()
        elif choice == "FFF":
            foster.find_free_foster()
        elif choice == "FP":
            pet.find_pet()
        elif choice == "AC":
            care.add_new_care()
        elif choice == "FC":
            care.find_care()
        elif choice == "E":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()