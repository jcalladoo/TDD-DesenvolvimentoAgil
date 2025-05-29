# src/servico.py

from models import Usuario
from repository import RepositorioUsuario

class ServicoUsuario:
    def __init__(self, repositorio: RepositorioUsuario):
        self.repositorio = repositorio

    def cadastrar_usuario(self, nome: str, email: str, senha: str) -> bool:
        if not nome or not email or not senha:
            return False
        if self.repositorio.buscar_por_email(email):
            return False
        usuario = Usuario(nome, email, senha)
        self.repositorio.adicionar_usuario(usuario)
        return True

    def login(self, email: str, senha: str) -> bool:
        usuario = self.repositorio.buscar_por_email(email)
        if not usuario or usuario.senha != senha:
            return False
        return True
