import difflib

# İki metni okuyun
with open("orijinal.txt", "r") as file:
    original_text = file.read()

with open("kontrol.txt", "r") as file:
    checked_text = file.read()

# Metinleri karşılaştırın ve farkları bulun
matcher = difflib.SequenceMatcher(None, original_text, checked_text)
difference = matcher.ratio()

# Benzerlik oranını kontrol edin
similarity = difference * 100
if similarity <= 25:
    print(f"Metin özgün. * Benzerlik oranı: {similarity:.2f}%")
else:
    print(f"Metin özgün değil. Benzerlik oranı: {similarity:.2f}%")
