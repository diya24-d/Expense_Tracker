# app.py
from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

# Create an empty list to store expenses
expenses = []

# Define expense categories
categories = ["Food", "Transportation", "Housing", "Entertainment", "Utilities", "Other"]

@app.route('/')
def index():
    return render_template('index.html', expenses=expenses, categories=categories)

@app.route('/add_expense', methods=['POST'])
def add_expense():
    date = request.form.get('date')
    description = request.form.get('description')
    category = request.form.get('category')
    amount = request.form.get('amount')
    
    if date and description and category and amount:
        expenses.append({'date': date, 'description': description, 'category': category, 'amount': amount})
    
    return redirect(url_for('index'))

@app.route('/export_csv')
def export_csv():
    with open('expenses.csv', 'w', newline='') as csvfile:
        fieldnames = ['Date', 'Description', 'Category', 'Amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for expense in expenses:
            writer.writerow({'Date': expense['date'], 'Description': expense['description'], 
                             'Category': expense['category'], 'Amount': expense['amount']})
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
