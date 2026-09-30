from sentence_transformers import SentenceTransformer
import chromadb
model = SentenceTransformer("all-MiniLM-L6-v2")
file_name = "sample.txt"
with open(file_name,"r") as file:
    text = file.read()

#Chunking
chunks = []
chunk_size = 100
chunk_overlap = 20
step = chunk_size - chunk_overlap # 100-20 = 80
for i in range(0,len(text),step):
    chunk = text[i:i+chunk_size] #(0 - 100)(80 - 180) (160 - 260)
    chunks.append(chunk)
# for i in range(len(chunks)):
#     print(f"chunk {i+1} -> {chunks[i]}")
embeddings = model.encode(chunks)
# print(embeddings[0])
# print(len(embeddings))
# print(embeddings.shape)
client  = chromadb.PersistentClient(path = "./chroma_db")
collection = client.get_or_create_collection(name = "MyDocuments")
ids = []
for i in range(len(chunks)):
    ids.append(f"{file_name}_{i}")
collection.add(
    ids = ids,
    documents = chunks,
    embeddings=embeddings.tolist()
)
results = collection.get()
chunk1 = collection.get(ids=['sample.txt_0'])
print(chunk1)
print("Collection created successfully")