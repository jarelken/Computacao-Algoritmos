

#criação de arquivo
nomeArquivo = "Conversor.txt"
arquivo = open(nomeArquivo, 'w')

#escreve no arquivo
arquivo.write("Remocao de Simbolos Inuteis")
arquivo.close()


#Trabalhar o algoritmo / separação em partes
print("Digite uma gramatica livre de contexto")
print("\nUse o formato a seguir: S->a|b|Aa|a,A->b|S,C->a|aAa(Sem espaços/vazio como e)")
lingFor=input("Digite:")
itens=lingFor.split(',')
var=[]
der = []
listacont=[]
for i in itens:
    cont=0   
    y=i.split("->")
    var.append(y[0])
    y=y[1].split("|")
    for j in range(i.count("|")+1):
        der.append(y[j])
        cont+=1
    listacont.append(cont)




#conversão
listasubs=[]
subs=0
u=0
lol=0
salva=[]
for o in var:
    u+=1
    for t in range(listacont[u-1]):
       lol+=1
       subs+=1
       for m in list(der[lol-1]):
            if((m.isupper()) and (m not in (var))):
                listasubs.append(subs)
                salva.append(u-1)
            elif (m == 'e'):
                listasubs.append(subs)
                salva.append(u-1)

for s in salva:
    listacont[s]= int(listacont[s])-1                   



contander=0
listacontander=[]
arquivo = open('Conversor.txt', 'r')
conteudo = arquivo.readlines()
conteudo.append('\n'+lingFor)
men="\nValores Obtidos:\n\n"
conteudo.append(men)
for i in itens:
    conteudo.append("\nItens: "+i)
for i in var:
    conteudo.append("\nVariaveis: "+i)
for i in der:
    contander+=1
    if contander not in listasubs:
        conteudo.append("\nDerivacoes: "+i)
    else:
        listacontander.append(contander)



j=1
for i in listacontander:
    der.pop(int(listacontander[0])-j)
    j+=int(len(der)-2)


z=0
x=0
semifinal="\n\n"
conteudo.append(semifinal)

mensagem="\nResultado apos conversao:\n\n"
conteudo.append(mensagem)
for v in var:
    final= v+"->"
    z+=1   
    q=0
    for i in range(listacont[z-1]):
        q+=1
        x+=1
        final=final+der[x-1]
        if (q<int(listacont[z-1])):
            final+="|"
    if (z<len(var)):
        final+=","
    conteudo.append(final)
arquivo = open('Conversor.txt', 'w')
arquivo.writelines(conteudo)

arquivo.close()

arquivo = open('Conversor.txt', 'r')
livro=arquivo.readlines()
et2=livro[len(livro)-1]
lista2=et2.split(',')

