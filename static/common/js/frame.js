
/*加载公共页面*/
$(function() {
    $(".headerpage").load("../static/common/html/header.html"); <!-- 顶部导航 -->
    $(".tpl-skiner").load("../static/common/html/skiner.html"); <!-- 风格切换 -->
    $(".left-sidebar").load("../static/common/html/sidebar.html");<!-- 侧边导航栏 -->
    // 侧边菜单
$('.sidebar-nav-sub-title').on('click', function() {
    $(this).siblings('.sidebar-nav-sub').slideToggle(80)
        .end()
        .find('.sidebar-nav-sub-ico').toggleClass('sidebar-nav-sub-ico-rotate');
})
})


