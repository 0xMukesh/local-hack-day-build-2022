import answerValidator from './answerValidator.js'

const questions = [
    {
        type: 'text',
        name: 'sessionName',
        message: 'Enter your session name:'
    },
    {
        type: 'text',
        name: 'sessionWorkDuration',
        message: 'Enter the session\'s work duration (in minutes):',
        validate: answerValidator
    },
    {
        type: 'text',
        name: 'sessionBreakDuration',
        message: 'Enter the session\'s break duration (in minutes):',
        validate: answerValidator
    },
    {
        type: 'text',
        name: 'sessionNumber',
        message: 'Enter the number of sessions you wanted to do:',
        validate: answerValidator
    }
]

export default questions