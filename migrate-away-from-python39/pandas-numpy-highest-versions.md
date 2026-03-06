[[_TOC_]]
**Here’s the definitive, up‑to‑date compatibility matrix showing the *maximum* versions of pandas and NumPy you can use with Python 3.9, 3.11, 3.12, and 3.13.**  
This is based on each library’s *latest releases that still support each Python version*, following their official Python‑support policies (NEP 29 / SPEC 0).

---

# 📦 Maximum Supported Versions of pandas & NumPy

| **Python Version** | **Max pandas Version** | **Max NumPy Version** |
|--------------------|------------------------|------------------------|
| **3.9**            | **pandas 2.2.x**       | **NumPy 1.26.x**       |
| **3.11**           | **pandas 2.2.x**       | **NumPy 2.0.x**        |
| **3.12**           | **pandas 2.2.x**       | **NumPy 2.0.x**        |
| **3.13**           | **pandas 2.2.x**       | **NumPy 2.1.x**        |

---

# 🧠 How These Maximums Are Determined

### 🐼 **pandas**
- pandas 2.2 (released 2024–2025) supports **Python 3.9 → 3.13**.  
- pandas 3.0 (2026) **drops Python ≤3.10**, so Python 3.11+ can use pandas 3.x, but **Python 3.9 cannot**.  
- Therefore:
  - **Python 3.9 max = pandas 2.2.x**  
  - **Python 3.11–3.13 max = pandas 3.x**, but since pandas 3.0 is still stabilizing, the safe max is **2.2.x** unless you explicitly want pandas 3.0+.

### 🔢 **NumPy**
- NumPy 1.26 is the last branch supporting **Python 3.9**.  
- NumPy 2.0 supports **Python 3.11 and 3.12**.  
- NumPy 2.1 adds support for **Python 3.13**.  
- Therefore:
  - **Python 3.9 max = NumPy 1.26.x**  
  - **Python 3.11–3.12 max = NumPy 2.0.x**  
  - **Python 3.13 max = NumPy 2.1.x**

---

# ✅ Quick Recommendations

If you want the **newest versions allowed** for each Python version:

- **Python 3.9:**  
  - `pandas==2.2.*`  
  - `numpy==1.26.*`

- **Python 3.11 / 3.12:**  
  - `pandas==2.2.*` (or 3.x if desired)  
  - `numpy==2.0.*`

- **Python 3.13:**  
  - `pandas==2.2.*` (or 3.x)  
  - `numpy==2.1.*`

---

If you want, I can also generate a **requirements.txt** or **conda environment** for any of these Python versions.