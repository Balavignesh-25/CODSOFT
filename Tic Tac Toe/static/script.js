const cells = document.querySelectorAll('.cell');
const message = document.getElementById('message');
const restartBtn = document.getElementById('restart-btn');


cells.forEach(cell => {
    cell.addEventListener('click', () => {
        const index = cell.getAttribute('data-index');
        fetch('/make_move', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ index })
        })
        .then(response => response.json())
        .then(data => {
            updateBoard(data.board);
            if (data.winner) {
                message.textContent = data.winner === 'D' ? "It's a draw!" : `${data.winner} wins!`;
                disableClicks();
            }
        });
    });
});


function updateBoard(board) {
    cells.forEach((cell, index) => {
        cell.textContent = board[index];
    });
}


function disableClicks() {
    cells.forEach(cell => {
        cell.style.pointerEvents = 'none';
    });
}


restartBtn.addEventListener('click', () => {
    fetch('/restart', { method: 'POST' })
    .then(response => response.json())
    .then(data => {
        updateBoard(data.board);
        message.textContent = '';
        cells.forEach(cell => {
            cell.style.pointerEvents = 'auto';
        });
    });
});
