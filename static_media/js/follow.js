var followbts = document.getElementsByClassName('process-follow')

for (i=0;i<followbts.length;i++){
    followbts[i].addEventListener('click',function(){
        var profile_id = this.dataset.profile
        var action = this.dataset.action
        console.log(action)

        processFollowAction(profile_id,action)
    })
}

function processFollowAction(profile_id,action){
    var url = '/follow/'
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken' : csrftoken,   
        },
        body:JSON.stringify({'profile_id':profile_id,'action':action})
    })
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log('data:',data)
        location.reload()
    })
}