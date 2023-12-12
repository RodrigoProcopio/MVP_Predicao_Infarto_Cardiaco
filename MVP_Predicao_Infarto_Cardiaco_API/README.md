# Preditor de Infarto Cardíaco - MVP


O infarto cardíaco, conhecido como ataque cardíaco, é uma grave condição que afeta pessoas de todas as idades, representando uma importante causa de morbidade e mortalidade global. 
Este evento ocorre quando o fornecimento de sangue para uma parte do músculo cardíaco é bloqueado, resultando em danos irreversíveis.

O impacto do infarto cardíaco na saúde pública é significativo, exigindo medidas preventivas para reduzir sua incidência. 
Adotar bons hábitos de vida, como alimentação saudável, prática regular de exercícios e controle de fatores de risco, é crucial para prevenir complicações.

Este projeto, visando a prevenção, passou por um processo de criação de um modelo de machine learning utilizando o dataset disponível [neste link](https://github.com/RodrigoProcopio/CAD_Prediction_Database). 
O problema foi abordado como um processo de classificação, com modelagem, inferência, criação e avaliação de modelos.

Os dados passaram por normalização e ajustes de hiperparâmetros, sendo que o modelo com melhor acurácia foi o Naive Bayes. 
Posteriormente, um arquivo pkl do modelo treinado foi gerado e incorporado ao backend deste sistema, servindo como modelo treinado para as predições.

Ao fornecer informações personalizadas, busca-se conscientizar sobre a importância da avaliação de riscos individuais e promover a adoção de um estilo de vida saudável. 
O projeto visa contribuir para uma sociedade mais saudável e resiliente diante dessa condição cardiovascular.

O notebook no Google Colab pode ser encontrado [aqui](https://colab.research.google.com/drive/1ZWDelNTwBCxxQhLnRLcA90jnO9474fxV?usp=sharing).

O vídeo sobre projeto pode ser encontrado [aqui](https://www.youtube.com/watch?v=X-GpuFiQmlg).

O vídeo com a execução do Pytest pode ser encontrado [aqui](https://www.loom.com/share/ec108e418e8548f19ce46d64cff50e8e?sid=ac087b51-ae5a-4de9-ab86-473f4754f1c9).

O back-end pode ser encontrado [aqui](https://github.com/RodrigoProcopio/MVP_Predicao_Infarto_Cardiaco/tree/main/MVP_Predicao_Infarto_Cardiaco_API).

O front-end pode ser encontrado [aqui](https://github.com/RodrigoProcopio/MVP_Predicao_Infarto_Cardiaco/tree/main/MVP_Predicao_Infarto_Cardiaco_Front).


## Requisitos

Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal.

Certifique-se de que você tenha  todas as libs python listadas no `requirements.txt` instaladas.

Este comando instala as bibliotecas, descritas no arquivo `requirements.txt`:

pip install -r requirements.txt

## Como Usar

Para utilizar esta API, siga os passos abaixo:

1. Inicie a aplicação Flask:

  flask run --host 0.0.0.0 --port 5000

2. Acesse a documentação Swagger para obter detalhes sobre as rotas e os parâmetros necessários.

3. Use as rotas para adicionar, visualizar ou remover dados de pacientes.

## Documentação Swagger

Para obter a documentação completa desta API no estilo Swagger, acesse: 
[http://localhost:5000//openapi/swagger#/](http://localhost:5000//openapi/swagger#/)

## Rotas da API

- [GET] `/paciente`

  Faz a busca por um paciente cadastrado na base a partir do ID.

- [POST] `/medicamento`

  Faz a adição de um novo paciente na base de dados.

  - **Entrada**: Um objeto JSON com os dados do paciente.
  - **Saída**: Uma representação dos dados do paciente cadastrados.

- [DELETE] `/paciente_id`

  Deleta um paciente a partir do ID do paciente informado.

- [GET] `/pacientes`

  Lista todos os pacientes cadastrados na base.

## Teste Automatizado
- Para executar o pytest utilize o seguinte comando:

  pytest -v test_modelos.py

## Notas de Versão

### Versão 1.0.0 (novembro/2023)

- Implementação inicial da API.
- Funcionalidade de adicionar, visualizar e remover dados de pacientes.

## Autor

Este projeto foi desenvolvido por Rodrigo Procópio e pode ser encontrado no [GitHub](https://github.com/RodrigoProcopio).

## Segurança e Confidencialidade

Visando a segurança e confidencialidade, este sistema não coleta dados sensíveis dos usuários.

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](https://github.com/RodrigoProcopio/MVP_Predicao_Infarto_Cardiaco/blob/main/MVP_Predicao_Infarto_Cardiaco_API/LICENSE.md) para obter detalhes.
