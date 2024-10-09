# AdvancedLivePortraitGradio

AdvancedLivePortraitGradio is a live portrait generation tool using Gradio and PyTorch with CUDA acceleration.

## Requirements
- CUDA >= 11.8
- Python >= 3.10.6, < 3.11

## Installation

### 1. Create a Virtual Environment
```bash
python -m venv path_to_your_venv/venv_name
```
### 2. Activate the Virtual Environment
On Windows:
```bash
path_to_your_venv/venv_name/Scripts/activate
```
On Linux:
```bash
source path_to_your_venv/venv_name/bin/activate
```
### 3. Install PyTorch with CUDA
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
### 4. Clone the Repository
```bash
git clone https://github.com/auroraintech/AdvancedLivePortraitGradio.git
cd AdvancedLivePortraitGradio
```
### 5. Install Requirements
```bash
pip install -r requirements.txt
```
### 6. Start the Application
```bash
python app.py

```
Go to http://localhost:7860 to access the application.

### Thanks to [camenduru](https://github.com/camenduru) and [fffiloni](https://huggingface.co/fffiloni) for providing the UI template.