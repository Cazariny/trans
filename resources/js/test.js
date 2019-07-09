$(function(){
    $("#employees").dxTreeList({
        dataSource: test,
        keyExpr: "ID",
        parentIdExpr: "Parent_ID",
        columns: [{
            dataField: "Title",
            caption: "Nombre"
        }],
        expandedRowKeys: [1],
        showRowLines: true,
        showBorders: true,
        columnAutoWidth: true
    });
});