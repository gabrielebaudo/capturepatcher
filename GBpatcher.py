import csv, os

def check_fields(fieldnames):
    if 'Fixture' not in fieldnames:
        print("\n'Fixture' field not found in CSV file.")
        return 1
    if 'Patch' not in fieldnames:
        print("\n'Patch' field not found in CSV file.")
        return 1
    if 'DMX Channels' not in fieldnames:
        print("\n'DMX Channels' field not found in CSV file.")
        return 1
    if 'Circuit' not in fieldnames:
        print("\n'Circuit' field not found in CSV file.")
        return 1
    if 'Note' not in fieldnames:
        print("\n'Note' field not found in CSV file.")
        return 1

def list_fixturetypes(reader, custom_names):
    fixture_dict = {}
    
    for row in reader:
        fixture_name = row[custom_names]
        if fixture_name not in fixture_dict:
            fixture_dict[fixture_name] = []
        
        fixture_dict[fixture_name].append(row)

    if fixture_dict:
        print("\nFixture types found: ")
        for fixture_name, rows in fixture_dict.items():
            print(f"{fixture_name} ({len(rows)})")
    else:
        print("No fixture found in the file")
    
    return fixture_dict

def patch_by_name(file_csv, output_file, field, custom_names):
    # Apri il file CSV in modalità lettura e crea un writer per scrivere i dati modificati
    with open(file_csv, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        fieldnames = reader.fieldnames

        if check_fields(reader.fieldnames):
            return
        
        fixture_dict = list_fixturetypes(reader, custom_names)

        csv_file.seek(0)
        next(reader)

        # Chiedi all'utente il nome della fixture
        while True:
            desidered_fixture = input("\nInsert desidered fixture name [check for capital letters]: ")

            if desidered_fixture in fixture_dict:
                break
            else:
                print("This fixture does not exsist, retry!")

        # Chiedi all'utente l'universo e il canale di partenza
        print()
        universe = int(input("Start Universe: "))
        channel = int(input("Start Channel: "))

        # Apri il file in modalità scrittura e scrivi i dati
        with open(f"{output_file}", 'w', newline='') as output_file:
            writer = csv.DictWriter(output_file, fieldnames=fieldnames)
            writer.writeheader()

            i = 0
            tot = 0
            used_channels = 0

            for row in reader:
                tot += 1
                fixture_name = row[custom_names]
                if fixture_name == desidered_fixture:
                    i += 1
                    dmx_channels = int(row['DMX Channels'])
                    if used_channels + dmx_channels > 512:
                        universe += 1
                        channel = 1
                        used_channels = 0

                    row[field] = f"{universe}.{channel}"
                    channel += dmx_channels
                    used_channels += dmx_channels

                writer.writerow(row)

    print()
    print(str(i) + " rows affected")
    print(str(tot - i) + " rows copied")
    print("Last address: " + str(universe) + "." + str(channel - dmx_channels))
    print("--------------------")

def patch_entire_file(file_csv, output_file, field, custom_names):
    # Apri il file CSV in modalità lettura e crea un writer per scrivere i dati modificati
    with open(file_csv, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        fieldnames = reader.fieldnames

        if check_fields(reader.fieldnames):
            return
        
        fixture_dict = list_fixturetypes(reader, custom_names)

        csv_file.seek(0)
        next(reader)
    
        print()
        universe = int(input("Start Universe: "))
        channel = int(input("Start Channel: "))

    # Apri il file in modalità scrittura e scrivi i dati
    with open(f"{output_file}", 'w', newline='') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()

        i = 0
        used_channels = 0
        
        for fixture_name, rows in fixture_dict.items():
            for row in rows:
                i += 1

                dmx_channels = int(row['DMX Channels'])
                if used_channels + dmx_channels > 512:
                    universe += 1
                    channel = 1
                    used_channels = 0

                row[field] = f"{universe}.{channel}"
                channel += dmx_channels
                used_channels += dmx_channels

                writer.writerow(row)
    print()
    print(str(i) + " rows affected")
    print("Last address: " + str(universe) + "." + str(channel - dmx_channels))
    print("--------------------")

def copy_circuit(file_csv, output_file, custom_names):
    # Apri il file CSV in modalità lettura e crea un writer per scrivere i dati modificati
    with open(file_csv, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        fieldnames = reader.fieldnames

        if check_fields(reader.fieldnames):
            return
        
        fixture_dict = list_fixturetypes(reader, custom_names)

        csv_file.seek(0)
        next(reader)
    
    # Apri il file in modalità scrittura e scrivi i dati
    with open(f"{output_file}", 'w', newline='') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()

        i = 0
        
        for fixture_name, rows in fixture_dict.items():
            for row in rows:
                i += 1

                circuit_value = row['Circuit']

                if circuit_value:
                    row['Patch'] = f"{circuit_value}"

                writer.writerow(row)
    print()
    print(str(i) + " rows affected")
    print("--------------------")

def clear_field(file_csv, output_file, field, custom_names):
    # Apri il file CSV in modalità lettura e crea un writer per scrivere i dati modificati
    with open(file_csv, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        fieldnames = reader.fieldnames

        if check_fields(reader.fieldnames):
            return
        
        fixture_dict = list_fixturetypes(reader, custom_names)

        csv_file.seek(0)
        next(reader)
    
    # Apri il file in modalità scrittura e scrivi i dati
    with open(f"{output_file}", 'w', newline='') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()

        i = 0
        
        for fixture_name, rows in fixture_dict.items():
            for row in rows:
                i += 1

                row[field] = f""

                writer.writerow(row)
    print()
    print(str(i) + " rows affected")
    print("--------------------")
  
#START DEL PROGRAMMA
# Esegui la funzione con il nome del file CSV come argomento
times = 0
print("--------------------------------------")
print("Capture Patcher Tool by Gabriele Baudo")
print("--------------------------------------")
print()
file_name = input("Insert the name of the file to be processed (with .csv): ")

if not os.path.exists(file_name):
    print("File not found into this folder, closing script...")
    exit()

output_file = input("Insert desidered output file name (with .csv): ")

while True:
    times += 1
    custom_names = "Fixture"

    if times > 1: #Se lo script esegue più volte modifichiamo il file nuovo, non quello originale
        file_name = output_file

    print()
    print("1. Patch by Fixture name [EDIT PATCH FIELD]")
    print("2. Patch by Fixture name [EDIT CIRCUIT FIELD]")
    print("3. Patch entire file [EDIT PATCH FIELD]")
    print("4. Patch entire file [EDIT CIRCUIT FIELD]")
    print("5. Copy Circuit field to Patch field")
    print("6. Clear all Patch fields")
    print("7. Clear all Circuit fields")
    print("8. Exit")
    n = int(input("Choose an option: "))

    if n == 8:
        exit()
    elif n == 3:
        patch_entire_file(file_name, output_file, "Patch", custom_names)
    elif n == 4:
        patch_entire_file(file_name, output_file, "Circuit", custom_names)
    elif n == 5:
        copy_circuit(file_name, output_file, custom_names)
    elif n == 6:
        clear_field(file_name, output_file, "Patch", custom_names)
    elif n == 7:
        clear_field(file_name, output_file, "Circuit", custom_names)
    else: 
        if times <= 1:
            tick = input("Do you want to use custom names? [Y/N]: ").upper()
            if tick == 'Y':
                custom_names = "Note" 

        if n == 1:
            patch_by_name(file_name, output_file, "Patch", custom_names)
        elif n == 2:
            patch_by_name(file_name, output_file, "Circuit", custom_names)
        else:
            print("\n-- There is no option for this number! --")