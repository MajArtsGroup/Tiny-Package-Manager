from urllib.request import URLopener
from sys import argv
from os import mkdir
from os.path import isdir

if not isdir('Packages'):
	mkdir('Packages')

if argv[1] == 'install':
	pkg = argv[2]
	try:
		URLopener().retrieve(f'https://raw.githubusercontent.com/MajArtsGroup/Tiny-Package-Manager/main/pack/{pkg}.pkg', f'Packages/{lib}.h')
	except:
		print(f"Package {pkg} not found")
