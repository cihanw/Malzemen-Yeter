  // Get the "View All Categories" button and categories section
  const viewAllBtn = document.getElementById("view-all-btn");
  const categoriesSection = document.getElementById("categories-section");

  // Add click event listener to the button
  viewAllBtn.addEventListener("click", function() {
      // Toggle the 'expanded' class to show or hide the categories
      categoriesSection.classList.toggle("expanded");
  });

  document.getElementById("chicken-meatball").addEventListener("click", function() {
    window.location.href = "recipe_page_template.html";  // Buraya gitmek istediğiniz URL'yi yazın
});

