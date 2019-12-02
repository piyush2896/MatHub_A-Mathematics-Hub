/*
Author: Piyush Malhotra
Date modified: 11/17/2019
*/

function studentDataForm(){
    element = "<div class='row'><div class='form-group col-xs-5 col-xs-offset-4'>\
        <label for='grade'>Grade</label>\
        <select id='grade' class='form-control' name='grade'>";
    for(i = 1; i <= 12; i++){
        element += "<option value='"+ i + "'>" + i + "</option>";
    }
    element += "</select></div></div>";
    return element;
}

function parentDataForm(){
    element = "<div class='row'><div class='form-group col-xs-5 col-xs-offset-4'>\
        <label for='stud-id'>Student ID</label>\
        <input type='text' class='form-control' id='stud-id' name='stud-id' placeholder='Student ID'>";
    element += "</div></div>";
    return element;
}

function teacherDataForm(){
    element = "<div class='row'><div class='form-group col-xs-5 col-xs-offset-4'>\
        <label for='grade'>Grade</label>\
        <select id='grade' class='form-control' multiple>";
    for(i = 1; i <= 12; i++){
        element += "<option value='"+ i + "'>" + i + "</option>";
    }
    element += "</select></div></div>";
    return element;
}

$(document).ready(function(){

    function updateExtraData(data){
        $('#extra-details').html('');
        $('#extra-details').html(data);
    }

    $('#usertype').change(function(){
        var usertype = $('#usertype option:selected').text();
        if(usertype == 'Student'){
            updateExtraData(studentDataForm());
        }else if(usertype == 'Teacher'){
            updateExtraData(teacherDataForm());
        }else if(usertype == 'Parent'){
            updateExtraData(parentDataForm());
        }else{
            updateExtraData('');
        }
    });
});
