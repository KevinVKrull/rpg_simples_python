# Recomendações de Organização - RPG Simples Python

## 📋 Sumário Executivo

Este documento apresenta sugestões de organização para o projeto **RPG Mago do Tempo**, um jogo de RPG turn-based com mecânicas de viagem no tempo. O objetivo é manter a arquitetura funcional (sem classes), melhorar a legibilidade e facilitar futuras expansões.

---

## 🗂️ Estrutura Atual vs Proposta

### Estrutura Atual
```
rpg_simples_python/
├── main.py
├── acoes.py
├── boss.py
├── boss_andar.py
├── boss_voltar_magias.py
├── gerador_mapas.py
├── inventario.py (vazio)
├── itens.py
├── magias_jogador.py
├── mercador.py
└── tesouros.py
```

### Estrutura Proposta
```
rpg_mago_do_tempo/
│
├── main.py                          # Ponto de entrada principal
│
├── config/                          # Configurações e constantes
│   ├── __init__.py
│   ├── constantes.py                # Constantes do jogo (HP inicial, mana, etc)
│   └── balanceamento.py             # Valores de balanceamento (dano, custos)
│
├── core/                            # Núcleo do jogo
│   ├── __init__.py
│   ├── loop_combate.py              # Loop principal de combate (extraído do main.py)
│   ├── loop_exploracao.py           # Loop de exploração da torre
│   └── gerenciador_estado.py       # Salvar/carregar estado do jogo
│
├── combate/                         # Sistema de combate
│   ├── __init__.py
│   ├── acoes_jogador.py             # Ações do jogador em combate (renomeado: magias_jogador.py)
│   ├── acoes_inimigo.py             # Ações dos inimigos (renomeado: boss.py)
│   ├── mecanica_tempo.py            # Sistema de viagem no tempo (renomeado: boss_voltar_magias.py)
│   └── calculo_dano.py              # Cálculos de dano, defesa, etc
│
├── entidades/                       # Definições de entidades
│   ├── __init__.py
│   ├── jogador.py                   # Definição e funções do jogador
│   ├── inimigos.py                  # Definições de inimigos (renomeado: boss_andar.py)
│   └── chefes.py                    # Definições dos 5 Lordes Sombrios
│
├── inventario/                      # Sistema de inventário
│   ├── __init__.py
│   ├── gerenciador.py               # Funções de gerenciamento (renomeado: inventario.py)
│   ├── definicoes_itens.py          # Definições de itens (renomeado: itens.py)
│   └── efeitos_itens.py             # Funções de uso/equipar itens
│
├── mundo/                           # Sistema de mundo/exploração
│   ├── __init__.py
│   ├── gerador_andar.py             # Gerar andares da torre (renomeado: gerador_mapas.py)
│   ├── tipos_sala.py                # Lógica de cada tipo de sala
│   ├── interacoes_tesouro.py        # Sistema de tesouros (renomeado: tesouros.py)
│   └── interacoes_mercador.py       # Sistema de mercador (renomeado: mercador.py)
│
├── ui/                              # Interface com usuário
│   ├── __init__.py
│   ├── menus.py                     # Menus e escolhas (renomeado: acoes.py)
│   ├── exibicao_combate.py          # Exibição de informações de combate
│   ├── exibicao_mapa.py             # Exibição do mapa e navegação
│   ├── narrativa.py                 # Textos narrativos e história
│   └── utilitarios.py               # Funções auxiliares (limpar tela, pausas)
│
├── dados/                           # Arquivos de dados (futuro)
│   ├── dialogos.json
│   ├── itens.json
│   └── inimigos.json
│
└── testes/                          # Testes (futuro)
    ├── __init__.py
    ├── test_combate.py
    └── test_inventario.py
```

---

## 📝 Renomeação de Arquivos (Mapeamento)

### Arquivos Existentes → Novos Nomes

