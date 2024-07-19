/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.html", "./src/static/**/*.js"],
  theme: {},
  variants: {
    extend: {},
  },
  plugins: [require("tailgrids/plugin")],
};

