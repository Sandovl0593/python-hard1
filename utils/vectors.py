import numpy as np


def cosine_similarity(v1: np.ndarray, v2: np.ndarray) -> float:
    """
    Retorna la similitud coseno entre dos vectores
    """
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))



def euclidean_distance(v1: np.ndarray, v2: np.ndarray) -> float:
    """
    Retorna la distancia euclidiana entre dos vectores
    """
    return np.sqrt(np.sum((v1 - v2) ** 2))



def manhattan_distance(v1: np.ndarray, v2: np.ndarray) -> float:
    """
    Retorna la distancia de Manhattan entre dos vectores
    """
    return np.sum(np.abs(v1 - v2))



def jaccard_similarity(v1: np.ndarray, v2: np.ndarray) -> float:
    """
    Retorna la similitud de Jaccard entre dos vectores
    """
    return np.sum(np.minimum(v1, v2)) / np.sum(np.maximum(v1, v2))



def unitarize(v: np.ndarray) -> np.ndarray:
    """
    Normaliza un vector (vector unitario)
    """
    return v / np.linalg.norm(v)

