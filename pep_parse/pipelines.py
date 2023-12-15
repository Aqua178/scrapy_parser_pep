# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import time
from pathlib import Path

BASE_DIR = Path(__file__).absolute().parent.parent
RESULTS_DIR = 'results'
TIME_FORMAT = r'%Y-%m-%dT%H-%M-%S'
FILENAME = 'status_summary_{}.csv'.format(time.strftime(TIME_FORMAT))


class PepParsePipeline:
    def open_spider(self, spider):
        """При запуске паука создается словарь со статусами PEP"""
        self.results = BASE_DIR / RESULTS_DIR
        self.results.mkdir(exist_ok=True)
        self.count_dir = dict()
        self.total = 0

    def process_item(self, item, spider):
        """В процессе переборки item добавляем статусы pep в словарь,
          и считаем их количество"""
        status_quantity = self.count_dir.get(item['status']) or 0
        self.count_dir[item['status']] = status_quantity + 1
        return item

    def close_spider(self, spider):
        """При закрытии паука задаем формат вывода данных"""
        with open(self.results / FILENAME, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            self.count_dir['Total'] = sum(self.count_dir.values())
            for status in self.count_dir.keys():
                f.write(f'{status},{self.count_dir[status]}\n')
