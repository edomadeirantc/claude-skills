import os, shutil, json
H = os.path.expanduser('~')
DST = os.path.join(H, 'claude-skills')
SRC = ['.omp/agent/skills', '.cursor/skills', '.claude/skills', '.agents/skills', '.codex/skills']
EX = shutil.ignore_patterns('node_modules', '.git', '__pycache__', '.venv', 'venv', '.pytest_cache',
                            '.env', '.env.local', '*.pyc', '.DS_Store')

cands = {}
for r in SRC:
    base = os.path.join(H, r)
    for root, dirs, files in os.walk(base, followlinks=True):
        dirs[:] = [d for d in dirs if d not in ('node_modules', '.git', '.venv', 'venv')]
        if 'SKILL.md' in files:
            cands.setdefault(os.path.basename(root), []).append(root)
            dirs[:] = []  # don't descend into a skill
pick = {n: max(ds, key=lambda d: os.path.getmtime(os.path.join(d, 'SKILL.md'))) for n, ds in cands.items()}
for n in ('docx', 'pdf', 'pptx', 'xlsx'): pick.pop(n, None)  # licença proprietária Anthropic

out = os.path.join(DST, 'skills')
shutil.rmtree(out, ignore_errors=True)
os.makedirs(out)
for n, d in sorted(pick.items()):
    shutil.copytree(d, os.path.join(out, n), ignore=EX, symlinks=False, dirs_exist_ok=True)
print(len(pick), 'skills copied')

# Directory limit: 50 MiB zipped. Drop big decorative media only referenced by READMEs.
MEDIA = ('.gif', '.png', '.jpg', '.jpeg', '.webp', '.mp3', '.mp4', '.mov', '.wav')
dropped = 0
for n in os.listdir(out):
    sd = os.path.join(out, n)
    text = ''
    for r, _, fs in os.walk(sd):
        for f in fs:
            if f.lower().endswith(('.md', '.py', '.js', '.mjs', '.ts', '.json', '.html', '.sh', '.yaml', '.yml', '.txt')) \
                    and not f.lower().startswith('readme'):
                p = os.path.join(r, f)
                if os.path.getsize(p) < 5e6:
                    text += open(p, encoding='utf-8', errors='ignore').read()
    for r, _, fs in os.walk(sd):
        for f in fs:
            p = os.path.join(r, f)
            if f.lower().endswith(MEDIA) and os.path.getsize(p) > 200_000 and f not in text:
                dropped += os.path.getsize(p); os.remove(p)
print(f'dropped {dropped/1e6:.1f} MB of unreferenced media')
