# Documentação do Agent OS

Esta pasta contém a documentação oficial do sistema Agent OS.

## Arquivos

- `ARCHITECTURE.md` - Visão geral da arquitetura do sistema
- `AGENTS.md` - Contrato global dos agentes (identidade, regras, memória, handoff)
- `SKILLS.md` - Catálogo de skills disponíveis (globais e específicas)
- `MEMORY.md` - Documentação do memory/knowledge (fonte de verdade, políticas de retenção)
- `CONTRACTS.md` - Formatos dos envelopes INPUT/OUTPUT e schemas
- `GOVERNANCE.md` (localizada na raiz) - Camada formal de governança (L0-L5, matriz de autorização, políticas)

## Como usar

Comece lendo `ARCHITECTURE.md` para entender a visão geral, depois consulte os documentos específicos conforme necessário.

Para desenvolvedores: veja `SKILLS.md` e os templates em `agentsos/templates/`.
Para arquitetos: veja `ARCHITECTURE.md` e `GOVERNANCE.md`.
Para contribuidores: veja `CONTRIBUTING.md` (se existir) ou os diretórios `proposals/` e `memory/policies/`.