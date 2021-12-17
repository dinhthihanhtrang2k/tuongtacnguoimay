from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
from bs4 import BeautifulSoup

updater = Updater('2131609700:AAE-YiQTR9aJK3a5nWPLbECkIvYCv59SNgs')

def get_news():
    list_new = []
    r = requests.get('https://www.baogiaothong.vn/du-lich/')
    soup = BeautifulSoup(r.text, 'html.parser')
    find_el = soup.find_all('div', class_="img rlt")
    print(len(find_el))
    for new in find_el:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_new.append(newdict)
    return list_new

def get_eogio():
    list_eogio = []
    a1 = requests.get('https://vietnamtourism.gov.vn/index.php/items/31346')
    soup = BeautifulSoup(a1.text, 'html.parser')
    find_el1 = soup.find_all('div', class_="items-detail")
    print(len(find_el1))
    for new in find_el1:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_eogio.append(newdict)
    return list_eogio

def get_kico():
    list_kico = []
    a2 = requests.get('https://sites.google.com/site/dulichkyco/')
    soup = BeautifulSoup(a2.text, 'html.parser')
    find_el2 = soup.find_all('td', class_="sites-layout-tile sites-tile-name-content-2")
    print(len(find_el2))
    for new in find_el2:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_kico.append(newdict)
    return list_kico

def get_culaoxanh():
    list_culaoxanh = []
    a3 = requests.get('http://www.dulichculaoxanh.vn/2017/01/tour-kham-pha-cu-lao-xanh-quy-nhon-binh.html')
    soup = BeautifulSoup(a3.text, 'html.parser')
    find_el3 = soup.find_all('div', class_="titlewrapper")
    print(len(find_el3))
    for new in find_el3:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_culaoxanh.append(newdict)
    return list_culaoxanh

def get_honkho():
    list_honkho = []
    a4 = requests.get('https://www.vntrip.vn/cam-nang/hon-kho-quy-nhon-binh-dinh-28735')
    soup = BeautifulSoup(a4.text, 'html.parser')
    find_el4 = soup.find_all('div', class_="container")
    print(len(find_el4))
    for new in find_el4:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_honkho.append(newdict)
    return list_honkho

def get_honseo():
    list_honseo = []
    a5 = requests.get('https://www.vntrip.vn/cam-nang/hon-kho-quy-nhon-binh-dinh-28735')
    soup = BeautifulSoup(a5.text, 'html.parser')
    find_el5 = soup.find_all('div', class_="container")
    print(len(find_el5))
    for new in find_el5:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_honseo.append(newdict)
    return list_honseo

def get_ghenhrang():
    list_ghenhrang = []
    a6 = requests.get('https://www.vntrip.vn/cam-nang/hon-kho-quy-nhon-binh-dinh-28735')
    soup = BeautifulSoup(a6.text, 'html.parser')
    find_el6 = soup.find_all('div', class_="container")
    print(len(find_el6))
    for new in find_el6:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_ghenhrang.append(newdict)
    return list_ghenhrang

def get_thapbanhit():
    list_thapbanhit = []
    a7 = requests.get('https://www.vntrip.vn/cam-nang/hon-kho-quy-nhon-binh-dinh-28735')
    soup = BeautifulSoup(a7.text, 'html.parser')
    find_el7 = soup.find_all('div', class_="container")
    print(len(find_el7))
    for new in find_el7:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_thapbanhit.append(newdict)
    return list_thapbanhit

def get_trungluong():
    list_trungluong = []
    a8 = requests.get('https://www.vntrip.vn/cam-nang/hon-kho-quy-nhon-binh-dinh-28735')
    soup = BeautifulSoup(a8.text, 'html.parser')
    find_el8 = soup.find_all('div', class_="container")
    print(len(find_el8))
    for new in find_el8:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_trungluong.append(newdict)
    return list_trungluong

def get_hamho():
    list_hamho = []
    a9 = requests.get('https://www.vntrip.vn/cam-nang/hon-kho-quy-nhon-binh-dinh-28735')
    soup = BeautifulSoup(a9.text, 'html.parser')
    find_el9 = soup.find_all('div', class_="container")
    print(len(find_el9))
    for new in find_el9:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_hamho.append(newdict)
    return list_hamho

