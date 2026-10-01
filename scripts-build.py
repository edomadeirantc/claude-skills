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
