"use client";

import { useEffect, useMemo, useState } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import reportData from "./report-data.json";

type Report = { week: string; title: string; content: string };

const reports = reportData as Report[];

function shortWeek(week: string) {
  return week.replace("2026-", "");
}

export default function Home() {
  const [selectedWeek, setSelectedWeek] = useState(reports[0]?.week ?? "");
  const [query, setQuery] = useState("");

  useEffect(() => {
    const fromHash = window.location.hash.slice(1);
    if (reports.some((report) => report.week === fromHash)) {
      setSelectedWeek(fromHash);
    }
  }, []);

  const selected =
    reports.find((report) => report.week === selectedWeek) ?? reports[0];

  const visibleReports = useMemo(() => {
    const normalized = query.trim().toLowerCase();
    if (!normalized) return reports;
    return reports.filter(
      (report) =>
        report.week.toLowerCase().includes(normalized) ||
        report.title.toLowerCase().includes(normalized) ||
        report.content.toLowerCase().includes(normalized),
    );
  }, [query]);

  function chooseWeek(week: string) {
    setSelectedWeek(week);
    window.history.replaceState(null, "", `#${week}`);
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  if (!selected) {
    return <main className="empty">No weekly reviews have been published yet.</main>;
  }

  return (
    <main className="shell">
      <aside className="rail">
        <div className="brandBlock">
          <p className="eyebrow">PRIVATE MARKET INTELLIGENCE</p>
          <h1>Startup<br />Tracking</h1>
          <p className="brandNote">
            A weekly reading of capital, conviction, and emerging company formation.
          </p>
        </div>

        <label className="searchBox">
          <span>Search archive</span>
          <input
            aria-label="Search weekly reports"
            value={query}
            onChange={(event) => setQuery(event.target.value)}
            placeholder="Company, theme, week…"
          />
        </label>

        <nav aria-label="Weekly report archive" className="archive">
          <div className="archiveHeading">
            <span>Archive</span>
            <span>{visibleReports.length}</span>
          </div>
          {visibleReports.map((report, index) => (
            <button
              key={report.week}
              className={report.week === selected.week ? "week active" : "week"}
              onClick={() => chooseWeek(report.week)}
            >
              <span>{shortWeek(report.week)}</span>
              <small>{index === 0 && !query ? "Latest" : "Review"}</small>
            </button>
          ))}
        </nav>
      </aside>

      <section className="readingPane">
        <header className="reportHeader">
          <div>
            <p className="issueLabel">WEEKLY MARKET REVIEW · {selected.week}</p>
            <h2>{selected.title}</h2>
          </div>
          <div className="status">
            <i /> Published
          </div>
        </header>

        <article className="report">
          <ReactMarkdown remarkPlugins={[remarkGfm]}>{selected.content}</ReactMarkdown>
        </article>

        <footer>
          <span>Startup Tracking</span>
          <span>Source: Axios Pro Rata · Curated weekly</span>
        </footer>
      </section>
    </main>
  );
}
