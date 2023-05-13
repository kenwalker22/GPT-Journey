function calculateAffordability() {
    // Get input values
    var loanPurpose = document.getElementById('loanPurpose').checked;
    var firstTimeHomeOwner = document.getElementById('firstTimeHomeOwner').checked;
    var jointMortgage = document.getElementById('jointMortgage').checked;
    var grossIncome = parseFloat(document.getElementById('grossIncome').value);
    var partnerGrossIncome = parseFloat(document.getElementById('partnerGrossIncome').value);
    var age = parseInt(document.getElementById('age').value);
    var partnerAge = parseInt(document.getElementById('partnerAge').value);
    
    // Calculate affordability logic
    var affordability = ''; // Add your logic here to calculate the affordability
    
    // Display the result
   
  