function openWebsocket() {
	console.log("Opening websocket");
	var endpoint = "wss://mgwws.hana.ondemand.com/endpoints/v1/ws";
	var topic = "in/nait/alex/codStats";
	var ws = new WebSocket(endpoint);

	ws.onopen = function () {
		var subscribe = '{"subscribe":"' + topic + '"}';
		ws.send(subscribe);
	};

	var self = this;
	ws.onclose = function () {
		console.log("Closing websocket")
		self.openWebsocket();
	};

	ws.onmessage = function (evt) {
		console.log("Receiving message");
        	var msg = JSON.parse(evt.data);
        	console.log(msg);
        	incrementCard();
	};
}
openWebsocket(); 
