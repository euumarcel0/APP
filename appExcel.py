import PyPDF2
import pandas as pd
import re

def read_pdf(file_path):
    # Abrir o arquivo PDF
    pdf_file = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Lista para armazenar as questões e respostas do PDF
    data = []

    # Inicializar variáveis para a questão atual
    current_question = None
    current_content = ""  # Inicializar uma string vazia para armazenar o conteúdo completo abaixo de cada "Tópico"
    current_options = {'A': '', 'B': '', 'C': '', 'D': ''}  # Dicionário para armazenar as alternativas

    # Ler cada página do PDF
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()

        # Verificar se o texto não é None
        if text:
            # Dividir o texto em linhas
            lines = text.split('\n')
            for line in lines:
                # Verificar se é uma nova questão
                if "Tópico" in line:
                    # Se já havia uma questão anterior, adicione-a aos dados
                    if current_question:
                        data.append((current_question, current_content, current_options['A'], current_options['B'], current_options['C'], current_options['D']))
                    # Inicializar nova questão
                    current_question = line.strip()
                    current_content = ""
                    current_options = {'A': '', 'B': '', 'C': '', 'D': ''}  # Resetar as opções
                elif re.match(r'^[ABCD]\.', line.strip()):
                    # Adicionar a linha à opção correta
                    option_key = line.strip()[0]
                    current_options[option_key] = line.strip()[2:].strip()  # Remover "A.", "B.", "C." ou "D." e espaço inicial
                else:
                    # Adicionar a linha ao conteúdo atual
                    current_content += line.strip() + "\n"

    # Adicionar a última questão
    if current_question:
        data.append((current_question, current_content, current_options['A'], current_options['B'], current_options['C'], current_options['D']))

    # Fechar o arquivo PDF
    pdf_file.close()

    # Retornar as questões e respostas
    return data

def write_to_excel(data, output_file):
    # Criar um DataFrame a partir dos dados
    df = pd.DataFrame(data, columns=['Tópico', 'Conteúdo', 'A', 'B', 'C', 'D'])

    # Escrever o DataFrame no arquivo Excel
    df.to_excel(output_file, index=False)

# Caminho do arquivo PDF e nome do arquivo Excel de saída
pdf_path = 'AWS Certified Solutions Architect - Associate SAA-C03 Exam 10 02 24(T).pdf'
excel_output_path = 'teste1.xlsx'

# Ler todas as questões e respostas do PDF
pdf_data = read_pdf(pdf_path)

# Escrever as questões e respostas no arquivo Excel
write_to_excel(pdf_data, excel_output_path)

print(f"Todas as questões e respostas do PDF foram escritas em {excel_output_path}")
