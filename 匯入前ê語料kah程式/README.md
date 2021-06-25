# SuiSiann-Dataset
台語媠聲錄音檔 

## 進度
Dropbox/母語/語料/TTS 語音合成錄製/錄音進度.pdf

|  | 錄音                             | 對齊音檔 | 照稿 | 匯入資料庫 |  
|--------------------------------|------|----|-------|--| 
| 806 頁岩石油發展緊  OPEC地位不保.odt.csv  | o  | o  | o |o  | 
| 807 美國面對Islam國的兩難.odt.csv     | o  | o  | o |o  |  
| 808 免錢的上貴 面冊拜託收我1箍.odt.csv    | o  | o  | o |o  | 
| 809 同性婚合法化 閣來看澳洲.odt.csv  | o  | o  | o |o  | 
| 810 教宗成做左派領袖？.odt.csv      | o  | o  | o |o  | 
| bô_kóng-liáu無講了_hanlo.odt.csv | o  | o  | o |o  | 
| hóo-tīng否定句_hanlo.odt.csv     | o  | o  | o |o  | 
| ing-gí-sû英語詞_hanlo.odt.csv    | o  | o  | o |o  | 
| khang-sû-luī空詞類_hanlo.odt.csv | o  | o  | o |o  | 
| kî-thann其他（問句後壁）.csv        | o  | o  | o |o  | 
| mn̄g-kù問句_hanlo.odt.csv        | o  | o  | o |o  | 
| phuà-pēnn破病_hanlo.odt.csv     | o  | o  | o |o  | 
| pí-kàu-kù比較句_hanlo.odt.csv    | o  | o  | o |o  | 
| sòo-sû數詞_hanlo.odt.csv         | o  | o  | o |o  | 
| suánn_ê散的_hanlo.odt.csv        |      |    |       |  | 
| tia̍h-jī-sû疊字詞_hanlo.odt.csv   |      |    |       |  | 
| tōng-sû動詞時貌kah補語_hanlo.odt.csv | o  | o  | o |o  | 
| tshua-thuan_hanlo.odt.csv      | o  | o  | o |o  | 
| 日語外來詞kap例句.odt.csv      | o  | o  | o |o  | 
| 服務台_hanlo.odt.csv           | o  | o  | o |o  | 
| 氣象_hanlo.odt.csv            | o  | o  | o |o  | 
| 翻身番身_話頭_劉承賢_hanlo.odt.csv | o  | o  | o |o  | 
| 角花仔佮素花仔_hanlo.odt.csv     | o  | o  | o |o  | 
| 賣圓仔的神仙_hanlo.odt.csv      | o  | o  | o |o  | 
| 附加詞類訊息_楊允言.odt.csv          | o  | o  | o |o  |
| 鐵路_hanlo.odt.csv           | o  | o  | o |o  | 
| 電影院_hanlo.odt.csv        | o  | o  | o |o  | 

## Kāng-pōo語料
```
SERVER=ip
rsync -av -e ssh TTS\ 語音合成錄製/ "ubuntu@$SERVER:./git/SuiSiann/TTS\ 語音合成錄製"
```

## 包--起-來
```
PANPUN=0.3
time docker-compose exec gunicorn python manage.py 匯出Dataset ./tsu-liāu/$PANPUN
cd tsu-liāu/
tar -cvf SuiSiann-$PANPUN.tar $PANPUN
cd ../
```

## 將csv匯入django admin
```
python manage.py 匯入csv csv/賣圓仔的神仙_hanlo.odt.csv
```

## 開發
```
bash 批次錄音稿odt轉csv.sh 
```
進前為著管理錄音，逐擺的錄音稿攏有家己的資料kiap。
這个程式會去揣錄音稿的資料kiap，將 in 轉做`.csv`囥佇`csv/`。
