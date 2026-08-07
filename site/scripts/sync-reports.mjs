import { readdir, readFile, writeFile } from "node:fs/promises";
import path from "node:path";

const reviewsDir = path.resolve(process.cwd(), "../reviews");
const output = path.resolve(process.cwd(), "app/report-data.json");
const names = (await readdir(reviewsDir))
  .filter((name) => /^\d{4}-W\d{2}\.md$/.test(name))
  .sort()
  .reverse();

const reports = await Promise.all(
  names.map(async (name) => {
    const content = await readFile(path.join(reviewsDir, name), "utf8");
    const firstHeading = content.match(/^#\s+(.+)$/m)?.[1]?.trim();
    return {
      week: name.replace(".md", ""),
      title: firstHeading || name.replace(".md", " Weekly Review"),
      content,
    };
  }),
);

await writeFile(output, `${JSON.stringify(reports, null, 2)}\n`);
console.log(`Synced ${reports.length} weekly reviews.`);
