/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html', // Pfade zu HTML-Dateien im 'templates'-Verzeichnis
    './static/admin/js/**/*.js',    // Pfade zu JS-Dateien im 'static'-Verzeichnis
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

