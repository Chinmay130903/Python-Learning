const item=document.querySelectorAll('.item')
item.forEach(element => {
    element.style.fontSize="25px"
});
item[0].classList.add('active')
const box=document.querySelectorAll('.box')
box[2].classList.add('hide')

box.forEach((element,index)=>{
if(index==0) element[index].style.color="red"
if(index==1) element[index].style.color="green"

if(index==2) element[index].style.color="blue"

})