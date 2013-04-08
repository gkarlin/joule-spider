DROP TABLE IF EXISTS prices;
CREATE TABLE prices
(
ept_hour_ending                             TIMESTAMP,
gmt_hour_ending                             TIMESTAMP,
dasrmcp_usd_per_mwh                         NUMERIC,
total_pjm_rt_load_mwh                       NUMERIC,
total_pjm_cleared_dasr_mwh                  NUMERIC,
total_pjm_dasr_credits_usd                  NUMERIC,
total_pjm_adjusted_dasr_obligation_mwh      NUMERIC
);
