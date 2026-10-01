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

## Dados e serviços externos

O plugin não coleta, armazena nem envia dados por conta própria. Algumas skills, **somente quando você as invoca e fornece a sua própria chave de API**, chamam serviços de terceiros:

- Geração de imagem/vídeo/áudio: fal.ai, Replicate, Venice.ai, OpenAI (Images, Sora, TTS), Google Gemini/Imagen, MiniMax, ElevenLabs, MuAPI, Atlas Cloud, PixelBin
- SEO e mapas: DataForSEO, Moz, Geoapify
- Pesquisa web: Reddit, X, YouTube, TikTok, Hacker News (skill `last30days`)
- Ferramentas de desenvolvedor: GitHub, Vercel, Supabase, Figma, Sentry, Mercado Pago

Os dados enviados a esses serviços seguem as políticas de privacidade de cada um. Nenhum dado é retido pelo autor deste plugin.

## Licenças

Cada skill em `skills/` mantém sua licença original (veja o arquivo LICENSE dentro da pasta de cada uma). Veja também `LICENSE` na raiz.
