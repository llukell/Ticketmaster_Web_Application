const alertTrigger = document.getElementById('liveAlertBtn')
let errorContainer = $('#error-container');

alertTrigger.addEventListener('click', (e) => {
    e.preventDefault()
    let search = $('#category').val();
    let place = $('#location').val();

    errorContainer.empty();
    if ((search === "") && (place === "") && alertTrigger) {
        errorContainer.append('<div class=" mt-2 alert alert-danger" role="alert">Please enter a search term and city</div>')
    } else if ((search === "") && (place !== "") && alertTrigger) {

        errorContainer.append('<div class=" mt-2 alert alert-danger" role="alert">Please enter a search term</div>');
    } else if ((search !== "") && (place === "") && alertTrigger) {
        errorContainer.append('<div class=" mt-2 alert alert-danger" role="alert">Please enter a city </div>')
    } else {
        document.forms["myForm"].submit();
    }
    if (errorContainer) {

        setTimeout(() => {
            errorContainer.empty();
        }, 6000);
    }

})

















