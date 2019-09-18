# start.py
from scrapy import cmdline

# 续爬模式，会自动生成一个crawls文件夹，用于存放断点文件
# cmdline.execute('scrapy crawl mySpider -s JOBDIR=crawls/storemySpider'.split())
keysList = ["mm131","meizitu","meizitu0","ishuhui","sgacg","dmzj","mzitu"]
keys = keysList[6]
book = "tzdgzsnldydszldmfs"
cmd = 'scrapy crawl %s -a book=%s -o scr_%s.jl -s CLOSESPIDER_ITEMCOUNT=3' % (keys,book,keys)

# 非续爬模式
cmdline.execute(cmd .split())
# cmd  =" scrapy runspider scrapy_sample/spiders/dmzj_spider.py  -a book=tzdgzsnldydszldmfs"