class DesafioGit:
    def mostrar_mensagem_inicial(self):
        print("Bem-vindo ao Desafio de Git!")
    
    def listar_comandos_git_basicos(self):
        comandosGit = ["git init", "git add", "git commit", "git status", "git push"]
        for comando in comandosGit:
            print(comando)

    def criar_mensagem_commit(self, funcao_nome):
        print(f"Implementa função {funcao_nome}")

    def verificar_tag_valida(self, tag):
        """
        Verifica se uma tag está no formato 'vX.Y' (ex: v1.0, v2.1).
        Retorna True se o formato for válido, caso contrário False.
        """
        if isinstance(tag, str) and tag.startswith('v'):
            partes = tag[1:].split('.')
            if len(partes) == 2 and all(parte.isdigit() for parte in partes):
                return True
            else:
                return False

"""
Desafio Módulo Git

Neste arquivo você encontrará funções **incompletas** que representam
tarefas relacionadas ao aprendizado de Git e GitHub.

Seu objetivo é:
- Criar uma issue para cada função.
- Implementar a função em uma branch específica.
- Fazer commit, criar tag e abrir Pull Request.
- Repetir o processo até concluir todas as funções.

Boa sorte e bons commits! 🚀
"""
def gerar_relatorio_final(funcoes_concluidas):
    """
    Recebe uma lista com os nomes das funções implementadas
    e retorna uma mensagem final do desafio.

    Exemplo:
    gerar_relatorio_final(["mostrar_mensagem_inicial", "listar_comandos_git_basicos"])
    ->
    "Desafio concluído! 2 funções implementadas com sucesso."
    """
    pass

desafio = DesafioGit()
if __name__ == "__main__":
    desafio.mostrar_mensagem_inicial()
    print("Comandos Git Básicos:")
    desafio.listar_comandos_git_basicos()
    desafio.criar_mensagem_commit("verificar_tag_valida")
    print(desafio.verificar_tag_valida("v2.0"))