from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    matricula = models.CharField(max_length=50)

class Rendimento(models.Model):

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, null=True)
    diario = models.ForeignKey('Diario', on_delete=models.CASCADE, null=True, related_name='diario_rendimentos')

    nota1 = models.IntegerField()
    nota2 = models.IntegerField()
    num_faltas = models.IntegerField()

    def media(self): # retorna inteiro
        return int((self.nota1 + self.nota2)/2)
    
    def percent_faltas(self): # retorna float
        if self.diario:
            diario = self.diario

        return round(((self.num_faltas / diario.num_aulas) * 100.0), 2)
    
    def aprovado(self): # retorna bool
        if self.media() >= 70 and self.percent_faltas() < 25:
            return True
        else:
            return False
    
    def final(self): # retorna bool
        if self.media() <= 70 and self.percent_faltas() < 25:
            return True
        else:
            return False

class Diario(models.Model):

    disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE, null=True, related_name='disciplina_diario')

    codigo = models.CharField(max_length=50)
    num_aulas = models.IntegerField()
    ano = models.IntegerField()
    semestre = models.IntegerField()

    def percent_conclusao(self):
        return (self.num_aulas / self.disciplina.carga_horaria) * 100

class Disciplina(models.Model):
    nome = models.CharField(max_length=50)
    carga_horaria = models.IntegerField()