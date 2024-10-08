https://closure-compiler.appspot.com/home


@code_url https://frankxue.com/cv_files/jquery-2.with.lazy.js






function paint_gs_cites(){
	if (gs_cites === undefined) {return;}
	var svg = d3.select("svg"),
			margin = 30,
			width = svg.attr("width") - margin,
			height = svg.attr("height") - margin;
	svg.append("text")
		 .attr("transform", "translate(0,0)")
		 .attr("x", margin*1.5)
		 .attr("y", margin/2)
		 .attr("font-size", "1em")
		 .text("Citations by year")

	var xScale = d3.scaleBand().range([0, width]).padding(1-0.618),
			yScale = d3.scaleLinear().range([height, 0]);
	var g = svg.append("g").attr("transform", "translate(" + margin + "," + 0 + ")");

	xScale.domain(gs_cites.map(function(d) { return d.year; }));
	yScale.domain([0, d3.max(gs_cites, function(d) { return parseFloat(d.value); })*1.05]);
	g.append("g")
	 .attr("transform", "translate(0," + height + ")")
	 .call(d3.axisBottom(xScale))
	 .append("text")
	 .attr("y", height - margin)
	 .attr("x", width - margin)
	 .attr("text-anchor", "end")
	 .attr("stroke", "black");

	g.append("g")
	 .call(d3.axisLeft(yScale).tickFormat(function(d){ return d; })
	 .ticks(6))
	 .append("text")
	 .attr("transform", "rotate(-90)")
	 .attr("dy", "-3em")
	 .attr("text-anchor", "end")
	 .attr("stroke", "black");

	g.selectAll(".bar")
	 .data(gs_cites)
	 .enter().append("rect")
	 .attr("class", "bar")
	 .attr("x", function(d) { return xScale(d.year); })
	 .attr("y", function(d) { return yScale(d.value); })
	 .attr("width", xScale.bandwidth())
	 .attr("height", function(d) { return height - yScale(d.value); });
 }

$(document).ready(function(){
	$('#loader-overlay').show();
	// on resize
	$(window).on('load resize', function(e){
		$('#top').css('height', $(window).height() * .995);
		$('#contact').css('height', $(window).height() * .995);
		$('#loader-overlay').delay(400).fadeOut(300);
	})

	// click title
	$('#top-titles').click(function(){
		$('html, body').animate({ scrollTop: $("#about").offset().top }, 450);
	});
	
	// "show / hide" buttons
	var coll = document.getElementsByClassName("collapsible");
	for (var i = 0; i < coll.length; i++) {
	  coll[i].nextElementSibling.style.display = "none";
	  coll[i].addEventListener("click", function() {
		this.classList.toggle("active");
		var content = this.nextElementSibling;
		if (content.style.display === "block") {
		  content.style.display = "none";
		} else {
		  content.style.display = "block";
		}
	  });
	}
	
	// lazy images for fast page loading
	$('.lazy').lazy({
			// with custom Google Scholar loaders
			draw_citations: function(element) {
				$.getScript('//d3js.org/d3.v4.min.js', function() {
					$.getScript('cv_files/gs_cite.js', function() {
						paint_gs_cites();
					});
				});},
			google_analytics: function(element) {
				$.getScript('//www.googletagmanager.com/gtag/js?id=UA-129904187-1', function() {
					// Google Analytics 
					window.dataLayer = window.dataLayer || [];
					function gtag(){dataLayer.push(arguments);}
					gtag('js', new Date());
					gtag('config', 'UA-129904187-1');
				});},
		});
});