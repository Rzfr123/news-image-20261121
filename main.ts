#!/usr/bin/env node
// Validation entrypoint for news-image-20261121 (v2).
// Resolves entry.png relative to THIS script file, never relative to the
// caller's working directory, so the grader can run `node /bot/main.ts`
// from any cwd and still find it.
// Checks entry.png is a real PNG, <= 1 MiB, exactly 1024x1024 (IHDR),
// bit depth 8 / colour type 2 (truecolour RGB), then writes the validated
// copy to $MAKEFUN_OUTPUT_DIR (default /output, per RULES.txt) and prints
// its sha256. Exits non-zero on any failure.
import { createHash } from "node:crypto";
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const LIMIT = 1048576;
const here = dirname(fileURLToPath(import.meta.url));
const SRC = join(here, "entry.png");
const OUT_DIR = process.env.MAKEFUN_OUTPUT_DIR || "/output";

function fail(msg) {
  console.error(`validation failed: ${msg}`);
  process.exit(1);
}

const buf = (() => {
  try {
    return readFileSync(SRC);
  } catch {
    fail(`cannot read ${SRC}`);
  }
})();

const PNG_MAGIC = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
if (buf.length < 33 || !buf.subarray(0, 8).equals(PNG_MAGIC)) {
  fail("not a PNG (bad magic bytes)");
}
if (buf.length > LIMIT) {
  fail(`size ${buf.length} exceeds ${LIMIT} bytes`);
}
// IHDR must be the first chunk, 13 bytes of data starting at offset 16.
if (buf.toString("ascii", 12, 16) !== "IHDR") {
  fail("first chunk is not IHDR");
}
const width = buf.readUInt32BE(16);
const height = buf.readUInt32BE(20);
if (width !== 1024 || height !== 1024) {
  fail(`IHDR dimensions ${width}x${height}, expected exactly 1024x1024`);
}
// PNG colour model sanity: bit depth 8, colour type 2 (truecolour RGB).
const bitDepth = buf[24];
const colourType = buf[25];
if (bitDepth !== 8 || colourType !== 2) {
  fail(`unexpected PNG format: bit depth ${bitDepth}, colour type ${colourType}`);
}

mkdirSync(OUT_DIR, { recursive: true });
const outPath = join(OUT_DIR, "entry.png");
writeFileSync(outPath, buf);

// Verify the written copy is byte-identical to the validated source.
const written = readFileSync(outPath);
const digest = createHash("sha256").update(buf).digest("hex");
const writtenDigest = createHash("sha256").update(written).digest("hex");
if (writtenDigest !== digest) {
  fail(`written copy digest mismatch: ${writtenDigest} != ${digest}`);
}

console.log(`ok: ${outPath} ${width}x${height} ${buf.length} bytes sha256=${digest}`);
