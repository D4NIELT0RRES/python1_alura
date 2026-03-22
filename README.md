# 🍽️ Sabor Express - Sistema de Gerenciamento de Restaurantes

Um aplicativo de linha de comando (CLI) desenvolvido em Python para gerenciar cadastros e status de restaurantes.

## 📋 Sobre o Projeto

Este projeto foi desenvolvido durante o curso de **Python** da Alura. Trata-se de um sistema interativo que permite gerenciar restaurantes através de um menu no terminal, armazenando informações como nome, categoria e status de funcionamento.

## ✨ Funcionalidades

- ✅ **Cadastrar restaurantes** - Adicione novos restaurantes com nome e categoria
- ✅ **Listar restaurantes** - Visualize todos os restaurantes cadastrados em formato de tabela
- ✅ **Alternar status** - Ative ou desative um restaurante com um único comando
- ✅ **Interface amigável** - Menu intuitivo com validação de entrada

## 🎯 Conceitos Aprendidos

### Python Fundamental
- **Variáveis e tipos de dados** - Strings, inteiros, booleanos
- **Estruturas de dados** - Listas e dicionários para armazenar informações
- **Estruturas de controle** - Condicionais (`if/elif/else`) e loops (`for`)
- **Tratamento de erros** - Blocos `try/except` para validação de entrada
- **Funções** - Criação e organização de código reutilizável
- **Docstrings** - Documentação de funções com explicações detalhadas

### Técnicas Avançadas
- **Operadores lógicos** - Uso do operador `not` para inverter booleanos
- **Formatação de strings** - Método `ljust()` para alinhar texto em tabelas
- **Comandos do sistema** - `os.system('clear')` para limpar o terminal
- **Boas práticas** - Código comentado e bem estruturado
- **Fluxo de controle** - Estrutura de menu com navegação entre seções

## 🚀 Como Usar

### Pré-requisitos
- Python 3.6+
- Terminal/Prompt de comando

### Executando o programa

```bash
python app.py
```

### Menu de Opções
1. **Cadastrar restaurante** - Digite o nome e categoria do novo restaurante
2. **Listar restaurantes** - Visualize todos os restaurantes cadastrados
3. **Alternar estado** - Ative ou desative um restaurante
4. **Sair** - Encerre o programa

## 📁 Estrutura do Código

```
app.py
├── restaurantes              # Lista global com restaurantes pré-cadastrados
├── exibir_nome_do_programa() # Exibe o nome em ASCII art
├── exibir_opcoes()          # Menu principal
├── cadastrar_novo_restaurante()  # Função de cadastro
├── listar_restaurantes()    # Função de listagem
├── alternar_estado_restaurante() # Função de alteração de status
├── escolher_opcao()         # Processa input do usuário
├── main()                   # Função principal
└── Funções auxiliares       # voltar_ao_menu_principal(), opcao_invalida(), etc.
```

## 💾 Estrutura de Dados

Cada restaurante é armazenado como um dicionário:

```python
{
    'nome': 'Nome do Restaurante',
    'categoria': 'Tipo de culinária',
    'ativo': True/False
}
```

## 🔑 Principais Aprendizados

| Conceito | Aplicação |
|----------|-----------|
| **Listas** | Armazenar múltiplos restaurantes |
| **Dicionários** | Organizar dados de cada restaurante |
| **Loops** | Iterar sobre restaurantes para listagem e busca |
| **Condicionais** | Validar entrada e alternar status |
| **Funções** | Dividir código em seções reutilizáveis |
| **Tratamento de erros** | Evitar crashes com entradas inválidas |
| **Formatação** | Criar saída visual organizada |

## 🎓 Próximos Passos

Melhorias futuras podem incluir:
- Persistência de dados (salvar em arquivo ou banco de dados)
- Interface gráfica (GUI)
- Busca e filtros avançados
- Sistema de avaliações e comentários
- Horário de funcionamento

## 📌 Notas Importantes

- O programa roda em macOS/Linux (usa comando `clear`)
- Dados são armazenados em memória e perdidos ao fechar o programa
- A interface é 100% baseada em terminal (CLI)

## 👨‍💻 Autor

Desenvolvido como projeto de aprendizado do curso Python - Alura

## 📄 Licença

Este projeto é livre para usar e modificar para fins educacionais.

---

**Obrigado por visualizar este repositório! 🎉**
