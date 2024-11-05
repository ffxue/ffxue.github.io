mypaths = ['pdf', 'misc', 'amp']

dois = [
#2024
'10.1016/j.isprsjprs.2024.01.020',
'10.1007/s44212-024-00039-7',
'10.3846/jcem.2024.20953',
'10.1038/s44296-024-00010-2',
'10.1016/j.autcon.2024.105576',
'10.1016/j.eng.2024.07.012',
#2023
'10.1016/j.autcon.2022.104645',
'10.1016/j.autcon.2023.104780',
'10.1016/j.landurbplan.2023.104714',
'10.1111/jiec.13348',
'10.1016/j.compind.2023.103883',
'10.1016/j.enbuild.2023.113417',
'10.5194/isprs-annals-X-M-1-2023-293-2023',
#2022
'10.1016/j.resconrec.2021.106013',
'10.1016/j.resconrec.2021.106022',
'10.1061/(ASCE)CO.1943-7862.0002229',
'10.1061/(ASCE)CO.1943-7862.0002226',
'10.1016/j.autcon.2021.104083',
'10.1061/(ASCE)ME.1943-5479.0001029',
'10.1177/87569728211061780',
'10.3389/fbuil.2021.813399',
'10.1016/j.compind.2021.103573',
'10.1016/j.buildenv.2022.109137',
'10.1016/j.landurbplan.2022.104505',
'10.1016/j.jclepro.2022.133460',
#2021
'10.1016/j.aei.2020.101245',
'10.1016/j.resconrec.2021.105480',
'10.1016/j.jclepro.2020.125391',
'10.1108/SASBE-08-2020-0124',
'10.1016/j.jenvman.2021.112233',
'10.1016/j.compind.2021.103437',
'10.1016/j.autcon.2021.103716',
'10.1016/j.autcon.2021.103738',
'10.1016/j.autcon.2021.103816',
'10.3390/rs13101882',
'10.1016/j.jenvman.2021.112822',
'10.1061/(ASCE)CO.1943-7862.0002148',
'10.1016/j.wasman.2021.08.012',
'10.3390/ijgi10080561',
'10.1016/j.resconrec.2021.105809',
#2020
'10.1016/j.autcon.2020.103270',
'10.1016/j.isprsjprs.2020.07.020',
'10.1016/j.ijproman.2020.07.007',
'10.1108/F-02-2019-0024',
'10.1016/j.landusepol.2019.104264',
'10.1016/j.resconrec.2019.104674',
'10.1016/j.wasman.2020.03.024',
'10.1061/(ASCE)CO.1943-7862.0001877',
'10.1080/17452007.2020.1768505',
'10.1016/j.jclepro.2020.121779',
#2019
'10.1016/j.isprsjprs.2018.12.005',
'10.1061/(ASCE)CP.1943-5487.0000839',
'10.1016/j.aei.2019.100965',
'10.1016/j.jclepro.2019.02.141',
'10.1016/j.ssci.2018.07.013',
'10.1016/j.aei.2019.100938',
'10.1016/j.autcon.2019.102922',
#2018
'10.1111/mice.12378',
'10.1016/j.autcon.2018.05.023',
'10.1016/j.autcon.2018.05.009',
'10.1016/j.autcon.2018.01.001',
'10.1061/(ASCE)ME.1943-5479.0000558',
'10.1016/j.jclepro.2018.07.319',
'10.1016/j.eiar.2018.08.005',
'10.3992/1943-4618.13.4.61',
'10.1080/0951192X.2017.1379095',
#2017
'10.1016/j.jclepro.2017.07.156',
'10.1016/j.jclepro.2016.11.028',
'10.1016/j.rser.2017.01.021',
'10.1016/j.autcon.2017.01.006',
#2016
'10.1016/j.habitatint.2016.07.002',
'10.1016/j.enpol.2016.01.017',
'10.1016/j.jclepro.2016.02.123',
'10.1016/j.rser.2015.09.068',
#2010-15
'10.1061/(ASCE)ME.1943-5479.0000341',
'10.1108/SASBE-08-2014-0046',
'10.1016/j.ifacol.2015.06.227',
'10.1007/s11066-011-9064-7']

