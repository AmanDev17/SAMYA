import os
import cv2
import numpy as np
from PIL import Image
import imagehash
import faiss
from pdf2image import convert_from_path

HASH_SIZE = 16
IMAGE_SIZE = 256


def preprocess_image(image):
    img = np.array(image)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img = cv2.equalizeHist(img)
    img = cv2.resize(img, (IMAGE_SIZE, IMAGE_SIZE))
    img = cv2.GaussianBlur(img, (3, 3), 0)
    return Image.fromarray(img)


def compute_phash(image):
    return imagehash.phash(image, hash_size=HASH_SIZE)


def hash_to_vector(phash):
    return np.array(phash.hash).astype(np.float32).flatten()


def text_to_image(text):
    img = np.ones((500, 500), dtype=np.uint8) * 255
    y = 20
    for line in text.split('\n')[:20]:
        cv2.putText(img, line[:50], (10, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0), 1)
        y += 20
    return Image.fromarray(img)


def extract_all_files(folder):
    data = []

    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        # PDF
        if file.lower().endswith('.pdf'):
            pages = convert_from_path(path)

            for i, page in enumerate(pages):
                processed = preprocess_image(page)
                phash = compute_phash(processed)

                data.append({
                    "label": f"{file} - Page {i+1}",
                    "type": "pdf",
                    "pdf": file,
                    "page": i + 1,
                    "hash": phash
                })

        # IMAGE
        elif file.lower().endswith(('.jpg', '.jpeg', '.png')):
            image = Image.open(path).convert('RGB')
            processed = preprocess_image(image)
            phash = compute_phash(processed)

            data.append({
                "label": file,
                "type": "image",
                "file": file,
                "hash": phash
            })

        # TEXT
        elif file.lower().endswith('.txt'):
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                text = f.read()

            image = text_to_image(text)
            processed = preprocess_image(image)
            phash = compute_phash(processed)

            data.append({
                "label": f"{file} (text)",
                "type": "text",
                "hash": phash
            })

    return data


def build_index(data):
    vectors = [hash_to_vector(item['hash']) for item in data]
    vectors = np.array(vectors).astype('float32')

    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(vectors)

    return index, vectors

def find_duplicates(data, index, vectors, threshold=50):
    distances, indices = index.search(vectors, 5)

    pairs = []

    for i in range(len(data)):
        for j in range(1, 5):
            idx = indices[i][j]
            dist = distances[i][j]

            if dist < threshold:
                pairs.append({
                    "item1": data[i],
                    "item2": data[idx],
                    "distance": float(dist)
                })

    return pairs

def process_files(folder):
    data = extract_all_files(folder)

    if len(data) < 2:
        return []

    index, vectors = build_index(data)
    pairs = find_duplicates(data, index, vectors)

    result = []

    for pair in pairs:
        result.append({
            "item1": {
                "label": pair["item1"]["label"],
                "type": pair["item1"].get("type"),
                "pdf": pair["item1"].get("pdf"),
                "page": pair["item1"].get("page"),
                "file": pair["item1"].get("file")
            },
            "item2": {
                "label": pair["item2"]["label"],
                "type": pair["item2"].get("type"),
                "pdf": pair["item2"].get("pdf"),
                "page": pair["item2"].get("page"),
                "file": pair["item2"].get("file")
            },
            "distance": pair["distance"]
        })

    return result