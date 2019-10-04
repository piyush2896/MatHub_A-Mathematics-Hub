function call_function()
{
    op1 = document.getElementById("a");
    opr = document.getElementById("op");
    op2 = document.getElementById("b");
    var data = JSON.stringify({"operand1": op1.valueAsNumber, "operand2": op2.valueAsNumber, "operator": opr.value});


      console.log(data);


    var xhr = new XMLHttpRequest();
    var url = "http://localhost:5000/eval";
    // var url = "http://192.168.43.212:5000/eval"
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");

    var json = '';
    xhr.onreadystatechange = function ()
    {
        if (xhr.readyState === 4 && xhr.status === 200)
        {
            json = JSON.parse(xhr.responseText);
            console.log('in onreadystatechange')
            console.log(json)
            document.getElementById('result_display').value = json.result

            add_row(json.result);
            reset();
        }
    };

    if(opr=='x'||opr=='X')
    {
      opr='*';
    }

    xhr.send(data);
}

function add_row(result){
    div = $('#results');
    old_html = div.html();

    new_html = '<div class="row"><div class="col-xs-offset-2 col-xs-2 text-center bbox">' + $('#a').val();
    new_html += '</div><div class="col-xs-1 text-center bbox">' + $('#op').val() + '</div>';
    new_html += '<div class="col-xs-2 text-center bbox">' + $('#b').val() + '</div>';
    new_html += '<div class="col-xs-1 text-center bbox"> = </div>';
    new_html += '<div class="col-xs-2 text-center bbox">' + result + '</div></div>';

    div.html(old_html + new_html)
}

function reset(){
  $('#a').val('');
  $('#b').val('');
  $('#op').val('');
  $('#result_display').val('');
}

// var answer = JSON.parse(json);
// document.getElementById("result_display").innerHTML= answer;