| Arquivo Atual | Novo Nome | Justificativa |
|--------------|-----------|---------------|
| `acoes.py` | `ui/menus.py` + `ui/utilitarios.py` | Separar menus de utilidades de UI |
| `boss.py` | `combate/acoes_inimigo.py` | Nome mais genérico para todos os inimigos |
| `boss_andar.py` | `entidades/inimigos.py` + `entidades/chefes.py` | Separar inimigos comuns de chefes |
| `boss_voltar_magias.py` | `combate/mecanica_tempo.py` | Nome mais descritivo da mecânica única |
| `gerador_mapas.py` | `mundo/gerador_andar.py` + `mundo/tipos_sala.py` | Separar geração de lógica das salas |
| `inventario.py` | `inventario/gerenciador.py` | Mover para módulo dedicado |
| `itens.py` | `inventario/definicoes_itens.py` | Clarificar que são definições |
| `magias_jogador.py` | `combate/acoes_jogador.py` | Incluir todas as ações, não só magias |
| `mercador.py` | `mundo/interacoes_mercador.py` | Agrupar com outras interações do mundo |
| `tesouros.py` | `mundo/interacoes_tesouro.py` | Agrupar com outras interações do mundo |

---

## 🔧 Detalhamento das Mudanças

### 1. **config/** - Configuração Centralizada

**Objetivo:** Centralizar constantes e valores de balanceamento para facilitar ajustes.

#### `config/constantes.py`
```python
# Extrair valores hardcoded do código
JOGADOR_VIDA_INICIAL = 150
JOGADOR_MANA_INICIAL = 120
JOGADOR_DEFESA_BASE = 0
JOGADOR_VELOCIDADE_BASE = 5

# Custos de mana
CUSTO_RAJADA_TEMPORAL = 5
CUSTO_FENDA_TEMPO = 15
CUSTO_RESSURGIR_TEMPORAL = 40

# Limites
MAX_INVENTARIO = 10
TURNOS_MINIMOS_RESSURGIR = 3
```

#### `config/balanceamento.py`
```python
# Dano das habilidades
RAJADA_TEMPORAL_DANO = (10, 15)
FENDA_TEMPO_DANO = (20, 30)
POCAO_VIDA_CURA = (20, 30)
POCAO_MANA_RESTAURACAO = (25, 35)

# Boss - Lorde Sombrio
EXPLOSAO_CAOS_PERCENTUAL = 0.5
SOCO_SOMBRIO_DANO = (10, 20)
CHANCE_EXPLOSAO_INICIAL = 0.3
INCREMENTO_EXPLOSAO = 0.2

# Probabilidades
CHANCE_MIMIC = 0.1
```

---

### 2. **core/** - Lógica Principal

**Objetivo:** Separar os loops principais que atualmente estão no `main.py`.

#### `core/loop_combate.py`
- `executar_combate(jogador, inimigo)` - Loop de combate completo
- `processar_turno_jogador(jogador, inimigo, acao)` - Turno do jogador
- `processar_turno_inimigo(jogador, inimigo)` - Turno do inimigo
- `verificar_fim_combate(jogador, inimigo)` - Condições de vitória/derrota

#### `core/loop_exploracao.py`
- `executar_exploracao_torre(jogador, andar_inicial)` - Loop principal da torre
- `processar_movimento(mapa, posicao, direcao)` - Movimentação WASD
- `processar_sala(tipo_sala, jogador, andar)` - Executar evento da sala
- `avancar_andar(jogador, andar_atual)` - Subir escadas

#### `core/gerenciador_estado.py` (Novo)
- `salvar_jogo(jogador, andar, posicao)` - Salvar progresso
- `carregar_jogo()` - Carregar save
- `criar_checkpoint(jogador)` - Checkpoint temporário

---

### 3. **combate/** - Sistema de Combate

#### `combate/acoes_jogador.py`
Consolidar todas as ações do jogador:
- `executar_rajada_temporal(jogador, inimigo)`
- `executar_fenda_tempo(jogador, inimigo)`
- `executar_ressurgir_temporal(jogador, inimigo, historico, ataques_boss)`
- `executar_defender(jogador)` - Ativar defesa
- `executar_usar_pocao_vida(jogador)`
- `executar_usar_pocao_mana(jogador)`
- `executar_usar_item_inventario(jogador, item)` - Nova função

#### `combate/acoes_inimigo.py`
Generalizar para todos os inimigos:
- `executar_ataque_inimigo(inimigo, jogador)` - Escolher e executar ataque
- `ataque_explosao_caos(inimigo, jogador)` - Boss específico
- `ataque_soco_sombrio(inimigo, jogador)` - Boss específico
- `ataque_guardiao_pedra(guardiao, jogador)` - Novo
- `ataque_necromante(necromante, jogador)` - Novo

