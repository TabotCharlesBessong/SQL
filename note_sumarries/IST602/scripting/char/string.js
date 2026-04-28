
const start = () => {
  var s = "ZEBRA";
  var s2 = "AbCdEfG";
  var result = "";
  result = "<p>Character at index 0 in '" + s + "' is " +
  s.charAt(0) + "</p>";
  result += "<p>Character code at index 0 in '" + s + "' is " +
  s.charCodeAt(0) + "</p>";
  result += "<p>'" + String.fromCharCode(87, 79, 82, 68) +
  "' contains character codes 87, 79, 82 and 68</p>";
  result += "<p>'" + s2 + "' in lowercase is '" +
  s2.toLowerCase() + "'</p>";
  result += "<p>'" + s2 + "' in uppercase is '" +
  s2.toUpperCase() + "'</p>";
  document.getElementById("results").innerHTML = result;

}

window.addEventListener("load",start,false)