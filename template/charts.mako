<!DOCTYPE html>
<html>
<head>
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="/static/css/bootstrap.min.css">
<link rel="stylesheet" href="/static/css/jumbotron.css">

<!-- Optional theme -->
<link rel="stylesheet" href="/static/css/bootstrap-theme.min.css">

<!-- Latest compiled and minified JavaScript -->
<script src="/static/js/bootstrap.min.js"></script>
<title>SqweebNet</title>
</head>
<body>
<nav class="navbar navbar-inverse navbar-fixed-top">
  <div class="container">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="/">SqweebNet</a>
    </div>
    <div id="navbar" class="navbar-collapse collapse">
      <form class="navbar-form navbar-right">
        <div class="form-group">
          <input type="text" placeholder="Email" class="form-control">
        </div>
        <div class="form-group">
          <input type="password" placeholder="Password" class="form-control">
        </div>
        <button type="submit" class="btn btn-success">Sign in</button>
      </form>
    </div><!--/.navbar-collapse -->
  </div>
</nav>

<div class="container" align="center">
  <h1>DHT22 Charts</h1>
  <embed type="image/svg+xml" src="/static/charts/current.svg" /><br>
  <embed type="image/svg+xml" src="/static/charts/last24.svg" /><br>
</div> <!-- /container -->


</div>
</body></html>
