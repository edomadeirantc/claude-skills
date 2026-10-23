#!/usr/bin/env node
// Gera o kit de sequência do carrossel (pontos, numeração e "ARRASTE →") como
// SVG transparente, um arquivo por slide, para aplicar POR CIMA da imagem.
// O gerador de imagem erra a contagem de elementos pequenos repetidos; por
// isso o kit nunca é pedido no prompt (familia-social-conversao.md §F.4).
//
// Uso:
//   node kit_overlay.mjs --total 8 --accent "#C8F028" --out ./kit
//   node kit_overlay.mjs --total 6 --w 1080 --h 1920 --arraste "ARRASTA →" --out ./kit-story
//
// Saída: kit-01.svg … kit-NN.svg (importáveis no Figma, Canva, Illustrator
// ou convertíveis para PNG por qualquer rasterizador de SVG).

import { mkdirSync, writeFileSync } from "node:fs";
import { join } from "node:path";

function parseArgs(argv) {
  const opts = {
    total: 8, w: 1080, h: 1350, accent: "#C8F028", grey: "#A0A0A0",
    arraste: "ARRASTE →", font: "Inter, Segoe UI, Helvetica, Arial, sans-serif",
    dotsY: 0.90, footerY: 0.92, marginX: 0.06, out: "./kit",
  };
  for (let i = 2; i < argv.length; i += 2) {
    const key = argv[i].replace(/^--/, "");
    const value = argv[i + 1];
    if (!(key in opts) || value === undefined) {
      throw new Error(`Argumento inválido: ${argv[i]}`);
    }
    opts[key] = typeof opts[key] === "number" ? Number(value) : value;
  }
  if (!Number.isInteger(opts.total) || opts.total < 2 || opts.total > 20) {
    throw new Error("--total deve ser um inteiro entre 2 e 20");
  }
  return opts;
}

const escapeXml = (s) =>
  s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");

export function kitSvg({ index, total, w, h, accent, grey, arraste, font, dotsY, footerY, marginX }) {
  const sq = Math.round(w * 0.0148);        // ~16 px a 1080 de largura
  const gap = Math.round(w * 0.0222);       // ~24 px
  const diamond = Math.round(sq * 1.25);
  const rowW = total * sq + (total - 1) * gap;
  const x0 = Math.round((w - rowW) / 2);
  const cy = Math.round(h * dotsY);
  const marks = [];
  for (let i = 1; i <= total; i++) {
    const cx = x0 + (i - 1) * (sq + gap) + sq / 2;
    if (i === index) {
      const d = diamond / 2;
      marks.push(`<polygon points="${cx},${cy - d} ${cx + d},${cy} ${cx},${cy + d} ${cx - d},${cy}" fill="${accent}"/>`);
    } else {
      marks.push(`<rect x="${cx - sq / 2}" y="${cy - sq / 2}" width="${sq}" height="${sq}" rx="${Math.round(sq * 0.15)}" fill="${grey}" fill-opacity="0.55"/>`);
    }
  }
  const fy = Math.round(h * footerY);
  const fs = Math.round(w * 0.026);         // ~28 px
  const pad = (n) => String(n).padStart(2, "0");
  const left = `<text x="${Math.round(w * marginX)}" y="${fy}" font-family="${font}" font-size="${fs}" fill="${grey}" dominant-baseline="middle">${pad(index)}/${pad(total)}</text>`;
  const right = index === total ? "" :
    `<text x="${Math.round(w * (1 - marginX))}" y="${fy}" font-family="${font}" font-size="${fs}" fill="${grey}" text-anchor="end" dominant-baseline="middle" letter-spacing="1">${escapeXml(arraste)}</text>`;
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}">${marks.join("")}${left}${right}</svg>\n`;
}

function main() {
  const opts = parseArgs(process.argv);
  mkdirSync(opts.out, { recursive: true });
  for (let i = 1; i <= opts.total; i++) {
    const file = join(opts.out, `kit-${String(i).padStart(2, "0")}.svg`);
    writeFileSync(file, kitSvg({ ...opts, index: i }), "utf8");
    console.log(file);
  }
}

if (import.meta.url === `file://${process.argv[1].replace(/\\/g, "/")}` || process.argv[1]?.endsWith("kit_overlay.mjs")) {
  main();
}
