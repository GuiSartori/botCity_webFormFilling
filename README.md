# BotCity Web Form Filling

Este projeto é um bot desenvolvido com BotCity para preencher formulários automaticamente usando dados de um arquivo Excel.

## Aviso

Certifique-se de instalar as dependências do bot com `pip install --upgrade -r requirements.txt` para obter todas as dependências no seu ambiente Python.

Além disso, se você estiver usando o PyCharm ou outro IDE, certifique-se de usar o MESMO interpretador Python que o seu IDE.

Se você receber um erro como:

ModuleNotFoundError: No module named 'botcity'


Isso significa que você provavelmente está usando um interpretador Python diferente daquele usado para instalar as dependências. Para corrigir isso, você pode:
- Usar o mesmo interpretador que o seu IDE e instalar o bot com `pip install --upgrade -r requirements.txt`
- Usar o mesmo interpretador que foi usado para instalar o bot (`pip install --upgrade -r requirements.txt`)

Por favor, consulte a documentação para mais informações em [BotCity Documentation](https://documentation.botcity.dev/tutorials/python-automations/web/).

## Como Usar

1. Clone o repositório:
    ```bash
    git clone https://github.com/GuiSartori/botCity_webFormFilling.git
    cd botCity_webFormFilling
    ```

2. Instale as dependências:
    ```bash
    pip install --upgrade -r requirements.txt
    ```

3. Configure o caminho do WebDriver no arquivo principal do bot:
    ```python
    bot.driver_path = r"C:\Users\guilh\Documents\BotCity\Drivers\msedgedriver.exe"
    ```

4. Execute o bot:
    ```bash
    python main.py
    ```

## Estrutura do Projeto

- `main.py`: Script principal que contém a lógica do bot.
- `requirements.txt`: Arquivo com as dependências do projeto.
- `data/Data.xlsx`: Arquivo Excel com os dados para preenchimento do formulário.

## Contribuição

Se você quiser contribuir com este projeto, sinta-se à vontade para abrir um pull request ou relatar problemas na seção de issues.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
