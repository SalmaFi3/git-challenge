# C07 - Undo sans paniquer : restore vs reset

## git restore — Annuler des modifications non commitées

`git restore <fichier>` annule les modifications d'un fichier dans le
working directory et le remet à l'état du dernier commit.

### Quand l'utiliser ?
- Tu as modifié un fichier par erreur
- Tu veux repartir de la dernière version commitée
- Les modifications ne sont PAS encore stagées

### Exemple utilisé dans ce challenge
```bash
# Modification accidentelle
echo "modification accidentelle" >> README.md

# Vérification
git status   # README.md apparaît en rouge (modified)
git diff     # montre les lignes ajoutées

# Annulation propre
git restore README.md

# Vérification
git status   # nothing to commit ✅
```

### ⚠️ Attention
`git restore` est **irréversible** — la modification est perdue définitivement.

---

## git reset — Annuler des commits

`git reset` agit sur l'**historique des commits**, pas sur les fichiers.

### Les 3 modes

| Mode | Commande | Effet |
|------|----------|-------|
| Soft | `git reset --soft HEAD~1` | Annule le commit, garde les fichiers stagés |
| Mixed | `git reset HEAD~1` | Annule le commit, déstage les fichiers |
| Hard | `git reset --hard HEAD~1` | Annule le commit ET supprime les modifications |

### Quand l'utiliser ?
- Tu veux annuler un ou plusieurs commits
- Tu veux réorganiser ton historique avant un push

---

## Résumé : restore vs reset

| | `git restore` | `git reset` |
|---|---|---|
| **Agit sur** | Fichiers (working dir) | Commits (historique) |
| **Annule** | Modifications locales | Commits entiers |
| **Dangereux ?** | Oui (irréversible sur fichiers) | Oui (`--hard` supprime tout) |
| **Casse l'historique ?** | ❌ Non | ⚠️ Oui si `--hard` |

---

*Rédigé avec l'aide de Claude (Anthropic) — compris et appliqué personnellement.*