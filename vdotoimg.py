import cv2

# กำหนดชื่อไฟล์วีดีโอ
filename = 'pig10sec.mp4'

# อ่านไฟล์วีดีโอ
cap = cv2.VideoCapture(filename)

# อ่านภาพจากวีดีโอและบันทึกภาพในแต่ละเฟรมเป็นไฟล์ภาพ
frame_count = 1
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    # บันทึกภาพในแต่ละเฟรมเป็นไฟล์ภาพ
    if frame_count % 30  == 0 : # ตัดภาพทุก 30 เฟรม
        filename = f'frame{frame_count}.jpg'
        cv2.imwrite(filename, frame)
    frame_count += 1

# คืนค่าความจุของหน่วยความจำ
cap.release()

# ปิดหน้าต่างการแสดงผลภาพ
cv2.destroyAllWindows()
