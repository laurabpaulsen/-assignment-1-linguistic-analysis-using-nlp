source env/bin/activate
echo "[INFO]: Extracting linguistic features from USE corpus. This may take a while..."
# run the python script
python src/extract_ling_features.py -i in/USEcorpus -o out
# deactivate virtual environment
deactivate