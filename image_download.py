from icrawler.builtin import GoogleImageCrawler

google_crawler = GoogleImageCrawler(storage={'root_dir': 'images/rumah'})
google_crawler.crawl(keyword='rumah adat indonesia', max_num=10)
