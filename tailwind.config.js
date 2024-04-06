/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html", // Pfade zu HTML-Dateien im 'templates'-Verzeichnis
    "./static/admin/js/**/*.js", // Pfade zu JS-Dateien im 'static'-Verzeichnis
  ],
  theme: {
    extend: {
      colors: {
        "glass-white": "rgba(255, 255, 255, 0.04)",
        "glass-border": "rgba(255, 255, 255, 0.21)",
      },
      boxShadow: {
        glass: "0 4px 30px rgba(0, 0, 0, 0.1)",
      },
      backdropFilter: {
        blur: "blur(3.9px)",
      },
      borderRadius: {
        glass: "16px",
      },
      borderWidth: {
        glass: "1px",
      },
      backdropFilter: ["hover", "focus"], // aktiviert backdrop-filter Klassen
    },
  },
  variants: {},
  plugins: [],
};

