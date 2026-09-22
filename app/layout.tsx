import "./globals.css";

export const metadata = {
  title: "FLIP — Digital Money Research Network",
  description: "FLIP protocol dashboard and monetary research prototype."
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return <html lang="en"><body>{children}</body></html>;
}
