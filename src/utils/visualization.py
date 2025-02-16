import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_fuel_type_count(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(x=df["fuel_type"], palette="viridis", ax=ax)
    ax.set_xlabel("Tipo de Combustible")
    ax.set_ylabel("Cantidad de Vehículos")
    ax.set_title("Cantidad de Vehículos por Tipo de Combustible")
    ax.grid()
    return fig

def plot_price_distribution(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(df['price'], bins=30, kde=True, ax=ax, color='blue')
    ax.set_xlabel("Precio del Vehículo")
    ax.set_ylabel("Frecuencia")
    ax.set_title("Distribución de Precios de Vehículos")
    return fig


