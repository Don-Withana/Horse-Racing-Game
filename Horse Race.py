# --------------------------------------------------------------
# | Name : Himan Withana                                       |
# | Date : 2023/12/25                                          |
# | AI & Data Science undergrad at Robert Gordon university UK |
# --------------------------------------------------------------

# Importing necessary libraries
import random
import time

# Check race start
race_start = False

# Creating an empty list to store horse details
horse_details = []

# Maximum number of horses
max_horses = 20

# Printing the introduction message with special formatting
print('=' * 27)
# Font bold and font color change
# References: https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
intro = "\033[1;31mRapid Run Horse Racing Game\033[0m\n"
for char in intro:
    print(char, end='', flush=True)
    # Time delay
    time.sleep(0.1)
print('=' * 27)

# Help messages with comments explaining each section
help1 = ("\n" + '=' * 50)
message = f"{'Welcome to Rapid Run Horse Racing Game!':^50}"
help2 = ("\n" + '=' * 50)
help3 = ("\nGame Instructions:"
         "\n   1.Add Horse Details (AHD):"
         "\n       Type AHD to add horse details."
         "\n       Follow prompts for Horse ID, Name, Jockey Name, Age, Breed, Race Record, and Group."
         "\n       Ensure Horse ID has 3 digits."
         "\n       System confirms successful addition."
         "\n"
         "\n   2.Update Horse Details (UHD):"
         "\n       Type UHD to update horse details."
         "\n       Enter Horse ID for the horse to update."
         "\n       Follow prompts to modify information."
         "\n       System confirms successful update."
         "\n"
         "\n   3.Delete Horse Details (DHD):"
         "\n       Type DHD to delete horse details."
         "\n       Enter Horse ID for the horse to delete."
         "\n       System confirms successful deletion."
         "\n"
         "\n   4.View Registered Horses (VHD):"
         "\n       Type VHD to view registered horses details."
         "\n       Details sorted by breed are displayed."
         "\n"
         "\n   5.Save Horse Details to Text File (SHD):"
         "\n       Type SHD to save horse details to a text file."
         "\n       Details categorized by group."
         "\n"
         "\n   6.Select Horses for Major Round (SDD):"
         "\n       Type SDD to simulate random draw and select horses."
         "\n       System displays randomly selected horse details for each group."
         "\n"
         "\n   7.Display Winning Horses (WHD):"
         "\n       Type WHD to display winning horses."
         "\n       Random times assigned, showing 1st, 2nd, and 3rd place winners based on race times."
         "\n"
         "\n   8.Visualize Winning Horses (VWH):"
         "\n       Type VWH to visualize time spent by winning horses."
         "\n       '*' symbols show 10-second intervals, displaying placement."
         "\n"
         "\n   9.Exit Program (ESC):"
         "\n       Type ESC to exit the game anytime."
         "\n" + '=' * 50)

# Create an empty set to store unique horse IDs
horse_id_set = set()


# Define a function for Horse ID
def id_1():
    global horse_id_set

    # Validate and get a valid horse ID with 3 digits
    while True:
        horse_id = input("\nEnter the horse ID (Must include 3 digits): ")

        # Check the entered horse ID is numeric value and exactly have 3 digits
        if horse_id.isdigit() and len(horse_id) == 3:
            if horse_id not in horse_id_set:
                horse_id_set.add(horse_id)
                break
            else:
                print("This horse ID has already been entered. Please enter a different one.")
        else:
            try:
                int(horse_id)
                print("Invalid horse ID. Must be a 3-digit number. Try again!")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    return horse_id


# Function to get a valid horse name
def name_2():
    while True:
        try:
            horse_name_input = input("Enter the horse name: ").strip()

            # Check if the entered name is not empty and contains only letters and spaces
            if horse_name_input and all(word.isalpha() or word.isspace() for word in horse_name_input.split()):
                horse_name = ' '.join(word.capitalize() for word in horse_name_input.split())

                break
            else:
                raise ValueError("Invalid horse name. Please enter a valid name with only letters and spaces.")

        except ValueError as e:
            print(e)

    return horse_name


