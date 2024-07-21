/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/templates/**/*.jinja2", "./static/**/*.js"],
  theme: {},
  variants: {
    extend: {},
  },
  plugins: [require("tailgrids/plugin")],
};

