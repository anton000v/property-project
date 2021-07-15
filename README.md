build apn-ui:

    docker build -f apn-ui/docker/vuejs/Dockerfile -t asnovostroi/apn-ui:1.0 .



Api Token:
Token eb3710a2f1a46c68657da822e0a4caf249564c25

Known errors and strange situations:
VueJS:
Error in mounted hook: "SyntaxError: '#/....' is not a valid selector"
Solution: Check if problem is in vue-scrollactive package in 375 and 376 lines.
The same situation:
https://github.com/eddiemf/vue-scrollactive/issues/46
I've switched router to the history mode and it has gone