
'''*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                        Program:  The Data Entry Program
                        Author:   Seawyrd
                        GitHub:   https://github.com/seawyrd/
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*'''


#*******************************import statements******************************#
import os
import sys
#********************************NOTES ON TUPLES*******************************#
                    # ln 168 - Tuple warning - see comments
                    # ln 390 - Add data to Tuple - see comments

'''*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-'''

#**************************begin function declaration**************************#


''' #**********************************************************************# (1)
    #                                                                      #
    #   FUNCTION NAME:    makeTxtFile()                                    #
    #         PURPOSE:    Prompts user to enter the name                   #
    #                       of a text file and creates the                 #
    #                       file in a+ mode (w+ if dne).                   #
    #                                                                      #
    #**********************************************************************# '''
def makeTxtFile() -> 'txt':
    """Creates or opens text file in append mode"""
    global filename
    filename  = input('Name of file [include \'.txt\' extension]: ')

    f = open(filename, 'a+')
    f.close()

    dataOrNoData()
            #end makeTxtFile()


''' #**********************************************************************# (2)
    #                                                                      #
    #   FUNCTION NAME:    dataOrNoData()                                   #
    #         PURPOSE:    Opens text file and asks                         #
    #                       whether to overwrite data                      #
    #                       if present.                                    #
    #                                                                      #
    #**********************************************************************# '''
def dataOrNoData():
    """Determines if data is present in text file
    and asks to overwrite or append"""
    isData = lineCount(filename)

    if isData > 0:
        print('\n%s already has data.' % filename)
        print('\n [A]dd or [O]verwrite data? [a/o]')
        choice = input('>>> ')

        if choice is 'o':
            print('\n Are you sure? [y/n]')
            choice2 = input('>>> ')

            if choice2 is 'y':
                f = open(filename, 'w+')
                print('\n Erasing data ...done.')
                f.close()
                keepGoing()
            else:
                pass
        elif choice is 'a':
            print('\n Keeping original data.')
            determineDataType()
            readFile()
        else:
            print('Invalid entry.')
            dataOrNoData()
    else:
        print('\n\tThe file %s has no data.' % filename)
        keepGoing()
                #end dataOrNoData()


''' #**********************************************************************# (3)
    #                                                                      #
    #   FUNCTION NAME:    determineDataType()                              #
    #         PURPOSE:    Determines data type in                          #
    #                       text file with data entries                    #
    #                       already present.                               #
    #                                                                      #
    #**********************************************************************# '''
def determineDataType():
    """Determines data type of data present in text file."""
    f = open(filename, 'r')
    global data_type
    for line in f:
        if 'dictionary' in line:
            data_type = 'd'
        elif 'list' in line:
            data_type = 'l'
        elif 'set' in line:
            data_type = 's'
        elif 'tuple' in line:
                # use ln 104-5 when "Tuple warning" enabled (ln )
            print('\n' + 'ERROR: "tuple" immutable, cannot append data.'.center(width))
            print('Restarting...'.center(width))

            ''' data_type = 't' '''     # use when "Tuple warning" disabled

            goAgain()
    f.close()
    return data_type
            #end determineDataType()


''' #**********************************************************************# (4)
    #                                                                      #
    #   FUNCTION NAME:    newDataType()                                    #
    #         PURPOSE:    Opens newly created text file                    #
    #                       and prompts user to create a                   #
    #                       data type for entry.                           #
    #                                                                      #
    #**********************************************************************# '''
