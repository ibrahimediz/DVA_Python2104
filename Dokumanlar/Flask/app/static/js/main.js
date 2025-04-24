// Ana JavaScript dosyasu0131
document.addEventListener('DOMContentLoaded', function() {
    // Sayfa yu00fcklendiu011finde u00e7alu0131u015facak kodlar
    console.log('Sayfa yu00fcklendi!');
    
    // Form dogrulama
    const forms = document.querySelectorAll('.needs-validation');
    
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            
            form.classList.add('was-validated');
        }, false);
    });
});