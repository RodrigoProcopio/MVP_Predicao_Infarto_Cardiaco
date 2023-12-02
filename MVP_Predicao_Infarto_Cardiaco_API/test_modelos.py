from model.avaliador import Avaliador
from model.carregador import Carregador
from model.modelo import Model

# Instanciação das Classes
carregador = Carregador()
modelo = Model()
avaliador = Avaliador()

# Parâmetros    
url_dados = "database/Heart_Attack_Prediction.csv"
colunas = ['Age', 'Sex', 'Cholesterol', 'Heart Rate', 'Diabetes', 'Family History', 'Smoking', \
            'Obesity', 'Alcohol Consumption', 'Diet', 'Previous Heart Problems', 'Medication Use', \
            'Stress Level', 'Triglycerides', 'Physical Activity Days Per Week', 'Sleep Hours Per Day', 'Heart Attack Risk'  ]

# Carga dos dados
dataset = carregador.carregar_dados(url_dados, colunas)

# Separando em dados de entrada e saída
X = dataset.iloc[:, 0:-1]
Y = dataset.iloc[:, -1]
    
# Método para testar o modelo de Regressão Logística a partir do arquivo correspondente
# Ajustes no teste test_modelo_lr
def test_modelo_lr():
    # Importando o modelo de regressão logística
    lr_path = 'ml_model/modelo_reglog.pkl'
    scaler_path = 'ml_model/scaler_reglog.pkl'
    modelo_lr, scaler_lr = Model.carrega_modelo(lr_path, scaler_path)
    
    # Obtendo as métricas da Regressão Logística
    acuracia_lr = avaliador.avaliar(modelo_lr, X, Y)
    
    # Testando as métricas da Regressão Logística
    assert acuracia_lr >= 0.64

# Ajustes no teste test_modelo_nb
def test_modelo_nb():
    # Importando modelo NB
    nb_path = 'ml_model/modelo_naive_bayes.pkl'
    scaler_path = 'ml_model/scaler.pkl'
    modelo_nb, scaler_nb = Model.carrega_modelo(nb_path, scaler_path)
    
    # Obtendo as métricas do NB
    acuracia_nb = avaliador.avaliar(modelo_nb, X, Y)
    
    # Testando as métricas do NB
    assert acuracia_nb >= 0.64
