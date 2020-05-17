
//alert('0element');

var pad= function (x)   { return x.toString().padStart(2, "0"); };
var pretty= function (x) { return x.split( '\n' ).join( '<br>' ); };
var iframe= function (vid) {
	return ` <iframe width="440" height="248" src="https://www.youtube.com/embed/${vid}?rel=0&amp;mute=1&cc_load_policy=1" frameborder="0" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> `;
   };

var img=  function (src) { return ` <img width=440 height=248 src='${src}'> `; }; 

var wrap= function (e) {
   var i;

   i= {};
   i.e= e;
   i.isdebug= false;
   i.ispretty= false;

   i.debug= function (id) { i.isdebug= true; return i; };
   i.pretty= function (id) { i.ispretty= true; return i; };

   i.setid= function (id) { i.e.id= id; return i; };
   i.setcn= function (x) { i.e.className= x; return i; };
   i.setsrc= function (x) { i.e.src= x; return i; };
   i.sethref= function (x) { i.e.href= x; return i; };
   i.settype= function (x) { i.e.type= x; return i; };
   i.setfontsize= function (x) { i.e.style.fontSize= x; return i; };
   i.setmarginleft= function (x) { i.e.style.marginLeft= x; return i; };
   i.setborder= function (x) { i.e.style.border= x; return i; };
   i.setborderleft= function (x) { i.e.style.borderLeft= x; return i; };
   i.setbackgroundcolor= function (x) { i.e.style.backgroundColor= x; return i; };
   i.setwidth= function (x) { i.e.style.width= x; return i; };
   i.setheight= function (x) { i.e.style.height= x; return i; };
   i.setvalue= function (x) { i.e.value= x; return i; };
   i.sethtml= function (x) {
	   var t= x;
	   if (x) {
		   if (i.isdebug) t= `${i.eT}=${x}`;
		   if (i.ispretty) t= pretty(t);
	   	   i.e.innerHTML= t;
	   }
	   return i;
   };

   i.setonclick= function (f) { i.e.onclick= f; return i; };
   i.getsrc= function (x) { return i.e.src; };

   i.replaceWith= function (c) { i.e.replaceWith(c.e); };

   i.appendTo= function (p) { p.e.appendChild(i.e); return i; };
   i.appendx= function (o) { return function (k,n) { if (o[k]) o[k].appendTo(i); }; };
	return i;
};


var sing= {
   find: function (id) { var e= document.getElementById(id); return wrap(e); },
   create: function (eT) { var e= document.createElement(eT); var w= wrap(e); w.eT= eT; return w; },
   b: wrap(document.body),
   h: wrap(document.head)
};


var sing2= {
   div: function (x) { return sing.create('div').sethtml(x); },
   button: function (x) { return sing.create('button').sethtml(x); },
   p: function (x) { return sing.create('p').sethtml(x); },
   a: function (x) { return sing.create('a').sethref(x).sethtml('link'); },
   mark: function (x) { return sing.create('mark').sethtml(x); },
   input: function (x) { 
	   return sing.create('input').settype( "text" ).setvalue(x);
   },
   y2: function (vid) {
	   var src= `https://www.youtube.com/embed/${vid}?rel=0&amp;mute=1&cc_load_policy=1`;
	   var w= sing.create('iframe').setsrc(src);
	   w.e.frameborder= 0;
	   w.e.width= 0; w.e.height= 0;
	   w.e.allow= "fullscreen; accelerometer; encrypted-media; gyroscope; picture-in-picture";
	   return w;
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
	var g= function () {  a.replaceWith(b); };
	var g2= function () {  b.replaceWith(a); };
                a.setonclick(g);
                b.setonclick(g2);
};

var zipme= function (a,b) { return a.map( function(e, i) { return [e, b[i]]; } ); };


