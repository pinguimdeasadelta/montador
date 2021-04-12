origem = input('Qual eh o nome do arquivo a ser convertido? (inclua a extensao)\n')
nome = input('Digite o nome do programa resultante:')
binary = open(origem, "r")
desth = open(nome+'_H.drs', "w")
destl = open(nome+'_L.drs', "w")
desth.write('#A 0000h\n#B\n\n') #linha magica
destl.write('#A 0000h\n#B\n\n') #linha magica
for i in binary:
    desth.write(i[:16] + '\n')
    destl.write(i[16:] + '\n')
desth.close()
destl.close()
binary.close()
print(f'Tudo pronto, os arquivos gerados foram: {nome}_L.drs e {nome}_H.drs')