base = 'https://frankxue.com/'

################## urllist.txt ####################
from os import listdir
from os.path import isfile, join
def write_sitemap_txt(folders):
	file1 = open("urllist.txt","w") 
	# \n is placed to indicate EOL (End of Line) 
	file1.write(base + "index.html\n")
	for p in folders:
		onlyfiles = [f for f in listdir(p) if isfile(join(p, f))]
		for f in onlyfiles:
			file1.write(base+p+'/'+f+'\n') 
	file1.close() #to change file access modes 
	print('> urllist.txt updated')

############### sitemap.xml #############
#from autocrawler import Crawler

#found_links = []
#crawler = Crawler('https://frankxue.com');

# fetch links
#links = crawler.start()

#write into file
import datetime
def write_sitemap_xml(folders):
	from os.path import getmtime
	with open('sitemap.xml', "w") as file: 
		file.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
		mod_time = datetime.datetime.fromtimestamp(round(getmtime('index.html')))
		file.write('\n\t<url><loc>{0}index.html</loc>\t<lastmod>{1}+08:00</lastmod>\t<changefreq>daily</changefreq>\t<priority>0.8</priority></url>'.format(base, mod_time).replace(' ', 'T'))
		for p in mypaths:
			onlyfiles = [f for f in listdir(p) if isfile(join(p, f))]
			for f in onlyfiles:
				file.write("\n\t<url><loc>{0}{1}/{2}</loc>".format(base, p, f))
				mod_time = datetime.datetime.fromtimestamp(round(getmtime(p+'/'+f)))
				file.write("\t<lastmod>{0}+08:00</lastmod>\t<changefreq>monthly</changefreq></url>".format(mod_time).replace(' ', 'T'))
		file.write('\n</urlset>')
	print('> sitemap.xml updated')

##################  google scholar ####################
def write_gscholar_cites():
	from bs4 import BeautifulSoup
	import urllib.request
	url="https://scholar.google.com/citations?user=CgyERlQAAAAJ&hl=en"
	page = urllib.request.urlopen(url)
	soup = BeautifulSoup(page, 'html.parser') 
	indexes = soup.find_all("td", "gsc_rsb_std")
	h_index = indexes[2].string
	i10_index = indexes[4].string
	citations = indexes[0].string

	print(h_index, i10_index, citations)
	years = soup.find_all("span", "gsc_g_t")
	cited = soup.find_all("span", "gsc_g_al")
	file2 = open("cv_files/gs_cite.js","w") 
	file2.write('var gs_cites=[')
	for i in range(len(years)):
		file2.write('{"year": '+years[i].string+', "value": '+cited[i].string+'}')
		if i < len(years)-1:
			file2.write(', ')
	file2.write('];\n')
	file2.write('var hindex='+h_index+';\n')
	file2.write('var tot_cites='+citations+';\n')
	file2.close() #to change file access modes 
	print('> cv_files/gs_cite.js updated')

