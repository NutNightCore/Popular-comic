import csv
import pygal
""" ทำการ พิมพ์ กราฟ และ ข้อมูลที่ได้รับ """
def reader_file():
    """ ดึงข้อมูล """
    file_2008 = open("W:/Project/Popular-comic/2008 - Sheet1.csv", "r", encoding='utf-8')
    file_2009 = open("W:/Project/Popular-comic/2009 - Sheet1.csv", "r", encoding='utf-8')
    file_2010 = open("W:/Project/Popular-comic/2010 - Sheet1.csv", "r", encoding='utf-8')
    file_2011 = open("W:/Project/Popular-comic/2011 - Sheet1.csv", "r", encoding='utf-8')
    file_2012 = open("W:/Project/Popular-comic/2012 - Sheet1.csv", "r", encoding='utf-8')
    file_2013 = open("W:/Project/Popular-comic/2013 - Sheet1.csv", "r", encoding='utf-8')
    file_2014 = open("W:/Project/Popular-comic/2014 - Sheet1.csv", "r", encoding='utf-8')
    file_2015 = open("W:/Project/Popular-comic/2015 - Sheet1.csv", "r", encoding='utf-8')
    file_2016 = open("W:/Project/Popular-comic/2016 - Sheet1.csv", "r", encoding='utf-8')
    file_2017 = open("W:/Project/Popular-comic/2017 - Sheet1.csv", "r", encoding='utf-8')
    file_2018 = open("W:/Project/Popular-comic/2018 - Sheet1.csv", "r", encoding='utf-8')
    list_file = {"2008" : file_2008, "2009" : file_2009, "2010" : file_2010, "2011" : file_2011, "2012" : file_2012, "2013" : file_2013, "2014" : file_2014, "2015" : file_2015, "2016" : file_2016, "2017" : file_2017, "2018" : file_2018}
    for file in list_file:
        read_file = csv.reader(list_file.get(file))
        graph_sale = port_graph_sale(file ,read_file)
        graph_genre = port_graph_genre(file ,read_file)

def port_graph_sale(year, file):
    """ สร้างกราฟยอดขาย """
    graph_sale = pygal.HorizontalBar()
    graph_sale.title = "ยอดขายหนังสือปี %s (ต่อ เล่ม)" %year
    for data in file:
        if data[0] != "Book title":
            graph_sale.add(data[0], int(data[2].replace(",", "")))
    graph_sale.render()
    graph_sale.render_to_file('W:/Project/Popular-comic/ยอดขาย/ยอดขาย_%s.svg' %year)
    return

def port_graph_genre(year, file):
    """ สร้างกราฟประเภทหนังสือ """
    genre_dic = {}
    for data in file:
        if data[1] != "Genre":
            key = str(data[1])
            genre_dic[key] = genre_dic.get(key, int(data[2].replace(",", "")))
    graph_genre = pygal.HorizontalBar()
    graph_genre.title = "ประเภทหนังสือที่มีคนซื้อในปี %s (ต่อ เล่ม)" %year
    for genre in genre_dic:
        graph_genre.add(genre, genre_dic.get(genre))
    graph_genre.render()
    graph_genre.render_to_file('W:/Project/Test/Genre_%s.svg' %year)
    return

reader_file()