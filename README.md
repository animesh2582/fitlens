# 🎯 FitLens - Job Role Fit Analyzer

A Streamlit web application that analyzes how well a candidate's skills and experience match job requirements for Data Engineer positions.

## 🌐 Live Demo
**Try the app now:** [https://fitlens.streamlit.app](https://fitlens.streamlit.app) *(Replace with your actual URL)*

## 🎯 How to Use

1. **Read the Job Description**: Review the Data Engineer role requirements
2. **Enter Your Experience**: Input your years of experience
3. **Paste Your Skills**: Add your resume or skill summary in the text area
4. **Check Fit**: Click the "Check Fit" button to see if you match the role

## 🔍 What It Analyzes

The app checks for these key skills:
- Python programming
- AWS cloud services
- Glue (data integration)
- Terraform (infrastructure)
- ETL workflows

**Requirements for a good fit:**
- Minimum 2 years of experience
- At least 2 matching skills from the list above

## 💻 Local Development

To run this app locally:

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/fitlens.git
   cd fitlens
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run app2.py
   ```
   Or alternatively:
   ```bash
   py -m streamlit run app2.py
   ```

## 🛠️ Technical Details

- **Framework**: Streamlit
- **Language**: Python
- **Dependencies**: Listed in `requirements.txt`
- **Deployment**: Streamlit Cloud

## 📁 Project Structure

```
fitlens/
├── app2.py             # Main application file
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🚀 Features

- ✅ **Instant Analysis**: Real-time skill matching
- ✅ **Experience Validation**: Checks minimum years required
- ✅ **User-Friendly**: Simple, clean interface
- ✅ **Mobile Responsive**: Works on all devices
- ✅ **No Registration**: Use immediately without signup

## 🐛 Troubleshooting

### Running Locally
- Make sure Python 3.7+ is installed
- Install dependencies: `pip install -r requirements.txt`
- Try: `py -m streamlit run app2.py` if `streamlit` command fails

### Web App Issues
- The live app should work on any modern browser
- Try refreshing if the page doesn't load
- Contact support if persistent issues occur

## 🚀 Deployment

This app is deployed on Streamlit Cloud and automatically updates when changes are pushed to this repository.

## 📞 Support

For issues or questions about this application, please create an issue in this repository.

## 📝 License

This project is for educational/demonstration purposes.
