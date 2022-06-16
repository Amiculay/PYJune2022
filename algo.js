/*
Testing Array and changing size
 */

var numberArray = [4, 3, 2, 1, 0];
console.log(numberArray)
var arrLength = numberArray.length;

function shiftLeft(arr) {
    var temp = arr[0];
    for (var i = 0; i < arr.length - 1; i++) {
        arr[i] = arr[i+1];
    }
    arr[arr.length-1] = temp;
    console.log(arr)
}

function shiftRight(arr) {
    var temp = arr[arr.length - 1];
    for (var i = arr.length-1; i > 0; i--) {
        arr[i] = arr[i-1];
    }
    arr[0] = temp;
    console.log(arr)
}

function shiftRightBy(arr, byCount) {
    byCount = byCount % arr.length;
    if (byCount < 0) {
        byCount += arr.length;
    }

    for (var i = 0; i < byCount; i++) {
        var temp = arr[arr.length - 1];
        for (var j = arr.length-1; j > 0; j--) {
            arr[j] = arr[j-1];
        }
        arr[0] = temp;
    }
    console.log(arr)
}

shiftRightBy((numberArray), )

function addToFront(arr, value) {
    for(var i = 0; i < arr.length; i++) {
        arr[arr.Length - i] = arr[arr.Length - i - 1];
    }
    arr[0] = value;
    console.log(arr);
}

function addToFrontMultiple(arr, value) {
    for (var j = value.length; j > 0; j--) {
        for(var i = 0; i < arr.length; i++) {
            arr[arr.length - i] = arr[arr.length - i - 1];
        }
        arr[0] = value[j - 1];

    }
    console.log(arr);
}

function removeFront(arr) {
    for (var i = 0; i < arr.length - 1; i++) {
        arr[i] = arr[i+1];
    }
    arr.length--;
    console.log(arr);
}



function isRotation(s1, s2) {
    if (s1.length != s2.length) {
      return false;
    }
    var double = s1 + s1;
    for (let i = 0; i < double.length; i++) {
        if (double[i] === s2[0]) {
            for (let j = 1; j < s2.length; j++) {
                if (s2[j] == double[i + j]) {
                    continue;
                } else {
            return false;
            }
        }
        return true;
        }
    }
    return false;
}