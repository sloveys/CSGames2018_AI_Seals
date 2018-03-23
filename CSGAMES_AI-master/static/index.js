$(document).ready(function () {

    var socket = io.connect('http://' + document.domain + ':' + location.port);
    var game_history = [];

    var tile_width = 32;

    var canvas = $('#gameCanvas')[0];

    var slider = $('#gameSlider')[0];
    slider.oninput = function () {
        update_canvas()
    };

    var canvas_updated = false;

    var play = false;
    setInterval(function () {
        if (play){
            var current_value = parseInt(slider.value);
            slider.value = (current_value + 1).toString();
            update_canvas()
        }
    }, 100);

    $('.startButton').on('click', function () {
        game_history = [];
        socket.emit('start');
        $('.startButton').text('Restart');
        play = true
    });

    $('#playButton').on('click', function () {
        play = true
    });

    $('#stopButton').on('click', function () {
        play = false
    });

    socket.on('next turn', function (data) {
        game_history.push(data);
    });

    var get_current_state = function () {
        var index = parseInt(slider.value) - 1;
        var game_state = null;
        if (index > game_history.length){
            game_state = game_history[game_history.length - 1]
        }
        else{
           game_state = game_history[index];
        }
        return game_state
    };

    var update_canvas_size = function (map) {
        var map_height = 0;
            for (var k = 0; k < map.length; k++) {
                var char = map[k];
                if (char == '\n'){
                    map_height += 1
                }
            }
            var map_width = map.length / map_height - 1;

            canvas.width = tile_width * map_width;
            canvas.height = tile_width * map_height;
    };

    var update_canvas = function () {
        var game_state = get_current_state();
        if (game_state){
            var map = game_state['game_state'];
            var players = parse_player_info(game_state['player_info']);
            slider.max = (1000 * players.length).toString();

            if (canvas_updated == false){
                update_canvas_size(map);
                canvas_updated = true
            }

            var canvas_context = canvas.getContext('2d');
            display_map(canvas_context, map);
            display_players(canvas_context, players);
            display_base(canvas_context, players);
            display_player_info();
        }
    };

    var display_player_info = function () {
        var container = $('#playerInfoContainer');
        var html = '';

        var game_state = get_current_state();
        var players = parse_player_info(game_state['player_info']);

        for (var i = 0; i < players.length; i += 1) {
            var id = players[i]['id'];
            var health = players[i]['health'];
            var carrying = players[i]['carrying'];
            var points = players[i]['points'];
            var status = players[i]['status'];
            var spawn = players[i]['spawn'];
            var name = players[i]['name'];
            var character_html = '<div class="playerInfo"><div>' + id + ' - ' + name + '</div>' +
                                 '<div>Health: ' + health + '</div>' +
                                 '<div>Points: ' + points + '</div>' +
                                 '<div>Carrying: ' + carrying + '</div>' +
                                 '<div>Status: ' + status + '</div>' +
                                 '<div>Spawn In: ' + spawn + '</div></div>';
            html += character_html
        }
        container.html(html)
    };

    var display_base = function (canvas_context, players) {
        for (var i = 0; i < players.length; i += 1) {
            var x = players[i]['base'][0];
            var y = players[i]['base'][1];


            canvas_context.fillStyle = '#338DFF';
            canvas_context.fillRect(y * tile_width, x * tile_width, tile_width, tile_width);
            write(canvas_context, players[i]['id'], x, y)
        }
    };

    var display_players = function (canvas_context, players) {
        for (var i = 0; i < players.length; i += 1) {
            if (players[i]['status'] == 'alive'){
                var x = players[i]['location'][0];
                var y = players[i]['location'][1];
                write(canvas_context, players[i]['id'], x, y)
            }
        }
    };

    var write = function(canvas_context, text, x, y){
        canvas_context.fillStyle = '#FFFFFF';
        canvas_context.font = '32px sans-serif';
        var width = canvas_context.measureText(text).width;
        var pad_x = (tile_width - width) / 2;
        canvas_context.fillText(text, y * tile_width + pad_x, (x + 1) * tile_width - 3)
    };

    var display_map = function (canvas_context, map) {
        var i = 0;
        var j = 0;
        for (var k = 0; k < map.length; k++) {
            var char = map[k];
            if (char == '0') {
                canvas_context.fillStyle = '#8B4513'; //Ground = Brown
            }
            else if (char == '1') {
                canvas_context.fillStyle = '#228B22'; //Tree = Green
            }
            else if (char == '2') {
                canvas_context.fillStyle = '#0000FF'; //Water = Blue
            }
            else if (char == 'J') {
                canvas_context.fillStyle = '#FF0000'; // Red
            }
            else if (char == 'S'){
                canvas_context.fillStyle = '#C0C0C0'; // Spike = Silver
            }

            else if (char == '\n') {
                i += 1;
                j = 0;
                continue;
            }
            else {
                canvas_context.fillStyle = '#000000'
            }
            canvas_context.fillRect(j * tile_width, i * tile_width, tile_width, tile_width);
            j += 1
        }
    };
});