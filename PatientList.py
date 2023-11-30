class Patient:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class DoctorApp:
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
                print(f"Name: {patient.name}, Age: {patient.age}, Gender: {patient.gender}")

# Example Usage
if __name__ == "__main__":
    doctor_app = DoctorApp()

    # Adding patients
    patient1 = Patient("John Doe", 30, "Male")
    doctor_app.add_patient(patient1)

    patient2 = Patient("Jane Smith", 25, "Female")
    doctor_app.add_patient(patient2)

    # Displaying the patient list
    doctor_app.display_patients()
