algoritmo "Gerenciamento_de_Fila"

var
   nomes: vetor[1..3] de caractere
   cpfs: vetor[1..3] de caractere
   i, inicio, fim: inteiro

inicio

   inicio <- 1
   fim <- 0

   escreval("=== FILA CLINICA VIDA+ ===")

   para i de 1 ate 3 faca

      escreval("")
      escreva("Nome do paciente: ")
      leia(nomes[i])

      escreva("CPF do paciente: ")
      leia(cpfs[i])

      fim <- fim + 1

      escreval("Paciente inserido na fila!")

   fimpara

   escreval("")
   escreval("=== ATENDIMENTO ===")

   escreval("Paciente chamado: ", nomes[inicio])
   escreval("CPF: ", cpfs[inicio])

   inicio <- inicio + 1

   escreval("")
   escreval("=== PACIENTES NA FILA ===")

   para i de inicio ate fim faca
      escreval("Nome: ", nomes[i])
      escreval("CPF: ", cpfs[i])
      escreval("----------------------")
   fimpara

fimalgoritmo