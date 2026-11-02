#!/usr/bin/env node
// Gera navegação editorial: fração legível e régua fina, sem marcadores por página.
// SVG transparente, um arquivo por slide, para aplicar sobre a arte final.
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
    footerY: 0.92, marginX: 0.06, out: "./kit",
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

export function kitSvg({ index, total, w, h, accent, grey, arraste, font, footerY, marginX }) {
  const x1 = Math.round(w * 0.37);
  const x2 = Math.round(w * 0.63);
  const cy = Math.round(h * footerY);
  const progressX = x1 + (x2 - x1) * index / total;
  const stroke = Math.max(1, Math.round(w * 0.0018));
  const rule = `<line x1="${x1}" y1="${cy}" x2="${x2}" y2="${cy}" stroke="${grey}" stroke-opacity="0.35" stroke-width="${stroke}"/>` +
    `<line x1="${x1}" y1="${cy}" x2="${progressX}" y2="${cy}" stroke="${accent}" stroke-width="${stroke}"/>`;
  const fy = Math.round(h * footerY);
  const fs = Math.round(w * 0.026);         // ~28 px
  const pad = (n) => String(n).padStart(2, "0");
  const left = `<text x="${Math.round(w * marginX)}" y="${fy}" font-family="${font}" font-size="${fs}" fill="${grey}" dominant-baseline="middle">${pad(index)} / ${pad(total)}</text>`;
  const right = index === total ? "" :
    `<text x="${Math.round(w * (1 - marginX))}" y="${fy}" font-family="${font}" font-size="${fs}" fill="${grey}" text-anchor="end" dominant-baseline="middle" letter-spacing="1">${escapeXml(arraste)}</text>`;
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}">${rule}${left}${right}</svg>\n`;
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
