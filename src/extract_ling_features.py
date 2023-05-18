"""
Assignment 1 for Language Analytics (S2023)

This script extracts linguistic features from data stored in hierarchical folders, and save the output files to a specified output directory.

Usage:
    extract_ling_features.py -i <input_dir> -o <output_dir>
    for this assignment: python src/extract_ling_features.py -i in/USEcorpus -o out (works if you run from the root directory of the project)

Author: Laura Bock Paulsen (202005791)
"""

import os
import spacy
import argparse
import pandas as pd
import re

def clean_text(text:str):
    """
    This function cleans the text by removing everything in between '<' and '>' as well as the '<' and '>'
    Args:
        text: text to clean
    
    Returns:
        text: cleaned text
    """
    text = re.sub(r"<.*?>", "", text)
    
    return text

def relative_freq(doc, feature:str, n:int=10000):
    """
    Calculates the relative frequency per n words (defaults to 10,000) of a feature in a document.
    Args:
        doc: spacy document
        feature: feature to calculate the relative frequency of
    
    Returns:
        rel_freq: relative frequency of the feature
    """
    rel_freq = sum([token.pos_ == feature for token in doc]) / len(doc) * n
    
    return rel_freq

def unique_entities(doc, feature:str):
    """
    Calculates the number of unique entities of a type of entity in a document.
    Args:
        doc: spacy document
        feature: type of labelled entity to calculate the number of unique entities of
    
    Returns:
        unique: number of unique entities
    """
    unique = len(set([ent.text for ent in doc.ents if ent.label_ == feature]))
    
    return unique

def list_colnames(rel_freq_features:list = ["NOUN", "VERB", "ADJ", "ADV"], unique_ents:list = ["PERSON", "LOC", "ORG"]):
    """
    This function creates the column names for the dataframe.
    Args:
        rel_freq_features: the list of features that are used to calculate the relative frequency
        unique_ents: list of features to calculate the number of unique entities of (defaults to PERSON, LOC, and ORG)

    Returns:
        colnames: list of column names
    """
    colnames = ["filename"]

    colnames.extend([f"relfreq_{feature}" for feature in rel_freq_features])
    colnames.extend([f"unique_{feature}" for feature in unique_ents])
    
    return colnames

def list_txt_files(input_dir:str):
    """
    This function lists all the .txt files in a given directory.
    Args:
        input_dir: directory to list the files in

    Returns:
        txt_files: list of .txt files in the directory
    """
    txt_files = os.listdir(input_dir)
    txt_files = [file for file in txt_files if file.endswith(".txt")]
    
    return txt_files

def list_folders(input_dir:str):
    """
    This function lists all the folders in a given directory. If there are any files in the directory, they are ignored.
    Args:
        input_dir: directory to list the folders in

    Returns:
        folders: list of folders in the directory
    """
    folders = os.listdir(input_dir)
    folders = [folder for folder in folders if os.path.isdir(os.path.join(input_dir, folder))]
    
    return folders

def extract_ling_features(nlp, text:str, file_name:str, rel_freq_features:list = ["NOUN", "VERB", "ADJ", "ADV"], unique_ents:list = ["PERSON", "LOC", "ORG"]):
    """
    This function extracts linguistic features from the text. The default features are:
        - relative frequency of nouns, verbs, adjective, and adverbs per 10,000 words
        - total number of unique PERSON, LOC, ORGS

    Args:
        nlp: spacy model
        text: text to extract features from
        file_name: name of the file
        rel_freq_features: list of features to calculate the relative frequency of (defaults to nouns, verbs, adjectives, and adverbs)
        unique_ents: list of features to calculate the number of unique entities of (defaults to PERSON, LOC, and ORG)

    Returns:
        df: dataframe with the features and name of the file
    """
    doc = nlp(text)

    columms = list_colnames(rel_freq_features, unique_ents)
    
    df = pd.DataFrame(columns=columms, index=[0])

    for feature in rel_freq_features: # loop over the features we want to calculate the relative frequency of
        df[f"relfreq_{feature}"].loc[0] = relative_freq(doc, feature)
    
    for feature in unique_ents: # loop over the features we want get the number of unique entities of
        df[f"unique_{feature}"].loc[0] = unique_entities(doc, feature)

    df["filename"] = file_name
        
    return df

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_dir", help = "Input directory", required=True)
    parser.add_argument("-o", "--output_dir", help = "Output directory", required=True)
    
    return parser.parse_args()


def main():
    args = parse_args()

    # ensure that the output directory exists and if not it is created
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
    
    # load spacy model
    nlp = spacy.load("en_core_web_md")

    # get all folders in the input directory
    folders = list_folders(args.input_dir)

    # loop over all folders
    for folder in folders: 
        files = list_txt_files(os.path.join(args.input_dir, folder)) # get all .txt files in the folder (solves the problem of hidden files, e.g. .DS_Store)
        
        df = pd.DataFrame() # initialise empty dataframe

        for file in files:
            with open(os.path.join(args.input_dir, folder, file), "r", encoding='latin-1') as f:
                text = f.read()
            
            # clean the text
            text = clean_text(text) 
            
            # extract the lingustic features
            df_tmp = extract_ling_features(nlp, text, file) 
            
            # append the features from the file to the dataframe
            df = pd.concat([df, df_tmp], ignore_index=True) 

        # save the dataframe as a csv file in the output directory    
        df.to_csv(os.path.join(args.output_dir, folder + ".csv"), index=False)


if __name__ in "__main__": # only run the code below if the script is run directly (not if it is imported)
    main()


