const progress = require('cli-progress')

function Example1(onComplete) {
    console.log('\nExample 1 - Standard configuration (4s)');
    const b1 = new progress.Bar();
    b1.start(200, 0);
    let value = 0;
    const timer = setInterval(function () {
        value++;
        b1.update(value)
        if (value >= b1.getTotal()) {
            clearInterval(timer);
            b1.stop();
        }
    }, 1000);
}
Example1()