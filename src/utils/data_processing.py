import pandas as pd

def load_and_clean_data(url: str) -> pd.DataFrame:
    """
    Carga un dataset desde una URL, limpia duplicados, 
    elimina valores nulos en 'brand' y formatea nombres de columnas.
    """
    try:
        # Cargar el dataset desde la URL
        df = pd.read_csv(url)
        
        # Eliminar duplicados
        df.drop_duplicates(inplace=True)
        
        # Eliminar filas donde 'brand' tenga valores nulos
        if 'brand' in df.columns:
            df.dropna(subset=['brand'], inplace=True)

        # Rellenar valores NaN con el método forward fill (sin advertencia)
        df.ffill(inplace=True)

        # Convertir nombres de columnas a snake_case
        df.columns = [col.lower().replace(" ", "_") for col in df.columns]

        return df

    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return pd.DataFrame()  # Retorna un DataFrame vacío en caso de error

# URL del dataset
url = "https://raw.githubusercontent.com/anfagudelogo-tpt/datasets/refs/heads/main/car_price_dataset.csv"

# Cargar y limpiar datos
df = load_and_clean_data(url)

# Mostrar las primeras filas del dataset ya limpio
print(df.head())

