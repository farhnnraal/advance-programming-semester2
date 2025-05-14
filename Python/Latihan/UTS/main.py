from function import alphabetScore, weightScore, weightDefinition
import datetime

class KHS:
    def __init__(self):
        self.ipScore = 0.0
        self.sksPerSemester = 20

    def writeKHSHead(self, khsData):
        print("\n===============================================================================================================================")
        print("-------------------------------------------------------------------------------------------------------------------------------\n")
        print("Kartu Hasil Studi (KHS)\n")

        print(f"Nama          : {khsData.studentName}")
        print(f"NIM           : {khsData.studentNIM}")
        print(f"Jurusan       : {khsData.studentMajor}")
        print(f"Studi Program : {khsData.studentStudyProgram}")
        print(f"Semester      : {khsData.studentSemester}\n")
        print("===============================================================================================================================")
        print("| NO  | Matakuliah                                                     | SKS | Nilai Angka | Nilai Huruf | Bobot | Nilai Mutu |")

    def writeKHSBody(self, dataset):
        for index, res in enumerate(dataset, start=1):
            lessonName = res.name
            sks = res.sks
            scoreValue = res.scoreValue
            alphabetScoreValue = alphabetScore(res.scoreValue)
            weight = weightDefinition(alphabetScoreValue)
            quality = weightScore(alphabetScoreValue, res.sks)

            self.ipScore += (weight * sks)

            print(f"|  {index:<1}  | {lessonName:<40}                                      | {sks:<3} | {scoreValue:<12}| {alphabetScoreValue:<12}| {weight:<5.1f} | {quality:<11.1f}|")

    def writeKHSFooter(self):
        xtime = datetime.datetime.now()

        print(f"\nIndeks Prestasi (IP)   : {self.ipScore / self.sksPerSemester}")
        print(f"Tanggal Kelulusan      : {xtime.strftime('%d-%m-%Y')}")
        print("Status Kelulusan       : Lulus")

class KHSData:
    def __init__(self, studentName, studentNIM, studentMajor, studentStudyProgram, studentSemester):
        self.studentName = studentName
        self.studentNIM = studentNIM
        self.studentMajor = studentMajor
        self.studentStudyProgram = studentStudyProgram
        self.studentSemester = studentSemester

class CollegeLesson:
    def __init__(self, name, sks, scoreValue):
        self.name = name
        self.sks = sks
        self.scoreValue = scoreValue

    def __repr__(self):
        return f"CollegeLesson(name={self.name}, sks={self.sks}, scoreValue={self.scoreValue})"

class StoredCollegeLesson:
    def __init__(self):
        self.collegeLessonArray = []
        self.khsData = None

    def __repr__(self):
        return 

    def addNewLessonResult(self, name, sks, scoreValue):
        self.collegeLessonArray.append(CollegeLesson(name, sks, scoreValue))

    def defNewKHS(self):
        print("-------------------------------------------------------------------------------------------------------------------------------")
        print("Masukkan data dirimu...\n")

        studentName = input("Siapa namamu? : ")
        studentNIM = input("Berapa NIM-mu? : ")
        studentMajor = input("Apa jurusanmu? : ")
        studentStudyProgram = input("Apa program studimu? : ")
        studentSemester = input("Berapa semester-mu? : ")

        self.khsData = KHSData(studentName, studentNIM, studentMajor, studentStudyProgram, studentSemester)

    def defNewLessonResult(self):
        print("\n-------------------------------------------------------------------------------------------------------------------------------")
        print("Masukkan hasil studi per matakuliah milikimu...\n")

        name = input("Apa matakuliahnya? : ")
        sks = int(input("Berapa SKS? : "))
        nilai_angka = float(input("Berapa nilaimu? : "))

        self.addNewLessonResult(name, sks, nilai_angka)


scl = StoredCollegeLesson()
dataset = scl.collegeLessonArray

khs = KHS()

print("===============================================================================================================================")
print("-------------------------------------------------------------------------------------------------------------------------------\n")
print("Selamat datang di KHS Generator!\n")

scl.defNewKHS()
khsData = scl.khsData

while True:
    scl.defNewLessonResult()
    condition = input("\nApakah ada matakuliah lain? (y/n) : ").lower()
    if condition == "n":
        break
    elif condition != "y":
        print("Input tidak valid. Silakan coba lagi.")
        continue

khs.writeKHSHead(khsData)
khs.writeKHSBody(dataset)

print("===============================================================================================================================")

khs.writeKHSFooter()

print("\n-------------------------------------------------------------------------------------------------------------------------------")
print("===============================================================================================================================\n")