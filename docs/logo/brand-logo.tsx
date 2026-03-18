const BrandLogo = ({ className, ...props }: React.SVGProps<SVGSVGElement>) => (
  <svg
    width={24}
    height={24}
    viewBox="0 0 24 24"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    aria-label="Brand logo"
    role="img"
    className={["dark:invert", className].filter(Boolean).join(" ")}
    {...props}
  >
    <image href="/logo.svg" width="24" height="24" preserveAspectRatio="xMidYMid meet" />
  </svg>
)

export default BrandLogo
