import fileinput
import os

path ="F:/Faculdade/UFG/Mestrado/NPL/AmericansHealth/arquivos_diabetes"

filelist = [] #lista de arquivos da pasta

#arquivo de estatisticas
arquivo = open('estatistica.txt', 'w')
arquivo.write('Arquivo'+'\t')
arquivo.write('qnt_paragrafos'+'\t')
arquivo.write('qnt_palavras' +'\n')
arquivo.close()

#lista todos arquivos de uma pasta
for root, dirs, files in os.walk(path):
	for file in files:
		if(file.endswith(".txt")):
			filelist.append(file)
			#print(os.path.join(root,file))

for aux in filelist:

	#abre arquivo selecionado
	f = open(aux, 'r')
	#paragrafos
	paragrafos = list(filter(lambda value: value != '', [value.replace('\n', '').strip('"') for value in f]))

	f = open(aux, 'r')
	data = f.read() #todo texto
	words = data.split() #palavras
	qnt_parag = str(len(paragrafos)-1)
	qnt_words=str(len(words))
	#print(paragrafos)
	#print(words)

	arquivo = open('estatistica.txt', 'a')
	arquivo.write(aux + '\n')
	arquivo.write(qnt_parag + '\t')
	arquivo.write(qnt_words + '\n')
	arquivo.close()
