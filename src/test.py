from tqdm import tqdm

a = 1
for i in tqdm(range(1000)):
    for j in range(1000):
        for k in range(200):
            a += a
            a = a / 2
