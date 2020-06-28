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
        "myFirstDark" : "#34D2AF",
        "mySecondDark" : "#846667",
        "myFirstLight" : "#ff9b9d",
        "mySecondLight" : "#cbcbcb",
        "myHeaderColor": "#002d31",

        "myMint-100" : "#5ED2B8",
        "myMint-200": "#34D2AF",
        "myMint-300" : "#00A480",
        "myMint-400" : "#1F7B67",
        "myMint-500" : "#006B53",
      }),
      textColor:{
        "myPageBackground": "#f8f8f8",
        
        "myFirstDark" : "#3c3838",
        "mySecondDark" : "#846667",
        "myFirstLight" : "#ff9b9d",
        "mySecondLight" : "#cbcbcb",
        "myHeaderColor": "#002d31",
        "myMint-100" : "#5ED2B8",
        "myMint-200": "#34D2AF",
        "myMint-300" : "#00A480",
        "myMint-400" : "#1F7B67",
        "myMint-500" : "#006B53",
      },
      borderColor:{
        "myMint-100" : "#5ED2B8",
        "myMint-200": "#34D2AF",
        "myMint-300" : "#00A480",
        "myMint-400" : "#1F7B67",
        "myMint-500" : "#006B53",
        "myHeaderColor": "#002d31",
      }
    },
  },
  variants: {
    textColor: ['group-hover', 'hover', 'responsive', 'focus', 'active'],
  },
  plugins: [
  ],
}
