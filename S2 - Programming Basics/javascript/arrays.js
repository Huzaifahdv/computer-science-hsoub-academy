
// U.6 lesson 1: إضافة عنصر للمصفوفة
//let alphabet = ['c', 'd'];
//alphabet[alphabet.length]='e';
//هذا للإضافة في نهاية المصفوفة
//alphabet.push('f','g');
//alphabet.push('h','i');
//هذا للإضافة في بداية المصفوفة
//alphabet.unshift('a');
//هذا للإضافة في أي مكان في المصفوفة.ويمتلك عاملين أساسيين :الأول لرقم العنصر الذي
//تريد إضافته ،الثاني لعدد الخانات اللي تبي تحذفهن . ثم تضيف العناصر الجديدة
//alphabet.splice(1 , 0, 'b');
//console.log(alphabet)



// U.6 lesson 2: حذف عنصر من مصفوفة
//let number = [1, 2, 3, 4, 5, 6, 7];
//console.log(number);
//هذا لحذف العنصر الأخير
//number.pop();
//console.log(number);
//هذا لحذف العنصر الأول 
//number.shift();
//console.log(number);
//هذا لحذف العنصر من أي مكان 
//number.splice(1, 3);
//console.log(number);



// U.6 lesson 3: إفراغ مصفوفة
//let langs = ['js','php','c++'];
//let lang = langs;
//langs.length =0;
//console.log(lang);
//console.log(langs);



// U.6 lesson 4: تمرين:عكس المصفوفات
//let number = [1, 2, 3, 4, 5];
//function reverse(arr){
//    let temp = [];
//    for (let i in arr)
//        temp.unshift(arr[i]);
//    return temp;
//}
//console.log(reverse(number));
// splice() نفس الشي باستخدام
//let number = [1, 2, 3, 4, 5];
//function reverse(arr){
//    for (let i in arr)
//        arr.splice(i, 0, arr.pop())
//    return arr;
//}
//console.log(reverse(number));



// U.6 lesson 5: التوابع في المصفوفات
//let numbers = [5, 12, 8, 130, 44];
//هذه الدالة للبحث عن قيمة معينة
//console.log(numbers.includes(44));
//هذه الدالة للبحث عن رقم خانة العنصر 
//console.log(numbers.indexOf(8))
//هذه الدالة للبحث عن أول عنصر يحقق الشرط المحدد
//let result = numbers.find(function(number){
//    return number >1;
//});
//console.log(result);
//هذه الدالة للبحث عن كافة العناصر التي تحقق شرطا معيناً
//let result = numbers.filter(function(number){
//    return number <100;
//});
//console.log(result);
//هذه الدالة للبحث عن رقم خانة أول عنصر يحقق الشرط المحدد
//let index = numbers.findIndex(function (number) {
//    return number> 12;
//});
//console.log(index)



// U.6 lesson 6: الدوال السهمية
// param =>{}
//let log = msg=> console.log(msg);
//log('alloooow');



// U.6 lesson 7: العبور على عناصر المصفوفة
//let langs = ['js', 'php', 'ruby'];
//langs.forEach(value => console.log(value));
//langs.forEach((value, index) => console.log(value, index));
// **



// U.6 lesson 8: ترتيب عناصر المصفوفات
//let jaq = ['basim', 'ahmad', 'calim'];  
//jaq.sort();
//console.log(jaq);
//لترتيب الارقام يفضل استخدام هذه الدالة مع هذه الدالة 
// let zaq  = [4, 1, 3, 2, 12, 3, 22, 32, 44,  36, 46];  
// zaq.sort((a, b)=> a-b );
// console.log(zaq);
// لترتيب الأرقام بشكل تنازلي 
// let zaq  = [4, 1, 3, 2, 12, 3, 22, 32, 44,  36, 46];  
// zaq.sort((a, b)=> b - a );
// console.log(zaq);



