
/*���ع���ҳ��*/
$(function() {
    $(".headerpage").load("../static/common/html/header.html"); <!-- �������� -->
    $(".tpl-skiner").load("../static/common/html/skiner.html"); <!-- ����л� -->
    $(".left-sidebar").load("../static/common/html/sidebar.html");<!-- ��ߵ����� -->
    // ��߲˵�
$('.sidebar-nav-sub-title').on('click', function() {
    $(this).siblings('.sidebar-nav-sub').slideToggle(80)
        .end()
        .find('.sidebar-nav-sub-ico').toggleClass('sidebar-nav-sub-ico-rotate');
})
})


