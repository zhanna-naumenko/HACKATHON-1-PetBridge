import psycopg2

conn = psycopg2.connect(database="PetBridge", user='postgres', password='jannetj0388', host='localhost', port='5432')
conn.autocommit = True
cursor = conn.cursor()

class Pets:


    def add_pet(self):

      pet_type = (input("Please enter is it CAT or DOG: ")).upper()
      pet_name = (input("Please enter pet's name: ")).upper()
      breed = (input("Please enter pet's breed:")).upper()
      pet_status = (input("Please enter pet's status (in the shelter, need foster care): ")).upper()
      address = (input("Please enter the address: ")).upper()
      contact_phone = input("Please enter phone number: ")
      start_date = input("Please enter start of the period: ")
      end_date = input("Please enter end of the period: ")
      query = '''INSERT INTO pets (pet_type, pet_name, breed, 
              pet_status, shelter_address, shelter_tel, start_period, end_period) 
              VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''
      val = (pet_type, pet_name, breed, pet_status, address, contact_phone, start_date,
             end_date)
      cursor.execute(query, val)
      conn.commit()
      conn.close()

    def update_pet(self):
        '''Asks for the name and breed whose data needs to be changed,
        asks to select a category of data to change and asks to enter new data.
        Updates data in the database according to these parameters.'''
        pet_name = (input("Please enter pet's name: ")).upper()
        pet_breed = (input("Please enter the breed of the pet: ")).upper()
        column_change = int(input('''Please choose what information you want to change.
        To change Pet Type: 0
        To change Pet Name: 1
        To change Breed: 2
        To change Pet Status: 3
        To change Address: 4
        To change Telephone: 5
        To change start of the period: 6
        To change end of the period: 7
        Please make your choice: '''))
        items_list = ['pet_type', 'pet_name', 'breed', 'pet_status', 'shelter_address', 'shelter_tel',
                      'start_period', 'end_period']
        new_value = (input("Please enter new information: ")).upper()
        cursor.execute(f"SELECT pet_id FROM pets WHERE pet_name = '{pet_name}' AND breed = '{pet_breed}'")
        id_pet = cursor.fetchall()
        id_pet = ''.join(str(item) for item in id_pet)
        id_pet = id_pet[1]
        cursor.execute(f"UPDATE pets SET {items_list[column_change]} = '{new_value}' WHERE pet_id = '{id_pet}'")
        conn.commit()
        cursor.close()
        conn.close()

    def delete_pet(self):
        '''Searches for the serial number in the database
        using the passed parameters: name and breed,
        and deletes all information from the database'''
        pet_name = (input("Please enter pet's name: ")).upper()
        pet_breed = (input("Please enter the breed of the pet: ")).upper()
        cursor.execute(f"SELECT pet_id FROM pets WHERE pet_name = '{pet_name}' AND breed = '{pet_breed}'")
        id_pet = cursor.fetchall()
        id_pet = ''.join(str(item) for item in id_pet)
        id_pet = id_pet[1]
        query = f"DELETE FROM pets WHERE pet_id = '{id_pet}'"
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()

    def find_pet(self):
        '''Finds a pet who needs a foster care'''
        pets_type = (input("Please enter pet type (CAT or DOG): ")).upper()
        cursor.execute(f"SELECT * FROM pets WHERE pet_status = 'NEED FOSTER CARE' AND pet_type = '{pets_type}'")
        rows = cursor.fetchall()
        if rows:
            print("Found pets who needs a foster care:")
            for row in rows:
                pet_id, pet_type, pet_name, breed, pet_status, shelter_address, shelter_tel, start_period, end_period = row
                string_inf = f"id: {pet_id}, Pet Type: {pet_type}, Pet's Name: {pet_name}, " \
                             f"Breed: {breed}, Status: {pet_status}, Address: {shelter_address}, " \
                             f"Contact number: {shelter_tel}, From: {start_period}, Till: {end_period}"
                print(string_inf)
        else:
            print("No pets found that need foster care.")
        conn.commit()
        conn.close()



if __name__ == '__main__':
    pet1 = Pets()
    # pet1.add_pet()
    # pet1.update_pet()
    # pet1.delete_pet()
    pet1.find_pet()