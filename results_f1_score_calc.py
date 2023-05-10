def f1_score(precision, recall) -> float:
    if (precision + recall) == 0:
        return 0
    return (2 * precision * recall) / (precision + recall)


def precision(res: list[float]) -> float:
    tp, fp, tn, fn = res
    denominator = tp + fp
    if denominator == 0:
        return 0.0
    return tp / denominator


def recall(res: list[float]) -> float:
    tp, fp, tn, fn = res
    denominator = tp + fn
    if denominator == 0:
        return 0.0
    return tp / denominator


if __name__ == '__main__':
    # [TP, FP, TN, FN]
    knn = [4, 0, 5, 1]
    mlp = [4, 1, 4, 1]
    rf = [0, 0, 5, 5]
    logit = [3, 0, 5, 2]

    models = [knn, mlp, rf, logit]

    print(f1_score(precision(knn), recall(knn)))
    print(f1_score(precision(mlp), recall(mlp)))
    print(f1_score(precision(rf), recall(rf)))
    print(f1_score(precision(logit), recall(logit)))
