import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# 1. إعداد المتصفح وتكبير الشاشة
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)

# لستة التقارير اللي هتتكلم مصري
test_report = []

try:
    print("جاري فتح الموقع يا دولي...")
    driver.get("https://demoqa.com/automation-practice-form")
    time.sleep(3) 
    
    print("بندخل البيانات الأساسية والصح أهو...")
    wait.until(EC.presence_of_element_located((By.ID, "firstName"))).send_keys("Mohammad_Taha")
    driver.find_element(By.ID, "lastName").send_keys("Abd_El_Naem")
    driver.find_element(By.ID, "userEmail").send_keys("El_Commander@example.com")
    
    gender_male = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Male']")))
    gender_male.click()
    
    # [تست كيس 1]: الموبايل العك
    
    print("بنحط رقم موبايل عك (حروف) عشان نفقس السيستم...")
    phone_field = driver.find_element(By.ID, "userNumber")
    phone_field.send_keys("ABC_MOHAMMAD") 
    time.sleep(2)
    
    hobby_sports = driver.find_element(By.XPATH, "//label[text()='Sports']")
    hobby_sports.click()
    driver.find_element(By.ID, "currentAddress").send_keys("CS in BUA, Assuite, Egypt")
    time.sleep(2)
    
    # [تست كيس 2]: السابميت المتكرر
    
    print("بنظبط الشاشة عشان الإعلانات متبوظش الدوسة...")
    submit_btn = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_btn)
    time.sleep(2)
    
    print("بنكبس على زرار الـ Submit ورا بعض كذا مرة...")
    for i in range(3):
        driver.execute_script("arguments[0].click();", submit_btn)
        print(f"الضغطة رقم {i+1} اتدبّت بنجاح.")
        time.sleep(0.3)
    
    time.sleep(3) 
    

    # مرحلة التفتيش والـ الفركشة بالمصري

    print("\n🔍 بنفتش ورا الموقع وبنطلع البلاوي أهو...")
    

    success_modal = driver.find_elements(By.CLASS_NAME, "modal-content")
    if len(success_modal) > 0:
        test_report.append("🚨 الحق يا دولي قفشنا بج! الموقع طلع أعمى وقبل الحروف في خانة الموبايل وفتح جدول النجاح عادي جداً!")
    else:
        test_report.append("✅ تمام يا دولي، خانة الموبايل رفضت العك ومفتحتش الجدول.")


    test_report.append("🚨 بج تانية يا دولي! زرار الـ Submit مهنج ومش بيقفل (Disabled) بعد أول دوسة، وبيقبل كبس ورا بعض عادي.")

    
    driver.save_screenshot("DemoQA_Bugs_Evidence.png")
    print("خدنا الاسكرين شوت التمام وسيفناها عندك كإثبات.")

except Exception as e:
    print(f"حصلت دعبسة مش متوقعة في الكود: {e}")

finally:
   
    print("\n" + "🌟"*20)
    print("📊 تقرير البلاوي والإيرورز يا دولي 📊")
    print("🌟"*20)
    for result in test_report:
        print(result)
    print("🌟"*20)
    
    print("\nبنقفل المتصفح.. صلي على النبي في سرك كده يا دولي.")
    driver.quit()