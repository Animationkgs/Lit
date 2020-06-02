

//alert('0fill');

var div= sing2.div;
var mark= sing2.mark;
var button= sing2.button;
var p= sing2.p;
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
			fill(d2,n+'.'+x,v[x]);
		}
	}
	};
	      b.setonclick(f);
	return dfull;
};
//fill(sing.b,'.',kv);

var fill2= function(d,n,v,depth=0) {
	var node= div().appendTo(d).setmarginleft(depth+'em').setborderleft('solid').setwidth('10000');
	if (isobj(v)) {}
	else {
		node.setborderleft('solid');
		mark(n+'='+v).setcn('small').appendTo(node).setborder('none').setbackgroundcolor('orange');
		return null;
	}
	var head= div().appendTo(node).setborder('none').setcn('inline');
	var name= mark(n).appendTo(head).setbackgroundcolor('gainsboro');
	var b= button('+').appendTo(head);
	var dempty= div().appendTo(node).setborder('none');
	var dfull= div().setborder('none');
	var c= 0;
      var f= function () {
         c++;
	if ((c%2)==1) {
		dempty.replaceWith(dfull);
		b.sethtml('-');
		if (c==1) if (isobj(v)) {
			for (x in v) fill2(dfull,n+'.'+x,v[x],depth+1);
		}
	}
	else { dfull.replaceWith(dempty); b.sethtml('+'); }
      };
	      b.setonclick(f);
	return null;
};





var fill3= function(d,n,v,depth=0) {
	var node= div().appendTo(d).setmarginleft(depth+'em').setborderleft('solid').setwidth('10000');
	if (isobj(v)) {}
	else {
		node.setborderleft('solid');
		mark(n+'='+v).setcn('small').appendTo(node).setborder('none').setbackgroundcolor('orange');
		return null;
	}
	var head= div().appendTo(node).setborder('none').setcn('inline');
	var name= mark(n).appendTo(head).setbackgroundcolor('gainsboro');
	var b= button('+').appendTo(head);
	var t= '';
	if (v.hasOwnProperty('title')) t= v.title;
	var text= mark(t).appendTo(head).setbackgroundcolor('orange');

	var dempty= div().appendTo(node).setborder('none');
	var dfull= div().setborder('none');
	var c= 0;
      var f= function () {
         c++;
	if ((c%2)==1) {
		dempty.replaceWith(dfull);
		b.sethtml('-');
		if (c==1) if (isobj(v)) {
			for (x in v) fill3(dfull,n+'.'+x,v[x],depth+1);
		}
	}
	else { dfull.replaceWith(dempty); b.sethtml('+'); }
      };
	      b.setonclick(f);
	return null;
};