def get_thapdoi():
    list_thapdoi = []
    a10 = requests.get('https://www.vntrip.vn/cam-nang/hon-kho-quy-nhon-binh-dinh-28735')
    soup = BeautifulSoup(a10.text, 'html.parser')
    find_el10 = soup.find_all('div', class_="container")
    print(len(find_el10))
    for new in find_el10:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_thapdoi.append(newdict)
    return list_thapdoi

def get_damthinai():
    list_damthinai = []
    a11 = requests.get('https://www.vntrip.vn/cam-nang/hon-kho-quy-nhon-binh-dinh-28735')
    soup = BeautifulSoup(a11.text, 'html.parser')
    find_el11 = soup.find_all('div', class_="container")
    print(len(find_el11))
    for new in find_el11:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_damthinai.append(newdict)
    return

def get_banahils():
    list_banahils = []
    a12 = requests.get('https://www.klook.com/vi/blog/dia-diem-du-lich-da-nang/')
    soup = BeautifulSoup(a12.text, 'html.parser')
    find_el12 = soup.find_all('div', class_="index_wrapper_19ddS")
    print(len(find_el12))
    for new in find_el12:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_banahils.append(newdict)
    return list_banahils

def get_bandaosontra():
    list_bandaosontra = []
    a13 = requests.get('https://www.klook.com/vi/blog/dia-diem-du-lich-da-nang/')
    soup = BeautifulSoup(a13.text, 'html.parser')
    find_el13 = soup.find_all('div', class_="area-selector_cities")
    print(len(find_el13))
    for new in find_el13:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_bandaosontra.append(newdict)
    return list_bandaosontra

def get_nguhanhson():
    list_nguhanhson = []
    a14 = requests.get('https://www.klook.com/vi/blog/dia-diem-du-lich-da-nang/')
    soup = BeautifulSoup(a14.text, 'html.parser')
    find_el14 = soup.find_all('div', class_="left")
    print(len(find_el14))
    for new in find_el14:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_nguhanhson.append(newdict)
    return list_nguhanhson

def get_chobenthanh():
    list_chobenthanh = []
    a15 = requests.get('https://www.bestprice.vn/blog/diem-den-8/ho-chi-minh-3/10-dia-diem-du-lich-thanh-pho-ho-chi-minh-noi-tieng-nhat_26-4491.html')
    soup = BeautifulSoup(a15.text, 'html.parser')
    find_el15 = soup.find_all('div', class_="content-article")
    print(len(find_el15))
    for new in find_el15:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_chobenthanh.append(newdict)
    return list_chobenthanh

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}\nTôi tên là Travle Tour\nTôi rất vui khi được giải đáp các thắc mắc liên quan đến du lịch ở Việt Nam\nBạn sẽ đến thăm thành phố nào của Việt Nam?')

