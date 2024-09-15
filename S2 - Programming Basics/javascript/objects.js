
// U.7 lesson 2:
// let object = {    //هذا هو الشكل العام للكائن 
//    name: 'ali',  //هكذا يتم تعريف خواص الكائن
//    level: 8,
//    functionName: function(parameters){   // هكذا يتم تعريف توابع الكائنات
//        //code to be executed
//    }
// }

//let student  = {
//    name: 'ali',
//    age: 12,
//    level: 8,
//}
//
//console.log(student);
//student.age = 15;

//Dot Notation
//console.log(student.age)

//Bracket Notation
//const attribute = 'name';
//console.log(student[attribute]);


// U.7 lesson 3: التوابع في الكائنات
//let student = {
//    name: 'ahmad',
//    age: 12,
//    level:6,
//    hello: function(){
//        console.log(this.name + ' '+this.age)
//    },
//    pass: function(){
//        this.age++;
//        this.level++;
//    }
//};
//student.hello();
//student.pass();
//student.hello()


// U.7 lesson 4: constructor التابع الباني
//function Student(name, age, level){
//    this.name = name;
//    this.age = age;
//    this.level= level;
//    this.hello=function(){
//        console.log(this.name + ', '+ this.age);

//    }
//    this.pass = function(){
//        this.age++;
//        this.level++;

//    }
//}
//let student = new Student('Ahmad' , 12, 6);
//student.hello();
//let student2 = new Student('Muhmmad', 11,5);
//student2.hello()
//student2.pass()
//student2.hello()
//ويمكن إنشاء مصفوفة من الكائنات بهذه الطريقة
//let students = [
//    new Student('umar',45,4),
//    new Student('Ahmad' , 12, 6),
//    new Student('ali' , 15, 5)
//]
//console.log(students);


// U.8 lesson 1: Date كائن التاريخ
//let myDate = new Date(1996, 2, 14, 4, 45, 21);
//console.log(myDate)
//let dob = new Date('1996-03-15 3:32:36');
//let dob2 = new Date('1996-03-15 3:32:37');
//console.log(dob)
//console.log(dob.getFullYear());
//console.log(dob.getMonth());
//console.log(dob.getDate());
//console.log(dob.getHours());
//unix timestamp
//console.log(dob.getTime());
//if (dob.getTime()===dob2.getTime()){
//    console.log('equal');
//}else{
//    console.log('not equal');
//}



// U.8 lesson 2: Regualr Expression التعابير النظامية
//const msg = 'hello there ! My name is huzaifa and my age is 19';
//const regex= /age is ([0-9]+)/;

//const isMached = regex.exec(msg);
//console.log(isMached);
// أحتاج مراجعة الدرس


// U.9 lesson 3: try...catch
// Runtime errors.
// try {
//     // Codes may produce errors.
//     console.log('Start of try.');
//     unknownCode;
//     console.log('End of try.')
// } catch (error) {
//     // Handle errors.
//     console.log('Oops! there is on error', error);
// } finally {
//     // Do something after try and catch.
//     console.log('Reached the finally statement.');
// }
// throw رمي خطأ باستخدام
// function sum(num1, num2){
//     if (typeof num1 !== 'number') throw new Error('The first parameter must be a number');
//     if (typeof num2 !== 'number') throw new Error('The second parameter must be a number');
//     return num1 + num2;
// }
// try {
//     // Codes may produce errors.
//     console.log(sum(1,'3'));
// } catch (error) {
//     // Handle errors.
//     console.log('Oops! there is on error', error);
// }