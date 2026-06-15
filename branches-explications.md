# C09 & C10 - Branches et Merge

## C09 — Créer une branche

### Commandes utilisées
```bash
git checkout -b feature/about   # crée et bascule sur la branche
git branch                       # vérifie la branche active
git push -u origin feature/about # pousse la branche sur GitHub
```

### Pourquoi utiliser des branches ?
- Isoler une fonctionnalité sans toucher au code principal
- Travailler en parallèle avec d'autres développeurs
- Expérimenter sans risque sur `main`

---

## C10 — Merger vers main

### Commandes utilisées
```bash
git checkout main          # retour sur main
git merge feature/about    # fusion de la branche
git log --oneline --graph  # vérification de l'historique
git push                   # envoi sur GitHub
```

### Fast-forward vs Merge commit

| | Fast-forward | Merge commit |
|---|---|---|
| **Quand ?** | Aucun commit sur main depuis la branche | Des commits ont divergé |
| **Historique** | Linéaire (propre) | Commit de merge créé |
| **Commande** | `git merge` (auto) | `git merge --no-ff` (forcé) |

---
*C09 et C10 réalisés avec l'aide de Claude (Anthropic)*