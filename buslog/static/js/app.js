var Chofer = React.createClass({
	render: function(){
		return(
			<option value={this.props.pk} >
				{this.props.nombre}
			</option>
		)
	}
});

var ListaChofer = React.createClass({
	getInitialState: function(){
		return {
			choferes : []
		}
	},
	componentWillMount: function(){
		var self = this;
		var chofer;
		var pagina;

		$.getJSON("http://127.0.0.1:8000/choferes/", function(data){
			for(pagina in data){
				//console.log("->",pagina,data[pagina]);
				for(chofer in data[pagina]){
					//console.log(chofer,data[pagina][chofer]);
					chofer = data[pagina][chofer];
					//console.log(chofer.pk,chofer.nombre);
					self.add(chofer);
				}
			}
			
		});
	},
    add: function(chofer) {
        var arr = this.state.choferes;
        arr.push(chofer);
        this.setState({choferes: arr});
    },
	eachItem: function(chofer,i){
		return(
				<Chofer key={i} index={i} 
					pk={chofer.pk} nombre={chofer.nombre} />
			)
	},
	render: function(){
		return(
				<div>
					<label htmlFor="select-choferes">Chofer:</label>
					<select id="select-choferes">
						{this.state.choferes.map(this.eachItem)}
					</select>
				</div>
			)
	}
});

ReactDOM.render(<ListaChofer />,document.getElementById('div-choferes'));