# SAMYA 🔍
### *साम्य — Seeing similarity beyond formats*

**Samya** is a high-performance cross-format duplicate detection engine. It identifies similar or duplicate content across **images, PDFs, and text files** by leveraging perceptual hashing (pHash) and FAISS-powered vector similarity search.

---

## 🖼️ Interface Preview

<img width="1600" alt="Samya Home Interface" src="https://github.com/user-attachments/assets/fa85fb56-afa8-4c7b-80c0-ee81c7faaba8" />

> **The Landing Page:** A minimalist, user-centric dashboard designed for seamless multi-format ingestion. The interface supports the simultaneous queuing of PDFs, raw images, and text files, feeding them directly into a unified cross-format processing pipeline.

---

## 🔍 Similarity Engine in Action

<img width="1600" alt="Duplicate Detection Results" src="https://github.com/user-attachments/assets/849e6487-f3d4-4698-8364-70ea62d6d9f3" />

**Technical Analysis of Results:**
* **Cross-Format Validation:** The engine successfully flags a match between a `.pdf` page and a `.jpg` export, proving the efficacy of the "unified visual representation" approach.
* **Hamming Distance (6.0):** The UI exposes the raw similarity metric. A distance of 6.0 indicates high-confidence visual correspondence, even if the files differ in resolution, compression, or encoding.
* **Vector Retrieval:** Results are fetched via **FAISS index lookups**, demonstrating sub-millisecond retrieval speeds even when comparing disparate file structures.

---

## 🚀 Overview

In real-world systems, duplicate detection is often limited to exact file matching or format-specific comparisons. This fails when:
* The same content exists in different formats (PDF vs Image)
* Documents are scanned or slightly modified
* Text content is stored in different representations

**Samya solves this by converting all inputs into a unified visual representation**, enabling intelligent, format-independent similarity detection.

---

## 🧠 Core Idea

Instead of comparing raw bytes, Samya follows a specialized computer vision pipeline:
1.  **Format Normalization:** Converts all inputs (PDF, image, text) into standardized images.
2.  **Preprocessing:** Applies grayscale conversion, normalization, and resizing.
3.  **Feature Extraction:** Generates **Perceptual Hashes (pHash)** that represent visual structure.
4.  **Vectorization:** Converts hashes into feature vectors.
5.  **Indexing:** Uses **FAISS (Facebook AI Similarity Search)** for efficient nearest-neighbor search.

---

## 🔥 Key Features

* 🖼️ **Multi-Format Support:** Detects duplicates across Images, PDFs (page-wise), and Text.
* 📝 **Text-to-Image Transformation:** Matches text based on visual layout and content.
* ⚡ **Lightning Fast:** Powered by FAISS for scalable similarity searches.
* 🧠 **Robust Matching:** pHash handles resized or compressed images where MD5/SHA would fail.
* 🚫 **Zero Redundancy:** In-memory comparison pipeline avoids wasteful file duplication.

---

## ⚙️ Tech Stack

* **Framework:** Django
* **Image Processing:** OpenCV, PIL / Pillow
* **Vector Engine:** FAISS (Facebook AI Similarity Search)
* **Math/Logic:** NumPy
* **Document Parsing:** pdf2image

---

## ❌ Why Traditional Approaches Fail

| Method | Flaw | Samya's Solution |
| :--- | :--- | :--- |
| **Exact Hashing (MD5/SHA)** | Fails if 1 pixel changes or format shifts. | Uses **Perceptual Hashing** for visual similarity. |
| **Brute-Force (O(n²))** | Extremely slow; does not scale. | Uses **FAISS** for logarithmic search speed. |
| **Text-Only Search** | Cannot "see" scanned documents or images. | **Unifies all formats** into a visual representation. |

---

## 🧩 Use Cases

* **Archive Deduplication:** Clean up digital libraries with mixed PDF/Image sources.
* **Enterprise Management:** Identify duplicate invoices or scanned identity documents.
* **ML Preprocessing:** Clean datasets by removing near-duplicate images before training.

---

## 🔮 Future Scope

* **Deep Learning:** Replace pHash with CNN-based embeddings (ResNet/CLIP) for semantic matching.
* **GPU Acceleration:** Utilize FAISS-GPU for billion-scale dataset indexing.
* **Extended Formats:** Support for `.docx`, `.pptx`, and video keyframe extraction.
* **Advanced Analytics:** Confidence heatmaps and visual similarity overlays.

---

## ⭐ Support the Project
If you found Samya useful, please give this repository a ⭐ to help it reach more developers!
