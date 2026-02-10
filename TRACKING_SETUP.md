# Guía de Instalación de Tracking Scripts & Troubleshooting

Este documento detalla cómo instalar correctamente los scripts de seguimiento (Meta Pixel, UTMify, Google Tag Manager) y cómo solucionar errores comunes de disparado (especialmente temas de CSP).

---

## 1. Meta Pixel (Facebook)

### Instalación Core
El código debe ir en el `<head>` de `index.html`. Asegúrate de usar el ID correcto de tu proyecto.

```html
<!-- Meta Pixel Code -->
<script>
  !function(f,b,e,v,n,t,s)
  {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
  n.callMethod.apply(n,arguments):n.queue.push(arguments)};
  if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
  n.queue=[];t=b.createElement(e);t.async=!0;
  t.src=v;s=b.getElementsByTagName(e)[0];
  s.parentNode.insertBefore(t,s)}(window, document,'script',
  'https://connect.facebook.net/en_US/fbevents.js');
  
  // IMPORTANTE: Desactiva autoConfig para evitar eventos duplicados
  fbq('set', 'autoConfig', false, 'TU_PIXEL_ID'); 
  fbq('init', 'TU_PIXEL_ID');
  fbq('track', 'PageView');
</script>
<noscript>
  <img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=TU_PIXEL_ID&ev=PageView&noscript=1" />
</noscript>
```

---

## 2. UTMify (Rastreo Inteligente)

### Instalación
Colocar inmediatamente después del Pixel o al inicio del `<body>`.

```html
<script src="https://cdn.utmify.com.br/scripts/utms/latest.js" data-utmify-prevent-subids async defer></script>
```

---

## 3. Google Tag Manager (GTM)

### Parte 1: `<head>`
Insertar lo más arriba posible en el `<head>`.

```html
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXX');</script>
```

### Parte 2: `<body>`
Insertar inmediatamente después de la etiqueta de apertura `<body>`.

```html
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-XXXXXX" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
```

---

## 4. Configuración Vital: Content Security Policy (CSP)

El error más común es que los scripts carguen pero el navegador bloquee el envío de datos. **DEBES** tener una meta tag de CSP que autorice los dominios de tracking.

### La Meta Tag Correcta (Consolidada)
Reemplaza cualquier otra meta tag de CSP por esta única versión completa:

```html
<meta http-equiv="Content-Security-Policy" content="
    default-src 'self' 'unsafe-inline' data: https://connect.facebook.net https://www.facebook.com https://cdn.utmify.com.br https://www.googletagmanager.com; 
    script-src 'self' 'unsafe-inline' 'unsafe-eval' data: https://connect.facebook.net https://cdn.utmify.com.br https://www.googletagmanager.com; 
    img-src 'self' data: https://www.facebook.com https://www.googletagmanager.com https://googleads.g.doubleclick.net; 
    connect-src 'self' https://connect.facebook.net https://www.facebook.com https://cdn.utmify.com.br https://www.googletagmanager.com https://*.google-analytics.com;
">
```

---

## 5. Troubleshooting: "¿Por qué no dispara el PageView?"

Si el Pixel no funciona, revisa esta lista en orden:

1.  **ID Incorrecto**: Verifica que el ID en el script (`fbq('init', '...')`) coincida exactamente con el de tu Business Manager.
2.  **Múltiples Meta Tags de CSP**: Si usas herramientas como *SingleFile* para guardar la página, a veces inyectan meta tags de CSP restrictivas al inicio del archivo. **Elimínalas** y deja solo la autorizada arriba.
3.  **Falta de `connect-src`**: Si el script carga (lo ves en el Network tab) pero no hay un hit de `PageView`, es porque el CSP bloquea el "envío" (Connect). Asegúrate de que `facebook.com` esté en `connect-src`.
4.  **Bloqueadores de Anuncios**: Desactiva AdBlock/uBlock durante las pruebas.
5.  **Extensión 'Facebook Pixel Helper'**: Úsala en Chrome para ver errores en tiempo real. Si dice "Can't load script", el problema es el `script-src` del CSP.

---

## Check-list Rápido para Nuevos Proyectos

- [ ] Reemplazar `TU_PIXEL_ID` en el script (2 lugares) y en el noscript (1 lugar).
- [ ] Reemplazar `GTM-XXXXXX` por el ID real de Tag Manager.
- [ ] Verificar que el archivo tenga una **ÚNICA** meta tag de CSP.
- [ ] Asegurarse de que el script de UTMify tenga el atributo `data-utmify-prevent-subids` si es necesario.
