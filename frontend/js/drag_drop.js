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

  cardspace = new CardSpace

  for (i=0; i < 10; i++){
    card = new Card(i);
    $("#cardPile").append(card.element)
    cardspace.array.push(i)
  }

  $(".number").draggable({
    helper: "clone",
  });

  
  $( "#cardSlots" ).droppable({
    drop: function( event, ui ) {

      var value_num = $(ui.draggable).text();
      card_slot = cardspace.array[value_num]
      // console.log(card_slot)
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