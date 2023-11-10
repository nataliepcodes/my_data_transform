def main():
    string = "Gender,FirstName,LastName,UserName,Email,Age,City,Device,Coffee Quantity,Order At\nMale,Carl,Wilderman,carl,wilderman_carl@yahoo.com,29,Seattle,Safari iPhone,2,2020-03-06 16:37:56\nMale,Marvin,Lind,marvin,marvin_lind@hotmail.com,77,Detroit,Chrome Android,2,2020-03-02 13:55:51\nFemale,Shanelle,Marquardt,shanelle,marquardt.shanelle@hotmail.com,21,Las Vegas,Chrome,1,2020-03-05 17:53:05\nFemale,Lavonne,Romaguera,lavonne,romaguera.lavonne@yahoo.com,81,Seattle,Chrome,2,2020-03-04 10:33:53\nMale,Derick,McLaughlin,derick,mclaughlin.derick@hotmail.com,47,Chicago,Chrome Android,1,2020-03-05 15:19:48\n"
    result = my_data_transform(string)
    transform_age(result)
    transform_email(result)
    transform_time(result)
    # Note: the output is 'string in List', NOT 'the string in list - in list'
    new_list = transform_list(result)
    print(new_list)
    

# Function to transform the nested lists of strings into one list of strings [['Gender', 'FirstName']] => ['Gender, FirstName']
def transform_list(list):
    new_list = []
    for i in range(len(list)):
        value = list[i]
        new_list.append(','.join(value))
    return new_list


# Function to transform time from this format => '2020-03-04 10:33:53' to this format => "morning"
def transform_time(list):
    for i in range(1, len(list)):
        list[i][9] = list[i][9].split(' ')[1]
        list[i][9] = list[i][9].split(':')[0]
        if int(list[i][9]) < 12:
            list[i][9] = "morning"
        elif int(list[i][9]) < 18:
            list[i][9] = "afternoon"
        elif int(list[i][9]) < 24:
            list[i][9] = "evening"
    return list

# Function to transform email from this format => 'wilderman_carl@yahoo.com' to this format => 'yahoo.com'
def transform_email(list):
    for i in range(1, len(list)):
        # print the 4th column from each row, starting from row 1 because the row 0 is the header row - print(list[i][4])
        list[i][4] = list[i][4].split('@')[1]
    return list


# Function to transform the age from this format => '29' to this format => [21->40]
def transform_age(list):
    for i in range(1, len(list)):
        # print the 5th column from each row, starting from row 1 because the row 0 is the header row - print(list[i][5]) #5th column of each row
        # to convert an int to str -> int("str")
        if int(list[i][5]) > 65:
            list[i][5] = "[66->99]"
        elif int(list[i][5]) > 40:
            list[i][5] = "[41->65]"
        elif int(list[i][5]) > 20:
            list[i][5] = "[21->40]"
        else:
            list[i][5] = "[1->20]"
    return list


# Function to print the list in list of strings
def formatted_print(list):
    for i in range(len(list)):
        print(f"\033[33m{i}: {list[i]}\033[0m")


# Function to transform the string into the strings in list of list
def my_data_transform(data):
    # Split the string separated with \n into multiple strings in the list
    list = data.split("\n")
    list = list[:-1]
    new_list = []
    for string in list:
        new_list.append(string.split(","))
    return new_list

if __name__ == "__main__":
    main()
