import pickle
from datetime import datetime

class Transaction:
    def __init__(self, amount, date, description, transaction_type):
        """
        Inicializa una nueva instancia de transacción con los detalles proporcionados.
        Args:
            amount (float): El monto de la transacción.
            date (datetime): La fecha y hora de la transacción.
            description (str): Descripción de la transacción.
            transaction_type (str): Tipo de transacción ('income' para ingresos, 'expense' para gastos).
        """
        self.amount = amount
        self.date = date
        self.description = description
        self.transaction_type = transaction_type

class PersonalFinanceApp:
    def __init__(self):
        """
        Inicializa la aplicación de finanzas personales con una lista vacía de transacciones.
        """
        self.transactions = []

    def add_transaction(self, amount, date, description, transaction_type):
        """
        Agrega una nueva transacción a la lista de transacciones.
        Args:
            amount (float): El monto de la transacción.
            date (datetime): La fecha y hora de la transacción.
            description (str): Descripción de la transacción.
            transaction_type (str): Tipo de transacción ('income' para ingresos, 'expense' para gastos).
        """
        transaction = Transaction(amount, date, description, transaction_type)
        self.transactions.append(transaction)

    def list_transactions(self):
        """
        Lista todas las transacciones ordenadas por fecha.
        """
        sorted_transactions = sorted(self.transactions, key=lambda x: x.date)
        for transaction in sorted_transactions:
            print(f"{transaction.date}: {transaction.description} - {transaction.amount} ({transaction.transaction_type})")

    def calculate_balance(self):
        """
        Calcula el balance financiero actual.
        Returns:
            tuple: Una tupla que contiene el total de ingresos, el total de gastos y la capacidad de ahorro.
        """
        total_income = sum(transaction.amount for transaction in self.transactions if transaction.transaction_type == 'income')
        total_expenses = sum(transaction.amount for transaction in self.transactions if transaction.transaction_type == 'expense')
        savings = total_income - total_expenses
        return total_income, total_expenses, savings

    def save_data(self):
        """
        Guarda la lista de transacciones en un archivo utilizando el módulo pickle.
        """
        with open('datos_financieros.pkl', 'wb') as f:
            pickle.dump(self.transactions, f)

    def load_data(self):
        """
        Carga los datos previos de transacciones desde un archivo utilizando el módulo pickle.
        Si el archivo no existe, inicializa en un estado vacío.
        """
        try:
            with open('datos_financieros.pkl', 'rb') as f:
                self.transactions = pickle.load(f)
        except FileNotFoundError:
            self.transactions = []

if __name__ == "__main__":
    app = PersonalFinanceApp()
    app.load_data()

    while True:
        print("\n1. Agregar Transacción")
        print("2. Listar Transacciones")
        print("3. Balance")
        print("4. Guardar Datos")
        print("5. Salir")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            amount = float(input("Ingrese el monto: "))
            date = datetime.now()
            description = input("Ingrese una descripción: ")
            transaction_type = input("Tipo de transacción (income/expense): ")
            app.add_transaction(amount, date, description, transaction_type)

        elif choice == "2":
            app.list_transactions()

        elif choice == "3":
            total_income, total_expenses, savings = app.calculate_balance()
            print(f"\nTotal de ingresos: {total_income}")
            print(f"Total de gastos: {total_expenses}")
            print(f"Capacidad de ahorro: {savings}")

        elif choice == "4":
            app.save_data()
            print("Datos guardados exitosamente.")

        elif choice == "5":
            break

        else:
            print("Opción inválida. Intente nuevamente.")
