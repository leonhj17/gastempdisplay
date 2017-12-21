/**
 * Created by Thinkpad on 2017/12/21.
 */

function adjustToFreezeWidth(rootSvg, widthscale) {
    var windowWidth = $(window).width();

    var viewBoxVal = rootSvg.getAttribute("viewBox");
    var viewBoxWidth = viewBoxVal.split(" ")[2];
    var viewBoxHeight = viewBoxVal.split(" ")[3];
    rootSvg.removeAttribute("width");
    rootSvg.removeAttribute("height");
    rootSvg.removeAttribute("viewBox");

    var setWidth = windowWidth*widthscale;
    var setHeight = (setWidth * viewBoxHeight) / viewBoxWidth;
    rootSvg.setAttribute("width", setWidth);
    rootSvg.setAttribute("height", setHeight);
    rootSvg.setAttribute("viewBox","0 0 "+setWidth+" "+setHeight)
}

function adjustToNone(rootSvg) {

    var viewBoxVal = rootSvg.getAttribute("viewBox");
    var viewBoxWidth = viewBoxVal.split(" ")[2];
    var viewBoxHeight = viewBoxVal.split(" ")[3];
    rootSvg.removeAttribute("width");
    rootSvg.removeAttribute("height");

    rootSvg.setAttribute("width", viewBoxWidth);
    rootSvg.setAttribute("height", viewBoxHeight);

}

function adjustToFreezeHeight(rootSvg) {

    var windowHeight = $(window).height();

    var viewBoxVal = rootSvg.getAttribute("viewBox");
    var viewBoxWidth = viewBoxVal.split(" ")[2];
    var viewBoxHeight = viewBoxVal.split(" ")[3];
    rootSvg.removeAttribute("width");
    rootSvg.removeAttribute("height");


    var setHeight = windowHeight;
    var setWidth = (setHeight * viewBoxWidth)/viewBoxHeight;
    rootSvg.setAttribute("width", setWidth);
    rootSvg.setAttribute("height", setHeight);

}

function adjustToFreezeAll() {

    var windowHeight = $(window).height();
    var windowWidth = $(window).width();

    rootSvg.removeAttribute("width");
    rootSvg.removeAttribute("height");

    rootSvg.setAttribute("width", windowWidth);
    rootSvg.setAttribute("height", windowHeight);

}