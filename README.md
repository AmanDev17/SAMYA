# SAMYA
# 🔍 Samya

### *साम्य — Seeing similarity beyond formats*

**Samya** is a cross-format duplicate detection web application that identifies similar or duplicate content across **images, PDFs, and text files** using perceptual hashing (pHash) and FAISS-powered similarity search.

---

## 🚀 Overview

In real-world systems, duplicate detection is often limited to exact file matching or format-specific comparisons. This fails when:

* The same content exists in different formats (PDF vs image)
* Documents are scanned or slightly modified
* Text content is stored in different representations

**Samya solves this by converting all inputs into a unified visual representation**, enabling intelligent, format-independent similarity detection.

---

## 🧠 Core Idea

Instead of comparing files directly, Samya:

1. Converts all inputs (PDF, image, text) into images
2. Applies preprocessing (grayscale, normalization, resizing)
3. Generates perceptual hashes (pHash)
4. Converts hashes into vectors
5. Uses FAISS for efficient similarity search

This creates a **scalable and format-agnostic similarity engine**.

---

## 🔥 Key Features

* 🖼️ Image duplicate detection
* 📄 PDF duplicate detection (page-wise)
* 📝 Text similarity via text-to-image transformation
* 🔄 Cross-format matching (Image ↔ PDF ↔ Text)
* ⚡ Fast similarity search using FAISS
* 🧠 Perceptual hashing for robust matching
* 🚫 No redundant file duplication
* ⚡ In-memory comparison pipeline

---

## ⚙️ Tech Stack

* Django (Web Framework)
* OpenCV (Image Processing)
* PIL / Pillow
* NumPy
* FAISS (Similarity Search)
* pdf2image

---

## ❌ Traditional Approaches (and why they fall short)

### 1. Exact File Matching (Hash-based: MD5, SHA)

* Only detects identical files
* Fails for resized, compressed, or scanned content
* Cannot handle cross-format data

👉 Not suitable for real-world duplicate detection

---

### 2. Brute-Force Image Comparison

* Compares every image with every other image (O(n²))
* Extremely slow for large datasets
* Memory and compute intensive

👉 Not scalable

---

### 3. Storing Multiple Copies for Comparison

* Requires duplicating files in different formats
* High storage overhead
* Inefficient pipeline design

👉 Wasteful and unnecessary

---

### 4. Text-Based Comparison Only

* Works only for pure text
* Fails for scanned documents and images
* Cannot capture visual similarity

👉 Not robust

---

## ✅ Why Samya is Better

* Uses **perceptual similarity instead of exact matching**
* Handles **multiple formats seamlessly**
* Uses **FAISS for scalable nearest-neighbor search**
* Avoids redundant storage and computation
* Works efficiently with large datasets

---

## 🧩 Use Cases

* 📚 Digital archive deduplication
* 🏢 Enterprise document management
* 🧾 Invoice and scanned document matching
* 🖼️ Media dataset cleaning
* 🤖 Preprocessing data for ML pipelines

---

## 🧪 Example

**Input:**

* `image1.jpg`
* `document.pdf`
* `notes.txt`

**Output:**

```
Match Found:
image1.jpg ↔ document.pdf (Page 2)
Similarity Distance: 41.7
```

---

## 🔮 Future Scope

Samya can be extended significantly:

### 🚀 1. Deep Learning Embeddings

* Replace pHash with CNN-based embeddings
* Improve semantic similarity detection

---

### 🌐 2. REST API Layer

* Expose endpoints for integration with other systems
* Enable SaaS-style deployment

---

### 🎨 3. Advanced UI

* Drag-and-drop uploads
* Visual similarity heatmaps
* Confidence score visualization

---

### ⚡ 4. GPU Acceleration

* Use FAISS GPU version for large-scale datasets

---

### ☁️ 5. Cloud Storage Integration

* AWS S3 / Google Cloud Storage for file handling
* Scalable production deployment

---

### 📄 6. Support for More Formats

* DOCX, PPTX
* Video frame extraction for similarity detection

---

### 🧠 7. Semantic Text Understanding

* Integrate NLP models for deeper text similarity
* Combine visual + semantic matching

---

## 🏆 Conclusion

Samya is not just a duplicate detector—it is a **unified content similarity engine** capable of identifying relationships across different data formats efficiently and intelligently.

---

## ⭐ If you found this useful

Give this repo a ⭐ and help it reach more people!
