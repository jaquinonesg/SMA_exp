
$(function() {
    var $canvas = $("canvas");
    $canvas.attr("width", window.innerWidth);
    $canvas.attr("height", window.innerHeight);
    
    var ctx = $canvas[0].getContext('2d');
    ctx.globalCompositeOperation = 'lighter';
    ctx.globalOpacity = 0.7;
    var catX = window.innerWidth * 0.85 - 370;
    var catEyes = {
      "x1": catX,
      "y1": window.innerHeight - 380,
      "x2": catX + 55,
      "y2": window.innerHeight - 309
    }
    
    ctx.fillStyle = "#ff4422";
    
    function extendVector(x1,y1, x2,y2, scale) {
      var slope = (y2 - y1) / (x2 - x1);
      var amplitude = Math.sqrt((y2 - y1)^2 + (x2 - x1)^2);
      
      var newX = x1 - scale * (x1 - x2);
      if (newX > catX) {
        newX = window.innerWidth;
      } else {
        newX = 0;
      }
      
      return {
        "x1": x1,
        "y1": y1,
        "x2": newX,
        "y2": y1 - (x1 - newX) * slope
      }
    }
    
    function drawLasers(mousePos) {
      ctx.globalCompositeOperation = 'lighter';
      var spread = Math.min(Math.abs(600 - mousePos.x), 720); 
      
      var scaled = extendVector(catEyes["x2"], catEyes["y2"],mousePos.x, mousePos.y +spread *0.3, 5);
      ctx.beginPath();
      ctx.moveTo(scaled["x1"], scaled["y1"]);
      ctx.lineTo(scaled["x2"], scaled["y2"]);
      ctx.stroke();
      
      scaled = extendVector(catEyes["x1"], catEyes["y1"],mousePos.x, mousePos.y - spread * 0.3, 5);
      ctx.beginPath();
      ctx.moveTo(scaled["x1"], scaled["y1"]);
      ctx.lineTo(scaled["x2"], scaled["y2"]);
      ctx.stroke();
      
      ctx.globalCompositeOperation = 'darken';
      ctx.fillStyle = "rgba(0,0,0,0.05)";
      ctx.font = "700 750px Helvetica";
      ctx.fillText("404", 350, 650);
    }
    
    function handler(evt) {
      var mousePos = {
        x: evt.clientX,
        y: evt.clientY
      };
      ctx.strokeStyle = "#ff5522";
      ctx.lineWidth = 8;
      drawLasers(mousePos);
      
    }
    $canvas.on('mousemove', handler);
    $canvas.on('touchmove', handler);
  });
  