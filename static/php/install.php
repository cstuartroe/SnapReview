<?php

// Set variables for our request
$shop = $_GET['shop'];
$api_key = "97db2b13d9e38f92a5267e192d1a9ca4";
$scopes = "read_orders,write_products";
$redirect_uri = "http://snapreview.conorstuartroe.com/generate_token.php";

// Build install/approval URL to redirect to
$install_url = "https://" . $shop . ".myshopify.com/admin/oauth/authorize?client_id=" . $api_key . "&scope=" . $scopes . "&redirect_uri=" . urlencode($redirect_uri);

// Redirect
header("Location: " . $install_url);
die();
