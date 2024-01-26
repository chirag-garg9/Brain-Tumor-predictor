<h1 align="center" id="title">Brain-Tumor-predictor </h1>

<h3>A Website to check wheather the MRI scan of a brain Contains Tumor or not.</h3>

Run the following command in your commmand Prompt

create a virtual environment
```bash
python -m venv brain-tumor
```

Activate the enviroment using 
```bash
brain-tumor/Scripts/activate
```
Download the requirements
```bash
pip install -r requirements.txt
```
Download and install git lfs 
To get model file
```bash
git lfs fetch --all
```
To run the Flask application
```bash
python predictor.py
```
Go to local host 4000 to run the application

Upload a Image file and click Predict to Get Your Prediction
