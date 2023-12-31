$('#agent-form').submit(e=>{
    e.preventDefault();
    // upload method
    makecall();
    // console.log(e.target)
})

// upload method
let makecall = async()=>{
    let formdata = $('#agent-form').serializeArray().reduce(
        (obj, item)=>(obj[item.name]=item.value, obj), {}
    );
    let imagedata = $('#image')[0].files[0];
    // initiailize Form
    let imagefile = new FormData()
    if(imagedata){
        imagefile.append('file', imagedata);
    }
    // end initialize

    // post to API
    if(formdata){
        let res = await $.ajax({
            url: '/api/resource/Agent',
            type: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-Frappe-CSRF-Token': frappe.csrf_token
            },
            data: JSON.stringify(formdata),
            success: function(data){
                return data
            },
            error: function(data){
                return data
            }
        })
        console.log(res);
        // upload images
        if(res.data && imagedata){
            let imgres = await fetch('/api/method/upload_file',{
                headers: {
                    'X-Frappe-CSRF-Token': frappe.csrf_token
                },
                method: 'POST',
                body: imagefile
            })
            .then(res=>res.json())
            .then(data=>{
                console.log(data)
                // finally update
                if(data.message){
                    // update agent
                    $.ajax({
                        url: `/api/resource/Agent/${res.data.name}`,
                        type: 'PUT',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-Frappe-CSRF-Token': frappe.csrf_token
                        },
                        data: JSON.stringify({image:data.message.file_url}),
                        success: function(data){
                            return data
                        },
                        error: function(data){
                            return data
                        }
                    })


                    // end update agent
                }
            })
        }
    }
}


// let imagefile = new FormData();
// imagefile.append('file_url', 
// 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSf6Hz7XHH7iFjxIxYBMBeiB73Y5XgG9SXrnw&usqp=CAU');
// // APPENDS AS AN ATTACHEMENT
// imagefile.append('doctype', 'Agent')
// imagefile.append('docname', 'AG-PR-23-10-0037');

// fetch('/api/method/upload_file', {
//     headers: {
//         'X-Frappe-CSRF-Token': frappe.csrf_token
//     },
//     method: 'POST',
//     body: imagefile
// })
// .then(res=>res.json())