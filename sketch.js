let result;

function preload() {
  result = loadStrings('assets/qiita.txt');
}
console.log("###");
function setup() { 
    createCanvas(800, 800);
    console.log(result);
    
    //Text("333")l
  } 
  
  function draw() { 
    background(220);
    fill(100);
    rect(500, 300, 100, 100);
  }