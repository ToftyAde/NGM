document.addEventListener('DOMContentLoaded', () => {
  const levelSelect = document.getElementById('levelSelect');
  const guessInput = document.getElementById('guess-input');
  const submitBtn = document.getElementById('submit-guess');
  const messageEl = document.getElementById('hint-message');
  const attemptsEl = document.getElementById('attempts-count');
  const resetBtn = document.getElementById('reset-game');

  let target, attempts, maxAttempts;

  function startGame(level) {
    const ranges = { 'Low': 100, 'Moderate': 1000, 'Expert': 10000 };
    maxAttempts = 10;
    target = Math.floor(Math.random() * ranges[level]);
    attempts = 0;
    attemptsEl.textContent = `Attempts: ${attempts} / ${maxAttempts}`;
    messageEl.textContent = '';
    guessInput.removeAttribute('disabled');
    submitBtn.removeAttribute('disabled');
  }

  function endGame() {
    guessInput.setAttribute('disabled', 'disabled');
    submitBtn.setAttribute('disabled', 'disabled');
  }

  submitBtn.addEventListener('click', (e) => {
    e.preventDefault();
    const guess = parseInt(guessInput.value, 10);
    if (isNaN(guess)) {
      messageEl.textContent = 'Please enter a valid number.';
      return;
    }
    attempts++;
    if (guess === target) {
      messageEl.textContent = `🎉 Correct! You guessed it in ${attempts} attempts.`;
      endGame();
    } else if (attempts >= maxAttempts) {
      messageEl.textContent = `❌ Out of attempts! The number was ${target}.`;
      endGame();
    } else {
      messageEl.textContent = guess < target ? 'Too low!' : 'Too high!';
      attemptsEl.textContent = `Attempts: ${attempts} / ${maxAttempts}`;
    }
    guessInput.value = '';
  });

  resetBtn.addEventListener('click', (e) => {
    e.preventDefault();
    startGame(levelSelect.value);
  });

  // Initialize on load
  if (levelSelect) {
    startGame(levelSelect.value);
  }
});
