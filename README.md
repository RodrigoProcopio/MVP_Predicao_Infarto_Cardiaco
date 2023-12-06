# Preditor de Infarto Cardíaco - MVP


O infarto cardíaco, conhecido como ataque cardíaco, é uma grave condição que afeta pessoas de todas as idades, representando uma importante causa de morbidade e mortalidade global. 
Este evento ocorre quando o fornecimento de sangue para uma parte do músculo cardíaco é bloqueado, resultando em danos irreversíveis.

O impacto do infarto cardíaco na saúde pública é significativo, exigindo medidas preventivas para reduzir sua incidência. 
Adotar bons hábitos de vida, como alimentação saudável, prática regular de exercícios e controle de fatores de risco, é crucial para prevenir complicações.

Este projeto passou por um processo de criação de um modelo de machine learning em um notebook no Google Colab, que pode ser encontrado [neste link](https://colab.research.google.com/drive/1ZWDelNTwBCxxQhLnRLcA90jnO9474fxV?usp=sharing).

O problema foi abordado como um processo de classificação, com modelagem, inferência, criação e avaliação de modelos.

Os dados passaram por normalização e ajustes de hiperparâmetros, sendo que o modelo com melhor acurácia foi o Naive Bayes. 
Posteriormente, um arquivo pkl do modelo treinado foi gerado e incorporado ao backend deste sistema, servindo como modelo treinado para as predições.

Ao fornecer informações personalizadas, busca-se conscientizar sobre a importância da avaliação de riscos individuais e promover a adoção de um estilo de vida saudável. 
O projeto visa contribuir para uma sociedade mais saudável e resiliente diante dessa condição cardiovascular.

Você pode conferir o vídeo sobre o projeto, [neste link](https://youtube.com).

## Descrição

O sistema permite que os usuários respondam um questionário que visa obter dados sobre: Idade, Sexo, Colesterol, Batimento cardíaco, Diabetes, Histórico na família, Fumante, Obesidade,
Consumo de álcool, Dieta, Problema cardíaco, Uso de medicação, Nível de estresse, Triglicerídeos, Atividade física na semana, Horas de sono.

Com esses dados é possível realizar uma predição de risco de infarto cardíaco, utilizando o modelo de machine learning Naive Bayes (NB). 

O backend pode ser encontrado [aqui](https://github.com/RodrigoProcopio/MVP_Predicao_Infarto_Cardiaco/tree/main/MVP_Predicao_Infarto_Cardiaco_API).

O front pode ser encontrado [aqui](https://github.com/RodrigoProcopio/MVP_Predicao_Infarto_Cardiaco/tree/main/MVP_Predicao_Infarto_Cardiaco_Front).

## Notas de Versão

### Versão 1.0.0 (novembro/2023)

- Funcionalidade de inserir dados através de um questionário.
- Gerar uma predição.
   
## Autor

Este projeto foi desenvolvido por Rodrigo Procópio e pode ser encontrado no [GitHub](https://github.com/RodrigoProcopio).

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](https://github.com/RodrigoProcopio/MVP_Predicao_Infarto_Cardiaco/blob/main/LICENSE)  para obter detalhes.
