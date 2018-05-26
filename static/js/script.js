$(document).ready(function() {
  console.log("doc ready");
  new WOW().init();
  $('#notify').click(function () {
    console.log("hide called");
    $(this).hide(2000, function () {
      $(this).remove();
    });
  });
   $('#example').DataTable
    $('#itemsTable').DataTable();
    $('#adminsTable').DataTable();
    $('#salaryTable').DataTable();
    $('#defaulterTable').DataTable();
    $('#propertyTable').DataTable();
    $('#vehicleTable').DataTable();
    $('select').addClass('select-wrapper .mdb-select');
   $('.mdb-select').material_select();

    $('.dataTables_wrapper').find('label').each(function() {
      $(this).parent().append($(this).children());
    });
    $('select').addClass('mdb-select');
    $('.mdb-select').material_select();
});
