import csv
from collections import defaultdict
from datetime import datetime as dt

from pep_parse.settings import BASE_DIR, DATETIME_FORMAT


class PepParsePipeline:
    def open_spider(self, spider):
        self.pep_status_dict = defaultdict(int)

    def process_item(self, item, spider):
        self.pep_status_dict[item['status']] += 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)

        now = dt.now()
        now_formatted = now.strftime(DATETIME_FORMAT)

        file_name = f'status_summary_{now_formatted}.csv'
        file_path = results_dir / file_name

        self.pep_status_dict['TOTAL'] += sum(self.pep_status_dict.values())

        with open(file_path, 'w', encoding='utf-8') as file:
            writer = csv.writer(file, dialect='unix')
            writer.writerow(['Status', 'Count'])
            writer.writerows(self.pep_status_dict.items())
