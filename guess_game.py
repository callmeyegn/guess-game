import random

play_again = "y"

while play_again == "y":
    secret = random.randint(1, 100)
    tries = 0
    won = False

    print("بازی حدس عدد! یک عدد بین 1 تا 100 انتخاب شد. 5 فرصت داری.")

    while tries < 5:
        print("تلاش", tries + 1, "از 5")
        print("جان باقی مانده:", 5 - tries)

        text = input("حدس بزن: ")

        # بررسی ورودی
        if not text.isdigit():
            print("ورودی نامعتبر! فقط عدد وارد کن.")
            continue

        guess = int(text)
        if guess < 1 or guess > 100:
            print("عدد باید بین 1 تا 100 باشه!")
            continue

        tries = tries + 1

        if guess == secret:
            won = True
            break

        # جهت راهنما
        if guess > secret:
            print("کوچکتر وارد کن")
        else:
            print("بزرگتر وارد کن")

        # نزدیکی
        diff = abs(guess - secret)
        if diff <= 5:
            print("خیلی نزدیکی!")
        elif diff <= 15:
            print("نزدیکی، ولی هنوز فاصله داری!")
        else:
            print("خیلی دوری!")

    if won:
        print("آفرین! درست حدس زدی.")
        if tries == 1:
            print("رتبه: نمونه ای")
        elif tries == 2:
            print("رتبه: بسیار خوب")
        elif tries == 3:
            print("رتبه: خوب")
        elif tries == 4:
            print("رتبه: قبول")
        else:
            print("رتبه: با شانس بردی!")
    else:
        print("باختی!")
        print("عدد مخفی", secret, "بود")

    play_again = input("دوباره بازی می کنی؟ (y/n): ")

print("خداحافظ!")
