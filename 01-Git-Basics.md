# 📚 Git Basics

---

# What is Git?

Git is a distributed Version Control System (VCS) used to track changes in source code and manage project history.

---

# What is GitHub?

GitHub is a cloud platform that hosts Git repositories online.

---

# Git vs GitHub

| Git                   | GitHub              |
| --------------------- | ------------------- |
| Works locally         | Works online        |
| Tracks changes        | Stores repositories |
| Installed on computer | Website             |

---

# Important Terms

## Repository

A project that is tracked by Git.

---

## .git

A hidden folder that stores all Git history, commits, branches and configuration.

Never delete it unless you intentionally want to remove Git tracking.

---

## Branch

A separate line of development.

Default branch:
`main`

---

## Staging Area

A temporary area where selected changes are prepared before committing.

---

## Commit

A snapshot of the staged changes.

Each commit has its own unique ID.

---

# Commands

## git init

### Purpose

Creates a new Git repository.

### When to use

Once when starting a new project.

---

## git status

### Purpose

Shows the current state of the repository.

### Displays

- Current branch
- Modified files
- Staged files
- Untracked files

---

## git add

### Purpose

Moves changes from the Working Directory to the Staging Area.

Example

git add README.md

---

## git commit -m "message"

### Purpose

Creates a snapshot of the staged files.

Example

git commit -m "Initial project setup"

---

## git log --oneline

### Purpose

Shows a short summary of commit history.

---

## git branch -M main

### Purpose

Renames the current branch to `main`.

---

## git remote add origin <repository-url>

### Purpose

Connects the local repository to GitHub.

---

## git push

### Purpose

Uploads commits from the local repository to GitHub.

---

# Common Beginner Mistakes

❌ Running `git init` multiple times inside the same project.

❌ Forgetting `git add` after editing a staged file.

❌ Forgetting to commit before pushing.

❌ Force pushing without understanding its effect.

---

# Interview Questions

## What is Git?

Git is a distributed version control system used to track changes in source code and maintain project history.

---

## Why is the Staging Area useful?

It allows developers to review and select specific changes before creating a commit, resulting in clean and organized commit history.

---

## What is the difference between Git and GitHub?

Git is a version control system, while GitHub is a cloud platform for hosting Git repositories.
