// U.10 lesson 4: File Reading قراءة الملفات
// node.js من fs استدعاء وحدة 
//const fs = require('fs');     // يتم استدعاؤه بهذه الطريقة
//هذا تابع لقراءة الملفات 
//fs.readFile('./messages.txt','utf8',(error,data)=>{
//    if(error)console.log(error);
//    else {
//        const messages = data.split(',');
//        console.log(messages);
//    }
// المعامل الاول يوضع فيه اسم الملف المطلوب قراءته
// المعامل الثاني يوضع فيه نظام الترميز الذي نود قراءة الملف به
// المعامل الأخير نضع فيه تابع الإستجابه ويحتوي على عاملين الأول يعبر عن الخطأ والثاني يطبع محتويات الملف إذا كان هناك بيانات
//"split"
// هذا التابع يفصل السلاسل النصية وفق محرف فصل معين ويعيد مصفوفة تحوي تلك الأجزاء
//});

// U.10 lesson 5: Files writing كتابة الملفات
//هذا تابع لكتابة ملف جديد
//const fs = require('fs');
//const messages = [
//    'mes1', 'mes2','mes3','mes4'
//];
//const content = messages.join('/');
//fs.writeFile('./new.txt', content ,'utf8',error => {
//    if(error) console.log(error);
//    else console.log('File written');
//} );
// المعامل الأول اسم الملف
// المعامل الثاني محتويات الملف
// المعامل الثالث نظام الترميز
// المعامل الأخير تابع الإستجابة ويحتوي على معامل واحد فقط 
//"join"
// هذا التابع يجمع عناصر المصفوفة معًا ضمن سلسلة نصية ويفصل بينها بمحرف فصل 

// U.10 lesson 6: Files Editing تعديل الملفات
// هذا تابع للإضافة إلى الملف وهي مشابهه للدالة اللي قبل
// const fs = require('fs');
// const content = '\nhou are you?';
// fs.appendFile('./new.txt', content ,'utf8',error => {
//     if(error) console.log(error);
//     else console.log('File written');
// } );

//هذا التابع لتغيير اسم الملف
// const fs = require('fs');
// fs.rename('./new.txt','my.txt', error => {
//     if (error) console.log(error);
//     else console.log('renamed');
// })
//المعامل الأول اسم الملف المطلوب تغييره
// المعامل الثاني الإسم الجديد
// المعامل الأخير تابع الإستجابة ويمكن الإستغناء عنه
 
// // هذا التابع لحذف ملف
// fs.unlink('./my.txt', error=>{
//     if(error) console.log(error);
//     else console.log('deleted');
// })

// U.10 lesson 7: الإدخال والإخراج
// هذه وحده في نود جي اس يستخدم للتعامل مع سطر الأوامر وعمليات الإدخال والإخراج
// const readline = require('readline');

// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout,
// });

// rl.question(`what's your name?`, answer =>{
//     console.log(`Hello: ${answer}`);
//     rl.close();
// });







