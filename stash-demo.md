# C13 - git stash : sauvegarde temporaire

## Qu'est-ce que git stash ?

`git stash` met de côté les modifications non commitées pour nettoyer
le working directory sans perdre le travail en cours.

## Scénario réel

Tu travailles sur une feature, un bug urgent arrive.
Tu dois changer de branche MAINTENANT mais tu ne veux pas commiter
un travail inachevé.

→ Solution : `git stash` !

## Commandes utilisées

```bash
# 1. Modification en cours (non commitée)
echo "travail en cours..." >> about.md

# 2. Mise de côté
git stash

# 3. Changement de branche propre
git checkout feature/a

# 4. Retour et récupération
git checkout main
git stash pop
```

## Commandes utiles

| Commande | Description |
|----------|-------------|
| `git stash` | Met de côté les modifications |
| `git stash list` | Liste tous les stashs |
| `git stash pop` | Récupère et supprime le dernier stash |
| `git stash apply` | Récupère sans supprimer |
| `git stash drop` | Supprime un stash |

---
*Rédigé avec l'aide de Claude (Anthropic)*