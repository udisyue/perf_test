var validateUsername = $('#validateUsername');
$(document).ready(function(){
    $('#test').click(function () {
        //alert('test');
        var t = this;
        if (this.value != this.lastValue && this.value != '') {
            if (this.timer) clearTimeout(this.timer);
             
             //show checking status
            validateUsername.html(
                '检查昵称是否存在...'
            );
            
            //this.timer = setTimeout(function () {
                $.ajax({
                    url: './AjaxSample',
                    data: 'action=check_nickname&value=' + t.value,
                    type: 'post',
                    success: function (j) {
                        $('#validateUsername').html(j);
                        //validateUsername.html(j);
                    }
                });
            
            //}, 10);
            //end timer
            //this.lastValue = this.value;
        }
    
    });
});