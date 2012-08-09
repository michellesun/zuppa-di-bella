$(function(){

   // Speaker Model
   // ----------
   window.SpeakerModel = Backbone.Model.extend();
   window.Speakers = Backbone.Collection.extend({
      model: SpeakerModel,
      url: '/scenario_speakers.js',
      findBySpeakerType: function(speaker_type){
         return this.where({speaker_type: speaker_type})[0];
      }

   });


   // Node Model
   // ----------

   window.NodeModel = Backbone.Model.extend({
      node_type: function() {
         return this.get('speaker').speaker_type;
      },
      speaker_name: function() {
         return window.speakers.get(this.get('speaker_id')).get('name');
      },
      speaker_type: function() {
         return window.speakers.get(this.get('speaker_id')).get('speaker_type');
      }
   });

   window.NextNodes = Backbone.Collection.extend({
      model: NodeModel,
      url: '/next_nodes'
   });



   window.TreeNodes = Backbone.Collection.extend({
      model: NodeModel,
      url: '/tree.js',
      lastNode: function(){
         return this.at(this.length-1);
      }
   });

   window.PreviewNodes = Backbone.collection.extend({
      model: NodeModel,
      url: '/next_nodes/tree',
      byPreviousNode: function(previous_node_id){
         return this.where({previous_node_id:previous_node_id});
      }
   });

   // Scenarios Model
   // ----------
   window.Scenario = Backbone.Model.extend();
   window.Scenarios = Backbone.Collection.extend({
      model: Scenario,
      url: '/scenarios.js'
   });

//-- VIEWS

   // NODE VIEW
   // ----------
   window.NodeView = Backbone.View.extend({
      template: _.template($("#node-template").html()),
      tagName: 'div',
      className: "span-center-inner",

      events: {
         'click .node-0': 'toNode',
         'click .node-1': 'toNode',
         'click .node--1': 'toNode',
         'hover': 'overNode',
         'mouseenter': 'enterNode',
         'mouseleave': 'outNode',
         'click .node-delete': 'deleteNode'

      },
      initialize: function() {
         _.bindAll(this, 'render','toNode', 'overNode');
         this.model.bind('reset', this.render);
      },
      render: function() {
         $(this.el).empty().append(this.template(this.model.toJSON()));
         this.$el.find('.node-side').hide();
         return this;
      },
      toNode: function(){
         treeNodesView.update(this.model.get('id'));
      },

      overNode: function() {
         this.$el.toggleClass('span-center-current');
         //var side_template = _.template($("#node-side-template").html());
         //this.$el.find('.node-side').append(side_template());
         this.$el.find('.node-side').toggle();
         //this.$el.find('.node-side').children().slideToggle('fast', function() {});


         // - $('.span-right-container').position().top
         return this;
      },

      enterNode: function() {
         $('.span-right-active').show();
         $('.span-right-active').css({'margin-top': this.$el.position().top - $('.span-right-active').offsetParent().position().top + "px", 'height': this.$el.height()+"px"});


      },
      outNode: function() {
         $('.span-right-active').css({'height': "0px"});

//         this.$el.removeClass('span-center-current');
//         this.$el.find('.node-side').slideUp('fast', function() {this.$el.find('.node-side').empty();});
      },

      deleteNode: function() {
         this.model.destroy({success: function(model, response) {
            console.log(response);
         }}, {silent: true});
      }
   });

   // TREE VIEW
   // ----------
   window.TreeNodesView = Backbone.View.extend({

      initialize: function() {
         _.bindAll(this, 'render');
         this.collection.bind('reset', this.render);
         //this.collection.bind('change', this.render);
      },
      render: function() {
         $(this.el).detach();
         $(this.el).empty();

         _.each(this.collection.models, function(node){
            node.set("speaker_type", node.speaker_type(),{silent: true});
         });


         _.each(this.collection.models, function(node){

            var nodeView = new NodeView({
               model: node
            });
            $(this.el).append(nodeView.render().el);
         }, this);
         $('#tree_nodes').empty().append($(this.el));
         //-- resize node to below 200 px --//

         resizeNodes($('#tree_nodes'));

         window.nextNodesView.update(this.collection.lastNode().get('id')); // render next nodes
         return this;

      },
      update: function(node_id) {
         this.collection.fetch({ data: $.param({ id: node_id}) });
      },
      initialTree: function(scenario_id) {
         this.collection.fetch({ data: $.param({ scenario_id: scenario_id}) });
         // remove next nodes for initial scenario load.
         // feature to build : memory
         $('#next_nodes').empty();

      }
   });

   // NEXT NODES VIEW
   // ----------
   window.NextNodesView = Backbone.View.extend({
      template: _.template($("#next_nodes-template").html()),
      initialize: function() {
         _.bindAll(this, 'render');
         this.collection.bind('reset', this.render);
         //this.collection.bind('change', this.render);
      },
      render: function() {
         //-- hack to insert the nested property "speaker_type" as a root parameter; --//
         _.each(this.collection.models, function(node){
            node.set("speaker_type", node.speaker_type(),{silent: true});
         });
         //this.collection.sort({silent: true});

         $(this.el).detach();
         $(this.el).empty();

         if (this.collection.length > 0) {
            this.renderBySpeaker(0);
            this.renderBySpeaker(1);
            this.renderBySpeaker(-1);
         } else {
            // if no next nodes, then
            this.appendNextSpeakerText(toggleSpeaker(window.treeNodes.lastNode().get('speaker_type')));
            this.appendInput(toggleSpeaker(window.treeNodes.lastNode().get('speaker_type')));
         }
         $('#next_nodes').append($(this.el));
         //-- resize node to below 200 px --//
         resizeNodes($('#next_nodes'));

         return this;
      },

      update: function(scenario_id) {
         //var scenario_id = scenario.get('id');
         this.collection.fetch({ data: $.param({ id: scenario_id}) });
         // NTD: this triggers the render function

      },
      renderBySpeaker: function(speaker_type){
         var nextNodesCollection = this.collection.where({speaker_type: speaker_type});
         if (nextNodesCollection.length >= 1){

            //-- insert speaker introduction text
            this.appendNextSpeakerText(speaker_type);
            //nextNodesCollection[0].get('speaker_id')

            //-- insert next nodes
            _.each(nextNodesCollection, function(node){
               //-- output the next node --//
               var nodeView = new NodeView({
                  model: node
               });
               $(this.el).append(nodeView.render().el);

            }, this);
            //-- insert input field --//
            this.appendInput(speaker_type);
         }
      },

      appendNextSpeakerText: function(speaker_type){
         var nextSpeakerModel = window.speakers.findBySpeakerType(speaker_type);
         var nextSpeakerView = new NextSpeakerView ({
            model: nextSpeakerModel
         });
         $(this.el).append(nextSpeakerView.render().el);

      },

      appendInput: function(speaker_type){
         $(this.el).append('<div id="endNextNodesSpeaker'+speaker_type+'"></div>');
         var nodeInputModel = new NodeModel();
         nodeInputModel.set({
            speaker_type: speaker_type,
            speaker_id: window.speakers.findBySpeakerType(speaker_type).get('id')
         });
         var nodeInputView = new NodeInputView ({model:nodeInputModel});
         $(this.el).append(nodeInputView.render().el);
      }

   });


   window.PreviewTreeView = Backbone.View.extend({

      initialize: function() {
         //_.bindAll(this, 'render');
         //this.collection.bind('reset', this.render);
      },
      render: function() {
         $(this.el).detach();
         $(this.el).empty();

         renderBranch(id);
         //-- resize node to below 200 px --//

         resizeNodes($('#tree_nodes'));


         return $(this.el);

      },
      renderBranch: function(previous_node_id){
         _.each(this.collection.byPreviousNode(previous_node_id), function(branch){
            if (branch.length > 0) {
               var previewNodeView = new PreviewNodeView({
                  model: node
               });
               $(this.el).append(previewNodeView.render().el);
            }
         }, this);
      }
   });


// Next Speakers.
   window.NextSpeakerView = Backbone.View.extend({
      template: _.template($("#next_speaker_label-template").html()),
      initialize: function() {
         _.bindAll(this, 'render');
         this.model.bind('reset', this.render);
      },
      render: function() {
         $(this.el).empty().append(this.template(this.model.toJSON()));
         return this;
      }
   });

//-- Speakers View --//
   window.SpeakersView = Backbone.View.extend({
      initialize: function() {
         _.bindAll(this, 'render');
         this.collection.bind('reset', this.render);
      },
      render: function() {
         var speaker_0 = this.collection.where({speaker_type: 0});
         var speaker_1 = this.collection.where({speaker_type: 1});
         //var speaker_event = this.collection.where({speaker_type: -1});
         $('#label-speaker0').empty().append(speaker_0[0].get('name'));
         $('#label-speaker1').empty().append(speaker_1[0].get('name'));

         // render treeNodes
         window.treeNodesView.initialTree(window.currentScenario);
         return this;
      },
      update: function(scenario_id) {
         //var scenario_id = scenario.get('id');
         this.collection.fetch({ data: $.param({ id: scenario_id}) });
      }
   });

   window.ScenarioView = Backbone.View.extend({
      template: _.template($("#scenario-template").html()),
      tagName: 'li',

      events: {
         'click .nav-scenario': 'renderInitialNodes'
      },

      initialize: function() {
         _.bindAll(this, 'render');
         this.collection.bind('reset', this.render);
         this.collection.bind('change', this.render);
      },

      render: function() {
         $(this.el).empty().append(this.template(this.model.toJSON()));
         return this;
      },

      renderInitialNodes: function() {
         // set global variable;
         window.currentScenario = this.model.get('id');
         $(".span-center").show(); // Show the center section.
         //window.speakersView.update(this.model.get('id'));

         window.speakers.fetch({ data: $.param({ id: this.model.get('id')}) });

         $(".scenario_name").empty().append(this.model.get('name'));
         $(".scenario_description").empty().append(this.model.get('description'));
         //update speakers collection based on scenario ID
         return this;
      }

   });

   window.ScenarioListView = Backbone.View.extend({

      tagName: 'ul',
      className: 'nav nav-list',

      initialize: function() {
         _.bindAll(this, 'render');

         //window.template = _.template($("#scenarios-template").html());

         this.collection.bind('reset', this.render);
      },
      render: function() {
         var collection =  this.collection;
         var $scenarios = $(this.el);
         collection.each(function(scenario){
            var view = new ScenarioView({
               model: scenario,
               collection: collection
            });
            $scenarios.append(view.render().el);
         });
         return this;
      }
   });

   // NODE INPUT VIEW
   // ----------
   window.NodeInputView = Backbone.View.extend({
      template: _.template($("#node-input-template").html()),
      tagName: 'div',
      className: "span-center-inner",

      events: {
         "keypress .form-node":  "createNewNode"
      },

      initialize: function() {
         _.bindAll(this, 'render','createNewNode');
      },

      render: function() {
         $(this.el).empty().append(this.template(this.model.toJSON()));
         this.input = this.$('#node_new_'+this.model.get('speaker_type'));
         return this;
      },

      createNewNode: function(e) {
         if (e.keyCode == 13) {
            e.preventDefault();
            var newNode = window.nextnodes.create(this.newNodeData());
            newNode.set("speaker_type", newNode.speaker_type(),{silent: true});
            var nodeView = new NodeView({
               model: newNode
            });
            $('#endNextNodesSpeaker'+this.model.get('speaker_type')).before(nodeView.render().el);
            this.input.val('');
         }
      },

      // Generate the attributes for the new node
      newNodeData: function() {
         return {
            node_text: this.input.val(),
            previous_node_id:   treeNodes.lastNode().get('id'),
            speaker_id:  this.model.get('speaker_id'),
            scenario_id: window.currentScenario,
            user_id: 0, // need to fix this
            node_type: 1
         };
      }
   });

   var AppRouter = Backbone.Router.extend({
      routes: {
         '': 'home'
      },

      initialize: function() {
         // should instantiate root level views
         window.scenarioslist = new Scenarios();

         window.scenariolistView = new ScenarioListView({
            collection: window.scenarioslist
         });

         // speakers
         window.speakers = new Speakers();
         window.speakersView = new SpeakersView ({
            collection: window.speakers
         });

         // tree view
         window.treeNodes = new TreeNodes();

         window.treeNodesView = new TreeNodesView ({
            collection: window.treeNodes
         });

         // next node view
         window.nextnodes = new NextNodes();

//         window.nextnodes.comparator = function(node) {
//            return node.get("speaker_type");
//         };

         window.nextNodesView = new NextNodesView ({
            collection: window.nextnodes
         });


      },

      home: function() {
          window.scenarioslist.fetch();
         $("#scenarios_list").append(window.scenariolistView.render().el);

         $(".span-center").hide(); // Hide the center section.
         $('.span-right-active').hide();
   },

      render: function(){

      }

   });

   $(function() {
      var app = new AppRouter();
      Backbone.history.start();

   });

   function resizeNodes(nodeTarget) {
      nodeTarget.find('button.node-0').each(function(element){
         $(this).width(Math.min(Math.ceil($(this).outerWidth()),200));
      });
      nodeTarget.find('button.node-1').each(function(element){
         $(this).width(Math.min(Math.ceil($(this).outerWidth()),200));
      });
   }

   function toggleSpeaker(speaker_type){
      if (speaker_type == 1) {
         return 0;
      } else if (speaker_type == 0) {
         return 1;
      } else {
         return speaker_type;
      }
   }

});