def newDataType() -> 'data type':
    """Opens new text file and inserts empty data type based on user input"""
    global data
    global data_type
    f = open(filename, 'a')
    print('\n Enter data type from the following list:')
    print('   [d] dictionary, [l] list, [s] set, [t] tuple\n')

    new_type = input('>>> ')        # new_type: local variable
                                        # to specify data type
    if new_type == 'd':
        print('\n Name?')
        dict_name = input('>>> ')
        print('\n\t You chose "dictionary" named %s.' % dict_name)

        f.write(dict_name + '\n')
        f.write('\n' + '# Column 1 = Key' + '\n' + '# Column 2 = Value')
        f.write('\n' + '# Delimiter = "tab"')
        f.write('\n' + '# Data type = dictionary' + '\n\n')

    elif new_type == 'l':
        print('\n Name?')
        list_name = input('>>> ')
        print('\n\t You chose "list" named %s.' % list_name)

        f.write(list_name + '\n')
        f.write('\n' + '# Column 1 = Index' + '\n' + '# Column 2 = Value')
        f.write('\n' + '# Delimiter = "tab"')
        f.write('\n' + '# Data type = list' + '\n\n')

    elif new_type == 's':
        print('\n Name?')
        set_name = input('>>> ')
        print('\n\t You chose "set" named %s.' % set_name)

        f.write(set_name + '\n')
        f.write('\n' + '# Column = Value')
        f.write('\n' + '# Delimiter = "tab"')
        f.write('\n' + '# Data type = set' + '\n\n')

    elif new_type == 't':
        print('\n Name?')
        tuple_name = input('>>> ')
        print('\n\t You chose "tuple" named %s.' % tuple_name)

            # Tuple warning - to disable, comment out ln 104-105 above,
                # ln 174-177 and 185-189 below, and dedent ln 180-183
                # Also, enable lines 396-417 under writeMoreData function
                        # see "add data to Tuple" line 390

            # Tuple warning - enabled
        print('\n')
        print('WARNING: "tuple" is immutable, cannot make changes once written.'.center(width))
        print('\nProceed? [y/n]')
        choice = input('>>> ')

        if choice is 'y':
            f.write(tuple_name + '\n')
            f.write('\n' + '# Column 1 = Index' + '\n' + '# Column 2 = Value')
            f.write('\n' + '# Delimiter = "tab"')
            f.write('\n' + 'Data type = tuple' + '\n\n')
        else:
            print('\n')
            print('"Tuple" not selected. Press RETURN to continue.'.center(width))
            input()
            newDataType()

    else:
        f.write('Invalid entry.')
        print('\n')
        print('Invalid entry. Press RETURN to continue'.center(width))
        input()
        keepGoing()

    data_type = new_type
    f.close()
    return data_type
                #end newDataType()


''' #**********************************************************************# (5)
    #                                                                      #
    #   FUNCTION NAME:      writeData(data_type)                           #
    #         PURPOSE:      Allows user to enter new data                  #
    #                           into text file using return                #
    #                           value from newDataType()                   #
    #                                                                      #
    #**********************************************************************# '''
def writeData(data_type) -> 'write':
    """Data entry in <filename>.txt"""
    f = open(filename, 'a+')

        # For creating a dictionary
    if data_type is 'd':
        print('\nEnter number of key:value pairs.')

        elements = input('>>> ')
        elements = int(elements)
        print('\n You chose %d element(s),' % elements)
        print('   starting at [0]')
        print(' and ending at [%d].\n' % (elements-1))

        counter = 0

        for elements in range(0, elements):
            key = input('Key %d: ' % counter)
            value = input(' Value: ')
            f.write(str(key) + '\t' + str(value) + '\n')
            counter += 1

        print('\n\tWriting to file ...done.\n')
                #end dictionary data type

        # For creating a list
    elif data_type is 'l':
        print('\nEnter number of list items.')

        elements = input('>>> ')
        elements = int(elements)
        print('\n You chose %d element(s),' % elements)
        print('   starting at [0]')
        print(' and ending at [%d].\n' % (elements-1))

        counter = 0

        for elements in range(0, elements):
            index = counter
            item = input('Item [%d]: ' % counter)
            f.write('[' + str(index) + ']' + '\t' + str(item) + '\n')
            counter += 1

        print('\n\tWriting to file ...done.\n')
                #end list data type

        # For creating a set
    elif data_type is 's':
        print('\nEnter number of set items.')

        elements = input('>>> ')
        elements = int(elements)
        print('\n You chose %d element(s).\n' % elements)

        counter = 0

        for elements in range(0, elements):
            item = input('Item [%d]: ' % counter)
            f.write(str(item) + '\n')
            counter += 1

        print('\n\tWriting to file ...done.\n')
                # end set data type

        # For creating a tuple
    elif data_type is 't':
        print('\nEnter number of tuple items.')

        elements = input('>>> ')
        elements = int(elements)
        print('\n You chose %d element(s),' % elements)
        print('   starting at [0]')
        print(' and ending at [%d].\n' % (elements-1))

        counter = 0

        for elements in range(0, elements):
            index = counter
            item = input('Item [%d]: ' % counter)
            f.write('[' + str(index) + ']' + '\t' + str(item) + '\n')
            counter += 1

        print('\n\tWriting to file ...done.\n')
                # end tuple data type

    else:
        print('Something went wrong.')
        f.close()
        endHere()                      # early termination to endHere()

    f.close()
                #end writeData()


''' #**********************************************************************# (6)
    #                                                                      #
    #   FUNCTION NAME:      writeMoreData(data_type)                       #
    #         PURPOSE:      Allows user to enter extra data                #
    #                           into text file using return                #
    #                           value from newDataType()                   #
    #                                                                      #
    #**********************************************************************# '''