def thanks(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Cảm ơn quý khách!')

def newsTour(update: Update, context: CallbackContext) -> None:
    data = get_news()
    update.message.reply_text(f'Thông tin tour mới nhất\n {data[0]}')

def quynhon(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Sự lựa chọn tuyệt vời!\nĐiểm tham quan nào bạn muốn trãi nghiệm khi đến Quy Nhơn?\n/eogio, /kico, /culaoxanh, /honkho, /honseo, /ghenhrang, /thapbanhit, /trungluong, /hamho, /thapdoi, /damthinai')

def eogio(update: Update, context: CallbackContext) -> None:
    d1 = get_eogio()
    update.message.reply_text(f'Chào mừng bạn đến với địa điểm du lịch eo gió\n{d1[0]}')

def kico(update: Update, context: CallbackContext) -> None:
    d2 = get_kico()
    update.message.reply_text(f'Chào mừng bạn đến với địa điểm du lịch kì co\n{d2[0]}')

def culaoxanh(update: Update, context: CallbackContext) -> None:
    d3 = get_culaoxanh()
    update.message.reply_text(f'Chào mừng bạn đến với địa điểm du lịch Cù Lao Xanh\n{d3[0]}')

def honkho(update: Update, context: CallbackContext) -> None:
    d4 = get_honkho()
    update.message.reply_text(f'Chào mừng bạn đến với địa điểm du lịch Hòn Khô\n{d4[0]}')

def honseo(update: Update, context: CallbackContext) -> None:
    d5 = get_honseo()
    update.message.reply_text(f'Chào mừng bạn đến với địa điểm du lịch Hòn Sẹo\n{d5[0]}')

def ghenhrang(update: Update, context: CallbackContext) -> None:
    d6 = get_ghenhrang()
    update.message.reply_text(f'Chào mừng bạn đến với địa điểm du lịch Ghềnh Ráng\n{d6[0]}')

def thapbanhit(update: Update, context: CallbackContext) -> None:
    d7 = get_thapbanhit()
    update.message.reply_text(f'Chào mừng bạn đến với địa điểm du lịch Ghềnh Ráng\n{d7[0]}')

def trungluong(update: Update, context: CallbackContext) -> None:
    d8 = get_trungluong()
    update.message.reply_text(f'Chào mừng bạn đến với địa điểm du lịch Ghềnh Ráng\n{d8[0]}')

def hamho(update: Update, context: CallbackContext) -> None:
    d9 = get_hamho()
    update.message.reply_text(f'Chào mừng bạn đến với địa điểm du lịch Hầm Hô\n{d9[0]}')

def thapdoi(update: Update, context: CallbackContext) -> None:
    d10 = get_thapdoi()
    update.message.reply_text(f'Chào mừng bạn đến với địa điểm du lịch Tháp Đôi\n{d10[0]}')

def damthinai(update: Update, context: CallbackContext) -> None:
    d11 = get_damthinai()
    update.message.reply_text(f'Chào mừng bạn đến với địa điểm du lịch Đầm Thị Nại\n{d11[0]}')

def danang(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Sự lựa chọn tuyệt vời!\nĐiểm tham quan nào bạn muốn trãi nghiệm khi đến Đà Nẵng?\n/banahils, /bandaosontra, /nguhanhson')

def banahils(update: Update, context: CallbackContext) -> None:
    d12 = get_banahils()
    update.message.reply_text(f'Chào mừng bạn đến với địa điểm du lịch BanaHils\n{d12[0]}')

def bandaosontra(update: Update, context: CallbackContext) -> None:
    d13 = get_bandaosontra()
    update.message.reply_text(f'Chào mừng bạn đến với địa điểm du lịch Bán Đảo Sơn Trà\n{d13[0]}')

def nguhanhson(update: Update, context: CallbackContext) -> None:
    d14 = get_nguhanhson()
    update.message.reply_text(f'Chào mừng bạn đến với địa điểm du Ngũ Hành Sơn\n{d14[0]}')

def tphcm(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Sự lựa chọn tuyệt vời!\nĐiểm tham quan nào bạn muốn trãi nghiệm khi đến Thành phố Hồ Chí Minh?\n/chobenthanh, /dinhdoclap, /nhathoducba')

def chobenthanh(update: Update, context: CallbackContext) -> None:
    d15 = get_chobenthanh()
    update.message.reply_text(f'Chào mừng bạn đến với địa điểm du lịch Chợ Bến Thành\n{d15[0]}')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('newstour', newsTour))
updater.dispatcher.add_handler(CommandHandler('thanks', thanks))
updater.dispatcher.add_handler(CommandHandler('quynhon', quynhon))
updater.dispatcher.add_handler(CommandHandler('eogio', eogio))
updater.dispatcher.add_handler(CommandHandler('kico', kico))
updater.dispatcher.add_handler(CommandHandler('culaoxanh', culaoxanh))
updater.dispatcher.add_handler(CommandHandler('honkho', honkho))
updater.dispatcher.add_handler(CommandHandler('honseo', honseo))
updater.dispatcher.add_handler(CommandHandler('ghenhrang', ghenhrang))
updater.dispatcher.add_handler(CommandHandler('thapbanhit', thapbanhit))
updater.dispatcher.add_handler(CommandHandler('trungluong', trungluong))
updater.dispatcher.add_handler(CommandHandler('hamho', hamho))
updater.dispatcher.add_handler(CommandHandler('thapdoi', thapdoi))
updater.dispatcher.add_handler(CommandHandler('damthinai', damthinai))
updater.dispatcher.add_handler(CommandHandler('danang', danang))
updater.dispatcher.add_handler(CommandHandler('banahils', banahils))
updater.dispatcher.add_handler(CommandHandler('bandaosontra', bandaosontra))
updater.dispatcher.add_handler(CommandHandler('nguhanhson', nguhanhson))
updater.dispatcher.add_handler(CommandHandler('thanhphohochiminh', tphcm))
updater.dispatcher.add_handler(CommandHandler('chobenthanh', chobenthanh))

updater.start_polling()
updater.idle()