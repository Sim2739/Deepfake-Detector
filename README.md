# Deepfake Detection Project

This project is a deepfake image detection tool that uses a pretrained model to classify real vs. AI-generated images. The model weights are hosted externally due to file size and are downloaded automatically.



## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Sim2739/Deepfake-Detector.git
cd Deepfake-Detector
```

### 2. Install Dependencies

```bash
pip install requirements.txt
```


### 3. Download the pretrained model which is hosted on Google Drive since it was too large
```bash
python download_model.py
```

### 4. Data can be downloaded at
https://www.kaggle.com/datasets/shahzaibshazoo/detect-ai-generated-faces-high-quality-dataset

### 5. Finally, to run the app
```bash
python deepfake.py
streamlit run app.py
```
