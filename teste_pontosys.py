from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configure automaticamente o ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Passo 1: Acessar o site da Ponto.Sys
    print("Tentando acessar o site da Ponto.Sys...")
    driver.get("https://pontosys.com")
    print("Site acessado com sucesso.")

    # Passo 2: Fechar o comunicado inicial (caso exista)
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
    try:
        print("Procurando o botão 'Chat de Atendimento'...")
        chat_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btnchat"))
        )
        chat_button.click()
        print("Botão 'Chat de Atendimento' clicado com sucesso.")
    except Exception as e:
        print(f"Erro ao clicar no botão 'Chat de Atendimento': {e}")
        driver.quit()
        exit()

    # Passo 4: Alternar para a nova aba ou janela
    try:
        print("Verificando se uma nova aba foi aberta...")
        WebDriverWait(driver, 10).until(
            lambda d: len(d.window_handles) > 1
        )
        driver.switch_to.window(driver.window_handles[-1])
        print("Alternado para a nova aba ou janela.")
    except Exception as e:
        print(f"Erro ao alternar para a nova aba ou janela: {e}")
        driver.quit()
        exit()

    # Passo 5: Aguardar a URL correta
    try:
        print("Aguardando mudança de URL...")
        WebDriverWait(driver, 20).until(
            lambda d: "chatsuporte" in d.current_url
        )
        current_url = driver.current_url
        print(f"URL atual após o clique: {current_url}")

        if "chatsuporte" not in current_url:
            raise Exception("Redirecionamento falhou. Página não é a esperada.")
        print("Redirecionado com sucesso para a página do formulário.")
    except Exception as e:
        print(f"Erro no redirecionamento: {e}")
        print(f"URL atual: {driver.current_url}")
        driver.quit()
        exit()

    # Passo 6: Preencher todos os campos do formulário
    try:
        print("Preenchendo os campos do formulário...")

        # Preencher campo 'Nome'
        nome_campo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ci"))
        )
        nome_campo.clear()
        nome_campo.send_keys("Caio Renato Rodrigues")
        print("Campo 'Nome' preenchido com sucesso.")

        # Preencher campo 'E-mail'
        email_campo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "chat-email"))
        )
        email_campo.clear()
        email_campo.send_keys("caioo.renato@outlook.com")
        print("Campo 'E-mail' preenchido com sucesso.")

        # Preencher campo 'Telefone'
        telefone_campo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "chat-telefone"))
        )
        telefone_campo.clear()
        telefone_campo.send_keys("(17) 99239-8283")
        print("Campo 'Telefone' preenchido com sucesso.")

        # Preencher campo 'CNPJ'
        cnpj_campo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "chat-cnpj"))
        )
        cnpj_campo.clear()
        cnpj_campo.send_keys("54.764.614/0001-79")
        print("Campo 'CNPJ' preenchido com sucesso.")

        # Preencher campo 'Razão Social'
        razao_campo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "chat-razao"))
        )
        razao_campo.clear()
        razao_campo.send_keys("Caio Imports")
        print("Campo 'Razão Social' preenchido com sucesso.")

        # Selecionar 'Segmento'
        segmento_campo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "chat-segmento"))
        )
        segmento_campo.clear()
        segmento_campo.send_keys("Perfumaria")
        print("Campo 'Segmento' preenchido com sucesso.")

        # Selecionar 'Departamento'
        departamento_campo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "chat-departamento"))
        )
        departamento_campo.clear()
        departamento_campo.send_keys("Suporte técnico")
        print("Campo 'Departamento' preenchido com sucesso.")

        # Selecionar 'Especialidade'
        especialidade_campo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "chat-especialidade"))
        )
        especialidade_campo.clear()
        especialidade_campo.send_keys("Sem acesso ao sistema / Vendas / Operação de caixa")
        print("Campo 'Especialidade' preenchido com sucesso.")

        # Preencher 'Descrição do problema'
        descricao_campo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "chat-descricao"))
        )
        descricao_campo.clear()
        descricao_campo.send_keys("Automação realizada com sucesso!")
        print("Campo 'Descrição do problema' preenchido com sucesso.")

        # Clicar no botão 'Iniciar Atendimento'
        iniciar_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        iniciar_button.click()
        print("Botão 'Iniciar Atendimento' clicado com sucesso.")

        # Verificar o redirecionamento para o chat
        print("Aguardando redirecionamento para a página de chat...")
        WebDriverWait(driver, 20).until(
            lambda d: "chatclient/chat.php" in d.current_url
        )
        print(f"Redirecionado para: {driver.current_url}")

    except Exception as e:
        print(f"Erro ao preencher os campos ou redirecionar: {e}")
        driver.quit()
        exit()

finally:
    # Aguarde para verificar o preenchimento manualmente
    print("A página permanecerá aberta para visualização.")
    input("Pressione Enter para fechar o navegador...")
    print("Fechando o navegador.")
    driver.quit()
