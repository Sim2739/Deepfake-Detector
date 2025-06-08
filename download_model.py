import gdown
import os

def download_model():
    model_dir = "model"
    model_path = os.path.join(model_dir, "model.safetensors")
    url = "https://drive.google.com/uc?id=1jKPtUByZviGEHwz0FNBxnz1MdT5GdaTT"

   
    os.makedirs(model_dir, exist_ok=True)

    
    gdown.download(url, model_path, quiet=False)
    print("Download completed!")
    

if __name__ == "__main__":
  download_model()
