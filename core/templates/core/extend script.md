{% extends "app/base_generic.html" %}


{% block MyStatics %}
<!-- My Style -->
      {% load static %}<link type="text/css" rel="stylesheet" href="{% static 'css/index.css' %}">
<!-- My JavaScript -->
      {% load static %}<script src="{% static 'js/index.js' %}"></script>
{% endblock %}




{% block content %}

   <main class="container">

   <!-- Agregar contenido en esta sección -->

   </main>

{% endblock %}














<!-- {% load django_bootstrap5 %}
{% bootstrap_css %}
{% bootstrap_javascript %}
{% bootstrap_messages %} -->