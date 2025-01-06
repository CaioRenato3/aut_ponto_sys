from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuração do WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Passo 1: Acessar o site da Ponto.Sys
    print("Tentando acessar o site da Ponto.Sys...")
    driver.get("https://pontosys.com")
    print("Site acessado com sucesso.")

    # Passo 2: Fechar o popup inicial 
    try:
        print("Procurando pelo popup inicial...")
        close_popup = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
        )
        close_popup.click()
        print("Popup inicial fechado com sucesso.")
    except Exception as e:
        print(f"Popup não encontrado ou já fechado: {e}")

    # Passo 3: Clicar no botão 'Chat de Atendimento'
    print("Procurando o botão 'Chat de Atendimento'...")
    chat_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "btnchat"))
    )
    chat_button.click()
    print("Botão 'Chat de Atendimento' clicado com sucesso.")

    # Passo 4: Alternar para a nova aba ou janela
    print("Verificando se uma nova aba foi aberta...")
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
    driver.switch_to.window(driver.window_handles[-1])
    print("Alternado para a nova aba ou janela.")

    # Passo 5: Preencher os campos do formulário
    print("Preenchendo os campos do formulário...")
    campos = {
        "ci": "Caio Renato Rodrigues",
        "chat-email": "caioo.renato@outlook.com",
        "chat-telefone": "(17) 99239-8283",
        "chat-cnpj": "54.764.614/0001-79",
        "chat-razao": "Caio Imports",
        "chat-segmento": "Perfumaria",
        "chat-departamento": "Suporte técnico",
        "chat-especialidade": "Sem acesso ao sistema / Vendas / Operação de caixa",
        "chat-descricao": "Automação realizada com sucesso!",
    }

    for campo_id, valor in campos.items():
        campo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, campo_id))
        )
        campo.clear()
        campo.send_keys(valor)
        print(f"Campo '{campo_id}' preenchido com sucesso.")

    # Clicar no botão 'Iniciar Atendimento'
    iniciar_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    iniciar_button.click()
    print("Botão 'Iniciar Atendimento' clicado com sucesso.")

    # Passo 6: Aguardar a página de chat carregar
    print("Aguardando a página de chat carregar...")

     # Obter identificadores de todas as guias
    all_tabs = driver.window_handles

    # Trocar para a nova guia (última aberta)
    driver.switch_to.window(all_tabs[-1])

    # Interagir com elementos na nova guia
    try:
        time.sleep(10)

        print("Tentando clicar no botão 'Encerrar'...")

        # Localizar o botão 'Encerrar'
        encerrar_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "end-chat"))
        )
        encerrar_button.click()

        time.sleep(5)

        # Confirmar o encerramento, se necessário
        confirmar_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "end-chat-confirm"))
        )
        confirmar_button.click()
        print("Confirmação de encerramento realizada com sucesso.")

        time.sleep(5)
        
        # 
        sair_chat = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "close-chat"))
        )
        sair_chat.click()
    except Exception as e:
        print(f"Erro ao clicar no botão 'Encerrar': {e}")

except Exception as e:
    print(f"Erro durante o processo: {e}")
finally:
    print("A página permanecerá aberta para visualização.")
    input("Pressione Enter para fechar o navegador...")
    driver.quit()
