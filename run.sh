source env/bin/activate
echo "[INFO]: Extracting linguistic features from USE corpus. This may take a while..."

# run the python script
python src/extract_ling_features.py -i in/USEcorpus -o out
echo "[INFO]: Done extracting linguistic features. Plotting the entities..."
python src/plot_entities.py 

# deactivate virtual environment
deactivate