def writeMoreData(data_type) -> 'write':
    """Additional data entry in <filename>.txt"""
    f = open(filename, 'a+')

    repeat = True
    while repeat is True:
            # For adding to dictionary
        if data_type is 'd':
            print('\nEnter number of additional key:value pairs.')

            add_elements = input('>>> ')
            add_elements = int(add_elements)
            prior_elements = lineCount(filename)
            current_elements = add_elements + prior_elements - 1

            print('\n You chose %d element(s),' % add_elements)
            print('   starting at [%d]' % prior_elements)
            print(' and ending at [%d].\n' % current_elements)

            counter = prior_elements

            for current_elements in range(prior_elements, current_elements + 1):
                key = input('Key %d: ' % counter)
                value = input(' Value: ')
                f.write(str(key) + '\t' + str(value) + '\n')
                counter = counter + 1

            print('\n\tWriting to file ...done.')
                        #end dictionary data type


        # For adding to list
        elif data_type is 'l':
            print('\nEnter number of additional list items.')

            add_elements = input('>>> ')
            add_elements = int(add_elements)
            prior_elements = lineCount(filename)
            current_elements = add_elements + prior_elements - 1

            print('\n You chose %d element(s),' % add_elements)
            print('   starting at [%d]' % prior_elements)
            print(' and ending at [%d].\n' % current_elements)

            counter = prior_elements

            for current_elements in range(prior_elements, current_elements + 1):
                index = counter
                item = input('Item [%d]: ' % counter)
                f.write('[' + str(index) + ']' + '\t' + str(item) + '\n')
                counter += 1

            print('\n\tWriting to file ...done.\n')
                        #end list data type


            # For adding to set
        elif data_type is 's':
            print('\nEnter number of additional set items.')

            add_elements = input('>>> ')
            add_elements = int(add_elements)
            prior_elements = lineCount(filename)
            current_elements = add_elements + prior_elements - 1

            print('\n You chose %d element(s).\n' % add_elements)

            counter = prior_elements

            for current_elements in range(prior_elements, current_elements + 1):
                item = input('Item [%d]: ' % counter)
                f.write(str(item) + '\n')
                counter += 1

            print('\n\tWriting to file ...done.\n')
                        # end set data type

            # Add data to Tuple - to enable, un-comment lines 396-417.
                # Also, comment out ln 104-105, 174-177 and 185-189
                # and dedent lines 180-183 under newDataType function
                        # see "Tuple warning" line 168

            # For adding to tuple - disabled
        '''elif data_type is 't':
            print('\nEnter number of tuple items.')

            add_elements = input('>>> ')
            add_elements = int(add_elements)
            prior_elements = lineCount(filename)
            current_elements = add_elements + prior_elements - 1

            print('\n You chose %d element(s).' % add_elements)
            print('   starting at [%d]' % prior_elements)
            print(' and ending at [%d].\n' % current_elements)

            counter = prior_elements

            for current_elements in range(prior_elements, current_elements + 1):
                index = counter
                item = input('Item [%d]: ' % counter)
                f.write('[' + str(index) + ']' + '\t' + str(item) + '\n')
                counter += 1

            print('\n\tWriting to file ...done.\n')
                        # end tuple data type                           '''

        else:
            print('Something went wrong.')
            f.close()
            endHere()                    # early termination to endHere()

            # while loop condition update
        print('\n Add additional data to %s? [y/n]' % filename)
        choice3 = input('>>> ')

        if choice3 is 'y':
            writeMoreData(data_type)
        else:
            repeat = False
                            #end while loop
    f.close()
                #end writeMoreData(data_type)


''' #**********************************************************************# (7)
    #                                                                      #
    #   FUNCTION NAME:      readFile()                                     #
    #         PURPOSE:      Allows user to read contents                   #
    #                           of text file following                     #
    #                           data entry.                                #
    #                                                                      #
    #**********************************************************************# '''
def readFile():
    """Read contents of text file"""
    print('\n\nRead back file? [y/n]')
    answer = input('>>> ')

    if answer is 'y':
        print('\n Reading contents of %s ...done.\n' % filename)
        f = open(filename, 'r')
        contents = f.read()
        print(contents)
        goAgain()
    else:
        goAgain()
                #end readFile()


''' #**********************************************************************# (8)
    #                                                                      #
    #   FUNCTION NAME:      keepGoing()                                    #
    #         PURPOSE:      Allows user to decide whether to               #
    #                           enter data into text file                  #
    #                           or exit the program.                       #
    #                                                                      #
    #**********************************************************************# '''
