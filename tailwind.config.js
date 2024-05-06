/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./portfolio/templates/**/*.html", "./portfolio/templates/**/*.jinja2", "./portfolio/static/**/*.js"],
  theme: {},
  variants: {
    extend: {},
  },
  plugins: [require("tailgrids/plugin")],
};
