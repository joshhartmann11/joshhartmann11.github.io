var projects = [
    {
        "name": "Codan Radio Co-op",
        "date": "2019-01-10",
        "path": "projects/codan.html"
    },
    {
        "name": "Battlesnake Arena",
        "date": "2018-05-07",
        "path": "projects/battlesnakearena.html"
    },
    {
        "name": "Fisher Finance 2.0",
        "date": "2018-12-13",
        "path": "projects/fisherfinance2-0.html"
    },
    {
        "name": "3D Printer Update",
        "date": "2017-10-15",
        "path": "projects/3dprinter.html"
    },
    {
        "name": "Sewing",
        "date": "2018-02-12",
        "path": "projects/sewing.html"
    },
    {
        "name": "Fisher Finance",
        "date": "2018-02-16",
        "path": "projects/fisherfinance.html"
    },
    {
        "name": "Battle Snake 2018",
        "date": "2018-03-08",
        "path": "projects/battlesnake2018.html"
    },
    {
        "name": "W-CIRC Co-op Recap",
        "date": "2018-01-14",
        "path": "projects/wcirc.html"
    },
    {
        "name": "Failed Project: Playbol",
        "date": "2018-04-16",
        "path": "projects/playbol.html"
    },
];

function insert_index(projects) {
    var prelude = '<h1>Index:</h1>\n';

    var list = '<ul><h2>\n';
    for (var i = 0; i < projects.length; i++) {
        var date = projects[i]["date"];
        var name = projects[i]["name"];
        list += '<li><a href="#' + date + '">' + date + " - " + name + '</a></li>\n';
    }
    list += '</h2></ul>\n';

    var postlude = '<br><div id="divline"></div><br>';

    var contents = prelude + list + postlude;
    document.getElementById("projects").innerHTML += contents;
}

function insert_project(project) {
    var name = project["name"];
    var date = project["date"];
    var path = project["path"];

    var projectClassPre = '<div class="project" id="' + date + '">\n'
    var projectTitle = '<h1>' + date + ' - ' + name + '</h1>\n'
    var projectText = '<h3><div include-html="' + path + '"></h3>\n'
    var projectLine = '<br><div id="divline"></div><br>\n'
    var projectClassPost = '</div>\n'

    var projectContents = projectClassPre + projectTitle + projectText + projectClassPost + projectLine;
    document.getElementById("projects").innerHTML += projectContents;
}

function insert_projects(projects) {
    for (var i = 0; i < projects.length; i++) {
        insert_project(projects[i]);
    }
}


projects.sort(function(a, b) {
    return ((a["date"] < b["date"]) ? -1 : ((a["date"] > b["date"]) ? 1 : 0))
})
projects.reverse();
insert_index(projects);
insert_projects(projects);
