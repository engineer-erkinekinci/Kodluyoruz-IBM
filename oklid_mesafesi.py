## iki boyutlu düzlemde x ve y eksenindeki konumları verilen noktalar arasındaki en kısa öklit mesafesinin bulunması
def  euclideanDistance(p):
    # noktalar arasında hesaplanan öklid mesafesinin listesi
    distances = []

    for nokta1 in range(len(p)):
        for nokta2 in range(len(p)):
            oklid = 0

            if p[nokta1]==p[nokta2]:
                continue

            for eksen in range(len(p[nokta2])):
                oklid += (p[nokta1][eksen]- p[nokta2][eksen])**2

            oklid **= (1/2)
            distances.append(oklid)

    return (f"noktalar arasındaki en kısa öklid mesafesi : {min(distances)}")

## veri bilgileri ve euclideanDistance fonksiyonunun çağrıldığı yer 
# iki boyutlu düzlemdeki 2 farklı noktanın x ve y konum bilgilerini içeren liste
points = [(2,8),(-1,4),(2,3),(3,4),(0,0),(1000,1000),(-5,-5)]
sonuc =  euclideanDistance(points)
print(sonuc)