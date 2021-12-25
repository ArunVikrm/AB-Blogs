var likebtn = document.getElementById('process-like')

likebtn.addEventListener('click',function(){
    var blog_id = this.dataset.blog
    processLikeAction(blog_id)
})

function processLikeAction(blog_id){
    var url = '/like/'
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken' : csrftoken,   
        },
        body:JSON.stringify({'blog_id':blog_id})
    })
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log('data:',data)
        location.reload()
    })
}
