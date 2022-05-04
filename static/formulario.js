$(document).ready(function () {
    var base_color = "rgb(230,230,230)";
    var active_color = "rgba(237,120,171,255)";
  
    var child = 1;
    var length = $("section").length - 1;
    $("#prev").addClass("disabled");
    $("#submit").addClass("disabled");
  
    $("section").not("section:nth-of-type(1)").hide();
    $("section")
      .not("section:nth-of-type(1)")
      .css("transform", "translateX(100px)");
  
    var svgWidth = length * 200 + 24;
    $("#svg_wrap").html(
      '<svg version="1.1" id="svg_form_time" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 ' +
        svgWidth +
        ' 24" xml:space="preserve"></svg>'
    );
  
    function makeSVG(tag, attrs) {
      var el = document.createElementNS("http://www.w3.org/2000/svg", tag);
      for (var k in attrs) el.setAttribute(k, attrs[k]);
      return el;
    }
  
    for (i = 0; i < length; i++) {
      var positionX = 12 + i * 200;
      var rect = makeSVG("rect", { x: positionX, y: 9, width: 200, height: 6 });
      document.getElementById("svg_form_time").appendChild(rect);
      // <g><rect x="12" y="9" width="200" height="6"></rect></g>'
      var circle = makeSVG("circle", {
        cx: positionX,
        cy: 12,
        r: 12,
        width: positionX,
        height: 6
      });
      document.getElementById("svg_form_time").appendChild(circle);
    }
  
    var circle = makeSVG("circle", {
      cx: positionX + 200,
      cy: 12,
      r: 12,
      width: positionX,
      height: 6
    });
    document.getElementById("svg_form_time").appendChild(circle);
  
    $("#svg_form_time rect").css("fill", base_color);
    $("#svg_form_time circle").css("fill", base_color);
    $("circle:nth-of-type(1)").css("fill", active_color);
  
    $(".button").click(function () {
      $("#svg_form_time rect").css("fill", active_color);
      $("#svg_form_time circle").css("fill", active_color);
      var id = $(this).attr("id");
      if (id == "next") {
        $("#prev").removeClass("disabled");
        if (child >= length) {
          $(this).addClass("disabled");
          $("#submit").removeClass("disabled");
        }
        if (child <= length) {
          child++;
        }
      } else if (id == "prev") {
        $("#next").removeClass("disabled");
        $("#submit").addClass("disabled");
        if (child <= 2) {
          $(this).addClass("disabled");
        }
        if (child > 1) {
          child--;
        }
      }
      var circle_child = child + 1;
      $("#svg_form_time rect:nth-of-type(n + " + child + ")").css(
        "fill",
        base_color
      );
      $("#svg_form_time circle:nth-of-type(n + " + circle_child + ")").css(
        "fill",
        base_color
      );
      var currentSection = $("section:nth-of-type(" + child + ")");
      currentSection.fadeIn();
      currentSection.css("transform", "translateX(0)");
      currentSection.prevAll("section").css("transform", "translateX(-100px)");
      currentSection.nextAll("section").css("transform", "translateX(100px)");
      $("section").not(currentSection).hide();
    });
  });
  


  $(document).ready(function() {
    var max_fields      = 10; //maximum input boxes allowed
    var wrapper         = $(".input_fields_wrap"); //Fields wrapper
  
    var add_button      = $(".add_field_button"); //Add button ID
    

    var x = 1; //initlal text box count
    $(add_button).click(function(e){ //on add input button click
        e.preventDefault();
        if(x < max_fields){ //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div><input type="text" name="mytext[]"/><a href="#" class="remove_field">Remover</a></div>'); //add input box
        }
    });

    $(wrapper).on("click",".remove_field", function(e){ //user click on remove text
        e.preventDefault(); $(this).parent('div').remove(); x--;
    })
});

$(document).ready(function() {
  var max_fields      = 10; //maximum input boxes allowed
  var wrapper2         = $(".input_fields_wrap2"); //Fields wrapper

  var add_button2      = $(".add_field_button2"); //Add button ID
  

  var x = 1; //initlal text box count
  $(add_button).click(function(e){ //on add input button click
      e.preventDefault();
      if(x < max_fields){ //max input box allowed
          x++; //text box increment
          $(wrapper).append('<div><input type="text" name="mytext2[]"/><a href="#" class="remove_field">Remover</a></div>'); //add input box
      }
  });

  $(wrapper).on("click",".remove_field", function(e){ //user click on remove text
      e.preventDefault(); $(this).parent('div').remove(); x--;
  })
});
  
