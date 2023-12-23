// document.addEventListener('DOMContentLoaded', function(){
//     let shop = document.getElementById('id_shop');
//     shop.addEventListener('change', function () {
//         console.log(shop.value);
//     })
//     console.log(document.getElementById('id_shop'));
//
// });
$(document).ready(function($){
    let shop = $('#id_shop');
    let categories = $('#id_product_category');
    shop.on('change', function () {
        $.ajax({
            method: 'GET',
            url: '/categories/',
            data: {data: shop.val()},
            success: function (data) {
                categories.html(data['html'])
            }
        })
    })
});
