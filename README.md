# Extracting linguistic features using spaCy
Assignment 1 for language analytics (S2023)

This repository contains a script that extracts linguistic features from a corpus with subcorpora of texts using spaCy. The script loops over all folders in the input directory, extracts the linguistic features of the texts in the folder, and saves the results in a csv file in the output directory. In this sense the code generalizes to any corpus of texts, with a folder for each subcorpus.

To solve the tasks in the assignment (see assignment_description.md), run the following command from the terminal at the root of the repository:
```python extract_ling_features.py -i in/USEcorpus -o out/```

For each subcorpus, a csv file is created in the output directory (for this assignment the `out` directory). Each csv file contains the following information:

filename|relfreq_NOUN|relfreq_VERB|relfreq_ADJ|relfreq_ADV|unique_PERSON|unique_LOC|unique_ORG
|---|---|---|---|---|---|---|---|
|file1.txt|---|---|---|---|---|---|---|
|file2.txt|---|---|---|---|---|---|---|
|etc|---|---|---|---|---|---|---|


# Usage
To extract the linguistic features of a corpus, run the following command from the root of the repository:
```
bash run.sh
```

This will create a virtual environment, install the required packages, and run the script. The script will extract the linguistic features of the USE corpus and save the results in the `out` directory.