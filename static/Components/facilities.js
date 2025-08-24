(function(){
  const video = document.querySelector('#campus-facilities .cf-video');
  if(!video) return;

  const id = video.getAttribute('data-video-id');
  const thumb = `https://img.youtube.com/vi/${id}/maxresdefault.jpg`;
  video.style.backgroundImage = `url(${thumb})`;

  const playBtn = video.querySelector('.cf-play');
  playBtn.addEventListener('click', function(){
    const iframe = document.createElement('iframe');
    iframe.src = `https://www.youtube.com/embed/${id}?autoplay=1&rel=0&modestbranding=1`;
    iframe.allow = 'autoplay; fullscreen';
    iframe.frameBorder = '0';
    iframe.style.width = '100%';
    iframe.style.height = '100%';
    iframe.style.position = 'absolute';
    iframe.style.top = '0';
    iframe.style.left = '0';

    video.innerHTML = '';
    video.appendChild(iframe);
  });
})();
