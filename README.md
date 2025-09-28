# 📂 Big Data CSV Import to MySQL  

This project was created to **complete a college task** on handling **big data** by importing a large CSV file into a **MySQL database** using Python. 🚀  

---

## 📌 Project Overview  
- **Goal**: Import a large CSV dataset into MySQL.  
- **Dataset Used**: [Sign Language MNIST](https://www.kaggle.com/datamunge/sign-language-mnist) (hand gesture images in CSV format).  
- **Tools & Libraries**:  
  - Python 🐍  
  - Pandas 📊  
  - SQLAlchemy ⚡  
  - PyMySQL 🗄️  
  - MySQL (via Laragon)  

---

## ⚙️ How It Works  
1. **Load CSV file** using Pandas.  
2. **Process & clean data** (e.g., encoding issues with UTF-8).  
3. **Connect to MySQL** using SQLAlchemy + PyMySQL.  
4. **Import into database table** (`sign_mnist_train`) with `df.to_sql()`.  

---

## 📜 Installation  

Clone the repo:  
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
