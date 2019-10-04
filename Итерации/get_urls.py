from urls_utils import gen_from_urls

urls = ('http://ngs.ru', 'http://ya.ru', 'http://med54.ru')

for  resp_len, status, url in gen_from_urls(urls):
    print(resp_len, '->', status, '->', url)