import json
from datetime import datetime

class CurrencyMismatchError(Exception):
    """Ошибка валюты при проведении операции."""
    pass

class InsufficientFundsError(Exception):
    """Ошибка нехватки средств при снятии."""
    pass

class AccountAlreadyExistsError(Exception):
    """Ошибка: счет в данной валюте уже существует."""
    pass

class ClientAlreadyExistsError(Exception):
    """Ошибка: такой клиент уже существует."""
    pass

class AccountNotFound (Exception):
    """Счет в этой валюте не был найден"""
    pass

class CurrencyMismatch (Exception):
    """Переводы разных валют запрещены"""

class ClientNotExistsError(Exception):
    """Ошибка: такого клиента не существует."""
    pass


class Bank:
    def __init__(self, clients=None):
        self.clients = clients if clients is not None else {}
        

    def add_client(self, client_id, name, surname):
        if client_id not in self.clients:
            self.clients[client_id] = Client(client_id, name, surname)
            print(f"Добавлен клиент {name} {surname} с ID {client_id}")
        else:
            print(f"Клиент с ID {client_id} уже существует.")

    def get_client(self, client_id):
        if client_id not in self.clients:
            raise ValueError("Клиент не найден")
        return self.clients[client_id]

    def transfer(self, from_client_id, from_currency, to_client_id, to_currency, amount):
        from_client = self.get_client(from_client_id)
        to_client = self.get_client(to_client_id)

        from_account = from_client.get_account(from_currency)
        to_account = to_client.get_account(to_currency)

        if from_account.currency != to_account.currency:
            raise CurrencyMismatch("Переводы разных валют запрещены.")

        from_account.withdraw(amount)
        to_account.deposit(amount)
        print(
            f"Перевод {amount} {from_currency} со счета {from_client.name}"
            f" в {from_currency} на счет {to_client.name} в {to_currency}"
        )
        
    def save_state(self, filename="bank_state.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=4)
    
    @staticmethod
    def load_state(filename="bank_state.json"):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                clients = {
                    client_id: Client.from_dict(client_data)
                    for client_id, client_data in data["clients"].items()
                }
                return Bank(clients)
        except FileNotFoundError:
            return Bank()

    def to_dict(self):
        return {
            "clients": {
                client_id: client.to_dict()
                for client_id, client in self.clients.items()
            }
        }


class Client:
    def __init__(self, client_id, name, surname):
        self.client_id = client_id
        self.name = name
        self.surname = surname
        self.accounts = {}  

    def create_account(self, currency):
        if currency not in self.accounts:
            self.accounts[currency] = Account(currency)
            print(f"Открыт счет в валюте {currency} для клиента {self.name} {self.surname}") 
        else:
            print(f"Счет в валюте {currency} уже существует.")

    def close_account(self, currency):
        if currency not in self.accounts:
            raise AccountNotFound("Счёт в этой валюте не был найден.")
        del self.accounts[currency]
        print(f"Счет в валюте {currency} закрыт для клиента {self.name}")

    def get_account(self, currency):
        if currency not in self.accounts:
            raise AccountNotFound("Счёт в этой валюте не был найден.")
        return self.accounts[currency]

    def get_all_accounts(self):
        return list(self.accounts.values())

    def generate_statement(self):
        statement = f"Выписка клиента {self.name} (ID: {self.client_id}):\n"
        total_balance = 0.0
        for currency, account in self.accounts.items():
            statement += f"Валюта: {currency}, Баланс: {account.balance}\n"
            total_balance += account.balance
        statement += f"Общий баланс: {total_balance}\n"

        file_name = f"{self.client_id}_statement.txt"
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(statement)
        print(f"Выписка сохранена в {file_name}")

    def get_transaction_history(self):
        history = (
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} "
            f"История операций клиента {self.name} (ID: {self.client_id}):\n"
        )
        for currency, account in self.accounts.items():
            history += f"\nСчёт в валюте {currency}:\n"
            for transaction in account.get_transaction_history():
                history += f"  - {transaction}\n"
        return history

    def to_dict(self):
        return {
            "client_id": self.client_id,
            "name": self.name,
            "accounts": {
                currency: account.to_dict()
                for currency, account in self.accounts.items()
            },
        }

    @staticmethod
    def from_dict(data):
        client = Client(data["client_id"], data["name"], data["accounts"])
        client.accounts = {
            currency: Account.from_dict(acc_data)
            for currency, acc_data in data["accounts"].items()
        }
        return client