#### `combate/mecanica_tempo.py`
Sistema único de viagem no tempo:
- `salvar_snapshot_historico(jogador, inimigo, turno)` - Salvar estado
- `reverter_tempo(jogador, inimigo, historico, num_turnos)` - Voltar no tempo
- `reproduzir_ataques_boss(jogador, ataques_reversos)` - Replay de ataques
- `limpar_historico_antigo(historico, limite)` - Gerenciar memória

#### `combate/calculo_dano.py` (Novo)
Centralizar cálculos:
- `calcular_dano(dano_base, defensor)` - Considerar armadura/defesa
- `calcular_dano_percentual(alvo, percentual)` - Para Explosão do Caos
- `aplicar_dano(alvo, dano)` - Aplicar e retornar se matou
- `calcular_ordem_turno(jogador, inimigo)` - Baseado em velocidade

---

### 4. **entidades/** - Definições de Entidades

#### `entidades/jogador.py`
- `criar_jogador()` - Retorna dicionário do Mago do Tempo
- `recuperar_vida(jogador, quantidade)`
- `recuperar_mana(jogador, quantidade)`
- `gastar_mana(jogador, quantidade)`
- `adicionar_moedas(jogador, quantidade)`
- `equipar_item(jogador, item)` - Nova
- `aplicar_regeneracao(jogador)` - Se tiver amuleto

#### `entidades/inimigos.py`
Definições de inimigos comuns:
- `criar_guardiao_pedra()`
- `criar_sombra_veloz()`
- `criar_necromante()`
- `criar_esqueleto()`
- `criar_golem_arcano()`
- `criar_mimic()` - Novo

#### `entidades/chefes.py`
Definições dos 5 Lordes:
- `criar_lorde_sombrio()` - Já existe
- `criar_lorde_do_gelo()` - Novo
- `criar_lorde_do_fogo()` - Novo
- `criar_lorde_da_tempestade()` - Novo
- `criar_lorde_final()` - Novo

---

### 5. **inventario/** - Sistema de Inventário

#### `inventario/gerenciador.py`
- `adicionar_item(jogador, item)` - Verificar limite
- `remover_item(jogador, item_nome, quantidade)`
- `buscar_item(jogador, item_nome)`
- `listar_inventario(jogador)` - Retornar lista formatada
- `inventario_cheio(jogador)`
- `empilhar_item(jogador, item)` - Para itens stackable

#### `inventario/definicoes_itens.py`
Manter definições atuais + adicionar:
- `obter_item_por_nome(nome)` - Helper para buscar
- `listar_itens_por_tipo(tipo)` - Filtrar por categoria
- Expandir categorias: poções, materiais, quest items

#### `inventario/efeitos_itens.py` (Novo)
- `usar_item(jogador, item)` - Aplicar efeito
- `equipar_arma(jogador, arma)`
- `equipar_armadura(jogador, armadura)`
- `equipar_amuleto(jogador, amuleto)`
- `desequipar_item(jogador, slot)`

---

### 6. **mundo/** - Exploração e Interações

#### `mundo/gerador_andar.py`
- `gerar_andar(numero_andar)` - Retornar mapa completo
- `gerar_layout_salas(tamanho)` - Grid de tipos de sala
- `criar_mapa_visivel(tamanho)` - Fog of war inicial
- `revelar_sala(mapa_visivel, posicao)`
- `balancear_salas_por_andar(numero_andar)` - Dificuldade progressiva

#### `mundo/tipos_sala.py`
- `processar_sala_combate(jogador, andar)` - Spawnar inimigo
- `processar_sala_tesouro(jogador, andar)` - Chamar sistema de tesouro
- `processar_sala_mercador(jogador, andar)` - Chamar mercador
- `processar_sala_descanso(jogador)` - Curar/restaurar
- `processar_sala_evento(jogador, andar)` - Eventos aleatórios
- `processar_sala_escadas(jogador, andar)` - Boss do andar

#### `mundo/interacoes_tesouro.py`
- `abrir_bau(jogador, tipo_bau)` - Lógica atual
- `rolar_item_bau(tipo_bau)` - Escolher item aleatório
- `encontrar_mimic(jogador)` - Combate surpresa
- `gerar_bau_por_andar(andar)` - Madeira → Prata → Ouro

