from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')
    
class ToVector(BaseEstimator, TransformerMixin):
    # To change to vectors for models that needs vectors
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        # Primero copiamos el dataframe de datos de entrada 'X'
        X_data = X.copy()
        X_columns = []
        for column in X_data.columns:
            X_columns.append([data for data in X_data[column]])
        num_muestras = len(X_columns[0])
        X_vectors = []
        for j in range(num_muestras):
            vector = []
            for i in range(len(X_data.columns)):
                vector.append(X_columns[i][j])
            X_vectors.append(vector)
        # X = X_vectors
        if y is not None:
            y_data = y.copy()
            y_column = [data for data in y_data["PROFILE"]]
            num_muestras = len (y_column)
            y_vector  = [y_column[i] for i in range(num_muestras)]
            # y = y_vector
            return X_vectors, y_vector
        # Devolvemos un nuevo dataframe de datos sin las columnas no deseadas
        return X_vectors
