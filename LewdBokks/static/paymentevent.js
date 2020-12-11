var lootboxtype = null
$('#payment-modal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget) // Button that triggered the modal
    lootboxtype = button.data('whatever') // Extract info from data-* attributes
    console.log(lootboxtype)
    $("#hiddenval").val(lootboxtype)
  })

$('#payment-modal-mp').on('show.bs.modal', function (event) {
var button = $(event.relatedTarget) // Button that triggered the modal
lootboxtype = button.data('whatever') // Extract info from data-* attributes
console.log(lootboxtype)
$("#hiddenval-mp").val(lootboxtype)
})



  // function checkph(texy){
  //     var phoneNumber = $(texy).val()
  //       if(/^\d+$/.test(phoneNumber) && phoneNumber.length == 8){
  //           console.log(lootboxtype)
  //           var val = null;
  //           console.log(val)
  //           $('#payment-modal-mp').modal('hide'); 
  //       }
  //   console.log($(texy).val().length)
  // }

  // function checkcard(number, holder, month, year, security){
  //     var cardNumber = $(number).val()
  //     var cNumberReal = false

  //     var holderName = $(holder).val()
  //     var hNameReal = false

  //     var monthEnd = $(month).val()
  //     var monthReal = false 

  //     var yearEnd = $(year).val()
  //     var yearReal = false

  //     var security = $(security).val()
  //     var sNumberReal = false

  //     if(cardNumber.length == 16 && /^\d+$/.test(cardNumber)){
  //       cNumberReal = true

  //     }

  //     if(holderName.length !== 0){
  //       hNameReal = true
  //     }

  //     if(/^\d+$/.test(monthEnd)){
  //       monthReal = true
  //     }

  //     if(/^\d+$/.test(yearEnd)){
  //       yearReal = true
  //     }

  //     if(/^\d+$/.test(sNumberReal) && sNumberReal.length == 3){
  //       cNumberReal = true
  //     }

  //     //check if all the information is correct
  //     if(cNumberReal && hNameReal && monthReal && yearReal && cNumberReal){
  //         console.log(lootboxtype)
  //         $('#payment-modal').modal('hide'); 
  //     }
  // }

