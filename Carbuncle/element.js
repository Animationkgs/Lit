


var wrap= function (e) {
   var i;

   i= {};
   i.e= e;

   i.setid= function (id) { i.e.id= id; return i; };
   i.setcn= function (x) { i.e.className= x; return i; };
   i.setsrc= function (x) { i.e.src= x; return i; };
   i.settype= function (x) { i.e.type= x; return i; };
   i.setvalue= function (x) { i.e.value= x; return i; };
   i.sethtml= function (x) { if (x) i.e.innerHTML= x; return i; };
   i.setonclick= function (f) { i.e.onclick= f; return i; };
   i.getsrc= function (x) { return i.e.src; };

   i.replaceWith= function (c) { i.e.replaceWith(c.e); };

   i.appendTo= function (p) { p.e.appendChild(i.e); return i; };
   i.appendx= function (o) { return function (k,n) { if (o[k]) o[k].appendTo(i); }; };
	return i;
};


var sing= {
   find: function (id) { var e= document.getElementById(id); return wrap(e); },
   create: function (eT) { var e= document.createElement(eT); return wrap(e); },
   b: wrap(document.body),
   h: wrap(document.head)
};


var sing2= {
   div: function (x) { return sing.create('div').sethtml(x); },
   input: function (x) { 
	   return sing.create('input').settype( "text" ).setvalue(x);
   },
   style: function (x) { return sing.create('style').sethtml(x); }
};


var preset= function () {
   var i;
   i= {};
   i.d= new Map();

   i.publish= function (w) { for ( let [k,v] of i.d ) w[k](v); return w;};
   i.publishx= function (x,n) { i.publish(x); };
   i.pushTo= function (p) { i.d.set('appendTo', p); return i; };
   i.setcn= function (cn) { i.d.set('setcn', cn); return i; };
   i.setid= function (id) { i.d.set('setid', id); return i; };
   i.setsrc= function (x) { i.d.set('setsrc', x); return i; };
   i.settype= function (x) { i.d.set('settype', x); return i; };
   i.setvalue= function (x) { i.d.set('setvalue', x); return i; };
   i.sethtml= function (x) { i.d.set('sethtml', x); return i; };
   i.setonclick= function (f) { i.d.set('setonclick', f); return i; };
	return i;
};

var pair= function(a,b) {
	var g= function () { a.replaceWith(b); };
	var g2= function () { b.replaceWith(a); };
                a.setonclick(g);
                b.setonclick(g2);
};
