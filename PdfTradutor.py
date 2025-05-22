import os
import zipfile
from PyPDF2 import PdfReader
from deep_translator import GoogleTranslator
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def translate_line(line, source="en", target="pt"):
    try:
        return GoogleTranslator(source=source, target=target).translate(line)
    except Exception as e:
        print(f"Erro ao traduzir a linha: {line}. Detalhes: {e}")
        return line or ""  # Retorna a linha original ou uma string vazia em caso de erro

def translate_pdf(input_pdf_path, output_dir, output_zip_path):
    # Leitor do PDF
    reader = PdfReader(input_pdf_path)

    # Certifique-se de que o diretório de saída existe
    os.makedirs(output_dir, exist_ok=True)

    translated_files = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""  # Garante que o texto não seja None

        # Traduzir linha por linha
        translated_lines = []
        for line in text.splitlines():
            if line and line.strip():  # Verifica se a linha não é None ou vazia
                translated_line = translate_line(line)
                translated_lines.append(translated_line)

        # Gerar um novo PDF traduzido para a página
        output_pdf_path = os.path.join(output_dir, f"page_{page_number}.pdf")
        translated_files.append(output_pdf_path)

        c = canvas.Canvas(output_pdf_path, pagesize=letter)
        c.setFont("Times-Roman", 12)

        y_position = 750  # Coordenada Y inicial
        line_height = 14  # Espaço entre linhas

        for line in translated_lines:
            if line:  # Garante que a linha não seja None ou vazia
                c.drawString(50, y_position, line.strip())
                y_position -= line_height
                if y_position < 50:  # Evitar ultrapassar os limites da página
                    c.showPage()
                    c.setFont("Times-Roman", 12)
                    y_position = 750

        c.save()

    # Compactar todos os arquivos traduzidos em um ZIP
    with zipfile.ZipFile(output_zip_path, 'w') as zipf:
        for file in translated_files:
            zipf.write(file, os.path.basename(file))

    print(f"Tradução concluída. Arquivos traduzidos salvos em: {output_zip_path}")

# Caminhos de entrada e saída
input_pdf_path = "PDF.pdf"  # Substitua pelo caminho do seu PDF
output_dir = "translated_pages"
output_zip_path = "translated_pages.zip"

translate_pdf(input_pdf_path, output_dir, output_zip_path)
