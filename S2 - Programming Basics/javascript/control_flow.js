
// U.4 lesson 2: if else
// let age = 16;
// if (age >14){
//     console.log('العمر أكبر من 14');
// } else {
//     if (age > 10){
//         console.log('age is above 10')
//     } else {
//         console.log('age is under or qual to 10')
//     }
// }
// متتالية فقط حسب الحاجة if حسب الحاجة أو  else if نستطيع استخدام الشروط المتداخلة أو 
// let mark = 40;
// let repeat = 1;
// if (mark >= 80)
//     console.log('very good')
// else if (mark >= 60)
//     console.log('good')
// else if (mark >= 50)
//     console.log('acceptable')
// else{
//     console.log('failed')
//     if (repeat > 0) console.log('sorry, you cannot repeat.')
// }


// U.4 lesson 3: ternary operator
// هذا العامل طريقة مختصرة لكتابة الجمل الشرطية
// يتكون من 3أقسام وهو المعامل الوحيد الذي يتكون من 3أقسام 
// condition ? positive : negative
// let mrk = 60;
// let result = mrk > 50 ? 'Passed' : 'Failed';
// console.log(result)
// ويمكن استخدامها بشكل متداخل أيضا
// let m = 90;
// let ag = 18;
// let status = ag >= 16 ? (m >= 50 ? 'Accepted' : 'Failed') : 'Decliend';
// console.log(status);


// U.4 lesson 4: switch
// let day = 5;
// switch(day){
//     case 0: 
//         console.log('Sunday');
//     break;
//     case 1: 
//         console.log('Monday');
//     break;
//     case 2:
//         console.log('Tuesday');
//     break;
//     case 3:
//         console.log('Wednesday');
//     break;
//     case 4:
//         console.log('Thursday');
//     break;
//     case 5:
//         console.log('Friday');
//     break; 
//     case 6:
//         console.log('Saturday');
//     break;
//     default:
//         console.log('Invalid day!');
// }
// if (day ===0) console.log('Sunday');
// else if (day ===1) console.log('monday');
// else if (day ===2) console.log('tuesday');
// else if (day ===3) console.log('wednesday');
// else if (day ===4) console.log('thursday');
// else if (day ===5) console.log('friday');
// else if (day ===6) console.log('saturday');
// else console.log('invalid day!');
// يستخدم حسب الحاجة وحسب المبرمج وذوقه


// U.4 lesson 5: for loop
//طباعة اعداد زوجية
//نقدر نغير حسب اللي نبيه
// for (let i= 0; i<= 10 ; i++) {
//     if (i % 2 === 0 ) console.log(i);
// }
//طباعة جدول الضرب لعدد معين 
//  let number = 4 ;
//  for (let i = 1 ; i<=10 ; i++)
//     console.log(number * i);
// طباعة ارقام عدة مرات بالحلقات المتداخلة
// for (let i=1 ; i<=2 ; i++){
//     for (let j = 1 ; j<=3 ; j++){
//         console.log(j);
//     }
// }
// للتمرين على الحلقات رح لموقع هرمش فيه تمارين واجد على الحلقات


// U.4 lesson 6: while loop
// لطباعة الأعداد الزوجية
// let i = 1;
// while (i<= 10){
//     if (i %2 === 0) console.log(i);
//     i++
// }
// لطباعة جدول الضرب لعدد معين
// let number = 4;
// let i =1;
// while(i<=10){
//     console.log(i*number);
//     i++;
// }


// U.4 lesson 7: do while loop
// let i = 1;
// do {
//     if (i % 2 === 0) console.log(i);
//         i++;
// } while (i <= 10);


// U.4 lesson 8: العبور على عناصر المصفوفات
// مع عناصر المصفوفة .length لطباعة أرقام خانات المصفوفة نستخدم هذه الدالة
// for طباعة عناصر المصفوفة مع ارقام الخانات باستخدام
// const names = ['ahmed', 'ibrahim', 'abdullah', 'omar']
// for (let i = 0; i<names.length; i++){
//     console.log(i, names[i]);
// }
// while باستخدام
// let x = 0;
// while (x < names.length){
//     console.log(x, names[x]);
//     x++;
// }
// for عرض عناصر المصفوفة بشكل معكوس باستخدام حلقة التكرار 
//let asma = [ 'ahmed','ali','nur','khalid'];
//for (let i =asma.length-1; i>=0 ; i--){
//    console.log(i, asma[i]);
//}
// while نفس الشي باستخدام 
//let x=asma.length-1;
//while(x>=0){
//    console.log(x, asma[x]);
//    x--;
//}


// انواع العبور على المصفوفات 
//كلهن نفس الشغل اللهم أن الأول تمر على العناصر والثاني تمر على القيم
// U.4 lesson 9: Crossing loop : for ... in
//const numbers = [10, 4, 21, 35, 99];
//for (let index in numbers){
//    console.log(index, numbers[index]);
//}


// U.4 lesson 10: crossing loop : for ... of العبور على الخاصيات
//const number = [10, 4, 21, 35, 99];
//for (let value of number){
//    console.log(value);
//}


// U.4 lesson 11: break...continue
// ذولا عشن توقف وتتابع وتستفيد منهن بس مدري ليه
// let i=0;
// while(i<10){
//     i++;
// //    if(i===3) break;
//     if(i % 2!==0) continue;
//     console.log(i);
// }


// U.4 lesson 12: تمرين جمع عناصر المصفوفة
// let cart = [10, 654, 654, 212, 1, 1, 12, 321];
// let total =0;
// for (let item of cart){
//     total+= item;
// }
// console.log(total);


// U.4 lesson 13: تمرين استخراج العناصر النصية من المصفوفة
// const name = ['huzaifa', 18, true, 'ali', 12, false, 'khalid', 23];
// for(let i=0; i<name.length; i++){
//     if (typeof name[i]==='string')console.log(name[i]);
// }


// U.4 lesson 14: تمرين طباعة النجوم
// let you = prompt('دخّل عدد الأسطر اللي تبيه :');
// for (let yous = 1 ; yous <= you ; yous++){
//     let stars = ' ';
//     for(let i=1 ; i <= yous ; i++){
//         stars += '*'   
//     }
//     console.log(stars);
// }

