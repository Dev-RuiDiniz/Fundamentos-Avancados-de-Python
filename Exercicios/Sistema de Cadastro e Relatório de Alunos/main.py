from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


# Tupla com os campos do cadastro (imutável)
campos = ('nome', 'idade', 'nota', 'aprovado')

# Lista para armazenar os alunos
alunos = []

# Flag de controle
continuar = True
contador = 1

while continuar:
    print(f"\n--- Cadastro do aluno {contador} ---")
    nome = input("Nome: ")                     # str
    idade = int(input("Idade: "))              # int
    nota = float(input("Nota final: "))        # float
    aprovado = nota >= 6.0                     # bool

    # Dicionário com os dados do aluno
    aluno = {
        'nome': nome,
        'idade': idade,
        'nota': nota,
        'aprovado': aprovado
    }

    alunos.append(aluno)
    contador += 1

    # Perguntar se o usuário quer continuar
    resposta = input("Deseja cadastrar outro aluno? (s/n): ").lower()
    if resposta != 's':
        continuar = False


# Exibir Relatório Geral
print("\n=== RELATÓRIO GERAL ===")
for aluno in alunos:
    status = "Aprovado" if aluno['aprovado'] else "Reprovado"
    print(f"{aluno['nome']} ({aluno['idade']} anos) - Nota: {aluno['nota']} - {status}")

# Gerar Conjunto com Alunos Aprovados (usando set)
aprovados = set()
for aluno in alunos:
    if aluno['aprovado']:
        aprovados.add(aluno['nome'])

print("\nAlunos aprovados (sem repetições):")
print(aprovados)

# Média das Notas (usando list + cálculo)
notas = [aluno['nota'] for aluno in alunos]
media = sum(notas) / len(notas)
print(f"\nMédia geral das notas: {media:.2f}")

# Função para gerar o PDF
def gerar_relatorio_pdf(alunos, nome_arquivo="relatorio_alunos.pdf"):
    pdf = canvas.Canvas(nome_arquivo, pagesize=A4)
    largura, altura = A4

    pdf.setTitle("Relatório de Alunos")
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(200, altura - 50, "Relatório de Alunos")

    pdf.setFont("Helvetica", 12)
    y = altura - 100

    for aluno in alunos:
        status = "Aprovado" if aluno['aprovado'] else "Reprovado"
        linha = f"Nome: {aluno['nome']} | Idade: {aluno['idade']} | Nota: {aluno['nota']} | Situação: {status}"
        pdf.drawString(50, y, linha)
        y -= 20

        if y < 100:  # Nova página se necessário
            pdf.showPage()
            y = altura - 50
            pdf.setFont("Helvetica", 12)

    pdf.save()
    print(f"\n📄 Relatório PDF gerado com sucesso: {nome_arquivo}")

# Chamada da função
gerar_relatorio_pdf(alunos)
