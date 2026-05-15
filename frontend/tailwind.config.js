/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        green: {
          light: '#e6f4ea',
          DEFAULT: '#2e7d32',
          dark: '#1b5e20',
          accent: '#4caf50'
        },
        dark: {
          base: '#ffffff',
          card: '#f9fafb',
          lighter: '#f3f4f6',
        },
        cream: '#ffffff',
      },
      fontFamily: {
        serif: ['"Plus Jakarta Sans"', 'sans-serif'],
        sans: ['"Plus Jakarta Sans"', 'sans-serif'],
      },
    },
  },
  plugins: [
    require("tailwindcss-animate"),
  ],
}