#### `mundo/interacoes_mercador.py`
- `iniciar_mercador(jogador, andar)` - Menu de compra
- `gerar_estoque_mercador(andar)` - Itens disponíveis
- `comprar_item(jogador, item)` - Processar compra
- `vender_item(jogador, item)` - Nova: vender por moedas

---

### 7. **ui/** - Interface do Usuário

#### `ui/menus.py`
- `exibir_menu_principal()` - Novo jogo / Carregar / Sair
- `exibir_menu_combate()` - 6 opções atuais + usar item
- `exibir_menu_inventario(jogador)` - Visualizar/usar itens
- `exibir_menu_mercador(estoque)` - Comprar/vender
- `obter_escolha_usuario(opcoes)` - Input validado

#### `ui/exibicao_combate.py`
- `exibir_status_combate(jogador, inimigo, turno)`
- `exibir_resultado_acao(mensagem, tipo)` - Sucesso/erro/dano
- `exibir_turno_inimigo(inimigo, acao, dano)`
- `exibir_fim_combate(vitoria, jogador, inimigo)`

#### `ui/exibicao_mapa.py`
- `exibir_mapa(mapa_visivel, posicao_jogador)`
- `exibir_legenda_mapa()`
- `exibir_entrada_sala(tipo_sala)`
- `exibir_comandos_movimento()`

#### `ui/narrativa.py`
- `exibir_introducao()`
- `exibir_dialogo_lorde_sombrio()`
- `exibir_transicao_torre()`
- `exibir_dialogo_andar(numero_andar)`
- `exibir_vitoria_final()`
- `exibir_derrota()`

#### `ui/utilitarios.py`
- `limpar_tela()` - Função atual `apagar()`
- `pausar(mensagem)` - Input para continuar
- `exibir_barra_vida(vida_atual, vida_max)`
- `exibir_barra_mana(mana_atual, mana_max)`
- `formatar_moedas(quantidade)`

---

## 🎯 Vantagens da Nova Estrutura

### 1. **Separação de Responsabilidades**
- UI separada da lógica de negócio
- Combate isolado de exploração
- Fácil encontrar e modificar funcionalidades

### 2. **Escalabilidade**
- Adicionar novos inimigos: apenas `entidades/inimigos.py`
- Adicionar novas salas: apenas `mundo/tipos_sala.py`
- Adicionar novos itens: apenas `inventario/definicoes_itens.py`

### 3. **Manutenibilidade**
- Constantes centralizadas facilitam balanceamento
- Módulos pequenos são mais fáceis de entender
- Nomes descritivos reduzem necessidade de documentação

### 4. **Testabilidade**
- Funções isoladas são mais fáceis de testar
- Mocks mais simples de criar
- Estrutura `testes/` paralela à estrutura do código

### 5. **Reutilização**
- Sistema de combate pode ser usado em várias situações
- Calculadora de dano centralizada evita inconsistências
- Gerenciador de inventário serve para todas as entidades

---

## 🚀 Sugestões de Evolução do Projeto

### Fase 1: Completar Funcionalidades Básicas (Curto Prazo)

#### 1.1 Sistema de Combate com Guardiões
- **Arquivo:** `mundo/tipos_sala.py` → `processar_sala_combate()`
- **Ação:** Implementar combates com inimigos do andar
- **Incluir:** Sistema de velocidade (ordem de ataque)

#### 1.2 Sala de Descanso
- **Arquivo:** `mundo/tipos_sala.py` → `processar_sala_descanso()`
- **Opções:**
  - Descansar: +30% vida, +50% mana (1x por andar)
  - Meditar: +100% mana
  - Dormir: +100% vida

#### 1.3 Sistema de Eventos Aleatórios
- **Arquivo:** `mundo/tipos_sala.py` → `processar_sala_evento()`
- **Exemplos:**
  - Fonte mística: escolha entre vida ou mana
  - Armadilha: teste de sorte (dano ou moedas)
  - Mercador ambulante: preços mais baratos
  - Biblioteca: aprender nova magia temporária

#### 1.4 Sistema de Equipamento
- **Arquivos:** `inventario/efeitos_itens.py` + `entidades/jogador.py`
- **Funcionalidade:**
  - Slots: arma, armadura, amuleto
  - Efeitos permanentes ao equipar
  - Bonificações aplicadas automaticamente

