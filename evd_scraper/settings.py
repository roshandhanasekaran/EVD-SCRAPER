# Scrapy settings for evd_scraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "evd_scraper"

SPIDER_MODULES = ["evd_scraper.spiders"]
NEWSPIDER_MODULE = "evd_scraper.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "evd_scraper (+http://www.yourdomain.com)"


# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "evd_scraper.middlewares.EvdScraperSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    "evd_scraper.middlewares.EvdScraperDownloaderMiddleware": 543,
    "evd_scraper.middlewares.ScrapeOpsFakeUserAgentMiddleware": 400,
    #'rotating_proxies.middlewares.RotatingProxyMiddleware': 510,
    #'rotating_proxies.middlewares.BanDetectionMiddleware': 520,
    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
    #'evd_scraper.middlewares.ScrapeOpsFakeBrowserHeaderAgentMiddleware': 300
}


# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "evd_scraper.pipelines.EvdScraperPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Enable a delay for requests for the same website
#DOWNLOAD_DELAY = 2  # 2 seconds of delay

# # Enable randomization of download delay
#RANDOMIZE_DOWNLOAD_DELAY = True

# # Set a custom user-agent to mimic a real browser
# USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

# # Enable or disable the AutoThrottle extension
# AUTOTHROTTLE_ENABLED = True
# AUTOTHROTTLE_START_DELAY = 1  # The initial download delay
# AUTOTHROTTLE_MAX_DELAY = 10  # The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0  # Average number of requests Scrapy should be sending in parallel to each remote server
# AUTOTHROTTLE_DEBUG = False  # Enable showing throttling stats for every response received


# # Add the rotating proxies middleware
# DOWNLOADER_MIDDLEWARES = {
#     'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
#     'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
# }

# # List of proxies
# ROTATING_PROXY_LIST = [
#     'proxy1.com:8000',
#     'proxy2.com:8031',
#     # Add more proxies here
# ]

# # Optional settings for rotating proxies
#ROTATING_PROXY_PAGE_RETRY_TIMES = 5  # Number of times to retry a request with a different proxy
# ROTATING_PROXY_BACKOFF_BASE = 300  # Base backoff time in seconds

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"



SCRAPEOPS_API_KEY = 'f9ceaf1b-1d37-49dc-a13f-d7f670405622'
SCRAPEOPS_FAKE_USER_AGENT_ENDPOINT = "https://headers.scrapeops.io/v1/user-agents"
SCRAPEOPS_FAKE_USER_AGENT_ENABLED = True
SCRAPEOPS_NUM_RESULTS= 100

# settings.py
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5  # The initial download delay (in seconds)
AUTOTHROTTLE_MAX_DELAY = 60   # The maximum download delay (in seconds) in case of high latencies
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0  # The average number of requests Scrapy should be sending in parallel to each remote server
AUTOTHROTTLE_DEBUG = False  # Enable showing throttling stats for every response received




SCRAPEOPS_API_KEY = 'f9ceaf1b-1d37-49dc-a13f-d7f670405622'
SCRAPEOPS_PROXY_ENABLED = True



#SCRAPEOPS_API_KEY = 'f9ceaf1b-1d37-49dc-a13f-d7f670405622'
#SCRAPEOPS_FAKE_BROWSER_HEADER_ENABLED = True


SCRAPEOPS_API_KEY = 'f9ceaf1b-1d37-49dc-a13f-d7f670405622'
SCRAPEOPS_PROXY_ENABLED = True
#SCRAPEOPS_PROXY_SETTINGS = {'country': 'uk'}


