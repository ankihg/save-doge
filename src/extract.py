from craigslist import CraigslistForSale

def query_craigslist():
    print('query_craigslist')
    cl_h = CraigslistForSale(site='seattle', category='foa',
                             filters={'query': 'xxx'})

    # for result in cl_h.get_results(sort_by='newest'):
    #     print(result)
    return cl_h.get_results(sort_by='newest')
