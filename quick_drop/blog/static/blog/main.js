$("#pop").on("click", function() {
   // here asign the image to the modal when the user click the enlarge link
   $('#imagepreview').attr('src', $('#imageresource').attr('src'));
   
   // imagemodal is the id attribute assigned to the bootstrap modal, then i use the show function
   $('#imagemodal').modal('show');
});