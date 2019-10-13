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
    else if(operator==='=')
      console.log("equals");
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

  opcardspace.array = ['+','-','x','/','=']
  // cardspace.array = [0,1,2,3,4,5,6,7,8,9,'+','-','*','/']

  for(i=0; i<10; i++){
    card = new Card(cardspace.array[i])
    $("#cardPile").append(card.element)
  }

  for(i=0; i<5; i++){
    card = new OpCard(opcardspace.array[i])
    $("#cardPile").append(card.element)
    // console.log("inside");
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

    var tokens=[];



    var value_num = $(ui.draggable).text();
    card_slot = cardspace.array[value_num]
	  cardspace.array_member.push(value_num)

	  var value_op = $(ui.draggable).text();
	  // console.log(value_op);
	  //card_slot = opcardspace.array[value_op]
	  card_slot=value_op;
	  // console.log(card_slot);
	  opcardspace.array_member.push(value_op)
	  $("#cardSlots").append("<div class='operator'>" + card_slot + "</div>")

	  // console.log(card_slot)
      var number_array_members = cardspace.array_member.length
      // console.log(number_array_members)
      console.log(cardspace.array_member)
     /* if ( number_array_members <= 10 ) {
        $("#cardSlots").append("<div class='number'>" + card_slot + "</div>")

		/* To add and display in result column
        value_sum = value_sum + card_slot
        $("#total_sum").text(value_sum)
      } */
	  
	  counter=0;
	  var j=0;
	  var k=0;
	  var term1 = [];
	  var term2 = [];
	  var opr;
		
		for(i=0; i<number_array_members; i++)
		{
			counter=counter+1;
			if(cardspace.array_member[i] != "+" && cardspace.array_member[i] != "-" && cardspace.array_member[i] != "x" && cardspace.array_member[i] != "/")
			{
				term1[j]=cardspace.array_member[i];
				j=j+1;
			}
			else
			{
				opr=cardspace.array_member[i];
				break;
			}
			
		}
		
		
		for(i=counter;i<number_array_members;i++)
		{
			if(cardspace.array_member[i]!= "=")
			{
				term2[k]=cardspace.array_member[i];
				k=k+1;
			}
		}
		
		console.log('Opr', opr);
		console.log('T1', term1);
		console.log('T2', term2);
		
      // op1=
      // op2=
      // opr=


    }
  });
});
