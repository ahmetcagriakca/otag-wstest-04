# wst04 Remote + PR-based

PR tabanli workflow arketipi. Main'e dogrudan commit yasak, feature branch + PR acilir.

## Active Task
`math_utils.py` olustur (bkz. COMMON_TASK.md). Python ile calistir. Sonra:
- `git checkout -b feat/modulo-sum`
- `git add math_utils.py`
- `git commit -m "add modulo_sum(a, b, m)"`
- `git push origin feat/modulo-sum`
- `gh pr create --title "Add modulo_sum" --body "Common archetype task"` ile PR ac
- `gh pr merge --auto --squash` (veya manuel merge)

## Closure Protocol
- Main'e dogrudan commit YASAK
- Feature branch, push, PR ac, merge et
- PR merge olana kadar `GOREV TAMAMLANDI` yazma
- Merge sonrasi `GOREV TAMAMLANDI`

## Rules
- Kisa cevap
- Main'e direkt push yok
- PR merge olmadan task bitmedi
- `GOREV TAMAMLANDI`
