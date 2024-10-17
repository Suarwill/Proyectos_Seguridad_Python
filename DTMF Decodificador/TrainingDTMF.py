import librosa
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier

from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

# Carga el archivo de audio
y, sr = librosa.load('output.wav')

# Extrae características MFCC
mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=48)
mfcc_features = np.mean(mfccs, axis=1)

# Maneja características MFCC unidimensionales
if len(mfcc_features.shape) == 1:
    mfcc_features = mfcc_features.reshape(-1, 1)

# Crea un DataFrame con nombres de columnas adecuados
data = pd.DataFrame(mfcc_features, columns=['mfcc' if mfcc_features.shape[1] == 1 else 'mfcc_' + str(i) for i in range(mfcc_features.shape[1])])

# Define las etiquetas DTMF
labels = ['1', '2', '3', 'A', '4', '5', '6', 'B', '7', '8', '9', 'C', '*', '0', '#', 'D']

# Verifica la longitud del DataFrame (opcional)
print(f"Número de puntos de datos: {len(data)}")

# Asegura que la longitud de las etiquetas coincida con la longitud de los datos
num_repeats = int(np.ceil(len(data) / len(labels)))  # Redondea hacia arriba para cubrir todos los datos
labels = labels * num_repeats  # Repite las etiquetas para que coincidan con la longitud de los datos

# Asigna las etiquetas al DataFrame
data['etiqueta'] = labels

# Divide los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(data.drop('etiqueta', axis=1), data['etiqueta'], test_size=0.2)

# Crea y entrena el modelo KNN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Evalúa la precisión del modelo
accuracy = knn.score(X_test, y_test)
print("Precisión del modelo:", accuracy)

# Balanceo de clases (ejemplo con SMOTE)
smote = SMOTE(sampling_strategy='minority')
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

# Normalización de los datos
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_res)
X_test_scaled = scaler.transform(X_test)

# Grid search para encontrar el mejor valor de n_neighbors
param_grid = {'n_neighbors': np.arange(1, 15)}
grid = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5)
grid.fit(X_train_scaled, y_train_res)
best_knn = grid.best_estimator_

# Evaluación del modelo con el mejor valor de n_neighbors
accuracy = best_knn.score(X_test_scaled, y_test)
print("Precisión del modelo:", accuracy)

# Guarda el modelo para futuras predicciones
import pickle
with open('modelo_knn.pkl', 'wb') as f:
    pickle.dump(knn, f)