#### 1.5 Balanceamento do Primeiro Boss
- **Arquivo:** `entidades/chefes.py` → `criar_lorde_sombrio()`
- **Ação:** Aumentar vida de 1 para ~200 HP
- **Ajustar:** Balancear pesos do gerador de mapas (remover 100% mercador)

---

### Fase 2: Expansão de Conteúdo (Médio Prazo)

#### 2.1 Sistema de Progressão Multi-Andar
- **Objetivo:** Implementar os 5 andares completos
- **Boss por Andar:**
  - Andar 1: Lorde Sombrio (Atual)
  - Andar 2: Lorde do Gelo (Congela mana)
  - Andar 3: Lorde do Fogo (Dano ao longo do tempo)
  - Andar 4: Lorde da Tempestade (Ataques que ignoram defesa)
  - Andar 5: Lorde Final (Todas as habilidades)

#### 2.2 Sistema de Magias Avançadas
- **Arquivo:** `combate/acoes_jogador.py`
- **Novas Magias:**
  - **Paradoxo Temporal** (60 mana): Próximo ataque do boss erra
  - **Aceleração Temporal** (30 mana): 2 ataques no próximo turno
  - **Bolha Temporal** (50 mana): Escudo que absorve 1 ataque
  - **Desintegração Temporal** (80 mana): Dano massivo ignora defesa

#### 2.3 Sistema de Crafting
- **Novo Módulo:** `inventario/crafting.py`
- **Funcionalidade:**
  - Combinar fragmentos temporais para criar itens
  - Melhorar equipamentos existentes
  - Criar poções especiais

#### 2.4 Inimigos Especiais e Mini-Bosses
- **Arquivo:** `entidades/inimigos.py`
- **Tipos:**
  - Inimigos de elite (2x vida, 1.5x dano)
  - Mini-bosses em salas especiais
  - Inimigos com habilidades únicas

#### 2.5 Sistema de Quests Secundárias
- **Novo Módulo:** `mundo/quests.py`
- **Exemplos:**
  - "Coletor de Fragmentos": Coletar 10 fragmentos temporais
  - "Exterminador": Derrotar 20 inimigos
  - "Explorador": Visitar todas as salas de um andar

---

### Fase 3: Polimento e Features Avançadas (Longo Prazo)

#### 3.1 Sistema de Save/Load
- **Arquivo:** `core/gerenciador_estado.py`
- **Funcionalidade:**
  - Salvar progresso em JSON
  - Múltiplos slots de save
  - Auto-save ao subir andar

#### 3.2 Sistema de Conquistas
- **Novo Módulo:** `core/conquistas.py`
- **Exemplos:**
  - "Mestre do Tempo": Usar Ressurgir Temporal 10x
  - "Pacifista": Completar andar sem matar inimigos
  - "Colecionador": Ter todos os itens épicos

#### 3.3 Modos de Dificuldade
- **Arquivo:** `config/balanceamento.py`
- **Modos:**
  - **Fácil:** +50% vida, custos -25%
  - **Normal:** Valores atuais
  - **Difícil:** -25% vida, inimigos +50% dano
  - **Pesadelo:** Permadeath, sem ressurgir temporal

#### 3.4 Sistema de Roguelike (Morte Permanente Opcional)
- **Funcionalidade:**
  - Ao morrer, reinicia do andar 1
  - Metaprogression: desbloquear itens iniciais melhores
  - Sementes para repetir runs

#### 3.5 Boss Rush Mode
- **Novo Arquivo:** `core/modo_boss_rush.py`
- **Funcionalidade:**
  - Enfrentar todos os 5 lordes em sequência
  - Descanso limitado entre lutas
  - Ranking de tempo

#### 3.6 Sistema de Narrativa Expandida
- **Arquivo:** `ui/narrativa.py`
- **Adicionar:**
  - História de cada Lorde Sombrio
  - Diálogos com mercadores
  - Lore encontrado em livros espalhados
  - Final múltiplo baseado em escolhas

#### 3.7 Trilha Sonora e Efeitos (Text-Based)
- **Novo Módulo:** `ui/audio_visual.py`
- **Funcionalidade:**
  - ASCII art para bosses
  - Animações de texto para ataques
  - Beeps do sistema para feedback

