class Patient(object):
    PATIENT_COUNT = 0
    def __init__(self, name, allergies):
        self.name = name
        self.allergies = allergies
        self.id = Patient.PATIENT_COUNT
        self.bed_num = None
        Patient.PATIENT_COUNT += 1

class Hospital(object):
    def __init__(self,name,cap):
        self.name = name
        self.cap = cap
        self.patients = []
        self.beds = self.initialize_beds()

    def initialize_beds(self):
        beds = []
        for i in range(0, self.cap):
            beds.append({
                "bed_id": 1,
                "Available": True
            })
        return beds