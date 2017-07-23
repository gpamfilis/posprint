import json


def get_configuration():
    f1 = open('/boot/e_orders_config.json', 'r')
    lines = f1.readlines()[0]
    f1.close()
    raw = [l.split('=') for l in lines.split(',')]
    vals = []
    for r in raw:
        try:
            vals.append({r[0]: int(r[1])})
        except Exception as e:
            vals.append({r[0]: r[1]})
    final = {}
    for v in vals:
        final.update(v)
    data = 'values.json'
    with open(data, 'w') as outfile:
        json.dump(final, outfile)

if __name__ == '__main__':
    get_configuration()