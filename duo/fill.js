

//alert('0fill');

var div= sing2.div;
var mark= sing2.mark;
var button= sing2.button;
var p= sing2.p;
var isobj= function (x) { return (typeof x === 'object' && x!==null ); };


var fill3= function(d,n,v,depth=0) {
	var node= div().appendTo(d).setmarginleft(depth+'em').setborderleft('solid').setwidth('10000');
	if (isobj(v)) {}
	else {
		if (n=='repr') return null;
		node.setborderleft('solid');
		key= `<span style= "background-color: orange"> ${n} </span>`;
		value= `<span style= "background-color: linen"> ${v} </span>`;
		mark(key+'='+value).setcn('small').appendTo(node).setborder('none').setbackgroundcolor('orange');
		return null;
	}
	var head= div().appendTo(node).setborder('none').setcn('inline');
	var name= mark(n).appendTo(head).setbackgroundcolor('gainsboro');
	var b= button('+').appendTo(head);
	var t= 'blank';
	if (v.hasOwnProperty('repr')) { t= v['repr']; }
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
			for (x in v) fill3(dfull,x,v[x],depth+1);
		}
	}
	else { dfull.replaceWith(dempty); b.sethtml('+'); }
      };
	      b.setonclick(f);
	return null;
};
