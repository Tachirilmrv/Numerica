import numpy as np

from joblib import Parallel, delayed



def random_square(seed):
    np.random.seed(seed)

    random_num = np.random.randint(0, 10)

    return random_num ** 2

results = Parallel(n_jobs = -1, backend = "multiprocessing", verbose = 1) \
    (delayed(random_square)(i) for i in range(1000000) )