parse_player_info = function (players) {
        var player_list = [];
        players = players.split('"');
        for (var i = 0; i < players.length; i++) {
            if (i % 2 == 1) {
                var player = players[i];
                player = JSON.parse(player.replace(/'/g, '"'));
                player['location'] = parse_location(player['location']);
                player['base'] = parse_location(player['base']);
                player_list.push(player)
            }
        }
        return player_list
    };

parse_location = function (location) {
    location = location.replace(/[()\s]/g, '').split(',');
    var x = parseInt(location[0]);
    var y = parseInt(location[1]);
    return [x, y]
};