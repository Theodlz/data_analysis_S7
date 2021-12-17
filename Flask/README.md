### Before Running app.py to use the model's web interface:
1. Open a command terminal in the repo (in /data_analysis_S7/) and run "pip install -r requirements.txt" if it was not already done before.
2. Read and follow the instructions for downloading and preprocessing the data in the README located in the '/preprocessing/' folder.
3. Once the datasets are created, execute all cells in the Jupyter Notebook : '/data_analysis_S7/RANDOM_FOREST_REGRESSION.ipynb' to train the models (the models were too heavy to be stored on Github). It can take several minutes.

#### Now you're good to go ! Just run in your terminal "python app.py" or "python3 app.py" to launch the server; the web page will then be available in your browser at the following address : http://127.0.0.1:5000/. You can also find a demo version with pre selected values at http://127.0.0.1:5000/demo
