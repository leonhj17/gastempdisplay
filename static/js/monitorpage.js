/**
 * Created by Thinkpad on 2017/11/23.
 */

function fig_xy() {
    var width = 580;
    var height = 250;
    var padding = {'left':30,'right':20,'top':20,'bottom':30};
    var svg_xy = d3.select('#xy');

    var xscale = d3.scaleLinear()
        .domain([0,1])
        .range([padding.left,width-padding.right]);

    var yscale = d3.scaleLinear()
        .domain([0,1])
        .range([height-padding.bottom,padding.top]);

    var pointundate = svg_xy.selectAll('circle')
        .data(query_vector);

    var pointenter = pointundate.enter();

    var pointexit = pointundate.exit();

    pointundate.attr('cx',function (d,i) {
        return xscale(parseFloat(d.x))
    })
        .attr('cy',function (d,i) {
            return yscale(parseFloat(d.y))
        })
        .attr('r',15)
        .attr('fill','green');

    pointenter.append('circle')
        .attr('cx',function (d,i) {
        return xscale(parseFloat(d.x))
    })
        .attr('cy',function (d,i) {
            return yscale(parseFloat(d.y))
        })
        .attr('r',15)
        .attr('fill','green');

    pointexit.remove();

}

function fig_z() {

}

function fig_ab() {

}

function fig_rate() {

}

