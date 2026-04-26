# Veri Yapıları Ödevi – Arama ve Sıralama Algoritmaları

## 📌 Proje Açıklaması
Veri yapıları kapsamında Python kullanılarak geliştirilmiş arama ve sıralama algoritmalarının (Linear Search, Binary Search, Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort) implementasyonudur.

Bu proje, algoritmaların hem mantığını anlamak hem de kod üzerinde uygulamak amacıyla hazırlanmıştır.

---

## 🔎 Arama Algoritmaları

### Linear Search
- Dizideki elemanları tek tek kontrol eder.
- Sıralı olma zorunluluğu yoktur.
- Zaman karmaşıklığı: **O(n)**

### Binary Search
- Sadece sıralı dizilerde çalışır.
- Diziyi ortadan ikiye bölerek arama yapar.
- Zaman karmaşıklığı: **O(log n)**

---

## 🔃 Sıralama Algoritmaları

### Bubble Sort
- Komşu elemanları karşılaştırarak yer değiştirir.
- Zaman karmaşıklığı: **O(n²)**

### Selection Sort
- Her adımda en küçük elemanı bulur ve başa alır.
- Zaman karmaşıklığı: **O(n²)**

### Insertion Sort
- Elemanları doğru konuma yerleştirerek sıralar.
- Zaman karmaşıklığı: **O(n²)**

### Merge Sort
- Diziyi bölerek küçük parçalara ayırır ve birleştirerek sıralar.
- Zaman karmaşıklığı: **O(n log n)**

### Quick Sort
- Pivot seçerek diziyi parçalara ayırır.
- Ortalama zaman karmaşıklığı: **O(n log n)**

---

## ⚖️ Algoritma Karşılaştırması

- En hızlı sıralama algoritmaları: Merge Sort, Quick Sort
- En yavaş sıralama algoritmaları: Bubble Sort, Selection Sort
- En verimli arama algoritması: Binary Search (sıralı veri için)

---

## ▶️ Projeyi Çalıştırma

```bash
python main.py
