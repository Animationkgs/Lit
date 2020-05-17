
var div= sing2.div;
var button= sing2.button;
var isobj= function (x) { return (typeof x === 'object' && x!==null ); };

var fill = function (d,n,v) {
      var b= button(n).appendTo(d);
      var dempty= div().appendTo(d);
      var dfull= div(v);
      var c= 0;
      var f= function () {
         c++;
	if ((c%2)==1) dempty.replaceWith(dfull);
	else dfull.replaceWith(dempty);
	if (c==3) if (isobj(v)) {
		alert('isobj');
		for (x in v) {
			var d2= div().appendTo(dfull);
			fill(d2,x,v[x]);
		}
	}
	};
	      b.setonclick(f);
	return dfull;
};
//fill(sing.b,'.',kv);

