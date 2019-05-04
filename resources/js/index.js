$(function(){
    var treeView = $("#treeview").dxTreeView({
        items: archivos,
        width: "60%",
        height: "80%",
        searchEnabled:true,
        searchEditorOptions: {
            placeholder: "buscar"
        }
    }).dxTreeView("instance");

    $("#searchMode").dxSelectBox({
        dataSource: ["contains"],
        value: "contains"
    });
});