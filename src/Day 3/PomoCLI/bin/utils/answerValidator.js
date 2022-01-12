const answerValidator = async (input) => {
    var regExp = /[a-zA-Z]/g;

    if (regExp.test(input)) {
        return 'Enter the time in only minutes with any alphabets/letters'
    }
    return true
};

export default answerValidator