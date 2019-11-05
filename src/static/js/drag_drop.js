$(document).ready(function () {

  var value_sum = 0
  var op1, op2, opr;

  var Card = function (number) {
    this.element = "<div class='number'>" + number + "</div>"
  }

  var CardSpace = function () {
    this.array = []
    this.array_member = []
    this.total = 0
  }

  var OpCard = function (operator) {
    this.element = "<div class='operator'>" + operator + "</div>"
  }

  var OpCardSpace = function () {
    this.array = []
    this.array_member = []
  }

  opcardspace = new OpCardSpace

  cardspace = new CardSpace

  cardspace.array = ['.', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

  opcardspace.array = ['+', '-', 'x', '/', '^']

  for (i = 0; i < cardspace.array.length; i++) {
    card = new Card(cardspace.array[i])
    $("#cardPile").append(card.element)
  }

  for (i = 0; i < opcardspace.array.length; i++) {
    card = new OpCard(opcardspace.array[i])
    $("#cardPile").append(card.element)
  }

  console.log(cardspace.array);
  console.log(opcardspace.array);

  $(".number").draggable({
    helper: "clone",
  });

  $(".operator").draggable({
    helper: "clone",
  });

  $("#cardSlots").droppable({
    drop: function (event, ui) {

      var value_num = $(ui.draggable).text();
      card_slot = cardspace.array[value_num]
      cardspace.array_member.push(value_num)

      var value_op = $(ui.draggable).text();

      card_slot = value_op;
      opcardspace.array_member.push(value_op)
      $("#cardSlots").append("<div class='operator'>" + card_slot + "</div>")

      var number_array_members = cardspace.array_member.length
      console.log(cardspace.array_member)

      counter = 0;
      var j = 0;
      var k = 0;
      var term1 = [];
      var term2 = [];

      for (i = 0; i < number_array_members; i++) {
        counter = counter + 1;
        if (!opcardspace.array.includes(cardspace.array_member[i])) {
          term1[j] = cardspace.array_member[i];
          j = j + 1;
        }
        else {
          opr = cardspace.array_member[i];
          if(opr=='x'||opr=='X'){
            opr = '*';
          }
          console.log(opr);
          break;
        }

      }


      for (i = counter; i < number_array_members; i++) {
        if (cardspace.array_member[i] != "=") {
          term2[k] = cardspace.array_member[i];
          k = k + 1;
        }
      }

      op1 = term1.join("");
      op2 = term2.join("");

    }


  });

  $('#button1').click(function () {
    call_function(op1, op2, opr);
    add_last_cards(op1, op2, opr);
    clear_dropable();
    cardspace.array_member = [];
    opcardspace.array_member = [];
  });
});

function add_last_cards(op1, op2, opr) {
  prev_html = $('#lastCards').html();

  if(opr == '*'){
    opr = 'x';
  }

  new_html = '<div class="row"><div class="number">' + op1 + '</div>';
  new_html += '<div class="operator">' + opr + '</div>';
  new_html += '<div class="number">' + op2 + '</div>';

  new_html += '</div>';
  $('#lastCards').html(prev_html + new_html);
}

function clear_dropable() {
  $('#cardSlots').html("");
}


function call_function(op1, op2, opr) {
  var data = JSON.stringify({ "operand1": parseFloat(op1), "operand2": parseFloat(op2), "operator": opr });

  var xhr = new XMLHttpRequest();
  var url = "http://localhost:5000/eval";
  xhr.open("POST", url, true);
  xhr.setRequestHeader("Content-Type", "application/json");

  var json = '';
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      json = JSON.parse(xhr.responseText);
      console.log('in onreadystatechange')
      console.log(json)
      $('#total_sum').text(json.result);
    }
  };
  console.log(data);
  xhr.send(data);
}