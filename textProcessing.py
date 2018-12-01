import csv
import re

class textProcessing:

    

    #print the primary key if the publisher is not found in the exported list 
    def compare_puber_import_export():

        filePath = 'H:\Wanqi_Zhao_Stuff\Kath_Stuff\Data_Migration\Austlit_original.csv' 
        testPath = 'H:\Wanqi_Zhao_Stuff\Kath_Stuff\Data_Migration\AustlitDataTest.csv'
        outputPath = 'H:\Wanqi_Zhao_Stuff\Kath_Stuff\Data_Migration\Publishers2.csv'
        exportPath = 'H:\Wanqi_Zhao_Stuff\Kath_Stuff\Data_Migration\publisher_export.csv'
        importPath = 'H:\Wanqi_Zhao_Stuff\Kath_Stuff\Data_Migration\Publishers_All.csv'
        exported_publisher = []
        index_list = []

        with open(exportPath,'r', encoding="utf8") as csvinput:
            reader = csv.reader(csvinput)

            for row in reader:
                exported_publisher.append(row[0])

        #print(len(exported_publisher))

        with open(importPath,'r', encoding="utf8") as csvinput2:
            print("=======================examine imported publishers====================================")
            reader2 = csv.reader(csvinput2)

            for row2 in reader2:
                if row2[0] not in exported_publisher:
                    print(row2[0]+" is not in the exported list")
                else:
                    if exported_publisher.index(row2[0]) not in index_list:
                        index_list.append(exported_publisher.index(row2[0]))

            print("=======================examine exported publishers====================================")
            for i in range(len(exported_publisher)):
                if i not in index_list:
                    print(exported_publisher[i])

    '''
    This function is used to extract author information out of authors field 
        #creating CSV for Author Table with fields: firstnames, surnames, gender, other info, fullname
        #text processing: 1) using ";" to separate all authors 2)extract the information between brackets in each author string 
                        3)if any string between brackets is not one of the roles identified at the beginning

    @inputPath: the original file 
        # field extracted (field name with column number, index would be the (column number - 1))
        # authors/4
        # authors is used for getting authors 
    '''
    def get_all_author(inputPath, outputPath):

        with open(inputPath,'r', encoding="utf8") as csvinput:
            with open(outputPath, 'w', encoding="utf8") as csvoutput:
                writer = csv.writer(csvoutput, lineterminator='\n')
                reader = csv.reader(csvinput)

                roles = ["translator", "compiler", "editor", "illustrator", "creator", "composer","publisher", "interviewer", "story teller", "director", "Visitor"]
                all = []
                row = next(reader)
        
                for row in reader:
                    authors = tetProcessing.separate_string_by(row[3])
                    for author in authors:
                        line = []
                        name = ""
                        firstname = ""
                        lastname = ""
                        info = ""

                        strings_in_brackets = textProcessing.get_string_matched_with_pattern(author)

                        if strings_in_brackets:
                            is_other = False
                            for s in strings_in_brackets:
                                if s in roles:
                                    is_other = True
                            if not is_other:
                                # as can only extract the string with whitespace in between or pure characters 
                                name = author.strip()
                        else:
                            if author != "":    
                                name = author.strip()
                        
                        if name:
                            if "," in name:
                                firstname = name.split(",")[0].strip()
                                lastname = name.split(",")[1].strip()
                            else:
                                lastname = name
                            
                            #only the string between brackets after the last name is recognised as other information
                            if "(" in lastname and ")" in lastname:
                                info = lastname.split("(")[1].split(")")[0].strip()
                                lastname = lastname.split(info)[0].strip("(")

                            line.append(firstname)
                            line.append(lastname)
                            line.append("") #gender requires other program to analyse
                            line.append(info)
                            line.append(name)
                            all.append(line)            

                writer.writerows(all)
    
    '''
    This function is used to get all publishers from the authors field and the publisher field
        #creating CSV for Publisher Table with fields: name (need to include "publisher" in the roles array and the Publisher field )
        #text processing: 1) using ";" to separate all authors 2)extract the information between brackets in each author string 
                        3)if any string between brackets is one of the roles identified at the beginning, get the role and name 

    @inputPath: the original file 
        # field extracted (field name with column number, index would be the (column number - 1))
        # authors/4; publisher/6
        # authors is used for getting just publisher role
    '''
    def get_all_publishers(inputPath, outputPath):

        with open(inputPath,'r', encoding="utf8") as csvinput:
            with open(outputPath, 'w', encoding="utf8") as csvoutput:
                writer = csv.writer(csvoutput, lineterminator='\n')
                reader = csv.reader(csvinput)

                all = []
                row = next(reader)

                for row in reader:

                    authors = textProcessing.separate_string_by(";", row[3])
                    line2 = [] 

                    for author in authors:
                        line = []
                        strings_in_brackets = textProcessing.get_string_matched_with_pattern(author)
                        is_publisher = False

                        for s in strings_in_brackets:
                            if s == "publisher":
                                is_publisher =True

                        if is_publisher:
                            processedname = fullname.split("publisher")[0].strip().strip("(").strip(',').strip(' ')
                            
                            line.append(processedname)
                            line.append(author)
                            all.append(line)

                    if row[5]:
                        fullname2 = row[5]
                        processedname2 = row[5].strip(',').strip(' ')
                        line2.append(processedname2)
                        line2.append(fullname2)
                        all.append(line2)
                    
                writer.writerows(all)
    
    '''
    This function is used to extract the information of all other roles
        #creating CSV for Other_Roles Table with fields: name (need to exclude "publisher in the roles array"), role 
        #text processing: 1) using ";" to separate all authors 2)extract the information between brackets in each author string 
                        3)if any string between brackets is one of the roles identified at the beginning, get the role and name 

    @inputPath: the original file 
        # field extracted (field name with column number, index would be the (column number - 1))
        # authors/4; 
        # authors is used for getting all roles info
    '''

    def get_all_otherRoles(inputPath, outputPath):

        with open(inputPath,'r', encoding="utf8") as csvinput:
            with open(outputPath, 'w', encoding="utf8") as csvoutput:
                writer = csv.writer(csvoutput, lineterminator='\n')
                reader = csv.reader(csvinput)

                roles = ["translator", "compiler", "editor", "illustrator", "creator", "composer", "interviewer", "story teller", "director", "Visitor"]
                all = []
                row = next(reader)                #read from the orginal file
                
                for row in reader:
                    authors = tetProcessing.separate_string_by(row[3])
                    for author in authors:
                        line = []
                        strings_in_brackets = textProcessing.get_string_matched_with_pattern(";", author)
                        is_other = False

                        for s in strings_in_brackets:
                            if s in roles: 
                                is_other = True

                        if is_other:
                            role = s
                            name = author.split(s)[0].strip().strip("(")
                            
                            line.append(name)
                            line.append(role)
                            line.append(author)
                            all.append(line)
                            
                writer.writerows(all)
    
    '''
    this function is used to extract all work information 
        
    @input file path: "..\Output.csv" which has CNumber and ZNumber obtained from the auslitlink 
        # field extracted (field name with column number, index would be the (column number - 1))
        # title/2; authors/4; forms/9; genres/10; cnumber/17
        # authors is used for creating author/work junction table
        # cnumber is used for creating manifestation table
    '''

    def get_all_work(inputPath, outputPath):

        with open(inputPath,'r', encoding="utf8") as csvinput:
            with open(outputPath, 'w', encoding="utf8") as csvoutput:

                writer = csv.writer(csvoutput, lineterminator='\n')
                reader = csv.reader(csvinput)
                all = []
                
                for row in reader:
                    line = []
                    line.append(row[1])
                    line.append(row[8])
                    line.append(row[9])
                    line.append(row[16])
                    line.append(row[3])
                    all.append(line)
                            
                writer.writerows(all)

    '''
    @inputPath1: read in all the authors
        # read in all author names with ids -- dict would be the data structure, key -- author, value -- ids
    @inputPath2: read in all the work
        # read from the Work.csv, get authors with corresponding work id -- dict would be data structure, key -- CNumbers, value -- authors
    '''
    def get_all_wa(inputPath1, inputPath2, outputPath):
        
        roles = ["translator", "compiler", "editor", "illustrator", "creator", "composer","publisher", "interviewer", "story teller", "director", "Visitor"]
        authors_id = []
        wid_authors = {}
        all = []
        
        with open(inputPath1,'r', encoding="utf8") as csvinput:
            reader = csv.reader(csvinput)

            for row in reader:
                author_name = row[4]
                authors_id.append(author_name)
                  

        with open(inputPath2,'r', encoding="utf8") as csvinput2:
            with open(outputPath, 'w', encoding="utf8") as csvoutput:
                writer = csv.writer(csvoutput, lineterminator='\n')
                reader2 = csv.reader(csvinput2)
                work_id = 0

                for row in reader2:

                    work_id = work_id+1
                    if len(row)>3:
                        authors = row[4]
                        authors = authors.split(";")

                        for author in authors:
                            
                            line = []
                            if "(" in author and ")" in author: 
                                    
                                name = author.split("(")[0].strip()
                                role = author.split("(")[1]
                                role = role.split(")")[0].strip()
                        
                                #===============================creating work and author junction Table=================================
                                #===============================ID, work id and author id  ================================
                                if role not in roles:
                                        
                                    if name in authors_id:
                                        line.append(work_id)
                                        line.append(authors_id.index(name))
                            
                                        all.append(line)
                            
                            else:
                                if author != "":
                                    if author in authors_id:
                                        line.append(work_id)
                                        line.append(authors_id.index(author)+1)
                            
                                        all.append(line)


                        
                writer.writerows(all)


    def get_all_mani():

        workExpPath = 'H:\Wanqi_Zhao_Stuff\Kath_Stuff\Data_Migration\Exported_From_Postgres\Work.csv'
        pubExpPath = 'H:\Wanqi_Zhao_Stuff\Kath_Stuff\Data_Migration\Exported_From_Postgres\Publisher.csv'
        inputPath = 'H:\Wanqi_Zhao_Stuff\Kath_Stuff\Data_Migration\Output.csv' 
        outputPath = 'H:\Wanqi_Zhao_Stuff\Kath_Stuff\Data_Migration\Manifestation.csv'
        #get all work
        work = textProcessing.load_table_with_id(workExpPath, 3)
        publisher = textProcessing.load_table_with_id(pubExpPath, 0)
        all = []

        print(work)

        with open(inputPath,'r', encoding="utf8") as csvinput:
            with open(outputPath, 'w', encoding="utf8") as csvoutput:
                writer = csv.writer(csvoutput, lineterminator='\n')
                reader = csv.reader(csvinput)

                for row in reader:
                    line = []
                    authors = row[3]
                    authors = authors.split(";")
                    #alternative titles
                    line.append(row[2])
                    #work type
                    line.append(row[7])
                    #issue detail
                    line.append(row[10])
                    #page number
                    line.append(row[11])
                    #ISBNs
                    line.append(row[14])
                    #year of pub 
                    line.append(row[6])
                    #place of pub
                    line.append(row[4])

                    #work id (FK) -- cnumber
                    work_id = None
                    pub_id = None
                    other_id = None

                    if row[16] in work:
                        work_id = work.index(row[16])+1
                    

                    #pub id (FK) -- publisher field first
                    #if the publisher field is null, check the authors field
                    if row[5] in publisher:
                        pub_id = publisher.index(row[5])+1
                    else:
                        for author in authors:
                            roles =  textProcessing.get_string_matched_with_pattern(author)

                            for s in roles:
                                if s == 'publisher': 
                                    name = author.split(s)[0].strip().strip("(")

                                    if name in publisher:
                                        pud_id = publisher.index(name)+1
                    
                    line.append(work_id)
                    line.append(pub_id)
                    
                    all.append(line)

                writer.writerows(all)
        

        
    '''
    To get all works: 
        filePath = 'H:\Wanqi_Zhao_Stuff\Kath_Stuff\Data_Migration\Exported_From_Postgres\Work.csv'
        field_index = 3
    
    To get all author's fullname:
        filePath = 'H:\Wanqi_Zhao_Stuff\Kath_Stuff\Data_Migration\Exported_From_Postgres\Authors.csv'
        field_index = 4

    To get all publisher:
        filePath = 'H:\Wanqi_Zhao_Stuff\Kath_Stuff\Data_Migration\Exported_From_Postgres\Publisher.csv'
        field_index = 0

    To get all other roles:
        filePath = 'H:\Wanqi_Zhao_Stuff\Kath_Stuff\Data_Migration\Exported_From_Postgres\Other_Role.csv'
        field_index = 0/1
    '''
    def load_table_with_id(filePath, field_index):

        data = []

        with open(filePath,'r', encoding="utf8") as csvinput:
            reader = csv.reader(csvinput)

            for row in reader:
                if len(row)>(field_index-1):
                    data.append(row[field_index])

        return data 

    '''
    This function can only extract the string that satisfies the regular expressions identified 
    At the moment, it can only extract the string between brackets that only contain numberics and alphabets, or contain one space in the string

    To get strings that just contains numerics, digits and letters/characters in bracket:
        reg_exp = r"\((\w+)\)"
    To get string that has space in between
        reg_exp = r'\((\w+\s\w+)\)'
    '''
    def get_string_matched_with_pattern(full_string):
        s = []

        s1 = re.findall(r'\((\w+\s\w+)\)', full_string)
        s2 = re.findall(r"\((\w+)\)", full_string)
        s = s1+s2

        return s
    
    def separate_string_by(delimiter, full_string):
        return full_string.split(delimiter)


        