$(document).ready(function(){
    data = {
        'name': '',
        'grade': '',
        'questions': [],
    }
    $('#create-user-btn').click(function(){
        console.log('HERE')
        restful_call(
            'http://localhost:3000/create_assignment',
            data, 'POST', function(data){
                window.confirm('Assignment Created!');
            });
    });

    $('#add-btn').click(function(){
        if(data['name'] == ''){
            name = $('#name').val();
            grade = $('#grade').val();
            data['name'] = name
            data['grade'] = grade
        }
        question = $('#question').val();
        solution = $('#solution').val();

        innerHtml = $('#questions').html();
        $('#questions').html(innerHtml + questionSolution2Html(question, solution));

        questionNum = Object.keys(data['questions']).length + 1
        data['questions'].push({
            'number': questionNum,
            'question': question,
            'solution': solution
        })
    });
});

function questionSolution2Html(question, solution){
    questionHtml = '<div class="row"><div class="col-xs-6 col-xs-offset-3">' + question;
    questionHtml += '</div></div>';
    solutionHtml = '<div class="row"><div class="col-xs-6 col-xs-offset-3">' + solution;
    solutionHtml += '</div></div>';
    return questionHtml + solutionHtml
}