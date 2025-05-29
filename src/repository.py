from typing import Dict, Optional
from models import Usuario

class RepositorioUsuario:
    def __init__(self):
        self.usuarios: Dict[str, Usuario] = {}

    def adicionar_usuario(self, usuario: Usuario) -> None:
        self.usuarios[usuario.email] = usuario

    def buscar_por_email(self, email: str) -> Optional[Usuario]:
        return self.usuarios.get(email)
