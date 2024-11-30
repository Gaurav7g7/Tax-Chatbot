import os
from llama_parse import LlamaParse
import nest_asyncio

def convert_pdfs_to_md(pdf_dir, output_dir):
    nest_asyncio.apply()
    os.environ["LLAMA_CLOUD_API_KEY"] = "llx-YJijdFnwVhZbrSh0i5XUvQYLjWm8xRR0yg7UbCcoAB7VdaR0"

    files = os.listdir(pdf_dir)

    for file in files:
        if file.endswith('.pdf'):
            file_path = os.path.join(pdf_dir, file)
            doc = LlamaParse(result_type="markdown").load_data(file_path)
            extracted_text = "\n".join([chunk.text for chunk in doc])

            md_file_name = file.replace('.pdf', '.md')
            with open(os.path.join(output_dir, md_file_name), "w") as md_file:
                md_file.write(extracted_text)

if __name__ == "__main__":
    pdf_directory = r"C:\Users\gaura\PycharmProjects\Tax Agents Chatbot\pdf_directory"
    output_directory = r"C:\Users\gaura\PycharmProjects\Tax Agents Chatbot\output_directory"
    convert_pdfs_to_md(pdf_directory, output_directory)
