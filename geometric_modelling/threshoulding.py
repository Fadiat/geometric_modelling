import os
import string
import csv
import seaborn as sns
import array
import numpy as np
import math
import pandas as pd
import subprocess
import shutil

def element_extraction_only():

    if os.path.exists("nodes_and_elements.txt"):
        os.remove("nodes_and_elements.txt")
        old_name = r"Dogbone.inp"
        new_name = r"nodes_and_elements.txt"
        shutil.copyfile(old_name, new_name)
    else:
        # Renaming the file
        old_name = r"Dogbone.inp"
        new_name = r"nodes_and_elements.txt"
        shutil.copyfile(old_name, new_name)

    # opening a text file
    file1 = open("nodes_and_elements.txt", "r")

    word = "*Element"

    with open("nodes_and_elements.txt", "r") as file:
        for line_number, line in enumerate(file, start=1):
            if word in line:
                print(f"Word '{word}' found on line {line_number}")
                break
    print("Node Search completed.")

    lines = file1.readlines()

    del lines[:line_number]

    file1.close()

    file1 = open("nodes_and_elements.txt", "r")
    element_line = "*Nset, nset=_PickedSet6, i"  ### check this edit here
    with open("nodes_and_elements.txt", "r") as file:
        for element_line_number, line in enumerate(file, start=1):
            if element_line in line:
                print(f"Word '{element_line}' found on line {element_line_number}")
                break
    print("Element Search completed.")
    del lines[element_line_number - (line_number + 1):]
    file1.close()

    new_file = open("nodes_and_elements.txt", "w+")

    for line in lines:
        new_file.write(line)

    new_file.close()

    # make a copy of the invoice to work with
    src = "nodes_and_elements.txt"
    dst = "_1_Elements.txt"
    shutil.copy(src, dst)
    # elements conversion

    if os.path.exists("nodes.csv"):
        os.remove("nodes.csv")
    else:
        # Renaming the file
        old_node = r"nodes_and_elements.txt"
        node_conv = r"3_nodes.csv"
        shutil.copyfile(old_node, node_conv)

def nodes_2_extraction():
    # Absolute path of a file

    if os.path.exists("nodes_and_elements.txt"):
        os.remove("nodes_and_elements.txt")
        old_name = r"Dogbone.inp"
        new_name = r"nodes_and_elements.txt"
        shutil.copyfile(old_name, new_name)
    else:
        # Renaming the file
        old_name = r"Dogbone.inp"
        new_name = r"nodes_and_elements.txt"
        shutil.copyfile(old_name, new_name)

    # opening a text file
    file1 = open("nodes_and_elements.txt", "r")

    word = "*Node"
    with open("nodes_and_elements.txt", "r") as file:
        for line_number, line in enumerate(file, start=1):
            if word in line:
                print(f"Word '{word}' found on line {line_number}")
                break
    print("Node Search completed.")

    lines = file1.readlines()

    del lines[:line_number]

    file1.close()

    file1 = open("nodes_and_elements.txt", "r")
    element_line = "*Element"
    with open("nodes_and_elements.txt", "r") as file:
        for element_line_number, line in enumerate(file, start=1):
            if element_line in line:
                print(f"Word '{element_line}' found on line {element_line_number}")
                break
    print("Element Search completed.")
    del lines[element_line_number - (line_number + 1):]
    file1.close()

    new_file = open("nodes_and_elements.txt", "w+")

    for line in lines:
        new_file.write(line)

    new_file.close()

    # elements conversion

    if os.path.exists("nodes.csv"):
        os.remove("nodes.csv")
    else:
        # Renaming the file
        old_node = r"nodes_and_elements.txt"
        node_conv = r"nodes.csv"
        shutil.copyfile(old_node, node_conv)

    original = "nodes_and_elements.txt"
    rename = "_3_nodes_alone.txt"
    shutil.copy(original, rename)