#### 3.8 Sistema de Estatísticas
- **Novo Módulo:** `core/estatisticas.py`
- **Rastrear:**
  - Total de dano dado/recebido
  - Inimigos derrotados por tipo
  - Itens coletados
  - Tempo de jogo
  - Turnos usados

#### 3.9 Modo Multiplayer Local (Turn-Based)
- **Funcionalidade:**
  - 2 jogadores alternando turnos
  - PvP ou Co-op contra bosses mais fortes
  - Habilidades de suporte entre jogadores

#### 3.10 Exportar para Executável
- **Ferramenta:** PyInstaller
- **Objetivo:** Distribuir jogo como .exe/.app
- **Incluir:** Ícone personalizado e instalador

---

## 🏗️ Plano de Migração (Como Reorganizar)

### Passo 1: Criar Estrutura de Pastas
```bash
mkdir -p config core combate entidades inventario mundo ui dados testes
touch config/__init__.py core/__init__.py combate/__init__.py
touch entidades/__init__.py inventario/__init__.py mundo/__init__.py
touch ui/__init__.py testes/__init__.py
```

### Passo 2: Extrair Configurações
1. Criar `config/constantes.py` e `config/balanceamento.py`
2. Copiar valores hardcoded de todos os arquivos
3. Substituir valores por imports

### Passo 3: Migrar Módulo por Módulo
**Ordem recomendada:**
1. **UI primeiro** (`ui/utilitarios.py`, `ui/menus.py`) - Menos dependências
2. **Entidades** (`entidades/jogador.py`, `entidades/inimigos.py`)
3. **Combate** (`combate/acoes_jogador.py`, `combate/acoes_inimigo.py`)
4. **Inventário** (`inventario/*`)
5. **Mundo** (`mundo/*`)
6. **Core** (`core/loop_combate.py`, `core/loop_exploracao.py`)
7. **Main.py** (refatorar para usar os novos módulos)

### Passo 4: Testar Após Cada Migração
- Executar o jogo após mover cada módulo
- Verificar se tudo funciona antes de continuar

### Passo 5: Remover Arquivos Antigos
- Apenas após confirmar que a nova estrutura funciona
- Manter backup por segurança

---

## 📚 Convenções de Nomenclatura

### Arquivos e Pastas
- **Pastas:** minúsculas, singular (`combate`, não `Combate` ou `combates`)
- **Arquivos:** minúsculas com underscore (`acoes_jogador.py`)

### Funções
- **Verbos descritivos:** `criar_`, `executar_`, `processar_`, `calcular_`
- **Snake_case:** `reverter_tempo()`, não `reverterTempo()`
- **Específicas:** `executar_rajada_temporal()` > `ataque1()`

### Variáveis
- **Descritivas:** `vida_maxima` > `vmax` ou `vm`
- **Dicionários de entidade:** `jogador`, `inimigo`, `item`
- **Booleanos:** `está_vivo`, `tem_mana_suficiente`

### Constantes
- **MAIÚSCULAS:** `JOGADOR_VIDA_INICIAL`, `CUSTO_RAJADA_TEMPORAL`
- **Agrupadas por contexto:** Todas as constantes de combate juntas

---

## 🎨 Exemplos de Código Refatorado

### Antes (main.py - linhas ~1-262)
```python
# Tudo em um arquivo gigante
mago_do_tempo = {
    'vida': 150,
    'mana': 120,
    # ... resto do código
}

# Loop de combate misturado com lógica de UI
if escolha == 1:
    if mago_do_tempo['mana'] >= 5:
        dano = random.randint(10, 15)
        # ... mais código
```

### Depois (Estrutura Modular)

**config/constantes.py:**
```python
JOGADOR_VIDA_INICIAL = 150
JOGADOR_MANA_INICIAL = 120
```

**entidades/jogador.py:**
```python
from config.constantes import JOGADOR_VIDA_INICIAL, JOGADOR_MANA_INICIAL

def criar_jogador():
    return {
        'vida': JOGADOR_VIDA_INICIAL,
        'mana': JOGADOR_MANA_INICIAL,
        'defesa': 0,
        'armadura': 0,
        'moedas': 0,
        'velocidade': 5,
        'inventario': []
    }
```

