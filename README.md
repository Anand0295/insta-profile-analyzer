# 📱 Instagram Profile Analyzer

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Instaloader](https://img.shields.io/badge/Powered%20by-Instaloader-orange.svg)](https://instaloader.github.io/)

A powerful yet beginner-friendly Python application that automatically fetches and analyzes Instagram profile information. Built with the reliable `instaloader` library, this tool provides comprehensive profile insights with just a username input.

## ✨ Features

- 🔍 **Automatic Profile Analysis** - No manual choices, everything runs automatically
- 👤 **Comprehensive Profile Info** - Username, full name, bio, follower statistics
- 📊 **Account Insights** - Verification status, account type, engagement ratios
- 📸 **Instant Profile Picture** - Downloads and opens profile pictures automatically
- 📋 **Recent Posts Analysis** - Analyzes latest 5 posts with likes, comments, and captions
- 🌐 **Cross-Platform** - Works on Windows, macOS, and Linux
- 🚀 **Beginner Friendly** - Clean code with extensive documentation

## 🖼️ Screenshots

### Main Interface
![Main Interface](screenshots/main_interface.png)
*Clean and intuitive command-line interface*

### Profile Analysis
![Profile Analysis](screenshots/profile_analysis.png)
*Comprehensive profile information display*

### Automatic Features
![Auto Features](screenshots/auto_features.png)
*Profile picture opens automatically with detailed post analysis*

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- Internet connection

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Anand0295/insta-profile-analyzer.git
   cd insta-profile-analyzer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python instagram_profile_info.py
   ```

## 📖 Usage

1. **Launch the program**
   ```bash
   python instagram_profile_info.py
   ```

2. **Enter Instagram username** (without @ symbol)
   ```
   Enter Instagram username (or 'quit' to exit): cristiano
   ```

3. **Automatic Analysis** - The program will:
   - Fetch complete profile information
   - Display comprehensive statistics
   - Download and open profile picture
   - Analyze recent posts automatically

4. **Continue or Exit**
   - Analyze another profile or quit the program

## 📊 What You Get

### Profile Information
- ✅ Username and Full Name
- ✅ User ID and Account Status
- ✅ Verification Badge Status
- ✅ Privacy Settings (Public/Private)
- ✅ Account Type (Personal/Business/Creator)
- ✅ Bio and External Links
- ✅ Business Category (if applicable)

### Statistics & Analytics
- 📈 Follower Count
- 📈 Following Count  
- 📈 Total Posts
- 📊 Following/Followers Ratio
- 📊 Engagement Insights

### Recent Posts Analysis
- 📅 Post Dates
- ❤️ Like Counts
- 💬 Comment Counts
- 📝 Caption Previews
- 🎥 Media Type (Photo/Video)
- 🔗 Direct Post Links

## 🛠️ Technical Details

### Built With
- **Python 3.7+** - Core programming language
- **Instaloader** - Instagram data extraction library
- **Cross-platform libraries** - For automatic image opening

### Architecture
```
insta-profile-analyzer/
├── instagram_profile_info.py    # Main application
├── requirements.txt             # Dependencies
├── README.md                   # Documentation
├── screenshots/                # Application screenshots
└── LICENSE                     # MIT License
```

### Key Components
- `InstagramProfileFetcher` - Main class handling all operations
- `get_profile_info()` - Profile data extraction
- `display_profile_info()` - Information formatting and display
- `save_and_open_profile_picture()` - Image handling
- `get_recent_posts_info()` - Post analysis

## 🔧 Configuration

The application works out-of-the-box with sensible defaults:
- **Recent Posts**: Analyzes 5 most recent posts
- **Profile Pictures**: Downloads to username-specific folders
- **Auto-open**: Uses system default image viewer

## 📝 Example Output

```
==================================================
📱 INSTAGRAM PROFILE INFO
==================================================
👤 Username: @cristiano
📝 Full Name: Cristiano Ronaldo
🆔 User ID: 173560420
📊 Status: ✅ Verified | 🌐 Public

📈 STATISTICS:
   👥 Followers: 615,000,000
   ➡️  Following: 560
   📸 Posts: 3,400
   📊 Following/Followers Ratio: 0.001

📝 Bio:
   SIUUUbscribe on YouTube

🔗 Website: https://www.youtube.com/c/cristiano

🚀 Auto-analyzing profile (downloading picture + analyzing posts)...
📸 Downloading and opening profile picture for @cristiano...
✅ Profile picture saved and opened!

📋 RECENT POSTS (5 posts):
1. Posted: 2024-01-15 14:30:22
   ❤️  Likes: 2,500,000 | 💬 Comments: 45,000
   📷 Photo Post
   📝 Caption: Training hard for the next match! 💪
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Development Setup
```bash
# Clone your fork
git clone https://github.com/Anand0295/insta-profile-analyzer.git

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
python -m pytest tests/
```

## 📋 Roadmap

- [ ] **GUI Interface** - Tkinter/PyQt desktop application
- [ ] **Data Export** - CSV/JSON export functionality
- [ ] **Batch Analysis** - Multiple profiles at once
- [ ] **Data Visualization** - Charts and graphs
- [ ] **Historical Tracking** - Track profile changes over time
- [ ] **Web Interface** - Flask/Django web application

## ⚠️ Important Notes

- **Public Profiles Only**: Works best with public Instagram profiles
- **Rate Limiting**: Instagram may limit requests if too many are made quickly
- **Ethical Use**: Only analyze profiles you have permission to view
- **Educational Purpose**: This tool is for learning and research purposes
- **Terms of Service**: Please respect Instagram's Terms of Service

## 🐛 Troubleshooting

### Common Issues

**"Profile does not exist" error:**
- Verify the username spelling
- Ensure the profile exists and is accessible

**"Private profile" error:**
- The profile is private and you don't follow them
- Try with a public profile instead

**Profile picture won't open:**
- Check if your system has a default image viewer
- The image is still downloaded to the username folder

**Installation issues:**
- Ensure Python 3.7+ is installed
- Try `pip3` instead of `pip`
- Use virtual environment to avoid conflicts

### Getting Help

If you encounter issues:
1. Check the [Issues](https://github.com/Anand0295/insta-profile-analyzer/issues) page
2. Create a new issue with detailed description
3. Include error messages and system information

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **[Instaloader](https://instaloader.github.io/)** - Excellent Instagram data extraction library
- **Python Community** - For amazing libraries and documentation
- **Contributors** - Everyone who helps improve this project


⭐ **Star this repository if you found it helpful!** ⭐

Made with ❤️ by Anand
