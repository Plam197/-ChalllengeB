import os 

def create_file(subject_name):
    filename = f"{subject_name.lower()}.txt"
    if not filename.endswith(".txt"):
        print("ชื่อ-นามสกุลไฟล์ไม่ถูกต้อง กรุณาป้อนใหม่ :")
        return None
    
    with open(filename, "w") as file:
        print(f"ไฟล์ {filename} ถูกสร้างเรียบร้อยแล้ว ^_^")

    return filename 

def add_data_to_file(filenamw):
    try:
        with open(filenamw, "a") as file:
            student_name = input ("ป้อนชื่อ-สกุลนักเรียน: ")
            midterm_score = float(input("ป้อนคะแนนกลางภาค: "))
            final_score = float(input("ป้อนคะแนนปลายภาค :"))
            homework_score = float(input("ป้อนคะแนนเก็บ :"))

            total_score = midterm_score + final_score + homework_score 
            result = "ผ่าน" if total_score > 50 else "ไม่ผ่าน"

            file.write(f"ชื่อ-สกุลนักเรียน :{student_name}\nคะแนนกลางภาค :{midterm_score}\nคะแนนปลายภาค :{final_score}\nคะแนนเก็บ :{homework_score}\nคะแนนรวม :{total_score}\nผลการสอบ :{result}\n")
            print("เพิ่มข้อมูลต่อท้ายไฟล์เรียบร้อยแล้ว")
    except ValueError:
        print("กรุณาป้อนคะแนนเป็นตัวเลข")

def display_files():
    files = [files for file in os.listdir() if file.endswith(".txt")]
    if not files:
        print("ไม่มีไฟล์ใดๆอยู่เลย")
        return None
    print("ไฟล์ทั้งหมด :")
    for file in files:
        print(file)
    return file

def read_and_display_data(filename):
    try:
        with open(filename, "r") as file:
            print(f"ข้อมูลในไฟล์ {filename}:")
            print(file.read())
    except FileNotFoundError :
        print("ไม่พบไฟล์ที่ระบุ")

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"ลบไฟล์ {filename} เรียบร้อยแล้ว")
    except FileNotFoundError :
        print("ไม่พบไฟล์ที่ระบุ")

def main():
    print("----------------------SCHOOL-----------------------")
    print("1.สร้างไฟล์วิชาใหม่ดพื่อเพิ่มข้อมูล \n2.เลือกวิชาและเพิ่มข้อมูลต่อท้ายไฟล์ \n3.เลือกวิชาและอ่านข้อมูลจากไฟล์มาแสดงผล \n4.เลือกวิชาและลบไฟล์ \n0.จบการทำงาน")

    while True:
        try:
            choice = int(input("--------------\nเลือกเมนู :"))
            print("---------------")

            if choice == 0:
                print("-----------------\nจบการทำงาน\n-----------------")
                break
            elif choice in [1, 2, 3, 4]:
                if choice == 1:
                    subjest_name = input("ป้อนชื่อไฟล์วิชาเพื่อเก็บข้อมูลคะแนน(xxxxx.txt):")
                    filename = create_file(subjest_name)
                    if filename:
                        add_data_to_file(filename)
                elif choice == 2:
                    files = display_files()
                    if files:
                        selected_file = input("เลือกไฟล์โดยการป้อนชื่อไฟล์: ")
                        if selected_file in files:
                            add_data_to_file(selected_file)
                elif choice ==3:
                    files = display_files()
                    if files:
                        selected_file = input("เลือกไฟล์โดยการป้อนชื่อไฟล์: ")
                        if selected_file in files:
                            read_and_display_data(selected_file)
                elif choice == 4:
                    files = display_files()
                    if files:
                        selected_file = input("เลือกไฟล์โดยการป้อนชื่อไฟล์ :")
                        if selected_file in files:
                            delete_file(selected_file)
            else:
                print("---------------------------\nกรุณาเลือกเมนู 1, 2, 3, 4, หรือ 0 เท่านั้น\n--------------------")
        except ValueError:
            print("------------------------------\nกรุณาป้อนตัวเลข\n---------------------")

if __name__=="__main__":
    main()