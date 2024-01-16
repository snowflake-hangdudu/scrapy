#使用那个爬虫，先导入爬虫类，然后在if __name__ == '__main__'添加爬虫
from hangdudu.spiders.baidu import BaiduSpider

# scrapy.crawler 是 Scrapy 框架中的一个模块，其中包含了与爬虫进程相关的类和函数。
# CrawlerProcess 是 Scrapy 框架中的一个类，它提供了创建和运行爬虫进程的功能。
# CrawlerProcess 类封装了 Scrapy 的核心组件，包括调度器、下载器、中间件等，可以通过调用其方法来执行爬取任务。
# 创建和配置爬虫进程：通过实例化 CrawlerProcess 类，您可以创建一个爬虫进程对象，并在对象上进行各种配置操作。
# 添加要运行的爬虫：使用 process.crawl() 方法，您可以向爬虫进程添加要运行的爬虫。可以根据需求添加一个或多个爬虫。
# 控制爬虫进程的启动和停止：通过调用 process.start() 方法，您可以启动爬虫进程，开始执行爬取任务。而调用 process.stop() 方法可以停止爬虫进程
from scrapy.crawler import CrawlerProcess

# scrapy.utils.project 是 Scrapy 框架中的一个模块，其中包含了与项目设置相关的实用函数。
# get_project_settings 是 scrapy.utils.project 模块中的一个函数，用于获取当前 Scrapy 项目的配置设置。
# 例如，在创建 CrawlerProcess 对象时，可以使用 get_project_settings() 获取项目的配置设置对象，并将其作为参数传递给 CrawlerProcess 构造函数，以确保使用正确的项目设置来配置爬虫进程。
from scrapy.utils.project import get_project_settings
  

if __name__ == '__main__':
    # 创建爬虫进程
    process=CrawlerProcess(get_project_settings())

    # 添加爬虫
    process.crawl(BaiduSpider)

    # 启动爬虫
    process.start()

