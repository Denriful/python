''' use function-generator '''

from urls_utils import gen_from_urls

import pprint

urls = ('http://ngs.ru', 'http://ya.ru', 'http://med54.ru')

for  resp_len, status, url in gen_from_urls(urls):
    print(resp_len, '->', status, '->', url)

print()


'''func gen inside dict gen'''

urls_res = {url: size for size, _, url in gen_from_urls(urls)}

pprint.pprint(urls_res)
