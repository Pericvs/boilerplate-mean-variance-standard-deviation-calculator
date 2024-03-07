import numpy as np


def calculate(numbers):
    if len(numbers) < 9:
        raise ValueError('List must contain nine numbers.')
        sys.exit(1)
    a=np.reshape(numbers,(3,3))
    output={
        'mean':[a.mean(0).tolist(), a.mean(1).tolist(), a.mean().tolist()],
        'variance':[a.var(0).tolist(), a.var(1).tolist(), a.var().tolist()],
        'standard deviation':[a.std(0).tolist(), a.std(1).tolist(), a.std().tolist()],
        'max':[a.max(0).tolist(), a.max(1).tolist(), a.max().tolist()],
        'min':[a.min(0).tolist(), a.min(1).tolist(), a.min().tolist()],
        'sum':[a.sum(0).tolist(), a.sum(1).tolist(), a.sum().tolist()],
}
    return output