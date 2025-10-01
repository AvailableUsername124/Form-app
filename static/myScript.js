$(document).ready(function() {
$('#btn btn-primary mt-3').on('click', function() {
    const $selectedRadio = $('input[name="form-check-input"]:checked');
    if ($selectedRadio.length > 0) {
    if ($selectedRadio.parent('label').hasClass('correct')) {
$('#result1').text('Correct!');
   $('#result1').css({"margin-left": "45%" , "color": "SpringGreen"});
        alert("Correct!");
    }
else {
        $('#result1').text('Good Try');
$('#result1').css({"margin-left": "45%" , "color": "Crimson"});
        alert("Incorrect:/");
         }
        }
     });