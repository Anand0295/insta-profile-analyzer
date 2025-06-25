# Contributing to Instagram Profile Analyzer

Thank you for your interest in contributing to the Instagram Profile Analyzer! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Bugs

1. **Check existing issues** first to avoid duplicates
2. **Use the bug report template** when creating new issues
3. **Provide detailed information**:
   - Python version
   - Operating system
   - Error messages (full traceback)
   - Steps to reproduce
   - Expected vs actual behavior

### Suggesting Features

1. **Check the roadmap** in README.md
2. **Open a feature request** with:
   - Clear description of the feature
   - Use cases and benefits
   - Possible implementation approach
   - Any relevant examples or mockups

### Code Contributions

#### Getting Started

1. **Fork the repository**
   ```bash
   git clone https://github.com/Anand0295/insta-profile-analyzer.git
   cd insta-profile-analyzer
   ```

2. **Set up development environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

#### Development Guidelines

**Code Style:**
- Follow PEP 8 Python style guide
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and small
- Use type hints where appropriate

**Example:**
```python
def get_profile_info(self, username: str) -> Optional[Profile]:
    """
    Get profile information for a given username.
    
    Args:
        username (str): Instagram username without @ symbol
        
    Returns:
        Optional[Profile]: Profile object or None if error occurs
    """
```

**Testing:**
- Test your changes thoroughly
- Include both positive and negative test cases
- Test on different operating systems if possible
- Verify error handling works correctly

**Documentation:**
- Update README.md if adding new features
- Add inline comments for complex logic
- Update docstrings for modified functions

#### Commit Guidelines

**Commit Message Format:**
```
type(scope): brief description

Detailed explanation if needed

- List any breaking changes
- Reference issues: Fixes #123
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples:**
```bash
git commit -m "feat(analysis): add engagement rate calculation"
git commit -m "fix(images): resolve profile picture opening on Linux"
git commit -m "docs(readme): update installation instructions"
```

#### Pull Request Process

1. **Update documentation** as needed
2. **Test your changes** thoroughly
3. **Create pull request** with:
   - Clear title and description
   - Reference related issues
   - List of changes made
   - Screenshots if UI changes

4. **Respond to feedback** promptly
5. **Keep PR focused** - one feature/fix per PR

## 🏗️ Development Setup

### Prerequisites
- Python 3.7+
- Git
- Text editor or IDE

### Local Development
```bash
# Clone and setup
git clone https://github.com/Anand0295/insta-profile-analyzer.git
cd insta-profile-analyzer
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run the application
python instagram_profile_info.py

# Test with different profiles
# (Use public profiles for testing)
```

### Project Structure
```
insta-profile-analyzer/
├── instagram_profile_info.py    # Main application
├── requirements.txt             # Dependencies
├── README.md                   # Main documentation
├── CONTRIBUTING.md             # This file
├── LICENSE                     # MIT License
├── .gitignore                  # Git ignore rules
└── screenshots/                # Application screenshots
```

## 🎯 Areas for Contribution

### High Priority
- [ ] **Error handling improvements**
- [ ] **Cross-platform compatibility fixes**
- [ ] **Performance optimizations**
- [ ] **Better user experience**

### Medium Priority
- [ ] **GUI interface (Tkinter/PyQt)**
- [ ] **Data export features (CSV/JSON)**
- [ ] **Batch profile analysis**
- [ ] **Configuration file support**

### Low Priority
- [ ] **Data visualization**
- [ ] **Web interface**
- [ ] **Database integration**
- [ ] **API development**

## 📋 Code Review Checklist

Before submitting your PR, ensure:

- [ ] Code follows PEP 8 style guidelines
- [ ] All functions have proper docstrings
- [ ] Error handling is implemented
- [ ] Code is tested on your system
- [ ] Documentation is updated
- [ ] Commit messages are clear
- [ ] No sensitive data is included
- [ ] .gitignore is respected

## 🚫 What Not to Contribute

- **Malicious code** or security vulnerabilities
- **Copyright violations** or plagiarized code
- **Features that violate** Instagram's Terms of Service
- **Spam or low-quality** contributions
- **Large binary files** without justification

## 📞 Getting Help

If you need help with contributing:

1. **Check existing documentation** first
2. **Search closed issues** for similar questions
3. **Open a discussion** for general questions
4. **Contact maintainers** for specific guidance

## 🏆 Recognition

Contributors will be:
- **Listed in README.md** acknowledgments
- **Credited in release notes** for significant contributions
- **Given collaborator access** for consistent contributors

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to Instagram Profile Analyzer! 🎉