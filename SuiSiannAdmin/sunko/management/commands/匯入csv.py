from django.core.management.base import BaseCommand
import argparse
from sunko.models import 句表, 文章表
from os.path import basename


class Command(BaseCommand):
    help = '逐篇文章音檔kah句的csv檔，寄入來db'

    def add_arguments(self, parser):
        parser.add_argument('--csv', nargs='+', type=argparse.FileType('r'))

    def handle(self, *args, **options):
        for csvPath in options['csv']:
            tongMia = 提著csv檔名(csvPath.name)
            # Khiam 文章名
            一文章 = 文章表(文章名=tongMia)
            一文章.save()
            # Khiam 文章的句
            for tsua in csvPath:
                一句 = 句表(
                    來源=一文章,
                    音檔=tsua['Im-tóng'],
                    漢字=tsua['Hàn-jī'],
                    臺羅=tsua['Lô-má-jī']
                )
                一句.save()


def 提著csv檔名(csv路徑):
    檔名 = basename(csv路徑)
    點所在 = 檔名.index('.')
    純檔名 = 檔名[:點所在].replace('_hanlo', '')
    return 純檔名
