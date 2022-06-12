import sqlite3
import xmltodict
import requests
from datetime import datetime


def is_exists(text):
    if data['d:PublicationSeriesFirstCall'] is not None:
        return None
    elif text == 'd:PublicationSeriesFirstCallID':
        return data[text]['@m:null']
    else:
        return data[text]['#text']


def text_null(text):
    try:
        arg = data[text]['@m:null']
    except:
        try:
            arg = data[text]['#text']
        except:
            if data[text] == 'true':
                arg = True
                return arg
            else:
                arg = data[text]
                return arg
    if arg == 'true':
        arg = True
    if arg is not None:
        return arg
    else:
        arg = False
    return arg


def str_to_date(s):
    if type(s) is not bool:
        year = int(s[:4])
        month = int(s[5:7])
        day = int(s[8:10])
        hour = int(s[11:13])
        minute = int(s[14:16])
        second = int(s[17:19])
        date_time_obj = datetime(year, month, day, hour, minute, second)
        return date_time_obj
    return datetime.min


if __name__ == '__main__':
    # str_to_date("2022-02-02T12:48:22.793")
    url = "https://knesset.gov.il/Odata/ParliamentInfo.svc/KNS_Bill()"
    xml_url = requests.get(url)
    dict = xmltodict.parse(xml_url.content)
    db = sqlite3.connect("my_database.db")
    cursor = db.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS KNS_Bill(BillID integer primary key, KnessetNum integer,
    Name varchar (255),
    SubTypeID integer,
    SubTypeDesc varchar (125),
    PrivateNumber integer,
    CommitteeID integer,
    StatusID integer,
    Number integer,
    PostponementReasonID integer,
    PostponementReasonDesc varchar (125),
    PublicationDate datetime2,
    MagazineNumber integer,
    PageNumber integer,
    IsContinuationBill BIT,
    SummaryLaw varchar (255),
    PublicationSeriesID integer,
    PublicationSeriesDesc varchar (125),
    PublicationSeriesFirstCallID integer,
    PublicationSeriesFirstCallDesc varchar (510),
    LastUpdatedDate datetime2)
    '''
                   )
    db.commit()
    for line in dict['feed']['entry']:
        data = line['content']['m:properties']
        BillID = data['d:BillID']['#text']
        KnessetNum = data['d:KnessetNum']['#text']
        Name = data['d:Name']
        SubTypeID = data['d:SubTypeID']['#text']
        SubTypeDesc = data['d:SubTypeDesc']
        PrivateNumber = text_null('d:PrivateNumber')
        CommitteeID = text_null('d:CommitteeID')
        StatusID = data['d:StatusID']['#text']
        Number = text_null('d:Number')
        PostponementReasonID = text_null('d:PostponementReasonID')
        PostponementReasonDesc = text_null('d:PostponementReasonDesc')
        PublicationDate = str_to_date(text_null('d:PublicationDate'))
        MagazineNumber = text_null('d:MagazineNumber')
        PageNumber = text_null('d:PageNumber')
        IsContinuationBill = text_null('d:IsContinuationBill')
        SummaryLaw = data['d:SummaryLaw']['@m:null']
        PublicationSeriesID = text_null('d:PublicationSeriesID')
        if type(PublicationSeriesID) is not int:
            if PublicationSeriesID is True:
                PublicationSeriesID = 0
            else:
                PublicationSeriesID = int(PublicationSeriesID)
        PublicationSeriesDesc = data['d:PublicationSeriesDesc']
        PublicationSeriesFirstCallID = is_exists('d:PublicationSeriesFirstCallID')
        PublicationSeriesFirstCallDesc = is_exists('d:PublicationSeriesFirstCallDesc')
        LastUpdatedDate = str_to_date(text_null('d:LastUpdatedDate'))
        params = [BillID, KnessetNum, Name, SubTypeID, SubTypeDesc, PrivateNumber, CommitteeID, StatusID, Number,
                  PostponementReasonID, PostponementReasonDesc, PublicationDate, MagazineNumber, PageNumber,
                  IsContinuationBill, SummaryLaw, PublicationSeriesID, PublicationSeriesDesc,
                  PublicationSeriesFirstCallID, PublicationSeriesFirstCallDesc, LastUpdatedDate]
        cursor.executemany('''INSERT OR IGNORE INTO KNS_Bill(BillID, KnessetNum, Name, SubTypeID, SubTypeDesc, 
    PrivateNumber, CommitteeID, StatusID, Number, PostponementReasonID, PostponementReasonDesc, PublicationDate, 
    MagazineNumber, PageNumber, IsContinuationBill, SummaryLaw, PublicationSeriesID, PublicationSeriesDesc, 
    PublicationSeriesFirstCallID, PublicationSeriesFirstCallDesc, LastUpdatedDate) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,
    ?,?,?,?,?,?,?,?)''', [params])
        db.commit()
    cursor.execute('''
                   SELECT * FROM KNS_Bill
                   ''')
    cursor.execute("DROP TABLE KNS_Bill")
