import Ember from 'ember';
import DS from "ember-data";

var OperisPpfatest = DS.Model.extend(Ember.Validations.Mixin,{
  name: DS.attr('string'),
  location: DS.attr('string'),
  date_created: DS.attr('isodate'),
  last_run: DS.attr('isodate'),
  status: DS.attr('boolean'),
  ppfa_test_runs: DS.hasMany('ppfa_test_runs',{async:true}),
  ppfa_test_assertions: DS.hasMany('ppfa_test_assertions',{async:true}),
  ppfa_test_steps: DS.hasMany('ppfa_test_steps',{async:true}),
  ppfa_test_requests: DS.hasMany('ppfa_test_requests',{async:true})
});
export default OperisPpfatest;