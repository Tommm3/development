import os
import urllib.request

data_dir = r'C:\Users\ssark\OneDrive\Dokumenty\Python_scripts'

pages = [

    { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},

    { 'name': 'huj', 'url': 'http://agfsdfghsdfhhsd.pl/' },

    { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'} ]

for page in pages:
    try:
        filepath = os.path.join(data_dir,page['name']+'.html')
        urllib.request.urlretrieve(page['url'], filepath)
        print(filepath)
    except:
        print('something wet wrong')
        break
else:
    print('wszystko gyt')


# import urllib.request
# import os
#
# data_dir = r'C:\Users\ssark\OneDrive\Dokumenty\Python_scripts'
# pages = [
#     { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},
#     { 'name': 'kwejk', 'url': 'http://kwejk.pl/' },
#     { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'} ]
#
# for page in pages:
#
#     try:
#         file_name = "{}.html".format(page["name"])
#         path = os.path.join(data_dir, file_name)
#
#         print("Processing: {}  => {} ...".format(page["url"], file_name))
#         urllib.request.urlretrieve (page["url"], path)
#         print('...done')
#
#     except:
#         print('FAILURE processing web page: {}'.format(page["name"]))
#         print('Stopping the process!')
#         break
#
# else:
#     print('All pages downloaded successfully!!!')
