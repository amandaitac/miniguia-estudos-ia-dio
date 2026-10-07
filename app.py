from pathlib import Path

# Localiza a base de dados do projeto
arquivo = Path(__file__).parent / "dados" / "exemplo.md"

# Verifica se o arquivo existe
if not arquivo.exists():
    print("Erro: arquivo de dados não encontrado.")
else:
    # Lê as informações da base de dados
    dados = arquivo.read_text(encoding="utf-8")

    print("=== ASSISTENTE IMOBILIÁRIO ===")
    print("Base de conhecimento carregada com sucesso!\n")
    print("Informações disponíveis:\n")
    print(dados)
