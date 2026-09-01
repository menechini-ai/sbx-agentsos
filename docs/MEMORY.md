# Memória Persistente (ai-memory)

## Visão

O ai-memory é a infraestrutura oficial de memória persistente do Agent OS. Mantém uma wiki de Markdown como fonte de verdade e utiliza SQLite como índice derivado para recuperação, busca textual e outras formas de retrieval.

## Estrutura do ai-memory

```
<data_dir>/
├── wiki/          # Markdown como fonte de verdade (versionado em Git)
├── raw/           # Dados brutos de sessões e observações
├── db/            # Índice SQLite derivado para retrieval
├── models/        # Modelos de embedding para vector search
└── logs/          # Logs de atividade e sessões
```

## Princípios

1. **Markdown como fonte de verdade**: Todo o conhecimento é armazenado em arquivos Markdown legíveis e editáveis, versionados em Git

2. **SQLite como índice derivado**: O SQLite é gerado a partir do conteúdo Markdown e serve para busca textual rápida, retrieval e relações entre páginas

3. **Não duplicar**: O Agent OS **não** deve criar sistemas paralelos de memória. O ai-memory já implementa:
   - Wiki Markdown versionado em Git
   - SQLite como índice derivado
   - Sessões, observações, handoffs
   - Decisões estruturadas
   - Retrieval por texto e relações

## Memória no Agent OS

No Agent OS, a memória é organizada em níveis conceituais:

```
MEMORY
│
├── Global
│   └── conhecimento comum
│
├── Project
│   └── conhecimento do projeto
│
├── Agent
│   └── conhecimento específico do agente
│
└── Session
    └── contexto episódico
```

## Políticas de Memória

- **Regras** (permanentes) → AGENTS.md — Não na memória episódica
- **Conhecimento** (contextual) → ai-memory — Promovido via pipeline Memory→Skill→Rule
- **Aprendizados** → memory/learnings/ → Candidates → Promoção revisada
- **Decisões** → memory/decisions/ → Registro estruturado

## Handoff entre Sessões

O ai-memory permite que agentes sejam interrompidos e outros continuem o trabalho utilizando a memória compartilhada. O handoff segue o contrato definido em `workflows/handoff/handoff-workflow.md`.

## Uso no Agent OS

Consultas de memória são feitas através de retrieval no ai-memory:

```
→ consultar ai-memory
  - para decisões arquiteturais
  - para conhecimento do projeto
  - para aprendizados anteriores
```