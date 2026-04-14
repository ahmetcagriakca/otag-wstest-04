# Expected Behavior — wst04 (remote + pr_based)

## Workspace Config
- path: `E:\dev\otag-workspacetests\wst04_remote_prbased`
- git: local + remote (origin → github.com/ahmetcagriakca/otag-wstest-04)
- work_model: pr_based
- ci_required: true
- qoe: disabled

## Expected Audit Steps
01-10 standart. Ama closure daha uzun — PR merge bekler.

## Expected Verdict
**PASS** — PR merge olmadan GOREV TAMAMLANDI gelmezse reviewer PR merge evidence gorur.

## Optimization Candidates
- `build_task_mode_suffix` pr_based icin dogru prompt uretiyor mu?
- PR merge checker (`closure_mode=pr_merge`) doğru sinyal aliyor mu?
- Reviewer PR URL'i gorup merge status kontrol edebiliyor mu?

## Risk Alanlari
- GOREV TAMAMLANDI PR merge'den once gelir mi? (prematur sinyal)
- CI yesil olmadan merge engelleniyor mu?
