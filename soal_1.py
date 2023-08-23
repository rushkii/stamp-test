# Soal 1: Program Kecil

# Tolong buat satu array / list dari 1 sampai 100. Print semua angka ini dalam urutan terbalik, tetapi ada beberapa peraturan :
# 1. Jangan print angka bilangan prima.
# 2. Ganti angka yang dapat dibagi dengan angka 3 dengan text "Foo".
# 3. Ganti angka yang dapat dibagi dengan angka 5 dengan text "Bar".
# 4. Ganti angka yang dapat dibagi dengan angka 3 dan 5 dengan text "FooBar".
# 5. Print angka menyamping tidak kebawah.


def is_prime_number(number: int) -> bool:
    """
    Cek angka apakah bilangan prima atau bukan.
    """
    if number < 2:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def answer():
    result = ""
    nums = list(range(100, 0, -1))
    for n in nums:
        if is_prime_number(n):
            continue
        elif n % 3 == 0 and n % 5 == 0:
            result += "FooBar, "
        elif n % 3 == 0:
            result += "Foo, "
        elif n % 5 == 0:
            result += "Bar, "
        else:
            result += f"{n}, "
    print(result.rstrip(", "))


if __name__ == "__main__":
    answer()
