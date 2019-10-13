$ ( document ). ready(function() {

  var value_sum = 0

  var Card = function(number){
    this.element = "<div class='number'>" + number + "</div>"
  }

  var CardSpace = function(){
    this.array = []
    this.array_member = []
    this.total = 0
  }

  var OpCard = function(operator){
    this.element = "<div class='operator'>" + operator + "</div>"
    if(operator==='+')
      console.log("plus");
    else if(operator==='-')
      console.log("minus");
    else if(operator==='x')
      console.log("multi");
    else if(operator==='/')
      console.log("divide");
  }

  var OpCardSpace = function(){
    this.array = []
    this.array_member = []
  }

  opcardspace = new OpCardSpace

  cardspace = new CardSpace

  // for (i=0; i < 10; i++){
  //   card = new Card(i);
  //   $("#cardPile").append(card.element)
  //   cardspace.array.push(i)
  // }

  cardspace.array = [0,1,2,3,4,5,6,7,8,9]

  opcardspace.array = ['+','-','x','/']
  // cardspace.array = [0,1,2,3,4,5,6,7,8,9,'+','-','*','/']

  for(i=0; i<10; i++){
    card = new Card(cardspace.array[i])
    $("#cardPile").append(card.element)
  }

  for(i=0; i<4; i++){
    card = new OpCard(opcardspace.array[i])
    $("#cardPile").append(card.element)
    console.log("inside");
  }

  console.log(cardspace.array);
  console.log(opcardspace.array);

  $(".number").draggable({
    helper: "clone",
  });

  $(".operator").draggable({
    helper: "clone",
  });

  $( "#cardSlots" ).droppable({
    drop: function( event, ui ) {

      var value_num = $(ui.draggable).text();
      card_slot = cardspace.array[value_num]
      console.log(card_slot)
      cardspace.array_member.push(value_num)
      var number_array_members = cardspace.array_member.length
      console.log(number_array_members)
      if ( number_array_members <= 10 ) {
        $("#cardSlots").append("<div class='number'>" + card_slot + "</div>")
        // console.log(cardspace)
        value_sum = value_sum + card_slot
        // console.log(value_sum)
        $("#total_sum").text(value_sum)
      }
    }
  });
});
