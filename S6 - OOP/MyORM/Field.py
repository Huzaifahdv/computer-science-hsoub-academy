from abc import ABC  # استيراد وحدة


class Field(ABC):  # إنشاء الصنف المجرد
    field_type = None  # خاصية صنف تمثل نوع الحقل
    # الذي يقابل نوع البيانات في بايثون sqlite وستكون قيمة هذه الخاصية سلسلة نصية تتضمن نوع البيانات في field سيستخدم في تحديد نوع العمود الذي يمثله كل صنف مشتق من الصنف

    def __init__(self, max_length=255, unique=None):  # يحمل المعاملان قيم افتراضية ويمكن تخصيصها عند إنشاء نسخة من صنف الحقل
        if unique is True:
            self.unique = 'UNIQUE'
        else:
            self.unique = ''

        if max_length:
            self.max_length = max_length

    # يجري تنفيذ هذا التابع السحري عند استدعاء الصنف ويعرض سلسلة نصية تتضمن تمثيلًا لذلك الصنف
    def __repr__(self):  # يعرف هذا التابع قائمة ثم يضيف إليها نوع العمود والقيود المفروضة عليه
        column = []  # تعريف القائمة
        if self.field_type == 'VARCHAR':  # VARCHAR تتحقق الجملة الشرطية مما إذا كان الحقل المراد إنشاؤه من نوع
            column.append(f'VARCHAR({self.max_length})')  # sqlite وذلك لإضافة العدد الأقصى من الحروف داخل القوسين , وكتابة اسم الحقل بالطريقة هذه هي من متطلبات محرك قواعد البيانات
        else:
            column.append(self.field_type)
            column.append(self.unique)
        return ''.join(column).strip()  # بعضها ببعض في سلسلة نصية ويفصل كل عنصر فيها بفاصلة column لربط عناصر القائمة join تستخدم الدالة
        # للتخلص من المسافات البيضاء الزائدة في حال وجودها strip() الدالة


# تعريف مجموعة من الأصناف التي تمثل أنواع مختلفة من الأعمدة
class CharField(Field):
    field_type = 'VARCHAR'

    def __init__(self, max_length=255, unique=None):
        self.max_length = max_length
        self.unique = unique
        super().__init__(max_length=max_length, unique=unique)


class TextField(Field):
    field_type = 'TEXT'

    def __init__(self, unique=None):
        self.unique = unique
        super().__init__(unique=unique)


class IntegerField(Field):
    field_type = 'INTEGER'

    def __init__(self, unique=None):
        self.unique = unique
        super().__init__(unique=unique)


class FloatFiled(Field):
    field_type = 'REAL'

    def __init__(self, unique=None):
        self.unique = unique
        super().__init__(unique=unique)


class BooleanField(Field):
    field_type = 'INTEGER'

    def __init__(self, unique=None):
        self.unique = unique
        super().__init__(unique=unique)


class DateTimeField(Field):
    field_type = 'TIMESTAMP'

    def __init__(self, unique=None):
        self.unique = unique
        super().__init__(unique=unique)