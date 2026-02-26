import os
import sys

from dataclasses import dataclass
from typing import List, Tuple, Optional

import pandas as pd
import numpy as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder


TARGET = "Pago_atiempo"

COLUMNAS_NUMERIC = [
    "capital_prestado",
    "plazo_meses",
    "edad_cliente",
    "salario_cliente",
    "total_otros_prestamos",
    "cuota_pactada",
    "puntaje",
    "puntaje_datacredito",
    "cant_creditosvigentes",
    "huella_consulta",
    "saldo_mora",
    "saldo_principal",
    "saldo_mora_codeudor",
    "creditos_sectorFinanciero",
    "creditos_sectorCooperativo",
    "creditos_sectorReal",
    "promedio_ingresos_datacredito"
]

COLUMNAS_CATEGORIC = [
    "tipo_laboral",
    "tendencia_ingresos"
]

COLUMNAS_ORDINAL = [
    "tipo_credito"
]

EXCLUDE_X = [
    "fecha_prestamo",
]

def get_feature_columns(df):
    """
    Devuelve listas de columnas (numéricas, categóricas, ordinales)
    filtradas a las que realmente existen en el dataframe.
    """
    numeric = [c for c in COLUMNAS_NUMERIC if c in df.columns]
    cat = [c for c in COLUMNAS_CATEGORIC if c in df.columns]
    ord_ = [c for c in COLUMNAS_ORDINAL if c in df.columns]
    return numeric, cat, ord_


def build_preprocessor(numeric_cols, categorical_cols, ordinal_cols):
    """
    Construye el ColumnTransformer:
    - Numéricas: imputación por mediana
    - Categóricas: imputación most_frequent + OneHot
    - Ordinales: imputación most_frequent + OrdinalEncoder
    """
    transformers = []

    if numeric_cols:
        numeric_pipeline = Pipeline(steps=[
            ("imputer", SimpleImputer(strategy="median"))
        ])
        transformers.append(("num", numeric_pipeline, numeric_cols))

    if categorical_cols:
        categorical_pipeline = Pipeline(steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore", drop="first", sparse_output=False))
        ])
        transformers.append(("cat", categorical_pipeline, categorical_cols))

    if ordinal_cols:
        ordinal_pipeline = Pipeline(steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("ordinal", OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=-1))
        ])
        transformers.append(("ord", ordinal_pipeline, ordinal_cols))

    preprocessor = ColumnTransformer(
        transformers=transformers,
        remainder="drop"
    )
    return preprocessor


def split_data(df, target="Pago_atiempo"):
    """
    Split de datos en train/test.
    Se excluyen target + columnas EXCLUDE_X.
    """
    X = df.drop(columns=[target] + EXCLUDE_X, errors="ignore")
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )
    return X_train, X_test, y_train, y_test


def build_datasets(df, target="Pago_atiempo"):
    """
    Función final: arma todo lo necesario para el modelado.
    Devuelve:
    X_train, X_test, y_train, y_test, preprocessor
    """
    numeric_cols, cat_cols, ord_cols = get_feature_columns(df)
    X_train, X_test, y_train, y_test = split_data(df, target=target)
    preprocessor = build_preprocessor(numeric_cols, cat_cols, ord_cols)
    return X_train, X_test, y_train, y_test, preprocessor