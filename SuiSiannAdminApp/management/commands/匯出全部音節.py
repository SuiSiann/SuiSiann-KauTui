import json

from SuiSiannAdminApp.models import 句表
from django.core.management.base import BaseCommand


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('json',)

    def handle(self, *args, **options):
        u = set()
        bo = set()
        for 句 in 句表.objects.all():
            for lmj in (
                拆文分析器.建立句物件(句.羅馬字, 句.羅馬字)
                .轉音(臺灣閩南語羅馬字拼音)
                .篩出字物件()
            ):
                if lmj.敢是標點符號():
                    pass
                elif lmj.音標敢著(臺灣閩南語羅馬字拼音):
                    u.add(lmj.轉音(臺灣閩南語羅馬字拼音, '轉調符').型)
                    bo.add(lmj.型.rstrip('0987654321'))
        with open(options['json'], 'w') as tong:
            json.dump(
                {'有聲調': sorted(u), '無聲調': sorted(bo)},
                tong,
                ensure_ascii=False,
                sort_keys=True,
                indent=2,
            )
