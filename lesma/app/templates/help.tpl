<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>lesma/{{ lesma_id }}</title>

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

    <div class="container-fluid pb-5">
      <div class="d-flex justify-content-between bg-primary text-white">
        <div class="p-2 px-4">lesma(1)</div>
        <div class="p-2">LESMA</div>
        <div class="p-2 px-4">lesma(1)</div>
      </div>

      <p class="text-primary pt-4">NAME</p>
      <p class="pl-4">lesma - simple paste app friendly with command line
      and browser</p>

      <p class="text-primary">SYNOPSIS</p>
      <p class="pl-4">&lt;command&gt; | curl -F 'lesma=&lt;-' <a
      href="https://pastein.connectical.com">https://pastein.connectical.com</a></p>

      <p class="text-primary">DESCRIPTION</p>
      <p class="pl-4">add any extension to resulting url for line numbers
      and syntax highlighting<br>
      add <strong>?raw</strong> for plain file<br>
      add <strong>#n-&lt;number&gt;</strong> for go directly to line number
      anchor</p>

      <p class="text-primary">SPECIALS</p>
      <p class="pl-4">/:help show this page</p>

      <p class="text-primary">EXAMPLES</p>
      <pre class="pl-4">
~$ cat lesma.py | curl -F 'lesma=&lt;-' <a
     href="https://pastein.connectical.com">https://pastein.connectical.com</a>
   <a
     href="https://pastein.connectical.com/lesma">https://pastein.connectical.com/lesma</a>
~$ firefox <a
     href="https://pastein.connectical.com/lesma.py">https://pastein.connectical.com/lesma.py</a></pre>

      <p class="text-primary">AUTHOR</p>
      <p class="pl-4">Written by Óscar García Amor</p>

      <p class="text-primary">COPYRIGHT</p>
      <p class="pl-4">Copyright © 2017 Óscar García Amor (<a
      href="https://ogarcia.me">https://ogarcia.me</a>).<br>
      Distributed under terms of the GNU GPLv3 license.</p>

      <p class="text-primary">REPORTING BUGS</p>
      <p class="pl-4"><a
      href="http://github.com/ogarcia/lesma">http://github.com/ogarcia/lesma</a></p>

      <p class="text-primary">SEE ALSO</p>
      <p class="pl-4"><a
      href="http://github.com/ogarcia/lesma">http://github.com/ogarcia/lesma</a></p>
    </div>

    <nav class="navbar fixed-bottom navbar-toggleable-md navbar-inverse bg-primary">
      <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <button id="savelesma" class="btn btn-primary" disabled>Save</button>
          </li>
          <li class="nav-item">
            <a id="newlesma" class="btn btn-primary" href="/">New</a>
          </li>
          <li class="nav-item">
            <a id="clonelesma" class="btn btn-primary" href="/clone/{{ lesma_id }}">Clone</a>
          </li>
          <li class="nav-item">
            <a id="rawlesma" class="btn btn-primary" href="?raw">Raw</a>
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
