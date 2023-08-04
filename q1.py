'''
Testes unitários tem o objetivo de verificar uma classe de modelo específica (0,5). Nesse 
tipo de teste, é criada uma classe (subclasse de TestCase), contendo uma série de 
métodos de teste, um para condição específica de teste de seus métodos (0,2).

'''

class PerguntaModelTest(TestCase): 
    def test_publicada_recentemente_com_pergunta_no_futuro(self):
        data = timezone.now() + datetime.timedelta(seconds=1)
        pergunta = Pergunta(data_pub = data)
        self.assertIs(pergunta.publicada_recentemente(), False)

'''
Já os testes funcionais possibilitam a análise do sistema do ponto de vista do usuário, 
onde são simuladas requisições HTTP direcionadas a um elemento de visão (0,5) e é 
verificado se o resultado está dentro do esperado. Também é criada uma subclasse de 
TestCase, com métodos específicos para cada requisição específica a ser testada (0,2).

'''

class IndexViewTest(TestCase):
    def test_sem_perguntas_cadastradas(self):
        resposta = self.client.get(reverse('enquetes:index'))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, 'Nenhuma enquete cadastrada')
        self.assertQuerysetEqual(
        resposta.context['pergunta_list'], []
 )