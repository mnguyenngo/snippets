def expand_dict(d, tabs=0, expand=False):
    for k in d:
        if not expand:
            print("  "*(tabs-1) + "{}".format(k))
            if type(d[k]) == dict:
                tabs += 1
                expand_dict(d[k], tabs, expand)
                tabs -= 1
        if expand:
            if type(d[k]) == dict:
                print("  "*(tabs-1) + "{}".format(k))
                tabs += 1
                expand_dict(d[k], tabs, expand)
                tabs -= 1
            elif type(d[k]) == list:
                print("  "*(tabs-1) + "{}: list".format(k))
            elif type(d[k]) == set:
                print("  "*(tabs-1) + "{}: set".format(k))
            else:
                print("  "*(tabs-1) + "{}: {}".format(k, d[k]))
