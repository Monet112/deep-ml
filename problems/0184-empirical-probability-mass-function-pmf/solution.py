def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    uniques=list(set(samples))
    counts=[]
    space=len(samples)
    for element in uniques:
        counts.append(samples.count(element))
    return [(uniques[i],counts[i]/space) for i in range(len(uniques))]