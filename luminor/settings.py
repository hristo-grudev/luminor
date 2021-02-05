BOT_NAME = 'luminor'

SPIDER_MODULES = ['luminor.spiders']
NEWSPIDER_MODULE = 'luminor.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'luminor.pipelines.LuminorPipeline': 100,

}