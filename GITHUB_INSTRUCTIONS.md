# GitHub Upload Instructions

Since the `git` command was not detected in the current automation environment, please run the following commands manually in your terminal (Git Bash, PowerShell, or VS Code terminal) to publish the repository.

## 1. Initialize Git

```bash
cd c:/Users/DELL/OneDrive/Documentos/Antigravity/rwe-safety-cohort-synthea
git init
git branch -M main
```

## 2. Commit Files

```bash
git add .
git commit -m "Initial release: RWE Diabetes Readmission Analysis (UCI ID 296)"
```

## 3. Create & Push to GitHub

If you have the GitHub CLI (`gh`) installed/authenticated:

```bash
# Create public repo and push
gh repo create rwe-safety-cohort --public --source=. --remote=origin --push
```

OR, if using standard Git (create the repo `rwe-safety-cohort` on <https://github.com/new> first):

```bash
git remote add origin https://github.com/YOUR_USERNAME/rwe-safety-cohort.git
git push -u origin main
```

## 4. Verification

After pushing, check the repository link: <https://github.com/YOUR_USERNAME/rwe-safety-cohort>
Ensure `README.md` and `docs/results.md` are rendering correctly.
