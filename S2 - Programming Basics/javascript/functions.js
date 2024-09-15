// U.5 lesson 2:
//function hello (){
//    const name = 'hsoub';
//    console.log('hello '+ name);
// }
// دالة لتصفية العناصر الرقمية من المصفوفة
// function filterArray(){
//    const array = ['ahmed', 6569878, 'ali', 'yara', 'sharlok', 45];
//    for (let item of array ){
//        if (typeof item ==='number'){
//            console.log(item);
//        }
//    }
// }
// filterArray()


// U.5 lesson 3: parameter المعاملات
//دايناميكي
//function sum(x , y){
//    console.log(x + y);
//}
//دالة لتصفية العناصر من أي مصفوفة سواء كان من نوع نصوص أو أرقام حسب ما يطلب منه 
//function filterarray(array,type){
//    for (let item of array ){
//        if (typeof item === type ){
//            console.log(item);
//        }
//    }
//}


// U.5 lesson 4: Defult parameters المعاملات الافتراضية
//نقدر نخليه يرجع قيمة 
// function sum (s, y=1){
//    return s + y;
// }
// let result= sum (6);
// console.log(result);


// U.5 lesson 5: Argumetns القيم أو الوسائط
//يستخدم داخل الدالة ويعبر عن المعاملات التي تم تمريرها لها
// function sum(x,y){
//    console.log(arguments);
//    return x + y;
// }
// const result = sum (2,3,4,5,6);
// console.log(result);
//استغلال هذه الخاصية زي ما تشوف
// function sum(x,y){
//    let total =0;
//    for (let num of arguments)
//        total += num;
//    return total;
// }
// const result = sum (2,356,4,55,5,6);
// console.log(result);


// U.5 lesson 6: rest المعامل
// function sum(...args){
//     let total = 0; 
//     for (let num of args) total += num;
//     return total;
// } 
// const result = sum(2, 3, 5, 10, 33)
// console.log(result);
// يمكننا استخدام معاملات اخرى بجانبه rest عند استخدام المعامل 
// function sum(multiply, ...args){
//     let total = 0; 
//     for (let num of args) total += num;
//     return multiply * total;
// } 
// const result = sum(2, 3, 5, 10, 33)
// console.log(result);


// U.5 lesson 8: Global scopes and Local scopes المجالات العامة والمجالات الخاصة 
// وهي سهلة . عن الاقواس المجعدة وهذي انا اعرفها


// U.5 lesson 9: Declaration and Expressions التصريح والتعبير 
// Declaration
// start()
// function start(){
//     console.log('started');
// }
// Expression
// let stop = function(){
//     console.log('stopped');
// }


// U.5 lesson 11: تمرين :الأعداد الأولية
// function isPrime(num){  // هذه الدالة تتحقق من أن العدد المدخل أولي أم لا
//     for (let i =2 ; i < num ; i++ ){
//         if (num % i === 0  ) return false;
//     }
//     return num > 1 ;
// }
// function primes(max){
//     for(let i = 2 ; i<max ; i++)
//         if (isPrime(i)) console.log(i);
// }
// let num = prompt('please enter number to check');
// primes(num);



// U.5 lesson 12: Recursion التعاود
//يشبه حلقات التكرار 
// لعدد ما Factorial أشهر مثال على استخدامه في لغات البرمجة عمومًا هو حساب العاملي
// function factorial(n){
//     return n===0 ? 1 : n * factorial(n-1);
// }
// راجع المقال وابحث عنه




//filterarray(['laila',65,'fahad',88],'number')
//sum(2,3)
//filterArray()
//hello(); 



