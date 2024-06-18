# poderada_MNIST
Usando o MNIST para convolução

# Detecção de Algarismos Manuscritos com Flask e Keras

Este projeto consiste em um sistema de backend desenvolvido em Flask que utiliza modelos de redes neurais convolucionais (CNN) e lineares, treinados com o dataset MNIST, para detectar algarismos manuscritos em imagens.

# Treinando o modelo
O modelo foi treinado com o dataset MNIST, que é um conjunto de dados de imagem. Foi treinado no COLAB e foram salvados com o nome de:

- `modelo_top.h5`: Pesos do modelo convolucional treinado.
- `linear_modelo_mnist.h5`: Pesos do modelo linear treinado.

Segue link do COLAB onde ocorreu o treinamento
(link_do_colab)[https://colab.research.google.com/drive/1XlHCURqXymAMdCrK67DkkpUUxWBgSXHd#scrollTo=n3rizq_3rexQ]

# Como executar o projeto
1. Clone o repositório.

```bash
git clone https://github.com/MuriloDeSouza/poderada_MNIST.git
```

2. Entre na pasta do projeto.

```bash
cd poderada_MNIST
```

3. Execute o script `app.py`.
Esteja no diretório correto para poder rodar o código: app/

```bash
python app.py
```

Pode tirar um print de um número como por exemplo esse aqui e salve no seu computador onde desejar:
(Imagem)[7.png]

4. Abra o navegador e acesse o endereço `http://127.0.0.1:5000

5. Clique no botão "Escolher arquivo" e selecione a imagem que você salvou.

6. Clique no botão "Enviar" para enviar a imagem para o servidor.

7. O servidor irá processar a imagem e exibir o resultado na página.

8. Para encerrar o servidor, pressione `Ctrl + C` no terminal.

## Estrutura do Projeto

- `app.py`: Script principal do backend Flask.
- `train_model.py`: Script para treinar e salvar o modelo convolucional.
- `train_linear_model.py`: Script para treinar e salvar o modelo linear.
- `templates/upload.html`: Página HTML para upload de imagens e exibição dos resultados.
- `modelo_top.h5`: Pesos do modelo convolucional treinado.
- `linear_modelo_mnist.h5`: Pesos do modelo linear treinado.

## Dependências

Para rodar este projeto, você precisará instalar as seguintes bibliotecas Python:

```bash
pip install numpy tensorflow flask pillow

pip install - r requirements.txt
```
# Vídeo de funcionamento do projeto:
Segue link do funcionamento do projeto:
(link)[https://drive.google.com/file/d/1tjqA7BixrtnSYQbSGbnN_fjhVoJ0PRGx/view?usp=sharing]

# Autor

Murilo de Souza Prianti Silva