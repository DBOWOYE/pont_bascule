
function updateTimer() {
    future = Date.parse("Dec 19, 2023 11:30:00");
    now = new Date();
    diff = future - now;

    days = Math.floor(diff / (1000 * 60 * 60 * 24));
    hours = Math.floor(diff / (1000 * 60 * 60));
    mins = Math.floor(diff / (1000 * 60));
    secs = Math.floor(diff / 1000);

    d = days;
    h = hours - days * 24;
    m = mins - hours * 60;
    s = secs - mins * 60;

    document.getElementById("timer")
        .innerHTML =
        '<div class="col-xxl-3 col-xl-3 col-lg-3 col-md-3 col-sm-3 col-6 mb-3 mb-sm-1"><div class="p-2 under-maintenance-time rounded"><p class="mb-1 fs-12 op-9">DAYS</p><h4 class="fw-semibold mb-0 text-fixed-white">' + d + '</h4></div></div>' +
        '<div class="col-xxl-3 col-xl-3 col-lg-3 col-md-3 col-sm-3 col-6 mb-3 mb-sm-1"><div class="p-2 under-maintenance-time rounded"><p class="mb-1 fs-12 op-9">HOURS</p><h4 class="fw-semibold mb-0 text-fixed-white">' + h + '</h4></div></div>' +
        '<div class="col-xxl-3 col-xl-3 col-lg-3 col-md-3 col-sm-3 col-6 mb-3 mb-sm-1"><div class="p-2 under-maintenance-time rounded"><p class="mb-1 fs-12 op-9">MINUTES</p><h4 class="fw-semibold mb-0 text-fixed-white">' + m + '</h4></div></div>' +
        '<div class="col-xxl-3 col-xl-3 col-lg-3 col-md-3 col-sm-3 col-6 mb-3 mb-sm-1"><div class="p-2 under-maintenance-time rounded"><p class="mb-1 fs-12 op-9">SECONDS</p><h4 class="fw-semibold mb-0 text-fixed-white">' + s + '</h4></div></div>'
}
setInterval('updateTimer()', 1000);