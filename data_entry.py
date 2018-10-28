
'''*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                        Program:  The Data Entry Program
                        Author:   Seawyrd
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*'''


#*******************************import statements******************************#
import os
import sys
#*****************************end import statements****************************#


'''*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-'''


#**************************begin function declaration**************************#


''' #**********************************************************************#
    #                                                                      #
    #   FUNCTION NAME:    makeTxtFile()                                    #
    #         PURPOSE:    Prompts user to enter the name                   #
    #                       of a text file and creates the                 #
    #                       file in write mode.                            #
    #                                                                      #
    #**********************************************************************# '''
def makeTxtFile() -> 'txt':
    """Creates text file in write mode"""
    global filename
    filename  = input('Name of file [include \'.txt\' extension]: ')

    f = open(filename, 'w+')
    f.close()

    keepGoing()
            #end makeTxtFile()


''' #**********************************************************************#
    #                                                                      #
    #   FUNCTION NAME:    dataType()                                       #
    #         PURPOSE:    Opens newly created text file                    #
    #                       and prompts user to create a                   #
    #                       data type for entry.                           #
    #                                                                      #
    #**********************************************************************# '''
def dataType() -> 'data type':
    """Opens new text file and inserts empty data type based on user input"""
    global data
    global data_type
    f = open(filename, 'w')
    print('\nEnter data type from the following list:')
    print('  [d] dictionary, [l] list, [s] set, [t] tuple')

    new_type = input('>>> ')        # new_type: local variable
                                        # to create data type
    if new_type == 'd':
        data = dict()                           # creates dictionary
        data_type = type(data)
        print('\nYou chose "dictionary".')
    elif new_type == 'l':
        data = list()                           # creates list
        data_type = type(data)
        print('\nYou chose "list".')
    elif new_type == 's':
        data = set()                            # creates set
        data_type = type(data)
        print('\nYou chose "set".')
    elif new_type == 't':
        data = tuple()                          # creates tuple
        data_type = type(data)                           # temp list used for
        print('\nYou chose "tuple".')           # data entry in writeData()
    else:
        f.write('Invalid entry.')
        print('\n')
        print('Invalid entry. Press RETURN to continue'.center(width))
        input()
        keepGoing()

    f.close()
    return data_type
                #end dataType()


''' #**********************************************************************#
    #                                                                      #
    #   FUNCTION NAME:      writeData()                                    #
    #         PURPOSE:      Allows user to enter new data                  #
    #                           into text file using return                #
    #                           value from dataType()                      #
    #                                                                      #
    #**********************************************************************# '''
def writeData(data_type) -> 'write':
    """Data entry in <filename>.txt"""
    f = open(filename, 'w')

        # For creating a dictionary
    if data_type is dict:
        temp_dict = dict()            # temporary dictionary
                                        # for iteration
        print('Enter number of key:value pairs.')
        elements = input('>>> ')
        elements = int(elements)
        print('\nYou chose %d elements,' % elements)
        print('\tstarting at [0] and ending at [%d]\n' % (elements-1))
        counter = 0

        for elements in range(0, elements):
            key = input('Key %d: ' % counter)
            value = input(' Value: ')
            temp_dict[key] = value
            print(temp_dict, '\n')
            counter = counter + 1

        data = temp_dict                # write back to data variable
        print('Writing to %s ...done.' % filename)
        f.write(str(data))

        # For creating a list
    elif data_type is list:
        temp_list = list()            # temporary list
                                        # for iteration
        print('Enter number of list items.')
        elements = input('>>> ')
        elements = int(elements)
        print('\nYou chose %d elements,' % elements)
        print('\tstarting at [0] and ending at [%d]\n' % (elements-1))
        counter = 0

        for elements in range(0, elements):
            item = input('Item %d: ' % counter)
            data.append(item)
            print(data, '\n')
            counter = counter + 1

        data = temp_list                # write back to data variable
        print('Writing to %s ...done.' % filename)
        f.write(str(data))

    elif data_type is set:
        temp_set = set()            # temporary set
                                        # for iteration

        print('Enter number of set items.')
        elements = input('>>> ')
        elements = int(elements)
        print('\nYou chose %d elements,' % elements)
        print('\tstarting at [0] and ending at [%d]\n' % (elements-1))
        counter = 0

        for elements in range(0, elements):
            item = input('Item %d: ' % counter)
            temp_set.add(item)
            print(temp_set, '\n')
            counter = counter + 1

        data = temp_set                # write back to data variable
        print('Writing to %s ...done.' % filename)
        f.write(str(data))

    elif data_type is tuple:
        temp_tuple_as_list = list()         # temporary list to be converted
                                                # to tuple after iteration
        print('Enter number of tuple items.')
        elements = input('>>> ')
        elements = int(elements)
        print('\nYou chose %d elements,' % elements)
        print('\tstarting at [0] and ending at [%d]\n' % (elements-1))
        print('Creating temporary list...\n')
        counter = 0

        for elements in range(0, elements):
            item = input('Item %d: ' % counter)
            temp_tuple_as_list.append(item)
            print(temp_tuple_as_list, '\n')
            counter = counter + 1

        print('...converting to tuple...done.')
        data = tuple(temp_tuple_as_list)         # write back to data variable
        print(data)

        print('Writing to %s ...done.' % filename)
        f.write(str(data))

    else:
        print('Something went wrong.')
                #end writeData()


''' #**********************************************************************#
    #                                                                      #
    #   FUNCTION NAME:      readFile()                                     #
    #         PURPOSE:      Allows user to read contents                   #
    #                           of text file following                     #
    #                           data entry.                                #
    #                                                                      #
    #**********************************************************************# '''
def readFile():
    """Read contents of text file"""
    print('Read back new file? [y/n]')
    answer = input('>>> ')

    if answer == 'y':
        print('Reading contents of %s ... ' % filename)
        f = open(filename, 'r')
        contents = f.read()
        print(contents)
                #end readFile()


''' #**********************************************************************#
    #                                                                      #
    #   FUNCTION NAME:      keepGoing()                                    #
    #         PURPOSE:      Allows user to decide whether to               #
    #                           enter data into text file                  #
    #                           or exit the program.                       #
    #                                                                      #
    #**********************************************************************# '''
def keepGoing():
    """Allows user to decide whether to continue or exit"""
    print('\nEnter new data to %s? [y/n]' % filename)
    answer1 = input('>>> ')
    if answer1 == 'y':
        dataType()
        writeData(data_type)
        readFile()
    else:
        print('\n\nCreate new data file? [y/n]')
        answer2 = input('>>> ')

        if answer2 == 'y':
            print('\n')
            makeTxtFile()
        else:
            endHere()
                #end keepGoing()


''' #**********************************************************************#
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
    print('Author: seawyrd'.center(width))
    print('https://github.com/seawyrd'.center(width))
    print('\n')
    print('{:*^80}'.format(''))
    print('\n')

    makeTxtFile()
            # end startHere()


''' #**********************************************************************#
    #                                                                      #
    #   FUNCTION NAME:      endHere()                                      #
    #         PURPOSE:      Closing function                               #
    #                                                                      #
    #**********************************************************************# '''
def endHere():
    """Closing function"""
    print('\n')
    print('{:*^80}'.format(''))
    print('\n')
    print('End of Program'.center(width))
    print('\n')
    print('{:*^80}'.format(''))
    print('\n')
    sys.exit()
            #end endHere()


#***************************end function declarations**************************#


'''*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-'''


#********************************function call*********************************#
startHere()
#******************************end function call*******************************#


'''#*****************************end of program*****************************#'''
