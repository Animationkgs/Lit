




var suitNames = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'];

function cardsEliminated(c) {
	var r = c.data('rank'), s = c.data('suit');
	var p = $('#parade .card');
	var n = p.length;
	return p.filter(function(i,o) {
		var c2 = $(o);
		return i < n-r && (c2.data('rank') <= r || c2.data('suit') == s);
	});
}

function cardClick() {
	var c = $(this).removeClass('willEliminate');
	c.replaceWith($('<div>', { 'class': 'placeholder' }));
	var e = cardsEliminated(c).each(function(i,o) {
		$(o).removeClass('card').addClass('placeholder').fadeOut("normal", function() { $(this).remove(); });
	});
	var n = $('#parade').append(c).find('.card').length;
	$('#parade_length').text(n + ' ' + (n == 1 ? 'card' : 'cards'));
	$('#deck .card').removeClass('willEliminate').filter(function(i,o) {
		return cardsEliminated($(o)).length > 0;
	}).addClass('willEliminate');
}

function makeCard(r, s, c='card') {
	return $('<div>', { 'class': c, 'data-rank': r, 'data-suit': s }).append(
		$('<span>', { 'class': 'rank', 'text': r }),
		$('<span>', { 'class': 'suit', 'text': suitNames[s] })
	).css('background-color', colours[s]);
}

function reset(maxRank, suits) {
	$('#parade').empty();
	$('#deck').empty();
	$('#parade_length').text('0 cards');
	for(var s = 0; s < suits; ++s) {
		var rowElem = $('<div>', { 'class': 'deck-row' });
		for(var r = 0; r <= maxRank; ++r) {
			var cardElem = makeCard(r, s);
			rowElem.append(cardElem);
			cardElem.on('click', cardClick);
		}
		$('#deck').append(rowElem);
	}
}

$(document).ready(function() {
	$('#help .parade').append(
		makeCard(8, 2, 'placeholder'),
		makeCard(2, 0, 'placeholder'),
		makeCard(5, 0, 'placeholder'),
		makeCard(1, 1, 'placeholder'),
		makeCard(3, 3, 'placeholder')
	);
	$('#help').append(makeCard(2, 2, 'placeholder willEliminate'));

	$('#help .suitA').css('color', colours[0]);
	$('#help .suitB').css('color', colours[1]);
	$('#help .suitC').css('color', colours[2]);
	$('#help .suitD').css('color', colours[3]);

	$('#reset').on('click', function() { reset(10, 6); }).click();

	$('#help_button').on('click', function() { $('#help').show(); });
	$('#help').on('click', function() { $('#help').hide(); });
});
