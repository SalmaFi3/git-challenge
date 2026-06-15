# C17 - Créer un repo GitHub + push

## Étapes réalisées

### 1. Création du repo sur GitHub
- Repo privé créé : `git-challenge`
- Collaborateur ajouté : `m.chibani@mundiapolis.ma`
- Aucun fichier initialisé depuis GitHub (pour éviter les conflits)

### 2. Liaison du repo local avec GitHub

```bash
git remote add origin https://github.com/SalmaFi3/git-challenge.git
git branch -M main
git push -u origin main
```

### 3. Vérification

```bash
git remote -v
# origin  https://github.com/SalmaFi3/git-challenge.git (fetch)
# origin  https://github.com/SalmaFi3/git-challenge.git (push)
```

## Commandes clés

| Commande | Description |
|----------|-------------|
| `git remote add origin <url>` | Lie le repo local au repo distant |
| `git push -u origin main` | Push + définit le tracking |
| `git remote -v` | Vérifie les remotes configurés |

---
*Rédigé avec l'aide de Claude (Anthropic)*