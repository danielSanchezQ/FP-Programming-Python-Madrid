from functools import reduce




myMap    = lambda f,    l : reduce(lambda x, y: x+[f(y)],                l, [])
myFilter = lambda cond, l : reduce(lambda x, y: x+[y] if cond(y) else x, l, [])



if __name__ == "__main__":
    l = range(10)
    map_res   = map(lambda x: x*x, l)
    mymap_res = myMap(lambda x: x*x, l)
    print(list(map_res) == list(mymap_res))
    l2 = range(100)
    filter_res   = filter(lambda x: x%7, l2)
    myfilter_res = myFilter(lambda x: x%7, l2)
    print(list(filter_res) == list(myfilter_res))