def threshoulding(percent):


    original = "Dogbone.csv"
    rename = "_2_Dogbone.csv"
    shutil.copy(original, rename)

    df2 = pd.read_csv("Dogbone.csv", header=None)

    ########
    df2.columns = ['new_col1', 'new_col2', 'new_col3', 'new_col4' ]
    r =df2['new_col4']
    max = r.max()
    # abs(max)
    # per_75 = 3
    per_75 = max*percent/100

    print("Maximum detected stress:", max)
    count = 0
    counter_line = -1
    nodes_above = []
    for i in r:
        counter_line += 1
        if i > per_75:
            count +=1
            nodes_above.append(counter_line)
    print(count)
    print(nodes_above) # fill in down manually, edit here

    df3 = pd.read_csv("_2_Dogbone.csv", header=None, delimiter=None )
    df3.columns = ['new_col1', 'new_col2', 'new_col3', 'new_col4' ]

    dup1  = print("length",len(df3))
    df3.drop_duplicates( inplace = True)
    dup2 = print("length",len(df3))

    if dup1 != dup2:
        print("Duplicated are found")


    elements = pd.read_csv("_1_Elements.txt")
    clean = (elements.loc[nodes_above])
    clean.to_csv("_5_Elements.txt", header=None)

    read_df = pd.read_csv("_5_Elements.txt", header=None)
    read_df.columns = ['new_col1', 'new_col2', 'new_col3', 'new_col4' , '5', '6']
    frames = [read_df['new_col3'],read_df['new_col4'],read_df['6']]
    result = pd.concat(frames)
    result.columns = ['col1']

    dup_1 = len(result)
    result.drop_duplicates( inplace = True)
    dup_2 = len(result)

    count = 0
    if dup_1 != dup_2:
        cal  = abs(dup_1 - dup_2)
        print(cal , "Duplicated are found")

    all_nodes  =np.hstack(result)
    # print("all",all_nodes)
    p =[]

    for i in all_nodes:
        p.append(i-1)
    all_nodes = p

    print(all_nodes)

    ### now read my nodes

    # define

    #################### BOUNDARIES AND CHECKING WHETHER X,Y, AND Z FALL WITHIN THE BOUNDARIES
    df4 = pd.read_csv("_3_nodes_alone.txt", header=None)
    df4.columns = ['1','2', '3','4']
    z_all = df4['4']
    max = z_all.max()
    min = z_all.min()

    x_all = df4['2']
    x_max = x_all.max()
    x_min = x_all.min()

    y_all = df4['3']
    y_max = y_all.max()
    y_min = y_all.min()

    starting_x = ( x_max - x_min) / 3 + x_min
    ending_x= ( x_max - x_min) / 3*2 +  x_min
    print("middle bit x is ranging from ", starting_x, "til", ending_x  ) # since its 3x3 so /3 and also since the unit cell is 10 so +- 5
    starting_x = ( x_max - x_min) / 3 + x_min
    ending_x= ( x_max - x_min) / 3*2 +  x_min
    print("middle bit x is ranging from ", starting_x, "til", ending_x  ) # since its 3x3 so /3 and also since the unit cell is 10 so +- 5


    starting_y = ( y_max - y_min) / 3 + y_min
    ending_y = ( y_max - y_min) / 3*2 +  y_min
    print("y", y_min, "and", y_max)
    print("middle bit y is ranging from ", starting_y, "til", ending_y ) # since its 3x3 so /3 and also since the unit cell is 10 so +- 5


    starting_z = ( max - min) / 3 + min
    print(all_nodes)
    ending_z = ( max - min) / 3*2 +  min
    print("middle bit z is ranging from ", starting_z, "til", ending_z  ) # since its 3x3 so /3 and also since the unit cell is 10 so +- 5


    new_DF = (df4.loc[all_nodes])
    # print(new_DF)

    # print(len(new_DF))
    new_DF.to_csv("_4_right_nodes_above_threshould.txt", header=None)
    new_DF.columns = ['1','2', '3','4']


    new_DF.dropna(inplace=True)
    new_DF.reset_index(drop=True, inplace=True)
    # print(new_DF)

    x = new_DF['2']
    y = new_DF['3']
    z = new_DF['4']

    print("d",z)

    # x_list.array.to_list()
    y_list  =np.hstack(y)
    z_list  =np.hstack(z)
    print(y_list)
    p1 = []


    ylist =[]
    for i in y_list:
        ylist.append(i)
    print(ylist)



    def right_middle_spot():
        max_inside_my_elements = 0
        list_counter_y = []
        countt = -1
        wrongy = 1
        uncertainty_increment = -1.4
        for i in ylist:
            countt += 1
            if i < starting_y - uncertainty_increment or i > ending_y + uncertainty_increment:
                wrongy += 1
                pass
            else:
                list_counter_y.append(countt)

        print("y", list_counter_y)
        after_y = (new_DF.loc[list_counter_y])
        after_y.reset_index(drop=True, inplace=True)
        print(after_y)

        after_y.columns = ['1', '2', '3', '4']
        x = after_y['2']
        xlist = []
        x_list = np.hstack(x)
        for i in x_list:
            xlist.append(i)
        print(xlist)

        list_counter_x = []
        countt = -1

        wrongx = 1
        uncertainty_increment = 0.01
        for i in xlist:
            countt += 1
            if i < starting_x - uncertainty_increment or i > ending_x + uncertainty_increment:
                wrongx += 1
                pass
            else:
                list_counter_x.append(countt)

        print("x", list_counter_x)

        after_x = (after_y.loc[list_counter_x])
        after_x.reset_index(drop=True, inplace=True)
        print(after_x)

        after_x.columns = ['1', '2', '3', '4']

        z = after_x['4']
        zlist = []
        z_list = np.hstack(z)
        for i in z_list:
            zlist.append(i)
        print(zlist)

        list_counter_z = []
        countt = -1
        wrongz = 1
        uncertainty_increment = 0.01
        for i in zlist:
            countt += 1
            if i < starting_z - uncertainty_increment or i > ending_z + uncertainty_increment:
                wrongz += 1
                pass
            else:
                list_counter_z.append(countt)
        print("z", list_counter_z)

        after_z = (after_x.loc[list_counter_z])
        after_z.reset_index(drop=True, inplace=True)

        print(after_z)
        print("The wrongs are", wrongx, wrongy, wrongz)

        large_enough = after_z.shape[0]
        if large_enough < 200:
           print("Job Done")
        else:
            print("Finding Maximum")

        restricted_elements = after_z['1']
        stresses = after_z['3']
        print('s',stresses)
        # result = pd.concat(frames)
        print(restricted_elements)
        ele = []
        ele_array = np.hstack(restricted_elements)
        print(ele_array)
        file_header = ["Elset, elset=_PickedSet6, internal, generate"]
        with open('1__vim_out.txt', 'w') as f:
            # using csv.writer method from CSV package
            write = csv.writer(f)
            write.writerow(ele_array)


        for i in ele_array:
            ele.append(i)
        conc = (df2.loc[ele])
        # print(conc)
        finding_max = pd.concat([after_z.reset_index(drop=True), stresses.reset_index(drop=True)], axis=1)

        finding_max.to_csv("_6_output_nodes.txt", header=None)
        max_inside_my_elements = (r.max())
        return  max_inside_my_elements



    if right_middle_spot() == 0:
        print("Still in complete work")
    else:
        print("Maximum stress in the middle node is ", right_middle_spot())

    # per_75 = right_middle_spot()*30/100
    print(per_75)

    return per_75