# Function to get a valid jockey name
def jockey_name_3():
    while True:
        try:
            jockey_name_input = input("Enter the jockey name: ").strip()

            if jockey_name_input and all(word.isalpha() or word.isspace() for word in jockey_name_input.split()):
                jockey_name = ' '.join(word.capitalize() for word in jockey_name_input.split())
                break
            else:
                raise ValueError("Invalid jockey name. Please enter a valid name with only letters and spaces.")

        except ValueError as e:
            print(e)

    return jockey_name


# Validate and get a valid horse age
def age_4():
    while True:
        try:
            horse_age = input("Enter the horse age (Between 3 and 25): ")

            # Convert the entered age to an integer
            age_int = int(horse_age)

            if 3 <= age_int <= 25:
                break
            else:
                print("Invalid horse age. Must be between 3 and 25. Try again!")

        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    return horse_age

# Validate and get a valid horse speed
def speed_5():
    while True:
        horse_speed = input("Enter horse speed in km/h (Between 16 and 27): ")
        try:

            # Convert the entered speed to a floating-point number
            speed_float = float(horse_speed)

            if 16 <= speed_float <= 27:
                break
            else:
                print("Invalid horse speed. Speed must be between 16 and 27 km/h.")

        except ValueError:
            print("Invalid input. Please enter a valid numeric value for horse speed.")

    return horse_speed


# Validate and get valid horse breed
def breed_6():
    while True:
        try:
            horse_breed = input("Enter the horse breed (Include only letters): ").capitalize()

            # Check if the entered breed contains only alphabetical characters
            if horse_breed.isalpha():
                break
            else:
                raise ValueError("Invalid horse breed. Please enter a valid name with only letters.")

        except ValueError as e:
            print(e)

    return horse_breed


# Validate and get valid race records
def race_rec_7():
    while True:
        try:
            race_records_input = input("Enter the horse race records: ").strip()

            if race_records_input and len(race_records_input) <= 25:
                race_records = race_records_input.title()
                break
            else:
                raise ValueError("Invalid race records. Please enter up to 25 characters.")

        except ValueError as e:
            print(e)

    return race_records


# Validate and get valid group
def group_8():
    while True:
        try:
            horse_group = input("Enter the horse group (A, B, C, D): ").upper()

            if horse_group not in ('A', 'B', 'C', 'D'):
                raise ValueError("Invalid horse group. Please enter A, B, C, or D.")

            # Check the limit only if the horse group is valid
            if sum(1 for horse in horse_details if horse['Horse Group'] == horse_group) >= 5:
                # Raise a ValueError if the group limit is reached
                raise ValueError(f"Maximum limit (5 horses) reached for group {horse_group}. Try a different group.")

            # If the horse group is valid and within the limit, break out of the loop
            break

        except ValueError as e:
            print(e)

    return horse_group


def add_horse_details():
    # Check if the race has already started
    if race_start:
        print("Cannot add details, Already race has been started")
        return

    global horse_details

    # Check if the maximum number of horses has been reached
    if len(horse_details) >= max_horses:
        print("\nMaximum number of horses reached (20 horses).")
        print("If you wish to add or modify data, "
              "\nPlease consider deleting data using the 'DHD' command or updating data using the 'UHD' command.")
        return

    print("=" * 50)
    print(f"{'Add Horse Details':^50}")
    print("=" * 50)

    horse_id = id_1()

    horse_name = name_2()

    jockey_name = jockey_name_3()

    horse_age = age_4()

    horse_speed = speed_5()

    horse_breed = breed_6()

    race_records = race_rec_7()

    horse_group = group_8()

    # Adding horse details to the list
    horse_details.append({
        "Horse ID": horse_id,
        "Horse Name": horse_name,
        "Jockey Name": jockey_name,
        "Horse Age": horse_age,
        "Horse Speed": horse_speed,
        "Horse Breed": horse_breed,
        "Horse Race Records": race_records,
        "Horse Group": horse_group
    })

    print("\nHorse details added successfully!")
    print(f"Total horses entered: {len(horse_details)}")


