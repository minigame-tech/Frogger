# 🤝 Contributing to Frogger

Thank you for your interest in contributing to this project! Every contribution — whether it's a bug report, a feature request, or a pull request — is greatly appreciated.

## 📋 Table of Contents

- [Getting Started](#-getting-started)
- [How to Contribute](#-how-to-contribute)
- [Development Setup](#-development-setup)
- [Code Style](#-code-style)
- [Commit Messages](#-commit-messages)
- [Pull Requests](#-pull-requests)
- [Reporting Bugs](#-reporting-bugs)
- [Suggesting Features](#-suggesting-features)

## 🚀 Getting Started

1. **Fork** the repository on GitHub.
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/<your-username>/Frogger.git
   cd Frogger
   ```
3. **Create a branch** for your changes:
   ```bash
   git checkout -b feature/my-new-feature
   ```

## 💡 How to Contribute

- 🐛 **Fix a bug** — Check the [Issues](https://github.com/SalvoCodes-developer/Frogger/issues) page for open bugs.
- ✨ **Add a feature** — Look at the roadmap in the [README](README.md) for planned features.
- 📝 **Improve documentation** — Typos, clarifications, and new examples are always welcome.
- 🎨 **Improve assets** — Better sprites, sounds, or UI enhancements.

## 🛠️ Development Setup

Make sure you have **Python 3.8+** installed, then:

```bash
pip install pygame
python main.py
```

The project uses:
- **Pygame** — for audio management.
- **g2d** — a lightweight graphics module (included in `lib/`).

## 📐 Code Style

- Follow **PEP 8** conventions.
- Use meaningful variable and function names.
- Add comments to explain non-obvious logic.
- Keep functions short and focused on a single responsibility.

## 💬 Commit Messages

Use clear and descriptive commit messages. A good format:

```
<type>: <short description>

<optional longer description>
```

**Types:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

**Examples:**
```
feat: add splash screen animation on startup
fix: correct frog collision detection on logs
docs: update README with new installation steps
```

## 🔀 Pull Requests

1. Make sure your branch is **up to date** with `main`.
2. Test your changes locally before submitting.
3. Open a Pull Request with:
   - A clear **title** and **description** of what you changed.
   - References to any related issues (e.g., `Closes #12`).
4. Be responsive to feedback during code review.

> **Note:** Pull requests that do not follow the project guidelines may be asked for revisions before merging.

## 🐛 Reporting Bugs

Open an [Issue](https://github.com/SalvoCodes-developer/Frogger/issues/new) and include:

- **Description** of the bug.
- **Steps to reproduce** the issue.
- **Expected** vs. **actual** behavior.
- Your **OS** and **Python version**.
- Screenshots or logs, if applicable.

## 💡 Suggesting Features

Feature requests are welcome! Open an [Issue](https://github.com/SalvoCodes-developer/Frogger/issues/new) and describe:

- The feature you'd like to see.
- Why it would be useful.
- Any ideas on how it could be implemented.

---

Thank you for helping make Frogger better! 🐸
