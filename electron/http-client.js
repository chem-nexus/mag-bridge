const http = require('http');
const https = require('https');

function isLoopbackUrl(rawUrl) {
  try {
    const { hostname } = new URL(rawUrl);
    return hostname === '127.0.0.1' || hostname === 'localhost' || hostname === '::1';
  } catch {
    return false;
  }
}

function requestDirectJson(url, method = 'GET', body = null) {
  return new Promise((resolve, reject) => {
    let parsed;
    try {
      parsed = new URL(url);
    } catch (err) {
      reject(err);
      return;
    }

    const isHttps = parsed.protocol === 'https:';
    const client = isHttps ? https : http;
    const payload = body != null ? JSON.stringify(body) : null;

    const req = client.request(
      {
        protocol: parsed.protocol,
        hostname: parsed.hostname,
        port: parsed.port || (isHttps ? 443 : 80),
        path: `${parsed.pathname}${parsed.search}`,
        method,
        headers: payload
          ? {
              'Content-Type': 'application/json',
              'Content-Length': Buffer.byteLength(payload),
            }
          : undefined,
      },
      (res) => {
        let data = '';
        res.setEncoding('utf8');
        res.on('data', (chunk) => {
          data += chunk;
        });
        res.on('end', () => {
          const status = res.statusCode || 0;

          if (status < 200 || status >= 300) {
            const httpError = new Error(`HTTP ${status}: ${data || '<empty body>'}`);
            httpError.status = status;
            reject(httpError);
            return;
          }

          try {
            resolve(data ? JSON.parse(data) : null);
          } catch (err) {
            reject(err);
          }
        });
      }
    );

    req.on('error', reject);

    if (payload) {
      req.write(payload);
    }

    req.end();
  });
}

module.exports = { isLoopbackUrl, requestDirectJson };
