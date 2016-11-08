# IFB's Antimicrobial Peptide Multidimensional Database

![logo](docs/logo_IFB.svg)

# Contents 

This project was built using the Django Framework. And it it separated in two 'web apps': 
- ampdb (main django application): Where all the logic behind main service is added.
- Blog app. : A simple blog for posting news about the service.



# How it works

#### Researchers will be able to search the database using:
- Basic search: using the globaly used PDB id and/or the organizm, 
- Advance search: searching for all the multidimensional data in our database
 
![image](ifbAMPdb/image/demonstration.gif)

In the future, we plan to add:
- Custom search with a shell script,
- Custom SQL search in a web page



# Objective:
#### This project aims to decrease the costs of *in-silico* antibiotic research. How ? Read the scientific text below.


Recently there has been a dangerous increase of drug-resistant pathogenous micro organisms. The antimicrobial peptides are part of the first layer of the immunologic system, and create a natural passive defense agains infections.
They could be a solution to the rising problem of antibiotic-resistant microbes [1].

This project is the creation of a web system that contains multidimensional information about antimicrobial peptides, and make them available to the scientific community. This system will contain in its database multidimensional information about the known peptides, cutting the research costs by making information easier to obtain, with non trivial information made available in a simple web search.


### References
[1] FERNANDES, F. C.; RIGDEN, D. J.; FRANCO, O. L. Prediction of antimicrobial peptides based on the adaptive neuro-fuzzy inference system application. Biopolymers, v. 98, n. 4, p. 280-7, 2012.


#How to Contribute : see [CONTRIBUTING.md](CONTRIBUTING.md)

#About the Authors

#### This project was conceived by Fabiano Cavalcanti Fernandes, Doctor in Genomic Sciences and Biotechnology and Professor of the Federal Institute of Brasilia (IFB). It was first proposed as a Scientific initiation project. 
#### Rafael de Campos Passos was the Scientific initiation student and the main contributor behind all the project.
