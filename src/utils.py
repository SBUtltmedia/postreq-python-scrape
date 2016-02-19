def flatten(nested_list):
    def f(x):
        for i in x:
            if isinstance(i, list) or isinstance(i, tuple):
                yield from flatten(i)
            else:
                yield i
    return list(f(nested_list))
