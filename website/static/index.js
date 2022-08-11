// This method will POST on the /delete-note route
function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    // This is how we reload the page (window.location.href = "/")
    window.location.href = "/";
  });
}
