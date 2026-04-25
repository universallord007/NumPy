# Linear Regression from Scratch (NumPy)

This project implements Linear Regression from scratch using only NumPy, without any machine learning libraries.

## 📌 Objective

To understand how a machine learning model learns from data by manually implementing:

* Prediction
* Loss calculation
* Gradient computation
* Gradient Descent optimization

---

## 🧠 Concept

We assume a linear model:

y = mx + b

The goal is to learn the best values of `m` (slope) and `b` (intercept) from data.

---

## ⚙️ Implementation Steps

1. Initialize parameters `m` and `b`
2. Predict values using:

   ```
   y_pred = m*x + b
   ```
3. Compute error:

   ```
   error = y_pred - y
   ```
4. Calculate loss (Mean Squared Error):

   ```
   loss = mean(error^2)
   ```
5. Compute gradients:

   ```
   dm = (2/n) * sum(error * x)
   db = (2/n) * sum(error)
   ```
6. Update parameters:

   ```
   m = m - lr * dm
   b = b - lr * db
   ```
7. Repeat for multiple epochs

---

## 📊 Visualization

* Blue dots → actual data
* Red line → model prediction

---

## 🚀 Result

The model successfully learns:

```
m ≈ 2
b ≈ 1
```

which matches the true relationship:

```
y = 2x + 1
```

---

## 🛠️ Technologies Used

* Python
* NumPy
* Matplotlib

---

## 📂 How to Run

```bash
python regression.py
```

---
