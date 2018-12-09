# AustLit_DataMigration

## This python file contains all functions used for migrating the AustLit data into Postgres DB

### 1. Input and ouput files
----
  - Austlit_original.csv (Containing following fields: rid; title	altertitle; authors; place; publisher; datepublished; type; forms; genres; issue pagenumber; firstline; numberissues; isbns; austlitlink)
  - Output.csv (Containing following fields: rid; title	altertitle; authors; place; publisher; datepublished; type; forms; genres; issue pagenumber; firstline; numberissues; isbns; austlitlink; cnumber; znumber)
  - Work.csv: title, forms, genres, cnumber, authors, work id
  - Author.csv: author_id, author firstnames, author surname, author gender, author info, author fullstring representations
  - Publisher.csv: pub_id; pub_name; pub fullstring representations
  - Other.csv: other_id, other_name, other_role, other fullstring representations

### 2. Functions 
----
  - Generating the full information of work 
    - Input: Austlit_original.csv 
    - Process: Extracting cnumber and znumber from austlit link 
    - Ouput: Output.csv 

  - 2.2 Function: Generating the csv file for creating Author table
    - Input: Austlit_original.csv 
    - Process: Extracting authors field, spliting the string by ";"
    - Output: Author.csv

  - 2.3 Function: Generating the csv file for creating Publisher table
    - Input: Austlit_original.csv 
    - Process: Extracting both publisher and authors field. In authors field, there is a role named publisher
    - Output: Publisher.csv

  - 2.4 Function: Generating the csv file for creating Others table
    - Input: Austlit_original.csv 
    - Process: Extracting authors field, spliting the string by ";". Using the string in brackets to justify the role.
    - Output: Other.csv
    
  - 2.5 Function: Generating the csv file for creating Work table
    - Input: Output.csv 
    - Process: Extracting title, form, genre and cnumber, authors field
    - Output: Work.csv

  - 2.6 Function: Generating the csv file for creating Work/Author Junction table
    - Input: Work.csv, Author.csv 
    - Process: Read in all the author, and traverse all the work to find out all the author and work pairs
    - Output: WA_Junction.csv
    
  - 2.7 Function: Generating the csv file for creating Manifestation table
    - Input: Work.csv, Publisher.csv, Other.csv 
    - Process: Read in 
    - Output: Manifestation.csv

### 3. Results:
----

