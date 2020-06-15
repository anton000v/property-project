module.exports = {
  theme: {
    extend: {
      height: theme => ({
        "screen/2": "50vh",
        "screen/3": "calc(100vh / 3)",
        "screen/4": "calc(100vh / 4)",
        "screen/5": "calc(100vh / 5)",
      }),
      backgroundColor: theme => ({
        "myPageBackground" : "#f8f8f8",
        "myFirstDark" : "#3c3838",
        "mySecondDark" : "#846667",
        "myFirstLight" : "#ff9b9d",
        "mySecondLight" : "#cbcbcb",
      }),
      textColor:{
        "myPageBackground": "#f8f8f8",
        "myFirstDark" : "#3c3838",
        "mySecondDark" : "#846667",
        "myFirstLight" : "#ff9b9d",
        "mySecondLight" : "#cbcbcb",
      }
    },
  },
  variants: {},
  plugins: [],
}
