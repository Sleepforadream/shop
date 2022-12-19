! function(e, t, n) {
    var r = [],
        o = [],
        a = {
            _version: "3.5.0",
            _config: {
                classPrefix: "",
                enableClasses: !0,
                enableJSClass: !0,
                usePrefixes: !0
            },
            _q: [],
            on: function(e, t) {
                var n = this;
                setTimeout(function() {
                    t(n[e])
                }, 0)
            },
            addTest: function(e, t, n) {
                o.push({
                    name: e,
                    fn: t,
                    options: n
                })
            },
            addAsyncTest: function(e) {
                o.push({
                    name: null,
                    fn: e
                })
            }
        },
        i = function() {};
    i.prototype = a, (i = new i).addTest("applicationcache", "applicationCache" in e), i.addTest("geolocation", "geolocation" in navigator), i.addTest("history", function() {
        var t = navigator.userAgent;
        return (-1 === t.indexOf("Android 2.") && -1 === t.indexOf("Android 4.0") || -1 === t.indexOf("Mobile Safari") || -1 !== t.indexOf("Chrome") || -1 !== t.indexOf("Windows Phone") || "file:" === location.protocol) && (e.history && "pushState" in e.history)
    }), i.addTest("postmessage", "postMessage" in e);
    var s = !1;
    try {
        s = "WebSocket" in e && 2 === e.WebSocket.CLOSING
    } catch (e) {}
    i.addTest("websockets", s), i.addTest("localstorage", function() {
        var e = "modernizr";
        try {
            return localStorage.setItem(e, e), localStorage.removeItem(e), !0
        } catch (e) {
            return !1
        }
    }), i.addTest("sessionstorage", function() {
        var e = "modernizr";
        try {
            return sessionStorage.setItem(e, e), sessionStorage.removeItem(e), !0
        } catch (e) {
            return !1
        }
    }), i.addTest("websqldatabase", "openDatabase" in e), i.addTest("webworkers", "Worker" in e);
    var l = a._config.usePrefixes ? " -webkit- -moz- -o- -ms- ".split(" ") : ["", ""];

    function c(e, t) {
        return typeof e === t
    }
    a._prefixes = l;
    var d = t.documentElement,
        u = "svg" === d.nodeName.toLowerCase();

    function f(e) {
        var t = d.className,
            n = i._config.classPrefix || "";
        if (u && (t = t.baseVal), i._config.enableJSClass) {
            var r = new RegExp("(^|\\s)" + n + "no-js(\\s|$)");
            t = t.replace(r, "$1" + n + "js$2")
        }
        i._config.enableClasses && (t += " " + n + e.join(" " + n), u ? d.className.baseVal = t : d.className = t)
    }
    var p, g, m = a._config.usePrefixes ? "Moz O ms Webkit".toLowerCase().split(" ") : [];

    function h(e, t) {
        if ("object" == typeof e)
            for (var n in e) p(e, n) && h(n, e[n]);
        else {
            var r = (e = e.toLowerCase()).split("."),
                o = i[r[0]];
            if (2 == r.length && (o = o[r[1]]), void 0 !== o) return i;
            t = "function" == typeof t ? t() : t, 1 == r.length ? i[r[0]] = t : (!i[r[0]] || i[r[0]] instanceof Boolean || (i[r[0]] = new Boolean(i[r[0]])), i[r[0]][r[1]] = t), f([(t && 0 != t ? "" : "no-") + r.join("-")]), i._trigger(e, t)
        }
        return i
    }

    function v() {
        return "function" != typeof t.createElement ? t.createElement(arguments[0]) : u ? t.createElementNS.call(t, "http://www.w3.org/2000/svg", arguments[0]) : t.createElement.apply(t, arguments)
    }
    a._domPrefixes = m, p = c(g = {}.hasOwnProperty, "undefined") || c(g.call, "undefined") ? function(e, t) {
        return t in e && c(e.constructor.prototype[t], "undefined")
    } : function(e, t) {
        return g.call(e, t)
    }, a._l = {}, a.on = function(e, t) {
        this._l[e] || (this._l[e] = []), this._l[e].push(t), i.hasOwnProperty(e) && setTimeout(function() {
            i._trigger(e, i[e])
        }, 0)
    }, a._trigger = function(e, t) {
        if (this._l[e]) {
            var n = this._l[e];
            setTimeout(function() {
                var e;
                for (e = 0; e < n.length; e++)(0, n[e])(t)
            }, 0), delete this._l[e]
        }
    }, i._q.push(function() {
        a.addTest = h
    });
    var y = function() {
        var e = !("onblur" in t.documentElement);
        return function(t, r) {
            var o;
            return !!t && (r && "string" != typeof r || (r = v(r || "div")), !(o = (t = "on" + t) in r) && e && (r.setAttribute || (r = v("div")), r.setAttribute(t, ""), o = "function" == typeof r[t], r[t] !== n && (r[t] = n), r.removeAttribute(t)), o)
        }
    }();

    function b(e) {
        return e.replace(/([a-z])-([a-z])/g, function(e, t, n) {
            return t + n.toUpperCase()
        }).replace(/^-/, "")
    }
    a.hasEvent = y, i.addTest("hashchange", function() {
        return !1 !== y("hashchange", e) && (t.documentMode === n || t.documentMode > 7)
    }), i.addTest("audio", function() {
        var e = v("audio"),
            t = !1;
        try {
            (t = !!e.canPlayType) && ((t = new Boolean(t)).ogg = e.canPlayType('audio/ogg; codecs="vorbis"').replace(/^no$/, ""), t.mp3 = e.canPlayType('audio/mpeg; codecs="mp3"').replace(/^no$/, ""), t.opus = e.canPlayType('audio/ogg; codecs="opus"') || e.canPlayType('audio/webm; codecs="opus"').replace(/^no$/, ""), t.wav = e.canPlayType('audio/wav; codecs="1"').replace(/^no$/, ""), t.m4a = (e.canPlayType("audio/x-m4a;") || e.canPlayType("audio/aac;")).replace(/^no$/, ""))
        } catch (e) {}
        return t
    }), i.addTest("canvas", function() {
        var e = v("canvas");
        return !(!e.getContext || !e.getContext("2d"))
    }), i.addTest("canvastext", function() {
        return !1 !== i.canvas && "function" == typeof v("canvas").getContext("2d").fillText
    }), i.addTest("video", function() {
        var e = v("video"),
            t = !1;
        try {
            (t = !!e.canPlayType) && ((t = new Boolean(t)).ogg = e.canPlayType('video/ogg; codecs="theora"').replace(/^no$/, ""), t.h264 = e.canPlayType('video/mp4; codecs="avc1.42E01E"').replace(/^no$/, ""), t.webm = e.canPlayType('video/webm; codecs="vp8, vorbis"').replace(/^no$/, ""), t.vp9 = e.canPlayType('video/webm; codecs="vp9"').replace(/^no$/, ""), t.hls = e.canPlayType('application/x-mpegURL; codecs="avc1.42E01E"').replace(/^no$/, ""))
        } catch (e) {}
        return t
    }), i.addTest("webgl", function() {
        var t = v("canvas"),
            n = "probablySupportsContext" in t ? "probablySupportsContext" : "supportsContext";
        return n in t ? t[n]("webgl") || t[n]("experimental-webgl") : "WebGLRenderingContext" in e
    }), i.addTest("cssgradients", function() {
        for (var e, t = "background-image:", n = "", r = 0, o = l.length - 1; r < o; r++) e = 0 === r ? "to " : "", n += t + l[r] + "linear-gradient(" + e + "left top, #9f9, white);";
        i._config.usePrefixes && (n += t + "-webkit-gradient(linear,left top,right bottom,from(#9f9),to(white));");
        var a = v("a").style;
        return a.cssText = n, ("" + a.backgroundImage).indexOf("gradient") > -1
    }), i.addTest("multiplebgs", function() {
        var e = v("a").style;
        return e.cssText = "background:url(https://),url(https://),red url(https://)", /(url\s*\(.*?){3}/.test(e.background)
    }), i.addTest("opacity", function() {
        var e = v("a").style;
        return e.cssText = l.join("opacity:.55;"), /^0.55$/.test(e.opacity)
    }), i.addTest("rgba", function() {
        var e = v("a").style;
        return e.cssText = "background-color:rgba(150,255,150,.5)", ("" + e.backgroundColor).indexOf("rgba") > -1
    }), i.addTest("inlinesvg", function() {
        var e = v("div");
        return e.innerHTML = "<svg/>", "http://www.w3.org/2000/svg" == ("undefined" != typeof SVGRect && e.firstChild && e.firstChild.namespaceURI)
    });
    var T = v("input"),
        x = "autocomplete autofocus list placeholder max min multiple pattern required step".split(" "),
        w = {};
    i.input = function(t) {
        for (var n = 0, r = t.length; n < r; n++) w[t[n]] = !!(t[n] in T);
        return w.list && (w.list = !(!v("datalist") || !e.HTMLDataListElement)), w
    }(x);
    var S = "search tel url email datetime date month week time datetime-local number range color".split(" "),
        C = {};

    function P(e, t) {
        return !!~("" + e).indexOf(t)
    }
    i.inputtypes = function(e) {
        for (var r, o, a, i = e.length, s = 0; s < i; s++) T.setAttribute("type", r = e[s]), (a = "text" !== T.type && "style" in T) && (T.value = "1)", T.style.cssText = "position:absolute;visibility:hidden;", /^range$/.test(r) && T.style.WebkitAppearance !== n ? (d.appendChild(T), a = (o = t.defaultView).getComputedStyle && "textfield" !== o.getComputedStyle(T, null).WebkitAppearance && 0 !== T.offsetHeight, d.removeChild(T)) : /^(search|tel)$/.test(r) || (a = /^(url|email)$/.test(r) ? T.checkValidity && !1 === T.checkValidity() : "1)" != T.value)), C[e[s]] = !!a;
        return C
    }(S), i.addTest("hsla", function() {
        var e = v("a").style;
        return e.cssText = "background-color:hsla(120,40%,100%,.5)", P(e.backgroundColor, "rgba") || P(e.backgroundColor, "hsla")
    });
    var k = "CSS" in e && "supports" in e.CSS,
        _ = "supportsCSS" in e;
    i.addTest("supports", k || _);
    var z = {}.toString;

    function E(e, n, r, o) {
        var a, i, s, l, c = "modernizr",
            f = v("div"),
            p = function() {
                var e = t.body;
                return e || ((e = v(u ? "svg" : "body")).fake = !0), e
            }();
        if (parseInt(r, 10))
            for (; r--;)(s = v("div")).id = o ? o[r] : c + (r + 1), f.appendChild(s);
        return (a = v("style")).type = "text/css", a.id = "s" + c, (p.fake ? p : f).appendChild(a), p.appendChild(f), a.styleSheet ? a.styleSheet.cssText = e : a.appendChild(t.createTextNode(e)), f.id = c, p.fake && (p.style.background = "", p.style.overflow = "hidden", l = d.style.overflow, d.style.overflow = "hidden", d.appendChild(p)), i = n(f, e), p.fake ? (p.parentNode.removeChild(p), d.style.overflow = l, d.offsetHeight) : f.parentNode.removeChild(f), !!i
    }
    i.addTest("svgclippaths", function() {
        return !!t.createElementNS && /SVGClipPath/.test(z.call(t.createElementNS("http://www.w3.org/2000/svg", "clipPath")))
    }), i.addTest("smil", function() {
        return !!t.createElementNS && /SVGAnimate/.test(z.call(t.createElementNS("http://www.w3.org/2000/svg", "animate")))
    });
    var A, O = (A = e.matchMedia || e.msMatchMedia) ? function(e) {
        var t = A(e);
        return t && t.matches || !1
    } : function(t) {
        var n = !1;
        return E("@media " + t + " { #modernizr { position: absolute; } }", function(t) {
            n = "absolute" == (e.getComputedStyle ? e.getComputedStyle(t, null) : t.currentStyle).position
        }), n
    };
    a.mq = O;
    var $, R, L, N = a.testStyles = E;
    i.addTest("touchevents", function() {
        var n;
        if ("ontouchstart" in e || e.DocumentTouch && t instanceof DocumentTouch) n = !0;
        else {
            var r = ["@media (", l.join("touch-enabled),("), "heartz", ")", "{#modernizr{top:9px;position:absolute}}"].join("");
            N(r, function(e) {
                n = 9 === e.offsetTop
            })
        }
        return n
    }), ($ = navigator.userAgent, R = $.match(/w(eb)?osbrowser/gi), L = $.match(/windows phone/gi) && $.match(/iemobile\/([0-9])+/gi) && parseFloat(RegExp.$1) >= 9, R || L) ? i.addTest("fontface", !1) : N('@font-face {font-family:"font";src:url("https://")}', function(e, n) {
        var r = t.getElementById("smodernizr"),
            o = r.sheet || r.styleSheet,
            a = o ? o.cssRules && o.cssRules[0] ? o.cssRules[0].cssText : o.cssText || "" : "",
            s = /src/i.test(a) && 0 === a.indexOf(n.split(" ")[0]);
        i.addTest("fontface", s)
    }), N('#modernizr{font:0/0 a}#modernizr:after{content:":)";visibility:hidden;font:7px/1 a}', function(e) {
        i.addTest("generatedcontent", e.offsetHeight >= 6)
    });
    var j = a._config.usePrefixes ? "Moz O ms Webkit".split(" ") : [];
    a._cssomPrefixes = j;
    var M = function(t) {
        var r, o = l.length,
            a = e.CSSRule;
        if (void 0 === a) return n;
        if (!t) return !1;
        if ((r = (t = t.replace(/^@/, "")).replace(/-/g, "_").toUpperCase() + "_RULE") in a) return "@" + t;
        for (var i = 0; i < o; i++) {
            var s = l[i];
            if (s.toUpperCase() + "_" + r in a) return "@-" + s.toLowerCase() + "-" + t
        }
        return !1
    };

    function I(e, t) {
        return function() {
            return e.apply(t, arguments)
        }
    }
    a.atRule = M;
    var W = {
        elem: v("modernizr")
    };
    i._q.push(function() {
        delete W.elem
    });
    var q = {
        style: W.elem.style
    };

    function V(e) {
        return e.replace(/([A-Z])/g, function(e, t) {
            return "-" + t.toLowerCase()
        }).replace(/^ms-/, "-ms-")
    }

    function B(t, r) {
        var o = t.length;
        if ("CSS" in e && "supports" in e.CSS) {
            for (; o--;)
                if (e.CSS.supports(V(t[o]), r)) return !0;
            return !1
        }
        if ("CSSSupportsRule" in e) {
            for (var a = []; o--;) a.push("(" + V(t[o]) + ":" + r + ")");
            return E("@supports (" + (a = a.join(" or ")) + ") { #modernizr { position: absolute; } }", function(t) {
                return "absolute" == function(t, n, r) {
                    var o;
                    if ("getComputedStyle" in e) {
                        o = getComputedStyle.call(e, t, n);
                        var a = e.console;
                        null !== o ? r && (o = o.getPropertyValue(r)) : a && a[a.error ? "error" : "log"].call(a, "getComputedStyle returning null, its possible modernizr test results are inaccurate")
                    } else o = !n && t.currentStyle && t.currentStyle[r];
                    return o
                }(t, null, "position")
            })
        }
        return n
    }

    function U(e, t, r, o) {
        if (o = !c(o, "undefined") && o, !c(r, "undefined")) {
            var a = B(e, r);
            if (!c(a, "undefined")) return a
        }
        for (var i, s, l, d, u, f = ["modernizr", "tspan", "samp"]; !q.style && f.length;) i = !0, q.modElem = v(f.shift()), q.style = q.modElem.style;

        function p() {
            i && (delete q.style, delete q.modElem)
        }
        for (l = e.length, s = 0; s < l; s++)
            if (d = e[s], u = q.style[d], P(d, "-") && (d = b(d)), q.style[d] !== n) {
                if (o || c(r, "undefined")) return p(), "pfx" != t || d;
                try {
                    q.style[d] = r
                } catch (e) {}
                if (q.style[d] != u) return p(), "pfx" != t || d
            } return p(), !1
    }
    i._q.unshift(function() {
        delete q.style
    });
    var H = a.testProp = function(e, t, r) {
        return U([e], n, t, r)
    };

    function G(e, t, n, r, o) {
        var a = e.charAt(0).toUpperCase() + e.slice(1),
            i = (e + " " + j.join(a + " ") + a).split(" ");
        return c(t, "string") || c(t, "undefined") ? U(i, t, r, o) : function(e, t, n) {
            var r;
            for (var o in e)
                if (e[o] in t) return !1 === n ? e[o] : c(r = t[e[o]], "function") ? I(r, n || t) : r;
            return !1
        }(i = (e + " " + m.join(a + " ") + a).split(" "), t, n)
    }
    i.addTest("textshadow", H("textShadow", "1px 1px")), a.testAllProps = G;
    a.prefixed = function(e, t, n) {
        return 0 === e.indexOf("@") ? M(e) : (-1 != e.indexOf("-") && (e = b(e)), t ? G(e, t, n) : G(e, "pfx"))
    };

    function D(e, t, r) {
        return G(e, n, n, t, r)
    }
    a.testAllProps = D, i.addTest("cssanimations", D("animationName", "a", !0)), i.addTest("backgroundsize", D("backgroundSize", "100%", !0)), i.addTest("borderimage", D("borderImage", "url() 1", !0)), i.addTest("borderradius", D("borderRadius", "0px", !0)), i.addTest("boxshadow", D("boxShadow", "1px 1px", !0)), i.addTest("flexbox", D("flexBasis", "1px", !0)), i.addTest("cssreflections", D("boxReflect", "above", !0)), i.addTest("csstransforms", function() {
            return -1 === navigator.userAgent.indexOf("Android 2.") && D("transform", "scale(1)", !0)
        }), i.addTest("csstransforms3d", function() {
            var e = !!D("perspective", "1px", !0),
                t = i._config.usePrefixes;
            if (e && (!t || "webkitPerspective" in d.style)) {
                var n;
                i.supports ? n = "@supports (perspective: 1px)" : (n = "@media (transform-3d)", t && (n += ",(-webkit-transform-3d)")), N("#modernizr{width:0;height:0}" + (n += "{#modernizr{width:7px;height:18px;margin:0;padding:0;border:0}}"), function(t) {
                    e = 7 === t.offsetWidth && 18 === t.offsetHeight
                })
            }
            return e
        }), i.addTest("csstransitions", D("transition", "all", !0)),
        function() {
            var e, t, n, a, s, l;
            for (var d in o)
                if (o.hasOwnProperty(d)) {
                    if (e = [], (t = o[d]).name && (e.push(t.name.toLowerCase()), t.options && t.options.aliases && t.options.aliases.length))
                        for (n = 0; n < t.options.aliases.length; n++) e.push(t.options.aliases[n].toLowerCase());
                    for (a = c(t.fn, "function") ? t.fn() : t.fn, s = 0; s < e.length; s++) 1 === (l = e[s].split(".")).length ? i[l[0]] = a : (!i[l[0]] || i[l[0]] instanceof Boolean || (i[l[0]] = new Boolean(i[l[0]])), i[l[0]][l[1]] = a), r.push((a ? "" : "no-") + l.join("-"))
                }
        }(), f(r), delete a.addTest, delete a.addAsyncTest;
    for (var J = 0; J < i._q.length; J++) i._q[J]();
    e.Modernizr = i
}(window, document);