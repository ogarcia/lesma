<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>lesma</title>

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css" integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ" crossorigin="anonymous">

    <!-- lesma CSS -->
    <link rel="stylesheet" href="/css/lesma.css">

    <!-- Favicons -->
    <link rel="icon" type="image/png" href="/img/favicon-512.png" sizes="512x512">
    <link rel="icon" type="image/png" href="/img/favicon-256.png" sizes="256x256">
    <link rel="icon" type="image/png" href="/img/favicon-128.png" sizes="128x128">
    <link rel="icon" type="image/png" href="/img/favicon-64.png" sizes="64x64">
    <link rel="icon" type="image/png" href="/img/favicon-32.png" sizes="32x32">
    <link rel="icon" type="image/png" href="/img/favicon-16.png" sizes="16x16">

  </head>
  <body class="py-2">

    <div class="container-fluid pb-5 lesma-input">
      <form id="lesmafrm" class="lesma-input pb-2" method="post" action="/">
        <textarea id="lesma" class="form-control lesma-input" name="lesma" autofocus>{{ lesma }}</textarea>
      </form>
    </div>


    <nav class="navbar fixed-bottom navbar-toggleable-md navbar-inverse bg-primary">
      <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <button id="savelesma" type="submit" class="btn btn-primary" form="lesmafrm">Save</button>
          </li>
          <li class="nav-item">
            <button id="newlesma" class="btn btn-primary">New</button>
          </li>
          <li class="nav-item">
            <button id="newlesma" class="btn btn-primary" disabled>Clone</button>
          </li>
          <li class="nav-item">
            <button id="rawlesma" class="btn btn-primary" disabled>Raw</button>
          </li>
        </ul>
      </div>
      <a class="navbar-brand" href="/:help">lesma</a>
    </nav>

    <!-- jQuery first, then Tether, then Bootstrap JS. -->
    <script src="https://code.jquery.com/jquery-3.1.1.slim.min.js" integrity="sha384-A7FZj7v+d/sdmMqp/nOQwliLvUsJfDHW+k9Omg/a/EheAdgtzNs3hpfag6Ed950n" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js" integrity="sha384-DztdAPBWPRXSA/3eYEEUWrWCy7G5KFbe8fFjk5JAIxUYHKkDx6Qin1DkWx51bBrb" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/js/bootstrap.min.js" integrity="sha384-vBWWzlZJ8ea9aCX4pEW3rVHjgjt7zpkNpZk+02D9phzyeVkE+jo0ieGizqPLForn" crossorigin="anonymous"></script>

    <script src="/js/lesma.js"></script>
  </body>
</html>
