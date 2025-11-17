class NoAVL:
    def __init__(self, chave, dado):
        self.chave = chave #ID
        self.dado = dado
        self.esquerda = None
        self.direita = None
        self.altura = 1

class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def _altura(self, no):
        if not no: # verifica se o nó exist
            return 0 # caso não, altura = 0
        return no.altura
    
    def _fb(self, no):
        # calculo do fator balanceamento
        if not no:
            return 0 
        return self._altura(no.esquerda) - self._altura(no.direita)
    #caso fb > 1, peso na esquerda, caso fb < -1, direita

    def _rotacaoDireita(self, y):


        x = y.esquerda # recebe o 'filho' da esquerda
        netoDireita = x.direita # recebe o neto da direita

        # rotação de fato
        x.direita = y
        y.esquerda = netoDireita # a variável com o valor de x.direita antigo

        # atualização de altura
        y.altura = 1 + max(self._altura(y.esquerda), self._altura(y.direita))
        x.altura = 1 + max(self._altura(x.esquerda), self._altura(x.direita))
        # pega a altura máxima x e y de ambos os lados e adiciona 1, sendo este '+1' o próprio nó ao topo da árvore

        return x # retorna o novo 'pai'
    
    def _rotacaoEsquerda(self, x):
        y = x.direita
        netoEsquerda = y.esquerda

        # rotação igual a direita
        y.esquerda = x
        x.direita = netoEsquerda

        # atualiza altura
        x.altura = 1 + max(self._altura(x.esquerda), self._altura(x.direita))
        y.altura = 1 + max(self._altura(y.esquerda), self._altura(y.direita))

        return y 
    
    def inserir(self, chave, dado):
        self.raiz = self._inserir(self.raiz, chave, dado)

    def _inserir(self, no, chave, dado):
        if not no: # se não tiver nenhum nó
            return NoAVL(chave, dado) # cria um nó
        
        #decide se irá para esquerda ou direita
        if chave < no.chave:
            no.esquerda = self._inserir(no.esquerda, chave, dado)
        elif chave > no.chave:
            no.direita = self._inserir(no.direita, chave, dado)
        else:
            return no
        
        # atualiza altura
        no.altura = 1 + max(self._altura(no.esquerda), self._altura(no.direita))

        fb = self._fb(no) # fator balanceamento (verificação)

        # 1. rotação esquerda esquerda
        if fb > 1 and chave < no.esquerda.chave:
            return self._rotacaoDireita(no)
        
        # 2. rotação direita direita
        if fb < -1 and chave > no.direita.chave:
            return self._rotacaoEsquerda(no)
        
        # 3. rotação esquerda direita
        if fb > 1 and chave > no.esquerda.chave:
            no.esquerda = self._rotacaoEsquerda(no.esquerda)
            return self._rotacaoDireita(no)
        
        # 4. rotação direita esquerda
        if fb < -1 and chave < no.direita.chave:
            no.direita - self._rotacaoDireita(no.direita)
            return self._rotacaoEsquerda(no)
        
        return no # caso balanceamento seja desnecessário
    
    def buscar(self, chave):
        # método que busca elemento pela chave
        return self._buscar(self.raiz, chave)

    def _buscar(self, no, chave):
        if not no:
            return None # retorna none caso não o encontre
        
        if chave == no.chave:
            return no.dado # caso encontrado, retorna todo o dicionário
        elif chave < no.chave:
            return self._buscar(no.esquerda, chave) # busca na esquerda
        else:
            return self._buscar(no.direita, chave) # busca na direita
        
    def ordenado(self):
        # retorna os elementos em ordem crescente
        resultado = []
        self._ordenado(self.raiz, resultado)
        return resultado
    
    def _ordenado(self, no, resultado):
        if no:
            self._ordenado(no.esquerda, resultado)
            resultado.append(no.dado)
            self._ordenado(no.direita, resultado)