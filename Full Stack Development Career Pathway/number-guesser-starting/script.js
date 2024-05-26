let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

function generateTarget () {
    return Math.floor(Math.random() * 10);
}
  
function compareGuesses (humanGuess, computerGuess, targetNumber) {
    computerCloseness = Math.abs(targetNumber - computerGuess);
    humanCloseness = Math.abs(targetNumber - humanGuess);

    return humanCloseness <= computerCloseness ? true : false;
}

function updateScore (whoWon) {
    switch (whoWon) {
        case 'human':
            humanScore++;
            break;
        case 'computer':
            computerScore++;
            break;
        default:
            console.log('Error occurred in updating score...');
            break;
    }
}

const advanceRound = () => currentRoundNumber ++;
