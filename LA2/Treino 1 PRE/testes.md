##
#
# All tests in the folder "test" are executed
# when the "Test" action is invoked.
#
##

from Root.src.frequencia import frequencia
from Root.src.robot import robot
from Root.src.cruzamentos import cruzamentos
from Root.src.factoriza import factoriza
from Root.src.apelidos import apelidos
from Root.src.hacker import hacker
from Root.src.isbn import isbn
from Root.src.repete import repete
from Root.src.futebol import tabela
from Root.src.aloca import aloca
import unittest

class frequenciaTest(unittest.TestCase):
    
    def test_frequencia_1(self):
        with test_timeout(self,1):
            self.assertEqual(frequencia("o tempo perguntou ao tempo quanto tempo o tempo tem"),['tempo','o','ao','perguntou','quanto','tem'])

    def test_frequencia_2(self):
        with test_timeout(self,1):
            self.assertEqual(frequencia("ola"),['ola'])

class factorizaTest(unittest.TestCase):
    
    def test_factoriza_1(self):
        with test_timeout(self,1):
            self.assertEqual(factoriza(6),5)
        
    def test_factoriza_2(self):
        with test_timeout(self,1):
            self.assertEqual(factoriza(28),9)

class apelidosTest(unittest.TestCase):
    
    def test_apelidos_1(self):
        with test_timeout(self,1):
            self.assertEqual(apelidos(['Jose Carlos Bacelar Almeida', 'Maria Joao Frade', 'Jose Bernardo Barros', 'Jorge Manuel Matos Sousa Pinto', 'Manuel Alcino Pereira Cunha', 'Xico Esperto']),['Xico Esperto', 'Jose Bernardo Barros', 'Maria Joao Frade', 'Jose Carlos Bacelar Almeida', 'Manuel Alcino Pereira Cunha', 'Jorge Manuel Matos Sousa Pinto'])

    def test_apelidos_2(self):
        with test_timeout(self,1):
            self.assertEqual(apelidos(['Pedro Silva','Pedro Pereira']),['Pedro Pereira','Pedro Silva'])
            
class robotTest(unittest.TestCase):
    
    def test_robot_1(self):
        with test_timeout(self,1):
            self.assertEqual(robot("EEAADAAAAAADAAAADDDAAAHAAAH"),[(-9,-2,0,2),(0,0,0,3)])

    def test_robot_2(self):
        with test_timeout(self,1):
            self.assertEqual(robot("H"),[(0,0,0,0)])

class cruzamentosTest(unittest.TestCase):
    
    def test_cruzamentos_1(self):
        with test_timeout(self,1):
            self.assertEqual(cruzamentos(["raio","central","liberdade","chaos","saovictor","saovicente","saodomingos","souto","capelistas","anjo","taxa"]),[('t',1),('a',2),('e',2),('l',2),('r',2),('c',3),('o',3),('s',6)])

    def test_cruzamentos_2(self):
        with test_timeout(self,1):
            self.assertEqual(cruzamentos(["ab","bc","bd","cd"]),[('a',1),('c',2),('d',2),('b',3)])

class hackerTest(unittest.TestCase):
    def test_hacker_1(self):
        with test_timeout(self,1):
            log = [("****1234********","maria@mail.pt"),
                   ("0000************","ze@gmail.com"),
                   ("****1111****3333","ze@gmail.com")]
            self.assertEqual(hacker(log),[("00001111****3333","ze@gmail.com"),("****1234********","maria@mail.pt")])       

    def test_hacker_2(self):
        with test_timeout(self,1):
            log = [("0000************","ze@gmail.com"),
                   ("****1234********","maria@mail.pt")]
            self.assertEqual(hacker(log),[("****1234********","maria@mail.pt"),("0000************","ze@gmail.com")])       

class isbnTest(unittest.TestCase):
    
    def test_isbn_1(self):
        with test_timeout(self,1):
            livros = {
                "Todos os nomes":"9789720047572",
                "Ensaio sobre a cegueira":"9789896604011",
                "Memorial do convento":"9789720046711",
                "Os cus de Judas":"9789722036757"
            }
            self.assertEqual(isbn(livros),["Memorial do convento","Todos os nomes"])

    def test_isbn_2(self):
        with test_timeout(self,1):
            livros = {
                "Ola mundo":"0000000000001"
            }
            self.assertEqual(isbn(livros),["Ola mundo"])

class repeteTest(unittest.TestCase):
    
    def test_repete_1(self):
        with test_timeout(self,1):
            self.assertEqual(repete("amanha",2),"amanhamanha")

    def test_repete_2(self):
        with test_timeout(self,1):
            self.assertEqual(repete("ola",3),"olaolaola")

class tabelaTest(unittest.TestCase):

    def test_tabela_1(self):
        with test_timeout(self,1):
            jogos = [("Benfica",3,"Porto",2),("Benfica",0,"Sporting",0),("Porto",4,"Benfica",1),("Sporting",2,"Porto",2)]
            self.assertEqual(tabela(jogos),[('Porto', 4), ('Benfica', 4), ('Sporting', 2)])

    def test_tabela_2(self):
        with test_timeout(self,1):
            jogos = [("Benfica",3,"Porto",2),("Benfica",0,"Sporting",0),("Porto",2,"Benfica",1),("Sporting",2,"Porto",2)]
            self.assertEqual(tabela(jogos),[('Benfica', 4), ('Porto', 4), ('Sporting', 2)])

class alocaTest(unittest.TestCase):

    def test_aloca_1(self):
        with test_timeout(self,1):
            prefs = {10885:[1,5],40000:[5],10000:[1,2]}
            self.assertEqual(aloca(prefs),[40000])
        
    def test_aloca_2(self):
        with test_timeout(self,1):
            prefs = {30000:[1],20000:[2],10000:[3]}
            self.assertEqual(aloca(prefs),[])
            
if __name__ == '__main__':
    unittest.main()

import time
import signal

class TestTimeout(Exception):
    pass

class test_timeout:
  def __init__(self, test, seconds, error_message=None):
    if error_message is None:
      error_message = 'test timed out after {}s.'.format(seconds)
    self.seconds = seconds
    self.error_message = error_message
    self.test = test

  def handle_timeout(self, signum, frame):
    raise TestTimeout(self.error_message)

  def __enter__(self):
    signal.signal(signal.SIGALRM, self.handle_timeout)
    signal.alarm(self.seconds)

  def __exit__(self, exc_type, exc_val, exc_tb):
    signal.alarm(0)
    if exc_type is not None and exc_type is not AssertionError:
        self.test.fail("execution error")