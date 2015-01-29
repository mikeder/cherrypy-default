<!DOCTYPE html>
<html>
<head>
<link href="/static/css/bootstrap.min.css" rel="stylesheet" media="screen">
<title>SqweebNet</title>
<script src="http://code.jquery.com/jquery-2.0.3.min.js"></script>
     <script type="text/javascript">
       $(document).ready(function() {

         $("#generate").click(function(e) {
           $.post("/generator", {"length": $("select[name='length']").val()})
            .done(function(string) {
               $("#string").show();
               $("#string input").val(string);
            });
           e.preventDefault();
         });
       });
     </script>
<script src="/static/js/bootstrap.min.js"></script>     
</head>
<body align="center">
<h2>SqweebNet - Index</h2>
<hr>
Random sequence generator:
<form name="generator">
  <select name="length">
    <option value="5">5</option>
    <option value="6">6</option>
    <option value="7">7</option>
    <option value="8">8</option>
    <option value="9">9</option>
    <option value="10">10</option>
    <option value="11">11</option>
    <option value="12">12</option>
    <option value="13">13</option>
    <option value="14">14</option>
    <option value="15">15</option>
    <option value="16">16</option>
    <option value="17">17</option>
    <option value="18">18</option>
    <option value="19">19</option>
    <option value="20">20</option>
  </select>
  <button id="generate">Generate</button>
</form>
<div id="string">
  <input type="text" width="25" />
</div>
</body>
</html>

