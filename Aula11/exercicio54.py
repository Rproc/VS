# Apenas para deixar o print em forma de tabela
# Comece a ver o codigo da linha 35 (onde encontra-se a declaração da classe Funcionario)
from tabulate import tabulate

# função para verificar se podemos adicionar novos funcionarios e se for possível, verificar se ele é professor ou não
def verificarDisponibilidade(listaFuncionario, nome, salario, cargo):

    # primeira verificação (se posso ter mais funcionarios) -- lembra que podemos ter apenas 5 funcionários no máximo.
    # caso já haja 5 funcionários não entrará no IF e irá para o ELSE na linha 28 e falará que não há mais vagas
    if len(listaFuncionario) < 5:

        # caso haja vaga, vou ver se o funcionário que eu quero cadastrar é um professor.
        if cargo != 'Professor': # caso não seja professor
            funcionario = Funcionario(nome, salario, cargo) # crio o funcionario (instancio um objeto da classe Funcionario)
            listaFuncionario.append(funcionario) # coloco ele na lista de funcionários
            print('Funcionário cadastrado') # Informo que ele foi criado e adicionado na lista com sucesso.
        else: # caso o funcionário que eu queria adicionar seja professor
            controleProfessores = 0 # variavel auxiliar para contar quantos professores já tem na lista de funcinários
            for funcionario in listaFuncionario: # para cada funcionário na lista de funcionarios
                if funcionario.cargo == 'Professor': # verifica se o cargo dele é professor
                    controleProfessores += 1 # caso seja soma +1 na variavel auxiliar
            # nota que só pode ter no máximo 2 professores
            if controleProfessores < 2: # caso haja menos de 2 professores cadastrados (nenhum professor ou 1 professor na lista de funcionários)
                funcionario = Funcionario(nome, salario, cargo) # adiciono o professor
                listaFuncionario.append(funcionario) # insiro meu novo funcionário (que é um professor na lista)
            else: # caso já exista 2 professores cadastrados na lista de funcionários
                print('Não há disponibilidade para cadastrar mais professores') # informo que não há mais vagas para professor
    else:
        print('Não há vagas')


# o jeito mais facil de iniciar a ideia de funcionario que tem seu tipo e tem atribuições é usar uma classe
# cada objeto vai ter atributos e funções atreladas a ele 
# (note que esse não é o melhor jeito de fazer no final, aqui para ficar mais bem feito deveria utilizar herança)
class Funcionario():

    # método construtor (criar nosso funcionario)
    # Pergunta: o que funcionario deve ter? (resposta: ler o enunciado, tudo que aparece la no texto deve aparecer aqui)
    # Versão mais facil: só atributos necessarios como o enunciado pede
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo # saber se ele é professor ou não
        self.disciplinas = [] # caso seja professor, adicionar as disciplinas (pq não fala de onde é o professor, se for de médio/técnico e/ou faculdade ele pode lecionar mais de uma disciplina)

    # cadastrar disciplina (num sistema maior (tipo de escola) está função não estaria aqui dentro de funcionário)
    def cadastrarDisciplina(self, disciplinas):
        # só pode ter disciplinas caso o cargo seja professor
        if self.cargo == 'Professor': #verifica se é professor
            self.disciplinas.append(disciplinas) # adiciona a(s) disciplina(s)
        else:
            print('Só professores podem lecionar') # erro caso não seja professor


# "Inicio do codigo (num cenario maior, definiriamos uma função main (função principal)"
lista = [] # cria uma lista vazia para colocar os funcionarios posteriormente
funcionario1 = Funcionario('Renan', 1000, 'Professor') # cria o primeiro funcionario
funcionorio2 = Funcionario('Will', 1000, 'Professor') # cria o segundo funcionario (note que nesse caso os 2 são professores, mas poderiam não ser)

lista.append(funcionario1) # adiciona o primeiro funcionario na lista
lista.append(funcionorio2) # adiciona o segundo funcionario na lista

# como nosso sistema só aceita 5 funcionarios no maximo e 2 professores, temos que verificar a disponibilidade das duas coisas:
# 1. já existem 5 funcionarios cadastrados no meu sistema?
# 2. já existem 2 professores cadastrados no meu sistema?
# Faremos essas perguntas dentro desta função -> passamos a lista de funcionários atual, e os dados do próximo funcionário a ser adicionado (agora vamos para a linha 5 do codigo)
verificarDisponibilidade(lista, 'Ana', 1000, 'Porteiro')
verificarDisponibilidade(lista, 'Bruno', 1000, 'Secretária')
verificarDisponibilidade(lista, 'Fernanda', 1000, 'Bibliotecária')

# adicionando uma disciplina ao funcionario 1, criado na linha 58
funcionario1.cadastrarDisciplina('Português')
# outra forma de cadastrar disciplinas seria acessando a lista
#lista[2].cadastrarDisciplina('Português') # essa linha de codigo resultara num erro, pois a posição [2] da lista é o funcionário "Ana" que não tem cargo de professor
#print(funcionario1.disciplinas)

# Isso é list comprehension (compreensão de lista) [poucas linguagens tem essa funcionalidade] (linguagem de uso geral que eu conheça só Python e Julia [apesar de Julia não ser muito geral] que tem)
# a ideia da linha abaixo é pegar os nomes, os salarios e os cargos de todos os funcionarios na lista de funcionarios e salvar na variavel "data"
# para fazer isso em outras linguagens vc precisaria estruturar o for em uma linha e os atributos na linha abaixo dentro do loop
data = [[funcionario.nome, funcionario.salario, funcionario.cargo] for funcionario in lista]
# essa estrutura tbm aceita IF na linha, ele viria após lista. Ex.: -> 
# data = [[funcionario.nome, funcionario.salario, funcionario.cargo] for funcionario in lista if funcionario.cargo == 'Professor']

# print de forma tabular, ao inves de ficar um embaixo do outro, cria-se uma tabela desenhada (estilo rudimentar de uma tabela do word) [quem faz isso é a tabulate]
# data é uma matriz (lista de lista) -> headers significa cabeçalho e recebe uma lista como parametro (que é o nome que vc quer dar as colunas)
print(tabulate(data, headers=["Nome", "Salário", "Cargo"]))
