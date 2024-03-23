import psycopg2

conn = psycopg2.connect(database="PetBridge", user='postgres', password='jannetj0388', host='localhost', port='5432')
conn.autocommit = True
cursor = conn.cursor()

class Fosters:

    def add_foster(self):
        '''Asks to enter the data you want to add about foster to the database'''
        user_first_name = (input("Please enter foster first name: ")).upper()
        user_last_name = (input("Please enter foster last name: ")).upper()
        user_status = (input("Please enter foster status (ONLY FREE or BUSY): ")).upper()
        user_address = (input("Please enter foster address: ")).upper()
        user_preference = (input("Please enter preferred pet (ONLY CAT, DOG or CAT/DOG): ")).upper()
        user_tel = input("Please enter foster telephone number: ")
        user_start_period = input("Please enter from what date foster can provide care (it should be in format YYYY-MM-DD): ")
        user_end_period = input("Please enter till what date foster can provide care (it should be in format YYYY-MM-DD): ")
        query = '''INSERT INTO fosters (first_name, last_name, foster_status, 
        foster_address, pet_preference, foster_tel, start_period, end_period) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''
        val = (user_first_name, user_last_name, user_status, user_address, user_preference, user_tel, user_start_period, user_end_period)
        cursor.execute(query, val)
        conn.commit()
        conn.close()


    def update_foster(self):
        '''Asks for the first name, last name whose data needs to be changed,
        asks to select a category of data to change and asks to enter new data.
        Updates data in the database according to these parameters.'''
        user_name = (input("Please enter foster first name: ")).upper()
        user_surname = (input("Please enter foster last name: ")).upper()
        column_change = int(input('''Please choose what information you want to change.
        To change First Name: 0
        To change Last Name: 1
        To change Status: 2
        To change Address: 3
        To change Pet Preference: 4
        To change Telephone: 5
        To change start of the period: 6
        To change end of the period: 7
        Please make your choice: '''))
        items_list = ['first_name', 'last_name', 'foster_status', 'foster_address', 'pet_preference', 'foster_tel',
                      'start_period', 'end_period']
        new_value = (input("Please enter new information: ")).upper()
        cursor.execute(f"SELECT foster_id FROM fosters WHERE first_name = '{user_name}' AND last_name = '{user_surname}'")
        id_foster = cursor.fetchall()
        id_foster = ''.join(str(item) for item in id_foster)
        id_foster = id_foster[1]
        cursor.execute(f"UPDATE fosters SET {items_list[column_change]} = '{new_value}' WHERE foster_id = '{id_foster}'")
        conn.commit()
        cursor.close()
        conn.close()

    def delete_foster(self):
        '''Searches for the serial number in the database
        using the passed parameters: first and last name,
        and deletes all information from the database'''
        user_name = (input("Please enter foster first name you want to delete: ")).upper()
        user_surname = (input("Please enter foster last name you want to delete: ")).upper()
        cursor.execute(f"SELECT foster_id FROM fosters WHERE first_name = '{user_name}' AND last_name = '{user_surname}'")
        id_foster = cursor.fetchall()
        id_foster = ''.join(str(item) for item in id_foster)
        id_foster = id_foster[1]
        query = f"DELETE FROM fosters WHERE foster_id = '{id_foster}'"
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()

    def find_free_foster(self):
        '''Finds a foster with FREE status with preferable animal type'''
        pref_pet = (input("Please enter preferable pet type (CAT, DOG or CAT/DOG): ")).upper()
        cursor.execute(f"SELECT * FROM fosters WHERE foster_status = 'FREE' AND pet_preference = '{pref_pet}'")
        rows = cursor.fetchall()
        if rows:
            print("Found free fosters with preferable animal type:")
            for row in rows:
                foster_id, first_name, last_name, foster_status, foster_address, pet_preference, foster_tel, start_period, end_period = row
                string_inf = f"id: {foster_id}, Name: {first_name}, Surname: {last_name}, " \
                             f"Status: {foster_status}, Address: {foster_address}, " \
                             f"Pet Type: {pet_preference}, Phone number: {foster_tel}, From: {start_period}, Till: {end_period}"
                print(string_inf)
        else:
            print("No free fosters found with preferable animal type.")
        conn.commit()
        conn.close()

if __name__ == '__main__':
    foster3 = Fosters()
    # foster3.add_foster()
    # foster3.update_foster()
    # foster3.delete_foster()
    foster3.find_free_foster()
