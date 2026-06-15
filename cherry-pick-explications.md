# C15 - Cherry-pick : récupérer un commit précis

## Qu'est-ce que cherry-pick ?

`git cherry-pick <hash>` copie un commit précis d'une branche
vers une autre, sans merger toute la branche.

## Scénario utilisé

- Commit `fix: correction bug critique` créé sur `feature/a`
- Cherry-pick appliqué sur `main`
- Résultat : le commit existe sur les deux branches

## Commandes utilisées

```bash
git checkout feature/a
git commit -m "fix: correction bug critique"
git log --oneline        # récupérer le hash
git checkout main
git cherry-pick abc1234  # appliquer le commit précis
```

## Quand utiliser cherry-pick ?

| Situation | Solution |
|-----------|----------|
| Bug fix à appliquer sur plusieurs branches | cherry-pick |
| Récupérer 1 commit sans merger toute une branche | cherry-pick |
| Merger toute une feature | git merge |

---
*Rédigé avec l'aide de Claude (Anthropic)*