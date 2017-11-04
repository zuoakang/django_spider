# -*- coding: utf-8 -*-

# Scrapy settings for Jdcomments project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Jdcomments'

SPIDER_MODULES = ['Jdcomments.spiders']
NEWSPIDER_MODULE = 'Jdcomments.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Jdcomments (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False


# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'Jdcomments.pipelines.JdcommentsPipeline': 300,
   # 'Jdcomments.pipelines.JdproductsPipelines':200,
}

EXTENSIONS = {
    'scrapy.extensions.logstats.LogStats': 1,
    #'scrapy.webservice.WebService': 500,
    #'scrapy.telnet.TelnetConsole': 500,
}


# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
#     'Jdcomments.middlewares.ProxyMiddleware': 100,
# }
DOWNLOAD_DELAY = 0.25


#指定使用scrapy-redis的Scheduler
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

#选择去重class
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 在redis中保持scrapy-redis用到的各个队列，从而允许暂停和暂停后恢复
SCHEDULER_PERSIST = False

# 指定排序爬取地址时使用的队列，默认是按照优先级排序
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
# 可选的先进先出排序
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderQueue'
# 可选的后进先出排序
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderStack'

DOWNLOAD_TIMEOUT = 300

# 指定RedisPipeline用以在redis中保存item

#mysql Master
MYSQL_IP='localhost'
MYSQL_PORT='3306'
MYSQL_NAME='root'
MYSQL_PASSWORD='123456'
MYSQL_DATABASE='python'

# 指定redis的连接参数 Master
# REDIS_PASS是我自己加上的redis连接密码，需要简单修改scrapy-redis的源代码以支持使用密码连接redis
REDIS_HOST = 'localhost'
REDIS_PORT = 6379


LOG_LEVEL = 'DEBUG'

