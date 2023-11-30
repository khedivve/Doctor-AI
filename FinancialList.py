class Patient:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.financial_section = FinancialSection()

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")

class FinancialTransaction:
    def __init__(self, description, amount, transaction_type):
        self.description = description
        self.amount = amount
        self.transaction_type = transaction_type  # 'Income' or 'Expense'

class FinancialSection:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        print(f"Transaction added successfully!")

    def display_transactions(self):
        if not self.transactions:
            print("No transactions recorded.")
        else:
            print("Financial Transactions:")
            for transaction in self.transactions:
                print(f"Description: {transaction.description}, Amount: {transaction.amount}, Type: {transaction.transaction_type}")

class DoctorAI:
    def __init__(self):
        self.patient_list = []

    def add_patient(self, patient):
        self.patient_list.append(patient)
        print(f"Patient {patient.name} added successfully!")

    def display_patients(self):
        if not self.patient_list:
            print("No patients in the list.")
        else:
            print("Patient List:")
            for patient in self.patient_list:
                patient.display_info()
                patient.financial_section.display_transactions()
                print()

# Example Usage
if __name__ == "__main__":
    doctor_ai = DoctorAI()

    # Adding patients with financial transactions
    patient1 = Patient("John Doe", 30, "Male")
    transaction1 = FinancialTransaction("Consultation Fee", 100.0, "Income")
    patient1.financial_section.add_transaction(transaction1)
    doctor_ai.add_patient(patient1)

    patient2 = Patient("Jane Smith", 25, "Female")
    transaction2 = FinancialTransaction("Medical Supplies", 50.0, "Expense")
    transaction3 = FinancialTransaction("Follow-up Visit", 75.0, "Income")
    patient2.financial_section.add_transaction(transaction2)
    patient2.financial_section.add_transaction(transaction3)
    doctor_ai.add_patient(patient2)

    # Displaying the patient list with financial transactions
    doctor_ai.display_patients()