# Function to update horse details
def update_horse_details():
    if race_start:
        print("Cannot update details, Already race has been started")
        return

    try:
        print("=" * 50)
        print(f"{'Update Horse Details':^50}")
        print("=" * 50)

        horse_id = input("Enter Horse ID to update: ")

        for horse in horse_details:

            if horse["Horse ID"] == horse_id:
                print("1. Update Horse Name")
                print("2. Update Jockey Name")
                print("3. Update Age")
                print("4. Update Speed")
                print("5. Update Breed")
                print("6. Update Race Record")
                print("7. Update Group")
                choice1 = input("Select an option (1-7): ")

                # Check if the user's choice is valid
                if choice1 not in ['1', '2', '3', '4', '5', '6', '7']:
                    print("Invalid choice. Back to Horse racing management system.")

                    return

                if choice1 == '1':

                    horse['Horse Name'] = name_2()

                elif choice1 == '2':

                    horse['Jockey Name'] = jockey_name_3()

                elif choice1 == '3':

                    horse['Horse Age'] = age_4()

                elif choice1 == '4':

                    horse['Horse Speed'] = speed_5()

                elif choice1 == '5':

                    horse['Horse Breed'] = breed_6()

                elif choice1 == '6':

                    horse['Horse Race Records'] = race_rec_7()

                elif choice1 == '7':

                    horse['Horse Group'] = group_8()

                print("Horse details updated successfully.")

                return

        print("Horse ID not found. Please enter a valid Horse ID.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Function to delete horse details
def delete_horse_details():
    if race_start:
        print("Cannot delete details, Already race has been started")
        return

    try:
        print("=" * 50)
        print(f"{'Delete Horse Details':^50}")
        print("=" * 50)

        horse_id = input("Enter Horse ID to delete: ")

        for horse in horse_details:
            if horse["Horse ID"] == horse_id:
                horse_details.remove(horse)
                horse_id_set.remove(horse_id)
                print("Horse details deleted successfully.")

                return

        print("Horse ID not found. Please enter a valid Horse ID.")

    except Exception as e:
        print(f"An error occurred: {e}")


# Function to sort horse details
def sort_horse_details_by_id(horses):
    n = len(horses)
    for i in range(n):

        for j in range(0, n - i - 1):

            if horses[j]['Horse ID'] > horses[j + 1]['Horse ID']:
                # Swap the positions of horses if they are out of order
                horses[j], horses[j + 1] = horses[j + 1], horses[j]


# Function to view horse details
def view_horse_details():
    print("=" * 50)
    print(f"{'Display Horse Details':^50}")
    print("=" * 50)

    # Check if there are horse details to display
    if not horse_details:
        print("No horse details to display.")
        return

    # Use the custom sorting function to sort horse details by 'Horse ID'
    sort_horse_details_by_id(horse_details)

    for horse in horse_details:
        print(f"ID: {horse['Horse ID']}, Name: {horse['Horse Name']}, "
              f"Breed: {horse['Horse Breed']}, Age: {horse['Horse Age']}, "
              f"Speed: {horse['Horse Speed']}, Jockey Name: {horse['Jockey Name']}, "
              f"Race Records: {horse['Horse Race Records']}, Group: {horse['Horse Group']}")


# Function to save horse details to a text file
def save_horse_details_to_file():
    print("=" * 50)
    print(f"{'Save Horse Details':^50}")
    print("=" * 50)

    try:
        # Open the file in write mode
        with open("horse_details.txt", "w") as file:
            # Write horse details to the file from horse details
            for horse in horse_details:
                file.write(f"{horse['Horse ID']},{horse['Horse Name']},{horse['Jockey Name']},"
                           f"{horse['Horse Age']},{horse['Horse Speed']},{horse['Horse Breed']},"
                           f"{horse['Horse Race Records']},{horse['Horse Group']}\n")
        print("Horse details saved to file successfully.")
    except Exception as e:
        print(f"An error occurred while saving horse details: {e}")


# Function to load horse details from a file
def load_horse_details_from_file():
    # Prints character by character with a slight delay to create a visual effect.
    load = "loading...\n"
    for char4 in load:
        print(char4, end='', flush=True)
        time.sleep(0.1)

    # Create list for store loaded horse details
    loaded_horses = []

    try:
        # Open the file in read mode
        with open("horse_details.txt", "r") as file:
            for line in file:
                # Split the line into details using commas as separators
                details = line.strip().split(',')
                loaded_horses.append({
                    "Horse ID": details[0],
                    "Horse Name": details[1],
                    "Jockey Name": details[2],
                    "Horse Age": details[3],
                    "Horse Speed": details[4],
                    "Horse Breed": details[5],
                    "Horse Race Records": details[6],
                    "Horse Group": details[7]
                })
        print("Horse details loaded successfully.")
    except FileNotFoundError:
        print("No previous horse details found.")
    except Exception as e:
        print(f"An error occurred while loading horse details: {e}")

    return loaded_horses


# Function to select horses for a major round
def select_horses_for_major_round():
    # Set the race_start flag to True
    global race_start
    race_start = True

    global horse_details
    global selected_horses

    # Creating list for store selected horses
    selected_horses = []

    print("=" * 50)
    print(f"{'Select Horses for Major Round':^50}")
    print("=" * 50)

    # Clear the horse_details list before appending loaded horses
    horse_details.clear()

    # Load horse details from the file and update the horse_details list
    loaded_horses = load_horse_details_from_file()
    horse_details.extend(loaded_horses)

    # Selecting one horse from each group (A, B, C, D)
    for group in ('A', 'B', 'C', 'D'):
        group_horses = [horse for horse in horse_details if horse.get('Horse Group') == group]

        if group_horses:
            selected_horse = random.choice(group_horses)
            selected_horses.append(selected_horse)

    # Print selected horses
    print("\nSelected horses for the major round:")
    for horse in selected_horses:
        print(f"ID: {horse['Horse ID']}, Name: {horse['Horse Name']}, "
              f"Breed: {horse['Horse Breed']}, Age: {horse['Horse Age']}, "
              f"Speed: {horse['Horse Speed']}, Jockey Name: {horse['Jockey Name']}, "
              f"Race Records: {horse['Horse Race Records']}, Group: {horse['Horse Group']}")

    return selected_horses


# Function to sort horses by 'Race Time'
def sort_horses_by_race_time(selected_horses):
    n = len(selected_horses)
    for i in range(n):
        for j in range(0, n - i - 1):
            if selected_horses[j]['Race Time'] > selected_horses[j + 1]['Race Time']:
                selected_horses[j], selected_horses[j + 1] = selected_horses[j + 1], selected_horses[j]


# Function to display winning horses
def display_winning_horses(selected_horses):
    global winning_horses

    print("=" * 50)
    print(f"{'Display Winning Horses':^50}")
    print("=" * 50)

    if not selected_horses:
        print("No selected horses to display.")
        return []

    # Assign random times for the final round
    for horse in selected_horses:
        horse['Race Time'] = random.randint(10, 90)

    # Sort horses based on race time using the custom function
    sort_horses_by_race_time(selected_horses)

    # Display winning horses
    print("\nWinning Horses:")
    winning_horses = selected_horses[:3]
    for position, horse in enumerate(winning_horses, start=1):
        place_suffix = "st" if position == 1 else "nd" if position == 2 else "rd"
        print(f"{position}{place_suffix} Place: {horse['Horse Name']}")

    return winning_horses


# List to store the stars for visualization
stars = []


# Function to visualize time of winning horses
def visualize_time_of_winning_horses(winning_horses):
    global race_start
    race_start = False
    global stars

    print("=" * 50)
    print(f"{'Visualize Time of Winning Horses':^50}")
    print("=" * 50)

    if not winning_horses:
        print("No winning horses to visualize.")
        return

    # Calculate the maximum race time based on assigned random times
    max_time = max(horse['Race Time'] for horse in winning_horses)

    if max_time == 0:
        print("Error: Maximum race time is zero.")
        return

    print("\nVisualizing Time of Winning Horses:")

    # Sorting based on race time
    n = len(winning_horses)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if winning_horses[j]['Race Time'] > winning_horses[j + 1]['Race Time']:
                winning_horses[j], winning_horses[j + 1] = winning_horses[j + 1], winning_horses[j]

    for position, horse in enumerate(winning_horses[:3], start=1):
        time.sleep(1)

        # Calculate the percentage of race completion
        completion_percentage = (horse['Race Time'] / max_time) * 100
        num_stars = int(completion_percentage / 10)
        stars = '*' * num_stars

        # Add constant spaces for formatting
        space_count = 8 - len(horse['Horse Name'])
        spaces = ' ' * space_count

        # Print one '*' for every 10 seconds
        star_count = int(horse['Race Time'] / 10)
        time_stars = '*' * star_count

        place_suffix = "st" if position == 1 else "nd" if position == 2 else "rd"
        print(f"{horse['Horse Name']}:{spaces}{time_stars} {horse['Race Time']:.2f}s ({position}{place_suffix} Place)")

    print("\nVisualization complete.")


# Function to print the instructions
def support():
    print(help1)

    for char1 in message:
        print(char1, end='', flush=True)
        time.sleep(0.05)

    print(help2)
    print(help3)


# Function to ask the player wants instructions
def user_wants_help_message():
    print("=" * 50)
    print(f"{'Support':^50}")
    print("=" * 50)

    while True:
        yes_or_no = input("Do you want to see instructions on how to play game? (Type 'Yes' or 'No'): ")

        if yes_or_no == 'yes' or yes_or_no == 'Yes':
            support()
            break
        elif yes_or_no == 'no' or yes_or_no == 'No':
            break
        else:
            print("Error: must type 'Yes' or 'No'")


# Global variable to store winning horses
winning_horses = []


# Main program loop
def main():
    global winning_horses
    while True:
        print("=" * 50)
        print(f"{'Horse Racing Management System':^50}")
        print("=" * 50)

        # Print the main menu
        print("1. Type HELP or 1 for instructions.")
        print("2. Type AHD or 2 for adding horse details.")
        print("3. Type UHD or 3 for updating horse details.")
        print("4. Type DHD or 4 for deleting horse details.")
        print("5. Type VHD or 5 for viewing the registered horse details table.")
        print("6. Type SHD or 6 for saving the horse details to the text file.")
        print("7. Type SDD or 7 for selecting four horses randomly for the major round.")
        print("8. Type WHD or 8 for displaying the Winning horses.")
        print("9. Type VWH or 9 for Visualizing the time of the winning horses.")
        print("10. Type ESC or 0 to exit the program.\n")

        choice = input("Enter your choice: ").upper()

        if choice == 'HELP' or choice == '1':
            user_wants_help_message()
            continue

        if choice == 'AHD' or choice == '2':
            while True:
                add_horse_details()

                # Ask the user if they want to add another horse
                add_another = input("\nDo you want to add another horse? (yes/no): ").lower()
                if add_another != 'yes':
                    break
            print("Returning to the main menu.")

        elif choice == 'UHD' or choice == '3':

            update_horse_details()

        elif choice == 'DHD' or choice == '4':

            delete_horse_details()

        elif choice == 'VHD' or choice == '5':

            view_horse_details()

        elif choice == 'SHD' or choice == '6':

            save_horse_details_to_file()

        elif choice == 'SDD' or choice == '7':

            select_horses_for_major_round()

        elif choice == 'WHD' or choice == '8':

            try:
                if not selected_horses:
                    print("Please select horses for the major round first.")

                else:
                    winning_horses = display_winning_horses(selected_horses)

            except NameError:
                print("Error: There are no selected horses.Did you select horses for the major round?\n")

        elif choice == 'VWH' or choice == '9':

            try:
                if not selected_horses:
                    print("Please select horses for the major round first.")

                else:
                    visualize_time_of_winning_horses(winning_horses)

            except NameError:
                print("Error: There are no selected horses.Did you select horses for the major round?\n")

        elif choice == 'ESC' or choice == '0':

            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


# Reference = https://profile.w3schools.com/
if __name__ == "__main__":
    main()
