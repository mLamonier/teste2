import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from PIL import Image
from io import BytesIO
import time

# Diretório para salvar as imagens
save_directory = 'Caderno de Atividades - Internet 3.0 Kids'

# Configura o webdriver com opções adicionais
chrome_options = Options()
chrome_options.add_argument("--headless")  # Executa em modo headless
chrome_options.add_argument('--no-sandbox')  # Bypass OS security model
chrome_options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Desabilita mensagens de logging do navegador
chrome_options.add_argument("window-size=1920x1080")  # Define o tamanho da janela do navegador
chrome_options.add_argument("force-device-scale-factor=2.0")  # Ajusta o fator de escala do dispositivo
chrome_options.add_argument("high-dpi-support=2.0")  # Suporte para DPI alto

service = Service('C:/chromedriver/chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

# Abre a primeira página
driver.get('https://www.apodigi.melhorsde.com.br/melhor/word2021/mobile/index.html#p=1')
time.sleep(2)  # Espera inicial para carregamento completo da primeira página

def capture_page(page_number):
    # Tira screenshot da página atual
    screenshot = driver.get_screenshot_as_png()
    image = Image.open(BytesIO(screenshot))
    
    # Define as coordenadas da área a ser mantida (excluir as áreas vermelhas)
    left = 500  # Ajuste conforme necessário
    top = 50  # Ajuste conforme necessário
    right = image.width - 500  # Ajuste conforme necessário
    bottom = image.height - 100  # Ajuste conforme necessário
    image = image.crop((left, top, right, bottom))
    
    image_path = os.path.join(save_directory, f'page_{page_number}.png')
    image.save(image_path)
    print(f"Page {page_number} captured at {image_path}.")

    # Encontra e clica no botão "Next"
    next_button = driver.find_element(By.XPATH, "//img[contains(@src,'next_normal.png')]")
    next_button.click()
    time.sleep(2)  # Aguarda a próxima página carregar após o clique

total_pages = 117  # Número de páginas para capturar

for page_number in range(1, total_pages + 1):
    capture_page(page_number)

driver.quit()
print("Todas as páginas foram capturadas e o driver foi fechado.")
