<?php

?>

<div id="login-main">
    <header id="login-header">
		<div id="login-logo">
			<a href="<?php echo $front_page ?>"><img src="<?php echo $base_path.$directory.'/images/iutah_logo.png' ?>" width="184" height="70" /></a>
		</div>
        <h1 id="login-headerTitle">GAMUT Management Database</h1>
	</header>
	<div id="login-site_content">
		<?php if ($tabs && $is_admin): ?>
            <div class="tabs">
		        <?php print render($tabs); ?>
		    </div>
	    <?php endif; ?>

		<section id="login-content">
			<h1>Log In</h1>
			<div id="login">
				<?php print render($page['content']); ?>
			</div>
		</section>
	</div>
	<footer>
		<span>Copyright © 2013 iUTAH</span>
        <span>This material is based upon work supported by the National Science Foundation (NSF) under Grant No. XXXXXXXX.</span>
        <span>Any opinions, findings, conclusions, or recommendations expressed in this material are those of the authors and do not necessarily reflect the views of the NSF.</span>
	</footer>
</div>