// Step 1: Enable next button when email is entered
document.getElementById('email').addEventListener('input', function () {
    var email = document.getElementById('email').value;
    var nextButton = document.getElementById('nextButton');
    if (email) {
      nextButton.classList.add('enabled');
    } else {
      nextButton.classList.remove('enabled');
    }
  });
  
  // Go to Step 2
  function goToNextStep() {
    document.getElementById('step1').style.display = 'none';
    document.getElementById('step2').style.display = 'block';
  }
  
  // Step 2: Enable next button when all fields are filled
  document.querySelectorAll('#firstName, #lastName, #dob').forEach(function(input) {
    input.addEventListener('input', function() {
      var firstName = document.getElementById('firstName').value;
      var lastName = document.getElementById('lastName').value;
      var dob = document.getElementById('dob').value;
      var nextButtonStep2 = document.getElementById('nextButtonStep2');
      if (firstName && lastName && dob) {
        nextButtonStep2.classList.add('enabled');
      } else {
        nextButtonStep2.classList.remove('enabled');
      }
    });
  });
  
  // Go to Step 3
  function goToPasswordStep() {
    document.getElementById('step2').style.display = 'none';
    document.getElementById('step3').style.display = 'block';
  }
  
  document.querySelectorAll('#password, #confirmPassword').forEach(function(input) {
    input.addEventListener('input', function() {
      // Şifre ve onay şifresi değerlerini alıyoruz
      var password = document.getElementById('password').value;
      var confirmPassword = document.getElementById('confirmPassword').value;
  
      // Şifreler eşleşiyorsa butonu aktif hale getirme işlemi
      var createAccountButton = document.getElementById('createAccountButton');
      if (password && confirmPassword) {
        if (password === confirmPassword) {
          createAccountButton.classList.add('enabled');
        } else {
          createAccountButton.classList.remove('enabled');
        }
      } else {
        createAccountButton.classList.remove('enabled');
      }
    });
  });
  
  // Butona tıklandığında şifre kontrolü yapılacak
  function checkPasswordsMatch() {
    var password = document.getElementById('password').value;
    var confirmPassword = document.getElementById('confirmPassword').value;
  
    if (password === confirmPassword) {
      // Şifreler eşleşirse bir sonraki sayfaya yönlendir
      goToHomePage();
    } else {
      // Şifreler eşleşmezse uyarı ver
      alert("Passwords do not match! Please try again.");
  
      // Şifreleri temizle ve tekrar girmesini iste
      document.getElementById('password').value = '';
      document.getElementById('confirmPassword').value = '';
    }
  }
  
  function goToHomePage() {
    alert("Account created successfully!");
    // Ana sayfaya yönlendir
    window.location.href = '../main_page/main_page.html';
  }
  