def get_gs_id(doi):
	from bs4 import BeautifulSoup
	import requests
	import datetime
	time = datetime.datetime.utcnow().strftime('%Y-%m-%d-%H')
	cookies = {'GSP': 'LM=1620096774:S=Un9fcsyiRcHsIxt9', '1P_JAR': time, 'NID':'214=NOmw3JNqVv5cgWJzy7bYIqH3c1D40ur0KNgeCLc5KYeduqcbD5MLWAdzF9ulwBNyFWG86_dadPEKcdW8UsvDuDVMRC9WaX7gn6-8j7B727bWm4FDz2r-X-2grS8haFqqENiAM0Es9AoQZr8BLPfMgtHHprwnLkLfI_AV5pWpJJY'}
	headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Accept-Language': 'en-US,en;q=0.7,zh;q=0.3', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'}
	url = 'https://scholar.google.com/scholar?hl=en&q=' + doi
	#print(url)
	try:
		page = requests.get(url, cookies=cookies, headers=headers)
		if page is None:
			return None
		soup = BeautifulSoup(page.text, 'html.parser') 
		indexes = soup.find_all("h3", "gs_rt")
		if len(indexes) < 1:
			return None
		indexes = indexes[0].find_all("a", href=True)
		if len(indexes) < 1:
			return None
		if indexes[0]['data-clk'] is not None:
			vals = indexes[0]['data-clk'].split('&')
			for v in vals:
				if v[0:2] == 'd=':
					return v[2:]
	except:
		pass
	return None

##################  plumx: paper metrics ####################
def build_msg(data):
	vtot = 0
	v1yr = 0
	v3yr = 0
	if 'total' in data:
		vtot = data['total']
	if '3year_rank' in data:
		v3yr = data['3year_rank']
	if '1year_rank' in data:
		v1yr = data['1year_rank']
	#print(v1yr, type(v1yr))
	if vtot == 0 or v1yr == 0 or v3yr == 0:
		return {}
	pctl = max(v3yr, v1yr)
	quartile = 4-int((pctl+0.01)/25)
	if quartile < 1:
		quartile = 1
	ret = {}
	ret['Q'] = quartile
	ret['N'] = vtot
	ret['%'] = int(pctl)
	ret['v1'] = int(v1yr)
	ret['v3'] = int(v3yr)
	return ret

def build_doi(data, doi):
	ret = {}
	if 'bibliographic_data' not in data or 'tags' not in data['bibliographic_data']:
		return ret
	ret['journal'] = data['bibliographic_data']['publication_title']
	ret['tags'] = data['bibliographic_data']['tags']
	if 'sort_count' in data:
		if 'citation' in data['sort_count']:
			ret['citations'] = build_msg(data['sort_count']['citation'])
		if 'usage' in data['sort_count']:
			ret['views'] = build_msg(data['sort_count']['usage'])
		if 'capture' in data['sort_count']:
			ret['captures'] = build_msg(data['sort_count']['capture'])
	return ret

def write_plumx_stat(mydois):
	import json
	import time
	import urllib.request
	opener = urllib.request.build_opener()
	output = {}
	for doi in mydois:
		print('fetching doi: ', doi, '...')
		f = opener.open("https://plu.mx/api/v1/artifact/doi/"+doi)
		data = json.load(f)
		output[doi]=build_doi(data, doi)
		print(output[doi])
		time.sleep(1.0)
	plumx = 'var art_metrics = ' + str(output) + ';'
	plumx = plumx.replace(", '", ",'").replace("': ", "':")
	if len(plumx) > 100:
		file1 = open("cv_files/art_metrics.js","w") 
		file1.write(plumx + "\n")
		file1.close()
		print('> cv_files/art_metrics.js updated')

def xcopy(folder, ext):
  import subprocess
  subprocess.run(['xcopy', folder+'\\*.'+ext, '..\\cv.github\\'+folder, "/D", "/Y"]) 

def copy_to_github():
  import time
  xcopy('.', 'html')
  xcopy('.', 'txt')
  xcopy('.', 'xml')
  time.sleep(1.0)
  xcopy('cv_files', '*')
  time.sleep(1.0)
  xcopy('misc', '*')
  time.sleep(1.0)
  xcopy('pdf', '*')
  time.sleep(1.0)
  xcopy('thumbnail', 'png')
  time.sleep(1.0)
  xcopy('thumbnail', 'jpg')

########### main ############
write_sitemap_txt(mypaths)
write_sitemap_xml(mypaths)
write_gscholar_cites()
write_plumx_stat(dois)
copy_to_github()