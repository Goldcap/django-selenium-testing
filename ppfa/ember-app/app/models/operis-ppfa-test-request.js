import Ember from 'ember';
import DS from "ember-data";

var OperisPpfatestrequest = DS.Model.extend(Ember.Validations.Mixin,{
  ppfa_test: DS.belongsTo('ppfa_test'),
  request_date: DS.attr('isodate')
});
export default OperisPpfatestrequest;