document.addEventListener('DOMContentLoaded', function () {
    const cartWrapper = document.querySelector('.cart-wrapper');
    if (!cartWrapper) return;

    const csrfToken = cartWrapper.dataset.csrf;

    document.querySelectorAll('.btn-update').forEach(btn => {
        btn.addEventListener('click', function () {
            const itemId = this.dataset.id;
            const action = this.dataset.action;

            fetch(`/cart/update/${itemId}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                body: `action=${action}`
            })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        const row = document.getElementById(`item-${data.item_id}`);
                        if (data.quantity === 0 || action === 'remove') {
                            row.remove();
                        } else {
                            row.querySelector('.quantity-value').textContent = data.quantity;
                            // Prezzo unitario dal quarto td (indice 4 perché ora c'è l'immagine al primo posto)
                            // Utilizziamo nth-child(4) per prendere il prezzo del prodotto
                            const unitPrice = parseFloat(row.querySelector('td:nth-child(4)').textContent);
                            row.querySelector('.item-total').textContent = (data.quantity * unitPrice) + ' €';
                        }
                        document.getElementById('cart-total').textContent = data.total + ' €';

                        // Se il carrello è vuoto, ricarichiamo la pagina per mostrare il messaggio "vuoto"
                        if (document.querySelectorAll('.cart-table tbody tr').length === 0) {
                            location.reload();
                        }
                    }
                });
        });
    });
});
