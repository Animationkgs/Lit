


var vidf= vid.map(iframe);
var fj= function(x) {
	var v= 'v'+x.replace('-','_');
	if (window.hasOwnProperty(v)) return window[v];
	return {title: v};
};
var vidj= vid.map(fj);
vid= zipme(vid,vidj);
var g= function(x) {
	var ret= { id: x[0], json: x[1] }; 
	ret.title= ret.json.title;
	return ret;
}
vid= vid.map(g);
