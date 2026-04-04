function login() {
    window.location.href = "/auth/login";
}

function getToken() {
    return document.getElementById("token").value;
}

function show(data) {
    document.getElementById("output").textContent =
        JSON.stringify(data, null, 2);
}

function clearOutput() {
    document.getElementById("output").textContent = "Cleared!";
}


function loading() {
    document.getElementById("output").textContent = "Loading...";
}

function getRepos() {
    loading();

    fetch(`/repos?token=${getToken()}`)
        .then(res => res.json())
        .then(show)
        .catch(err => show(err));
}


function getIssues() {
    loading();

    const owner = document.getElementById("owner").value;
    const repo = document.getElementById("repo").value;

    fetch(`/issues?token=${getToken()}&owner=${owner}&repo=${repo}`)
        .then(res => res.json())
        .then(show)
        .catch(show);
}


function createIssue() {
    loading();

    const owner = document.getElementById("owner").value;
    const repo = document.getElementById("repo").value;
    const title = document.getElementById("title").value;
    const body = document.getElementById("body").value;

    fetch(`/create-issue?token=${getToken()}&owner=${owner}&repo=${repo}&title=${title}&body=${body}`, {
        method: "POST"
    })
    .then(res => res.json())
    .then(show)
    .catch(show);
}


function createPR() {
    loading();

    const owner = document.getElementById("owner").value;
    const repo = document.getElementById("repo").value;
    const title = document.getElementById("pr_title").value;
    const head = document.getElementById("head").value;
    const base = document.getElementById("base").value;

    fetch(`/create-pull-request?token=${getToken()}&owner=${owner}&repo=${repo}&title=${title}&head=${head}&base=${base}`, {
        method: "POST"
    })
    .then(res => res.json())
    .then(show)
    .catch(show);
}