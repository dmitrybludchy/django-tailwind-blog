module.exports = {
  future: {
      removeDeprecatedGapUtilities: true,
      purgeLayersByDefault: true,
  },
  purge: {
      enabled: false, //true for production build
      content: [
          '../**/templates/*.html',
          '../**/templates/**/*.html'
      ]
  },
  theme: {
      extend: {},
      spacing: {
          '112': '28rem',
          '128': '32rem',
          '144': '36rem',
          '160': '40rem',
      }
  },
  variants: {},
  plugins: [],
}
