import csv

def write_to_file(info_list):
    with open('stu_details.csv', 'a', newline='')as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["name", "age", "contact number", "email id"])

        writer.writerow(info_list)


if __name__ == '__main__':
    condition = True
    student_num = 1

    while(condition):
        student_details = input("enter the student - {} details(name age contact_num email) : ".format(student_num))
        print("the details are : " + student_details)
    
        details_list = student_details.split(' ')
        print("\n the details list is :\n Name: {}\n Age: {}\n contact_number: {}\n email-id: {}\n "
              .format(details_list[0], details_list[1], details_list[2], details_list[3]))

        choice_check = input("is the entered input correct (yes/no) ? : ")

        if choice_check == "yes":
            write_to_file(details_list)

            condition_check = input("do you wanna enter details of other student (yes/no): ")
            if condition_check == "yes":
                condition = True
                student_num = student_num + 1
       
            elif condition_check == "no":
                condition = False

        elif choice_check == "no":
            print("\n please re-enter the values ")




    
  
