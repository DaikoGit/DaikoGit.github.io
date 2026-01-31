// android/service-worker.js
self.addEventListener('install', event => {
  console.log('Service Worker installing...');
  self.skipWaiting(); // Activate immediately
});

self.addEventListener('activate', event => {
  console.log('Service Worker activated');
});

self.addEventListener('fetch', event => {
  // Optional: basic offline cache
  event.respondWith(
    fetch(event.request).catch(() => caches.match(event.request))
  );
});
