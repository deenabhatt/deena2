log_file = open("um-server-01.txt")


def sales_reports(log_file): # This line will creat the function with parameter log file
    for line in log_file:    # for loop will cycle through each line in the para meter log file.
        line = line.rstrip() # this will remove all speces 
        day = line[0:3]      # This code will store fist three characters of line in variable'day'
        if day == "Fri":     # this line will just itrate mon
            print(line)


sales_reports(log_file)
