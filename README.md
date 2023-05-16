# Extracting linguistic features using spaCy
This repository holds the code for assignment 1 for language analytics (S2023). Linguistic features are extracted from each subcopora of the USEcorpus. In addition to csv files, a plot is created for each subcorpus showing the relative frequency of nouns, verbs, adjectives and adverbs.

## Description of the data
The data used 

## Usage and reproducibility
To extract the linguistic features of the USE corpora run the following commands from the root of the directory.

1. Clone the repository
2. Create a virtual environment and install the requirements
```
bash setup.sh
```
3. Run the analysis
```
bash run.sh
```

The linguistic features of the USE corpus will be extracted and the results will be saved in the `out` directory.

## Repository structure
```
├── in                                
│   └── USEcorpus
├── out                                 
│   ├── a1.csv
│   └── ...
├── src
│   ├── plot_entities.py
│   └── extract_ling_features.py            
├── assignment_description.md
├── requirements.txt       
├── run.sh
├── setup.sh      
└── README.md                           
```


## Results
For each subcorpus, a csv file is created in the output directory (for this assignment the `out` directory). Each csv file contains the following information:

filename|relfreq_NOUN|relfreq_VERB|relfreq_ADJ|relfreq_ADV|unique_PERSON|unique_LOC|unique_ORG
|---|---|---|---|---|---|---|---|
|file1.txt|---|---|---|---|---|---|---|
|file2.txt|---|---|---|---|---|---|---|
|etc|---|---|---|---|---|---|---|


In the plot below the relative frequency of nouns, verbs, adjectives and adverbs are plotted for each subcorpus.
![rel freq plot](out/entities.png)