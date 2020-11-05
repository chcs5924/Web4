const highlight = document.querySelector('.highlight');
const thumb = document.querySelector('.thumb');

highlight.addEventListener('click', function (e) {

if( e.target.className =='books') {
  thumb.src=e.target.src;
  thumb.classlist.add('fade');
  setTimeout(function() {
    thumb.classList.remove('fade');
  }, 500)

  bookss.forEach(function() {
    // if( thumb.classList.contains('active')) {
    // thumb.classList.remove('active');
    //}
    bookss.className = 'thumb';
  });

  e.target.classList.add('active');
}
});
