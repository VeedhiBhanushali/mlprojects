# 📚 Student Performance Predictor

A machine learning web application that predicts student math scores based on various parameters using multiple ML algorithms.

## 🎯 Overview

This project implements a student performance prediction system that helps estimate math scores based on various features like:
- Gender
- Race/Ethnicity
- Parental Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score

## 🏗️ Architecture

- Frontend: HTML/CSS
- Backend: Flask
- ML Models: 
  - Linear Regression
  - Ridge Regression
  - Lasso
  - K-Neighbors Regressor
  - Decision Tree
  - Random Forest
  - XGBoost
  - CatBoost
  - AdaBoost

## 🔧 Tech Stack

- Python 3.13
- Scikit-learn
- Pandas
- NumPy
- Flask
- HTML
- CatBoost
- XGBoost
- Feature-engine

## 📊 Model Performance

After evaluating multiple models, the following R2 scores were achieved:
- Ridge: 0.88
- Linear Regression: 0.87
- CatBoost: 0.85
- Random Forest: 0.85
- AdaBoost: 0.84
- XGBoost: 0.82
- Lasso: 0.82
- KNN: 0.78
- Decision Tree: 0.74

## 🚀 Setup & Installation

1. Clone the repository
git clone
https://github.com/veedhibhanushali/student-performance-predictor.git

2. Create a virtual environment
```bash
python -m venv venv
```

3. Activate virtual environment
```bash
# Windows
venv\Scripts\activate

# Unix/macOS
source venv/bin/activate
```

4. Install dependencies
```bash
pip install -r requirements.txt
```

5. Run the application
```bash
python app.py
```

## 📁 Project Structure

```
├── artifacts/          # Trained models and preprocessors
├── notebook/          # Jupyter notebooks for analysis
├── src/               # Source code
│   ├── components/    # Model components
│   ├── pipelines/     # Training and prediction pipelines
│   └── utils.py       # Utility functions
├── templates/         # HTML templates
├── app.py            # Flask application
└── requirements.txt  # Project dependencies
```

## 🎮 Usage

1. Navigate to `http://localhost:5000` in your web browser
2. Input the required student information
3. Click "Predict" to get the estimated math score

## 🔍 Features

- Interactive web interface for predictions
- Multiple ML model comparisons
- Detailed EDA in notebooks
- Modular code structure
- Error handling and logging
- Model persistence

## 📈 Future Improvements

- Add more ML models
- Implement cross-validation
- Add feature importance visualization
- Deploy on cloud platforms
- Add user authentication
- Implement batch prediction capability

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Acknowledgments

- Dataset source: [Student Performance Dataset](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
- Inspired by various ML projects and tutorials

## 📧 Contact

For any queries or suggestions, please reach out to [your-email@example.com]
