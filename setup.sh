# create virtual environment
python3 -m venv env

# activate virtual environment
source env/bin/activate

# install dependencies
pip install -r requirements.txt

# install spacy model
python -m spacy download en_core_web_md