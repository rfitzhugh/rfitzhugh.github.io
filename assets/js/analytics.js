(function () {
  "use strict";

  var scrollMilestones = [50, 90];
  var firedMilestones = {};

  function hasGtag() {
    return typeof window.gtag === "function";
  }

  function sendEvent(eventName, params) {
    if (!hasGtag()) {
      return;
    }

    window.gtag("event", eventName, params);
  }

  function normalizeText(value) {
    if (!value) {
      return "";
    }

    return value.replace(/\s+/g, " ").trim().slice(0, 120);
  }

  function getLocation(link) {
    if (link.closest(".navbar, nav.menu, .trigger-container")) {
      return "nav";
    }

    if (link.closest(".footer_social-icons, footer.footer")) {
      return "social";
    }

    if (link.closest("article, .page-content")) {
      return "content";
    }

    return "other";
  }

  function isTrackableLink(href) {
    return href && !href.startsWith("#") && !href.startsWith("javascript:");
  }

  function isExternal(url) {
    try {
      var parsed = new URL(url, window.location.href);
      return parsed.origin !== window.location.origin;
    } catch (error) {
      return false;
    }
  }

  function onClick(event) {
    var link = event.target.closest("a[href]");
    if (!link) {
      return;
    }

    var rawHref = link.getAttribute("href");
    if (!isTrackableLink(rawHref)) {
      return;
    }

    var location = getLocation(link);
    var params = {
      link_url: link.href,
      link_text: normalizeText(link.textContent),
      location: location,
      page_path: window.location.pathname
    };

    if (location === "nav") {
      sendEvent("click_nav", params);
      return;
    }

    if (location === "social") {
      sendEvent("click_social", params);
      return;
    }

    if (isExternal(link.href)) {
      sendEvent("click_outbound", params);
    }
  }

  function getScrollPercent() {
    var scrollTop = window.scrollY || window.pageYOffset || 0;
    var scrollHeight = document.documentElement.scrollHeight - window.innerHeight;

    if (scrollHeight <= 0) {
      return 100;
    }

    return Math.round((scrollTop / scrollHeight) * 100);
  }

  function onScroll() {
    var percent = getScrollPercent();

    scrollMilestones.forEach(function (milestone) {
      if (percent >= milestone && !firedMilestones[milestone]) {
        firedMilestones[milestone] = true;
        sendEvent("scroll_depth", {
          depth_percent: milestone,
          page_path: window.location.pathname
        });
      }
    });
  }

  document.addEventListener("click", onClick, { capture: true, passive: true });
  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("load", onScroll);
})();
