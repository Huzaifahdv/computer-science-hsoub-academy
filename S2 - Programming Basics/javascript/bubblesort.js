// U.11:
// function bubbleSort(array){
//     let swapped;
//     do {
//         swapped = false;
//         for (let i=0; i<array.length; i++ ){
//             if (array[i]>array[i+1]){
//                 let tmp = array[i];
//                 array[i]= array[i+1];
//                 array[i+1]= tmp;
//                 swapped = true;
//             }
//         }
//     }while(swapped)
//     return array;
// }

// let sor = bubbleSort([6,5,3,4,2,1]);
// console.log(sor);


let num =[21,32,2,4,13,45,564,53];
num.sort((a, b)=> a-b);
console.log(num);