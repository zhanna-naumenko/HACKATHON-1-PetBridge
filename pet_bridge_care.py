import psycopg2

conn = psycopg2.connect(database="PetBridge", user='postgres', password='jannetj0388', host='localhost', port='5432')
conn.autocommit = True
cursor = conn.cursor()

class Care:

    def add_new_care(self):

        pet_name = (input("Please enter pet's name: ")).upper()
        pet_breed = (input("Please enter the breed of the pet: ")).upper()
        cursor.execute(f"SELECT pet_id FROM pets WHERE pet_name = '{pet_name}' AND breed = '{pet_breed}'")
        id_pet = cursor.fetchall()
        id_pet = ''.join(str(item) for item in id_pet)
        id_pet = id_pet[1]
        user_name = (input("Please enter foster first name: ")).upper()
        user_surname = (input("Please enter foster last name: ")).upper()
        cursor.execute(f"SELECT foster_id FROM fosters WHERE first_name = '{user_name}' AND last_name = '{user_surname}'")
        id_foster = cursor.fetchall()
        id_foster = ''.join(str(item) for item in id_foster)
        id_foster = id_foster[1]

        start_date = input("Please enter start of the period: ")
        end_date = input("Please enter end of the period: ")
        query = '''INSERT INTO care (pet_id, foster_id, start_period, end_period) 
              VALUES (%s, %s, %s, %s)'''
        val = (id_pet, id_foster, start_date, end_date)
        cursor.execute(query, val)
        cursor.execute(f"UPDATE pets SET pet_status = 'FOSTER CARE', start_period = '{start_date}', end_period = '{end_date}' WHERE pet_id = '{id_pet}'")
        cursor.execute(f"UPDATE fosters SET foster_status = 'BUSY', start_period = '{start_date}', end_period = '{end_date}' WHERE foster_id = '{id_foster}'")
        conn.commit()
        conn.close()

    def find_care(self):
        user_name = (input("Please enter foster first name: ")).upper()
        user_surname = (input("Please enter foster last name: ")).upper()
        cursor.execute(f"SELECT care.care_id, fosters.first_name, fosters.last_name, fosters.foster_address, "
                       f"fosters.foster_tel, pets.pet_name, fosters.start_period, fosters.end_period "
                       f"FROM fosters INNER JOIN care ON fosters.foster_id = care.foster_id "
                       f"INNER JOIN pets ON pets.pet_id = care.pet_id "
                       f"WHERE fosters.first_name = '{user_name}' AND fosters.last_name = '{user_surname}'")
        rows = cursor.fetchall()
        if rows:
            print("Found foster care:")
            for row in rows:
                care_id, first_name, last_name, foster_address, foster_tel, pet_name, start_period, end_period = row
                string_inf = f"Care Number: {care_id}, Name: {first_name}, Surname: {last_name}, Address: {foster_address}, " \
                             f"Contact number: {foster_tel}, Pet's Name: {pet_name}, " \
                             f"From: {start_period}, Till: {end_period}"
                print(string_inf)
        else:
            print("No free fosters found with preferable animal type.")
        conn.commit()
        conn.close()

    def delete_care(self):
        '''Deletes all information from the database'''
        care_id = input("Please enter care id number: ")
        query = f"DELETE FROM care WHERE care_id = '{care_id}'"
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()

if __name__ == '__main__':
    pet_care = Care()
    # pet_care.add_new_care()
    # pet_care.find_care()
    # pet_care.delete_care()