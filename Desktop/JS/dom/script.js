let count=0;
let display = document.getElementById("display");
display.innerHTML=count;

const incCount = () => {
    count++;
    display.innerHTML=count;
};

const decCount = () => {
    if (count>0){
        count--;
    }
    display.innerHTML=count;
};