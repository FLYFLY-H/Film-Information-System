function beforesubmit2(){
	        var key=document.getElementById("task2").value;
	        if(key == ""){
                alert("关键字不能为空");
            return false;
            }
	        // 通过jquery发送出去
        $.ajax({
            url: "/Task2",
            type: "POST",
            data: key,
            processData: false,  // 告诉jQuery不要去处理发送的数据
            contentType: false,   // 告诉jQuery不要去设置Content-Type请求头
            success:function (data) {           //成功回调
            document.open();
            document.write(data);  //根据python返回的模板更新当前页面
            document.close();
        }
    }).done(function(resp) {
        alert('success!');
    }).fail(function(err) {
        alert('fail!')
    });
        return true;
        }
