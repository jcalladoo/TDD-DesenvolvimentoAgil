# tests/teste_servico_usuario.py

import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from models import Usuario
from repository import RepositorioUsuario
from service import ServicoUsuario

@pytest.fixture
def servico_usuario():
    repositorio = RepositorioUsuario()
    return ServicoUsuario(repositorio)

def test_cadastro_valido(servico_usuario):
    resultado = servico_usuario.cadastrar_usuario("Alice", "alice@example.com", "senha123")
    assert resultado is True

def test_cadastro_com_email_existente(servico_usuario):
    servico_usuario.cadastrar_usuario("Alice", "alice@example.com", "senha123")
    resultado = servico_usuario.cadastrar_usuario("Joao", "alice@example.com", "senha456")
    assert resultado is False

def test_cadastro_com_dados_faltando(servico_usuario):
    assert servico_usuario.cadastrar_usuario("", "Joao@example.com", "senha123") is False
    assert servico_usuario.cadastrar_usuario("Joao", "", "senha123") is False
    assert servico_usuario.cadastrar_usuario("Joao", "Joao@example.com", "") is False

def test_login_credenciais_validas(servico_usuario):
    servico_usuario.cadastrar_usuario("Alice", "alice@example.com", "senha123")
    resultado = servico_usuario.login("alice@example.com", "senha123")
    assert resultado is True

def test_login_email_invalido(servico_usuario):
    servico_usuario.cadastrar_usuario("Alice", "alice@example.com", "senha123")
    resultado = servico_usuario.login("Joao@example.com", "senha123")
    assert resultado is False

def test_login_senha_invalida(servico_usuario):
    servico_usuario.cadastrar_usuario("Alice", "alice@example.com", "senha123")
    resultado = servico_usuario.login("alice@example.com", "senhaerrada")
    assert resultado is False