class Account:
    def __init__(self, currency):
        self.currency = currency
        self.balance = 0.0
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return print(f"Счет пополнен на {amount} {self.currency}. Текущий баланс: {self.balance} {self.currency}")
        self.transaction_history.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                                        f"Пополнение или перевод: +{amount} {self.currency}"
                                        f"Текущий баланс {self.balance} {self.currency}")
        if amount < 0:
             print("Нельзя пополнять счет на отрицательную сумму.")
        

    def withdraw(self, amount):
        if amount <= 0:
             print("Сумма снятия должна быть положительной.")
             return
        if amount <= self.balance:
            self.balance -= amount
            return print(f"Со счета снято {amount} {self.currency}. Текущий баланс: {self.balance} {self.currency}")
        if amount >= self.balance:
            raise InsufficientFundsError(f"Недостаточно средств на счете. Текущий баланс: {self.balance} {self.currency}")
        self.transaction_history.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                                        f"Снятие или перевод: +{amount} {self.currency}"
                                        f"Текущий баланс {self.balance} {self.currency}")

    def get_balance(self):
        self.transaction_history.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                                        f"Просмотр баланса: +{self.balance} {self.currency}"
                                        )
        return self.balance
    
    def get_transaction_history(self):
        return self.transaction_history
    
    def to_dict(self):
        return {
            "currency": self.currency,
            "balance": self.balance,
            "transaction_history": self.transaction_history
        }

    @staticmethod
    def from_dict(data):
        account = Account(data["currency"])
        account.balance = data["balance"]
        account.transaction_history = data["transaction_history"]
        return account

def main():
    bank = Bank.load_state()
    print("Добро пожаловать!")
    
    while True:
        print("\nВыберите действие: ")
        print("1. Зарегистрировать нового клиента")
        print("2. Войти в систему")
        print("3. Выйти из системы")

        choice = input("Введите номер операции: ")

        if choice == '1':
            client_id = input("Введите ID клиента: ")
            name = input("Введите имя клиента: ")
            surname = input("Введите фамилию клиента: ")
            try:
                bank.add_client(client_id, name, surname)
            except ClientAlreadyExistsError:
                print("Такой клиент уже существует")
        
        if choice == "2":
            client_id = input("Введите Ваш ID: ")
            try:
               client = bank.get_client(client_id)
               print("")
            except ClientNotExistsError:
                print("Ошибка: такого клиента не существует.")
                continue

            while True:
                print(f"\nДобро пожаловать, {client.name}")
                print("1. Открыть счет.")
                print("2. Закрыть счет.")
                print("3. Пополнить счет.")
                print("4. Снять сумму со счета.")
                print("5. Перевести деньги между счетами.")
                print("6. Сделать выписку по всем счетам.")
                print("7. Посмотреть историю операций.")
                print("8. Выйти из системы")
                
                action = input("Выберите операцию: ")
               
                if action == "1":
                    currency = input("Введите валюту счёта: ")
                                        
                    try:
                        client.create_account(currency)
                    except ValueError as e:
                        print(e)

                elif action == "2":
                    currency = input("Введите валюту счёта: ")
                    try:
                        client.close_account(currency)
                    except AccountNotFound as e:
                        print(e)

                elif action == "3":
                    currency = input("Введите валюту счета: ")
                    amount = float(input("Сумма для пополнения счёта: "))
                    
                    try:
                        account = client.get_account(currency)
                        account.deposit(amount)
                    except (AccountNotFound, ValueError) as e:
                        print(e)

                elif action == "4":
                    
                    currency = input("Введите валюту счета: ")
                    
                    amount = float(input("Сумма для снятия со счёта: "))
                    try:
                        account = client.get_account(currency)
                        account.withdraw(amount)
                    except (
                        AccountNotFound,
                        InsufficientFundsError,
                        ValueError,
                    ) as e:
                        print(e)

                elif action == "5":
                    
                    from_currency = input(
                        "Введите валюту счета, с которого переводите: "
                    )
                    to_client_id = input("ID клиента к переводу: ")
                    to_currency = input("Валюта счета к переводу: ")
                    amount = float(input("Введите сумму для перевода: "))
                    
                    try:
                        bank.transfer(
                            client_id,
                            from_currency,
                            to_client_id,
                            to_currency,
                            amount,
                        )
                    except (
                        ValueError,
                        AccountNotFound,
                        CurrencyMismatch,
                        InsufficientFundsError,
                    ) as e:
                        print(e)

                elif action == "6":
                    try:
                        client.generate_statement()
                    except Exception as e:
                        print(f"Ошибка при создании выписки: {e}")

                elif action == "7":
                    print(client.get_transaction_history())

                elif action == "8":
                    break

                else:
                    print("Неверный выбор, попробуйте снова")
                    
        elif choice == "3":
            bank.save_state()
            print("Вы вышли из системы. Всего доброго!")
            break

        else:
            print("Неверный выбор, попробуйте снова")
            
if __name__ == "__main__":
    main()
        