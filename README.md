# Demo LLM
A simplified adaption of the https://github.com/karpathy/nanoGPT repository, for a small model trained on the german translation of shakespeares works.

## Showcase
If you only want to see the results open the jupyter notebook LLM-showcase.ipynb.

Direct link to Google Colab https://colab.research.google.com/github/phonosync/demo_llm/blob/main/LLM-showcase.ipynb
(Generated by the Open in Colab Chrome extension.)

## How to train the model
- create a venv from the requirements.txt
  - if you get dependency problems, try to resolve them with the information from the requirements-pip-freeze.txt
- python data/shakespeare_deutsch/prepare.py
- on my hardware setup i ran into a memory shortage, setting this env variable helped (export 'PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:512')
- python train.py config/train_shakespeare.py
