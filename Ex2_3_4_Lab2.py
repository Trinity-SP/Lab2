# Trinity Chong (DCPE/FT/2A/04)
# Exercise 2/3/4 - Lab 2

# Show main menu page
def display_main_menu(): 
    print("display_main_menu function") 
    print("This is the main menu")

# Get user inputs of temperature values
def get_user_input():
    print("get_user_input function")
    print("Enter min, then max temperature values, do separate them by commas (e.g. 5, 67, 32)")
    user_input = input()
    # Codes I tried but did not seem to work??
    #print("You have entered" + num_list)
    #num_list = num_list.split(",")
    #print(num_list)
    num_list = [int(num) for num in user_input.split(",")]
    return num_list

# Calculate the average of the temperature values
def calc_average_tempeature(num_list): 
   print("calc_average function")
   avg = sum(num_list)/len(num_list)
   print("The calculated average is " , avg)
   return avg

def calc_min_max_temperature(num_list):
    print("calc_min_max_temperature function")
    min_temp = min(num_list)
    max_temp = max(num_list)
    return min_temp, max_temp

# Start to run program from main function
def main(): 
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python") 
    display_main_menu() 
    num_list = get_user_input()

    # Call calculate average temperature function
    num_list = calc_average_tempeature(num_list)

    # Call min and max function
    min_temp, max_temp = calc_min_max_temperature(num_list)

    # Display min and max temperature values
    print("The minimum temperature is " + str(min_temp) + "degrees")
    print("The maximum temperature is " + str(max_temp) + "degrees")

# Calling the main function
if __name__ == "__main__": 
    main()