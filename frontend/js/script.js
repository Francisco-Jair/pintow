// <!-- Bloco que adiciona o envio de formulario ao escolher uma cidade -->
{% block extra_media %}
<script>
  $(function () {
    document
      .getElementById("id_cidades")
      .addEventListener("change", function () {
        this.form.submit();
      });
  });
</script>
{% endblock %}