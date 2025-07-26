# Sales Market Analysis Project

A comprehensive market analysis project that demonstrates how to analyze sales data using SQL, Python, pandas, and matplotlib. This project provides a complete workflow from data loading to visualization and insights.

## 🚀 Features

- **Data Management**: CSV to SQLite database conversion
- **SQL Integration**: Direct SQL queries for data analysis
- **Data Visualization**: Interactive charts and graphs using matplotlib
- **Jupyter Notebooks**: Interactive analysis environment
- **Conda Environment**: Isolated Python environment with all dependencies

## 📁 Project Structure

```
market-analysis/
├── data/
│   ├── sales_data.csv          # Sample sales data
│   └── sales.db               # SQLite database
├── notebooks/
│   └── sales_analysis.ipynb   # Jupyter notebook for analysis
├── scripts/
│   └── load_sales_to_sql.py   # Script to load CSV data into SQLite
└── README.md
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.11+
- Conda (recommended) or pip

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd market-analysis
```

### 2. Create and Activate Conda Environment
```bash
conda create -n market_analysis python=3.11
conda activate market_analysis
```

### 3. Install Dependencies
```bash
pip install pandas sqlalchemy matplotlib jupyter
```

## 📊 Usage

### 1. Load Sample Data
```bash
python scripts/load_sales_to_sql.py
```

### 2. Start Jupyter Notebook
```bash
jupyter notebook
```

### 3. Open Analysis Notebook
- Navigate to `notebooks/sales_analysis.ipynb`
- Run cells to see the analysis

## 📈 Sample Analysis

The project includes analysis of:
- **Total sales by product**
- **Sales distribution by region**
- **Monthly sales trends**
- **Customer analysis**

## 🗄️ Database Schema

The SQLite database contains a `sales` table with the following columns:
- `OrderID`: Unique order identifier
- `Date`: Order date
- `Product`: Product name
- `Category`: Product category
- `Quantity`: Number of units sold
- `Price`: Unit price
- `Total`: Total order value
- `Customer`: Customer name
- `Region`: Sales region

## 🔍 Sample SQL Queries

```sql
-- Total sales by product
SELECT Product, SUM(Total) as TotalSales 
FROM sales 
GROUP BY Product 
ORDER BY TotalSales DESC;

-- Sales by region
SELECT Region, SUM(Total) as RegionalSales 
FROM sales 
GROUP BY Region;

-- Monthly sales trend
SELECT strftime('%Y-%m', Date) as Month, SUM(Total) as MonthlySales 
FROM sales 
GROUP BY Month 
ORDER BY Month;
```

## 📊 Visualizations

The project generates various visualizations:
- Bar charts for product performance
- Pie charts for regional distribution
- Line charts for temporal trends

## 🛠️ Customization

### Adding Your Own Data
1. Replace `data/sales_data.csv` with your sales data
2. Ensure your CSV has the same column structure
3. Run the loading script again

### Extending Analysis
- Add new cells to the Jupyter notebook
- Create additional Python scripts in the `scripts/` folder
- Import additional libraries as needed

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with pandas, SQLAlchemy, matplotlib, and Jupyter
- Sample data structure inspired by real-world sales analysis scenarios

## 📞 Support

If you have any questions or need help with the project, please open an issue on GitHub.

---

**Happy Analyzing! 📊✨**
