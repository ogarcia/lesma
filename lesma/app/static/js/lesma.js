/*
 * lesma.js
 * Copyright (C) 2017-2018 Óscar García Amor <ogarcia@connectical.com>
 *
 * Distributed under terms of the GNU GPLv3 license.
 */

// prevent send empty lesmas
$("#lesmafrm").submit(function(event) {
  if (!$.trim($("#lesma").val())) {
    // textarea is empty or contains only white-space
    event.preventDefault();
  }
});

// clear lesma and maintain focus
$("#newlesma").click(function() {
  $("#lesma").val('').focus();
});