**combate/acoes_jogador.py:**
```python
from config.balanceamento import RAJADA_TEMPORAL_DANO, CUSTO_RAJADA_TEMPORAL
import random

def executar_rajada_temporal(jogador, inimigo):
    if jogador['mana'] < CUSTO_RAJADA_TEMPORAL:
        return {'sucesso': False, 'mensagem': 'Mana insuficiente!'}

    jogador['mana'] -= CUSTO_RAJADA_TEMPORAL
    dano_min, dano_max = RAJADA_TEMPORAL_DANO
    dano = random.randint(dano_min, dano_max)

    inimigo['vida'] -= dano

    return {
        'sucesso': True,
        'dano': dano,
        'mensagem': f'Rajada Temporal causou {dano} de dano!'
    }
```

**main.py (Refatorado):**
```python
from entidades.jogador import criar_jogador
from entidades.chefes import criar_lorde_sombrio
from core.loop_combate import executar_combate
from core.loop_exploracao import executar_exploracao_torre
from ui.narrativa import exibir_introducao, exibir_transicao_torre

def main():
    exibir_introducao()

    jogador = criar_jogador()
    primeiro_boss = criar_lorde_sombrio()

    vitoria = executar_combate(jogador, primeiro_boss)

    if vitoria:
        exibir_transicao_torre()
        executar_exploracao_torre(jogador, andar_inicial=1)

if __name__ == '__main__':
    main()
```

---

## 📖 Documentação Adicional Recomendada

### Arquivos a Criar:

1. **README.md** - Descrição do jogo, como jogar, requisitos
2. **INSTALACAO.md** - Guia de instalação e setup
3. **CONTRIBUINDO.md** - Como contribuir com o projeto
4. **CHANGELOG.md** - Histórico de versões
5. **MECÁNICAS.md** - Documentação das mecânicas do jogo
6. **ITENS.md** - Lista de todos os itens e efeitos
7. **INIMIGOS.md** - Bestiário completo

---

## ✅ Checklist de Implementação

### Reorganização Básica
- [ ] Criar estrutura de pastas
- [ ] Criar `config/constantes.py`
- [ ] Criar `config/balanceamento.py`
- [ ] Migrar `ui/utilitarios.py`
- [ ] Migrar `entidades/jogador.py`
- [ ] Migrar `entidades/inimigos.py`
- [ ] Migrar `combate/acoes_jogador.py`
- [ ] Migrar `combate/acoes_inimigo.py`
- [ ] Migrar `inventario/gerenciador.py`
- [ ] Migrar `mundo/gerador_andar.py`
- [ ] Refatorar `main.py`
- [ ] Testar jogo completo

### Funcionalidades Faltantes
- [ ] Implementar sala de combate (guardiões)
- [ ] Implementar sala de descanso
- [ ] Implementar sala de evento
- [ ] Implementar sistema de equipamento
- [ ] Balancear primeiro boss (aumentar HP)
- [ ] Corrigir pesos do gerador de mapas

### Expansão de Conteúdo
- [ ] Criar 4 novos lordes sombrios
- [ ] Adicionar 4 novas magias
- [ ] Criar sistema de crafting
- [ ] Adicionar inimigos especiais
- [ ] Implementar quests secundárias

### Polimento
- [ ] Sistema de save/load
- [ ] Sistema de conquistas
- [ ] Modos de dificuldade
- [ ] Sistema de estatísticas
- [ ] Criar README.md completo

---

## 🎯 Resumo Final

### Princípios da Organização:
1. **Modularidade:** Cada módulo tem uma responsabilidade clara
2. **Escalabilidade:** Fácil adicionar novos conteúdos
3. **Manutenibilidade:** Código organizado e bem nomeado
4. **Funcional:** Sem classes, apenas funções puras e dicionários

### Próximos Passos Imediatos:
1. ✅ Revisar este documento
2. 🔄 Criar estrutura de pastas
3. 🔄 Migrar módulo UI (baixa dependência)
4. 🔄 Testar após cada migração
5. 🔄 Completar funcionalidades faltantes

### Benefícios a Longo Prazo:
- Código mais limpo e profissional
- Mais fácil colaborar com outras pessoas
- Facilita debugging e correção de bugs
- Base sólida para expansões futuras
- Portfólio mais impressionante

---

**Boa sorte com a reorganização do seu projeto! 🎮✨**

*Se precisar de ajuda para implementar qualquer parte desta recomendação, é só pedir!*