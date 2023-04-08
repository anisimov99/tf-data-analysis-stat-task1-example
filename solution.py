import pandas as pd
import numpy as np


chat_id = 232587297 # Ваш chat ID, не меняйте название переменной


def solution(x: np.array) -> float:
    # v = a*t
    t = 10
    v = np.min(x) + 9 # почему min, и почему + 9?
    return v/t
