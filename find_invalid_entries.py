import hashlib
import json

items = ['name', 'address']

def main():
    """
    1.load data as string from file(considering file is present in same path as script).
    2.convert to json
    3. to find invalid ids
        i. each row, check for null name, address, zip
        ii.if zip is present and valid.
            * should be present
            * should be either 5 digits
            * should not be all zero's
        iii. observed extra case from data.json that ID is duplicated.
    """
    data_file = './data.json'
    data = []
    with open(data_file) as fd:
        data = json.load(fd)

    invalids = []
    cache = {}
    for item in data:
        hshlib = hashlib.md5()
        hshlib.update(str(item).encode('utf8'))
        hash_id = hshlib.hexdigest()
        if hash_id in cache:
            invalids.append(item['id'])
            continue
        cache[hash_id] = 1
        s = 0
        for ele in items:
            if not(ele in item and item[ele]):
                invalids.append(item['id'])
                s = 1
                break
        if s:
            continue
        if not('zip' in item and item['zip'] and len(item['zip']) == 5 \
                and item['zip'].isdecimal() and item['zip'] != '00000'):
            invalids.append(item['id'])
    return invalids

if __name__ == "__main__":
    invalids = main()
    for item in invalids:
        print(item)
