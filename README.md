# 🤖 MIUUL Machine Learning | Makine Öğrenmesi

## 📌 Proje Hakkında

Bu proje, **MIUUL Makine Öğrenmesi Eğitim Programı** kapsamında, **Python** ve **veri bilimi** odaklı araçlar kullanılarak oluşturulmuş **makine öğrenmesi uygulamalarını** içermektedir. Temel ve ileri düzeyde **makine öğrenmesi algoritmalarının** eğitimini ve uygulamalarını içerir. 

Proje kapsamında, **veri analizi, özellik mühendisliği, model oluşturma, model değerlendirme ve optimizasyon** gibi konular ele alınmıştır.

---

## 📂 İçerik ve Konular

### 📊 **Veri Analizi ve Ön İşleme**
- Veri analizi ve görselleştirme (Pandas, Matplotlib, Seaborn)
- Eksik veriler ve aykırı değer analizi
- Kategorik ve sayısal değişkenlerin analizi
- Özellik mühendisliği (Feature Engineering)

### 🔍 **Makine Öğrenmesi Algoritmaları**
- **Supervised Learning (Denetimli Öğrenme)**
  - Regresyon (Linear, Multiple, Polynomial)
  - Sınıflandırma (Logistic Regression, KNN, SVM, Decision Trees, Random Forest)
- **Unsupervised Learning (Denetimsiz Öğrenme)**
  - Kümeleme (K-Means, Hierarchical Clustering, DBSCAN)
  - PCA (Principal Component Analysis)
- **Model Değerlendirme ve Optimizasyon**
  - Doğruluk ölçütleri (Accuracy, Precision, Recall, F1-score)
  - Hiperparametre optimizasyonu (GridSearchCV, RandomizedSearchCV)

---

## 🛠️ Kullanılan Teknolojiler

- **Python 3.8+**
- **Pandas, NumPy, Matplotlib, Seaborn**
- **Scikit-Learn**
- **XGBoost, LightGBM**
- **TensorFlow, Keras (Opsiyonel Derin Öğrenme İçin)**

---

## 📂 Proje Klasör Yapısı

```plaintext
MIuul_Machine_Learning/
├── datasets/                  # Kullanılan veri setleri
│   ├── train.csv
│   ├── test.csv
│   └── sample_data.csv
├── notebooks/                 # Jupyter Notebook dosyaları
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_selection.ipynb
│   └── 04_model_evaluation.ipynb
├── scripts/                   # Python scriptleri
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   ├── model_evaluation.py
│   └── utils.py
├── results/                   # Model sonuçları ve değerlendirme raporları
│   ├── best_model.pkl
│   └── evaluation_report.txt
├── README.md                  # Proje dökümantasyonu
└── requirements.txt           # Gerekli kütüphaneler
