def ft_statistics(*args: any, **kwargs: any) -> None:
    """
This function take in *args a quantity of unknown number and make the Mean,
Median, Quartile (25% and 75%), Standard Deviation and Variance according
to the **kwargs ask
    """
    try:
        for val in kwargs.values():
            larg = len(args)
            if larg == 0:
                print("ERROR")
                continue
            sarg = sorted(args)
            if val == "mean":
                res = sum(sarg) / larg
                print("mean :", res)
            elif val == "median":
                res = sarg[larg // 2] if larg % 2 == 1 else sarg[larg // 2 + 1]
                print("median :", res)
            elif val == "quartile":
                q25 = sarg[int(0.25 * larg)]
                q75 = sarg[int(0.75 * larg)]
                res = [float(q25), float(q75)]
                print("quartile :", res)
            elif val == "std":
                mean = sum(sarg) / larg
                var = sum(pow(x - mean, 2) for x in args) / larg
                res = var ** 0.5
                print("std :", res)
            elif val == "var":
                mean = sum(sarg) / larg
                res = sum(pow(x - mean, 2) for x in args) / larg
                print("var :", res)
    except Exception as e:
        print(f"ERROR: {e}")
