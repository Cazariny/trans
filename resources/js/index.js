$(function(){
    var treeView = $("#treeview").dxTreeView({
        items: productos,
        width: "60%",
        height: "80%",
        searchEnabled:true
    }).dxTreeView("instance");

    $("#searchMode").dxSelectBox({
        dataSource: ["contains"],
        value: "contains"
    });
});