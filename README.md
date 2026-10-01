# claude-skills

438 skills pessoais empacotadas como plugin do Claude Code (`all-skills`) no marketplace `edo-skills`.

## Local (CLI)

```
claude plugin marketplace add edomadeirantc/claude-skills
claude plugin install all-skills@edo-skills
```

## Claude Code na nuvem (claude.ai/code)

Copie `.claude/settings.json` deste repo para o `.claude/settings.json` de cada projeto que você abrir na nuvem.
A sessão registra o marketplace e ativa o plugin sozinha. As skills aparecem como `all-skills:<nome>`.

## Atualizar

Rode `python ~/claude-skills-build.py`, faça commit e push. Na CLI: `claude plugin marketplace update edo-skills`.
