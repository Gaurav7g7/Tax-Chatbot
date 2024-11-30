# setup.py

import subprocess


def install_packages():
    packages = [
        'nltk',
        'langchain',
        'llama-parse',
        'colab-xterm',
        'unstructured[md]',
        'langchain-community',
        'beautifulsoup4',
        # 'chromadb',
        # 'gradio',
        'faiss-cpu',
        'streamlit',
        'tiktoken',
    ]

    for package in packages:
        subprocess.run(f'pip install {package}', shell=True, check=True)


if __name__ == "__main__":
    install_packages()
