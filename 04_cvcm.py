class Bank:
    bank_name = "Initial Bank"

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name


if __name__ == "__main__":
    bank1 = Bank()
    bank2 = Bank()

    print("Before changing the bank name:")
    print(f"Bank.bank_name = {Bank.bank_name}")
    print(f"bank1.bank_name = {bank1.bank_name}")
    print(f"bank2.bank_name = {bank2.bank_name}")

    Bank.change_bank_name("XYZ Bank")

    print("\nAfter changing the bank name:")
    print(f"Bank.bank_name = {Bank.bank_name}")
    print(f"bank1.bank_name = {bank1.bank_name}")
    print(f"bank2.bank_name = {bank2.bank_name}")