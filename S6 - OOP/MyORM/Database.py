import sqlite3  # استيراد الوحدة


# يحتوي هذا الصنف على جميع التوابع المسؤولة عن التعامل مع قواعد البيانات
# إنشاء الاتصال و قطع الاتصال وتطبيق نتيجة الاستعلام على قاعدة البيانات
class Database:
    def __init__(self, path):  # Database يطلب تغيير قيمتها عند إنشاء كائن path الخاصية
        self.path = path  # على هيئة سلسلة نصية sqlite تمثل هذه الخاصية مسار قاعدة البيانات
        self.connection = None  # الذي سينشأ عند الاتصال بقاعدة البيانات بنجاح connection هذه الخاصية تتضمن كائن الاتصال
        self.connected = False  # ويمثل حالة الاتصال بقاعدة البيانات True أو False متغير منطقي يحمل قيمة
        self.connect()  # Database نستدعي هذا التابع لإجراء الاتصال عند إنشاء نسخة من الصنف

    def connect(self):  # تابع إنشاء الاتصال
        try:  # حاول
            self.connection = sqlite3.connect(self.path)  # ومرر إليه مسار قاعدة البيانات  sqlite3 من الوحدة connect استخدام التابع
            self.connection.row_factory = sqlite3.Row  # الذي يتيح إجراء العديد من العمليات على النتائج sqlite3.Row إلى نسخ من الكائن sqlite3 تحويل القيم المعادة من توابع الوحدة
            # مثل الوصول إليها عن طريق اسم العمود أو موقع الحقل والمرور على النتائج وتمثيلها بطرق مختلفة
            self.connected = True  # True غير هذه الخاصية إلى
        except sqlite3.Error as e:  # إذا نتج خطأ من الكتلة البرمجية السابقة فأوقف التنفيذ ومرر متغير يمثل الإستثناء الناتج من الخطأ الحاصل وطباعته للمستخدم
            print(e)
        return self.connection  # أعد كائن الاتصال هذه الذي نشأ بعد الاتصال بقاعدة البيانات بنجاح

    def commit(self):  # يثبت هذا التابع عملية التغيير التي حصلت على قاعدة البيانات
        self.connection.commit()

    def close(self):  # connected يغلق قاعدة البيانات بعد التحقق من حالتها بقراءة قيمة الخاصية
        if self.connected:
            self.connection.close()
        self.connected = False
