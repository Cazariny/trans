// Expected format of the node (there are no required fields)
$('#jstree_demo_div').jstree({ 'core' : {
        'data' : [
            'Simple root node',
            {
                'text' : 'Root node 2',
                'state' : {
                    'opened' : true,
                    'selected' : true
                },
                'children' : [
                    { 'text' : 'Child 1',
                      'a_atr':{"href" : "google.com" }
                    },
                    'Child 2'
                ]
            }
        ]
    }
}).bind("changed.jstree", function (e, data) {
    if(data.node) {
        document.location = data.node.a_attr.href;
    }
});

$(function () {
    $('#jstree_demo_div').jstree();
});
$('#jstree_demo_div').on("changed.jstree", function (e, data) {
    console.log(data.selected);
});

