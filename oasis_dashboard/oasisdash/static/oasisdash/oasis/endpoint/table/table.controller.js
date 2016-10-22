(function () {
    'use strict';

    /**
     * @ngdoc overview
     * @name BaysTableController
     * @ngController
     *
     * @description
     * Controller for the container-infra bay table
     */
    angular
        .module('horizon.dashboard.oasisdash.endpoint')
        .controller('EndpointTableController', EndpointTableController);

    EndpointTableController.$inject = [
        '$scope',
        '$location',
        'horizon.app.core.openstack-service-api.oasisdash',
        'horizon.dashboard.oasisdash.endpoint.events',
        'horizon.framework.conf.resource-type-registry.service',
        'horizon.dashboard.oasisdash.endpoint.resourceType',
        'horizon.framework.widgets.modal.wizard-modal.service',
        'horizon.dashboard.oasisdash.endpoint.detailworkflow',
        'horizon.dashboard.oasisdash.endpoint.endpointDetailModel'
    ];

    function EndpointTableController($scope, $location, oasis, events, registry, endpointResourceType, wizardModalService, detailWorkFlow, model) {
        var ctrl = this;

        ctrl.endpoint = [];
        ctrl.endpointSrc = [];
        ctrl.endpointResource = registry.getResourceType(endpointResourceType);
        ctrl.showDetailModal = showDetailModal;

        /**
         * Filtering - client-side MagicSearch
         * all facets for endpoint table
         */
        ctrl.endpointFacets = [
            {
                'label': gettext('Name'),
                'name': 'name',
                'singleton': true
            },
            {
                'label': gettext('ID'),
                'name': 'id',
                'singleton': true
            },
            {
                'label': gettext('Status'),
                'name': 'status',
                'singleton': true
            }
        ];

        var createWatcher = $scope.$on(events.CREATE_SUCCESS, onCreateSuccess);
        //var deleteWatcher = $scope.$on(events.DELETE_SUCCESS, onDeleteSuccess);

        $scope.$on('$destroy', destroy);

        init();

        function init() {
            registry.initActions(endpointResourceType, $scope);
            oasis.getEndpoints().success(getEndpointsSuccess);
        }

        function getEndpointsSuccess(response) {
            ctrl.endpointSrc = response.items;
        }

        function onCreateSuccess(e, createdItem) {
            ctrl.endpointSrc.push(createdItem);
            e.stopPropagation();
        }

        function showDetailModal(func) {
            $scope.params = func;
            $scope.model = model;
            wizardModalService.modal({
                scope: $scope,
                workflow: detailWorkFlow,
                submit: submit
            });
        }

        function submit() {

        }

        //endpoint onDeleteSuccess(e, removedIds) {
        //    ctrl.baysSrc = difference(ctrl.baysSrc, removedIds, 'id');
        //    e.stopPropagation();
        //
        //    // after deleting the items
        //    // we need to clear selected items from table controller
        //    $scope.$emit('hzTable:clearSelected');
        //}

        function difference(currentList, otherList, key) {
            return currentList.filter(filter);

            function filter(elem) {
                return otherList.filter(function filterDeletedItem(deletedItem) {
                        return deletedItem === elem[key];
                    }).length === 0;
            }
        }

        function destroy() {
            createWatcher();
            //deleteWatcher();
        }
    }

})();
