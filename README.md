# AustLit_DataMigration

## This python file contains all functions used for migrating the AustLit data into Postgres DB

### 1. Input and ouput files:
#### 1.1 Austlit_original.csv (Containing following fields: rid; title	altertitle; authors; place; publisher; datepublished; type; forms; genres; issue pagenumber; firstline; numberissues; isbns; austlitlink)
#### 1.2 Output.csv (Containing following fields: rid; title	altertitle; authors; place; publisher; datepublished; type; forms; genres; issue pagenumber; firstline; numberissues; isbns; austlitlink; cnumber; znumber)
#### 1.3 Work.csv: 
#### 1.4 Author.csv:
#### 1.5 Publisher.csv: pub_id; pub_name; pub fullstring representations
#### 1.6 Other.csv: 

### 2. Functions 
#### 2.1 Generating the full information of work 
#### Input: Austlit_original.csv 
#### Process: Extracting cnumber and znumber from austlit link 
#### Ouput: Output.csv 

#### 2.2 Function: Generating the csv file for creating Author table
#### Input: 
#### Process:
#### Output: 
