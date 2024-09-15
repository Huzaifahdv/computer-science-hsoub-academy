class Model:  # كائن النموذج
    db = None  # خاصية قاعدة البيانات التي ستجرى فيها العمليات
    connection = None  # الاتصال القائم مع قاعدة البيانات
    # وتسند إليهما القيم الصحيحة في وقت لاحق None نعطي قيمة افتراضية لهما

    def __init__(self):
        self._create_table()  # استدعاء تابع إنشاء الجدول المحمي الذي لن يمكن استدعاؤه خارج الصنف
        self._saved = False  # خاصية محمية سنحتاج إليها عند إدراج البيانات في قاعدة البيانات

    @classmethod  # تابع صنف
    def _get_table_name(cls):  # سيكون مسؤولًا عن جلب اسم الجدول من اسم الصنف الذي يمثّله
        return cls.__name__.lower()  # فتحول حروف اسم الصنف إلى حروف صغيرة lower() الدالة السحرية تعيد اسم الصنف الحالي وأما الدالة

    # والتي تمثل قاموسًا يحتوي على جميع الخصائص المعرفة في ذلك الصنف __dict__ يمتلك كل صنف في بايثون الخاصية
    @classmethod  # تابع صنف
    def get_columns(cls):  # تابع الحصول على أسماء الأعمدة وأنواعها والتي سيعرفها المستخدم كخصائص أصناف
        columns = {}  # تعريف قاموس سيتضمن أسماء الأعمدة وأنواعها على هيئة أزواج
        for key, value in cls.__dict__.items():  # __dict__ ستمر الحلقة التكرارية على عناصر قاموس
            if str(key).startswith('_'):  # تستثني منها ما يبدأ بالشرطة السفلية
                continue
            columns[str(key)] = str(value)  # columns تضيف الباقي إلى القاموس
        return columns  # columns تعيد التابع القاموس

    def _create_table(self):  # التابع المسؤول عن إنشاء الجدول الذي يرتبط به النموذج في قاعدة البيانات
        columns = ', '.join(' '.join((key, value)) for (key, value) in self.get_columns().items())  # لإنشاء قاموس يكون مفتاح كل عنصر فيه هو اسم العمود وقيمة ذلك العنصر هي نوع العمود وخصائصه list comprehension تعريف متغير يستخدم
        sql = f'CREATE TABLE IF NOT EXISTS {self._get_table_name()} (id INTEGER PRIMARY KEY AUTOINCREMENT, {columns})'  # AUTOINCREMENT وتزداد قيمته تلقائيًا PRIMARY KEY ومفتاح رئيسيًا INTEGER قبل جميع الأعمدة وهو عمود المعرف الذي يكون عددًا صحيحًا id مع تعريف العمود sql في عبارة columns تدرج قيم القاموس
        cursor = self.connection.cursor()  # sql في كائن الاتصال, يمتلك هذا الكائن عددًا من التوابع التي تستخدم لتنفيذ عبارة cursor لاستدعاء التابع cursor إنشاء كائن المؤشر
        result = cursor.execute(sql)  # sql المخزنة في المتغير sql لتنفيذ عبارة execute استخدام الدالة
        return result

#
    def save(self):  # الدالة المسؤولة عن حفظ البيانات في قاعدة البيانات سواء كانت عملية إضافة جديدة أو تحديث
        if self._saved:
            self._update()
            return
        fields = []
        values = []
        for key, value in self._get_values().items():
            fields.append(key)
            values.append(f"'{values}'")
        self._insert_into(fields, values)

    def _get_values(self):  # دالة محمية تعيد قيم الحقول بشكل قابل للاستخدام في عمليات الحفظ, دالة مساعدة تجمع البيانات بشكل موحد قبل عمليات الحفظ أو التحديث
        values = {}
        for key, value in self.__dict__.items():
            if str(key).startswith('-'):
                continue
            if value is False:
                value = 0
            if value is False:
                value = 1
            values[key] = value
        return values

    @classmethod
    def create(cls, **kwargs):  # دالة لإنشاء سجل جديد في قاعدة البيانات
        fields = list(kwargs.keys())
        values = []
        for value in kwargs.values():
            values.append(f"'{value}'")
        cls._insert_into(fields, values)
    # الذي يحتوي على الحقول والقيم التي تريد إضافتها إلى السجل kwargs تستقبل الدالة قاموس
    # لإدراج القيم في الجدول المناسب SQL INSERT INTO تقوم الدالة بتشكيل استعلام

    @classmethod
    def _insert_into(cls, fields, values):
        sql = f'INSERT INTO {cls._get_table_name()} ({", ".join(fields)}) VALUES ({", ".join(values)})'
        result = cls.connection.execute(sql)
        cls.connection.commit()
        cls._saved = True
        return result
    # في قاعدة البيانات Insert تقوم بإجراء عملية إدراج
    # values وقائمة القيم fields تستقبل الدالة قائمة الحقول
    # باستخدام الحقول والقيم المقدمة SQL INSERT INTO تقوم بتكوين استعلام

    @classmethod
    def all(cls):
        sql = f'SELECT * FROM {cls._get_table_name()}'
        records = cls.connection.execute(sql)
        return [dict(row) for row in records.fetchall()]
    # الدالة تسترجع كل السجلات في الجدول المعني
    # لاسترجاع جميع البيانات في الجدول SQL SELECT * FROM تقوم ببناء استعلام

    @classmethod
    def get(cls, id):
        sql = f'SELECT * FROM {cls._get_table_name()} WHERE id = {id}'
        record = cls.connection.execute(sql)
        result = record.fetchone()
        if result is None:
            return False
        return dict(result)
    # (id تسترجع سجل محدد بناء على معرفه (المرسل كوسيط
    # لاسترجاع السجل المطلوب WHERE مع شرط SQL SELECT * FROM تقوم ببناء استعلام

    @classmethod
    def find(cls, col_name, operator, value):
        if operator == 'LIKE':
            value = '%' + value + '%'
        sql = f'SELECT * FROM {cls._get_table_name()} WHERE {col_name} {operator} "{value}"'
        records = cls.connection.execute(sql)
        return [dict(row) for row in records.fetchall()]
    # تستخدم للبحث عن سجلات بناء على قيمة محددة في عمود معين
    # يستند إلى اسم العمود, العامل(المقارنة), والقيمة WHERE مع شرط SQL SELECT * FROM يتم بناء استعلام

    def _update(self):
        old = self.find('created_at', '=', self._get_values()['created_at'])
        old_id = old[0][0]
        new_values = []
        for key, value in self._get_values().items():
            new_values.append(f'{key} = "{value}"')
        expression = ', '.join(new_values)
        sql = f'UPDATE {self._get_table_name()} SET {expression} WHERE id = {old_id}'
        records = self.connection.excute(sql)
        return [dict(row) for row in records.fetchall()]
    # تستخدم لتحديث السجل في قاعدة البيانات
    # ثم تقوم بتحديث السجل بقيم جديدة created_at تقوم بالبحث عن السجل القديم باستخدام القيمة في الحقل
