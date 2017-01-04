$("select[name$='-time_start']").change(function() {
    var from = parseFloat($(this).val());
    var thisName = $(this).attr("id");
    var num = thisName.slice(thisName.indexOf("-") + 1, thisName.indexOf("time") - 1);
    var time = parseFloat($("select[name$='" + num + "-time']").val());
    var end = from + time;
    $("select[name$='" + num + "-time_end']").val(end);
    changeStartTime(num, end);
});


$("select[name$='-time']").change(function() {
    var time = parseFloat($(this).val());
    var thisName = $(this).attr("id");
    var num = thisName.slice(thisName.indexOf("-") + 1, thisName.indexOf("time") - 1);
    var from = parseFloat($("select[name$='" + num + "-time_start']").val());
    var end = from + time;
    $("select[name$='" + num + "-time_end']").val(end);
    changeStartTime(num, end);
});


// check if the end time is not ahead of the next task
// if the end time is ahead of the next one, change start time and end time of the next ones
// until there is no problem.
function changeStartTime(num , end) {
    num = parseFloat(num);
    end = parseFloat(end);
    while(num <= 10) {
        num += 1;
        var start = parseFloat($("select[name$='" + num + "-time_start']").val());
        if(start != 'NaN' && end > start) {
            var time = parseFloat($("select[name$='" + num + "-time']").val());
            $("select[name$='" + num + "-time_start']").val(end);
            end += time;
            $("select[name$='" + num + "-time_end']").val(end);
        } else {
            break;
        }
    }
}