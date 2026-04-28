
function start() {
  var a = [1,2,3,4,5]
  outputArray("Original array: ", a , document.getElementById("originalArray"))
  modifyArray(a)
  outputArray("modified array: ", a, document.getElementById("modifiedArray"))
  document.getElementById("originalElement").innerHTML = "a[3] after element has been modified " + a[3]
}

function outputArray(heading,theArray,output){
  output.innerHTML = heading + theArray.join(" ")
}

function modifyArray(theArray){
  for (var j in theArray){
    theArray[j] *= 2
  }
}

function modifyElement(e){
  e *=2
  document.getElementById("inModifyElement").innerHTML = "Value in modifyElement: " + e
}

window.addEventListener("load",start,false)