def keepGoing():
    """Allows user to decide whether to continue or exit"""
    print('\n\nEnter data to %s? [y/n]' % filename)
    answer1 = input('>>> ')

    if answer1 is 'y':
        newDataType()
        writeData(data_type)
        readFile()
    elif answer1 is 'n':
        print('\n\nCreate new data file? [y/n]')
        answer2 = input('>>> ')

        if answer2 is 'y':
            print('\n')
            makeTxtFile()
        elif answer2 is 'n':
            endHere()
        else:
            print('\n')
            print('Invalid entry. Press RETURN to continue'.center(width))
            input()
            keepGoing()
    else:
        print('\n')
        print('Invalid entry. Press RETURN to continue'.center(width))
        input()
        keepGoing()
                #end keepGoing()

''' #**********************************************************************# (9)
    #                                                                      #
    #   FUNCTION NAME:      goAgain()                                      #
    #         PURPOSE:      Allows user to decide whether to               #
    #                           enter additional data into                 #
    #                           text file or exit the program.             #
    #                                                                      #
    #**********************************************************************# '''
def goAgain():
    """Allows user to decide whether to add additional data or exit"""
    if data_type is not 't':
        print('\n\nEnter additional data to %s? [y/n]' % filename)
        answer = input('>>> ')

        if answer is 'y':
            writeMoreData(data_type)
            readFile()
        else:
            print('\n\nEnter data for different file? [y/n]')
            answer2 = input('>>> ')

            if answer2 is 'y':
                print('\n')
                makeTxtFile()
            elif answer2 is 'n':
                endHere()
            else:
                print('\n')
                print('Invalid entry. Press RETURN to continue'.center(width))
                input()
                goAgain()
    else:
        print('\n\nEnter data for different file? [y/n]')
        answer2 = input('>>> ')

        if answer2 is 'y':
            print('\n')
            makeTxtFile()
        elif answer2 is 'n':
            endHere()
        else:
            print('\n')
            print('Invalid entry. Press RETURN to continue'.center(width))
            input()
            goAgain()
                #end goAgain()

''' #**********************************************************************#(10)
    #                                                                      #
    #   FUNCTION NAME:      lineCount(filename)                            #
    #         PURPOSE:      Counts number of lines in                      #
    #                           text file created by                       #
    #                           writeData()                                #
    #                                                                      #
    #**********************************************************************# '''
def lineCount(filename):
    global lines
    global actual_lines
    lines = 0
    with open(filename) as f:
    # ignore up to the first line with "Data type"
        for line in f:
            if "Data type" in line:
                break

        # then process the rest
        for line in f:
            lines += 1

    actual_lines = lines - 1

    return actual_lines
            # end lineCount()


''' #**********************************************************************#(11)
    #                                                                      #
    #   FUNCTION NAME:      startHere()                                    #
    #         PURPOSE:      Opening function                               #
    #                                                                      #
    #**********************************************************************# '''
def startHere():
    """Opening function"""
    global width
    width = os.get_terminal_size().columns

    print('\n')
    print('{:*^80}'.format(''))
    print('\n')
    print('Welcome to the Data Entry Program in Python!'.center(width))
    print('\n')
    print('Author: Seawyrd | GitHub: https://github.com/seawyrd'.center(width))
    print('\n')
    print('{:*^80}'.format(''))
    print('\n')

    makeTxtFile()
            # end startHere()


''' #**********************************************************************#(12)
    #                                                                      #
    #   FUNCTION NAME:      endHere()                                      #
    #         PURPOSE:      Closing function                               #
    #                                                                      #
    #**********************************************************************# '''
def endHere():
    """Closing function"""
    print('\n\nQuit the program? [y/n]')
    final_answer = input('>>> ')

    if final_answer is 'y':
        print('\n')
        print('{:*^80}'.format(''))
        print('\n')
        print('End of Program'.center(width))
        print('\n')
        print('{:*^80}'.format(''))
        print('\n')
        sys.exit()
    else:
        print('\n' + 'Restarting the program...'.center(width) + '\n')
        makeTxtFile()
            #end endHere()


#***************************end function declarations**************************#


'''*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-'''


#********************************function call*********************************#
startHere()



'''#*****************************end of program*****************************#'''


'''                        Indexed Function List

            (1) makeTxtFile()               (7)  readFile()
            (2) dataOrNoData()              (8)  keepGoing()
            (3) determineDataType()         (9)  goAgain()
            (4) newDataType()               (10) lineCount(filename)
            (5) writeData(data_type)        (11) startHere()
            (6) writeMoreData(data_type)    (12) endHere()                   '''
