document.querySelectorAll('.room-product').forEach(product => {
    product.onclick = () => {
        const previewContainer = document.querySelector('.room-products-preview');
        const previewBox = document.querySelector(`.room-preview[data-target='${product.getAttribute('data-name')}']`);
        
        previewContainer.style.display = 'flex';
        previewBox.classList.add('active');
    };
});

document.querySelectorAll('.ri-close-fill').forEach(closeBtn => {
    closeBtn.onclick = () => {
        const previewContainer = document.querySelector('.room-products-preview');
        previewContainer.style.display = 'none';
        document.querySelectorAll('.room-preview').forEach(previewBox => {
            previewBox.classList.remove('active');
        });
    };
});
