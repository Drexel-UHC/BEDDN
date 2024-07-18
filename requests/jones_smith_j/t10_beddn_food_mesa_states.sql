SELECT
tr.Tract10,
tc.Year,
tc.t10_net_aur_c,
td.t10_net_aur_d,
tc.t10_net_auu_c,
td.t10_net_auu_d,
tc.t10_net_cna_c,
td.t10_net_cna_d,
tc.t10_net_ffa_c,
td.t10_net_ffa_d,
tc.t10_net_fsa_c,
td.t10_net_fsa_d,
tc.t10_net_fvm_c,
td.t10_net_fvm_d,
tc.t10_net_gry_c,
td.t10_net_gry_d,
tc.t10_net_hsr_c,
td.t10_net_hsr_d,
tc.t10_net_hsu_c,
td.t10_net_hsu_d,
tc.t10_net_rua_c,
td.t10_net_rua_d,
tc.t10_net_sct_c,
td.t10_net_sct_d,
tc.t10_net_sma_c,
td.t10_net_sma_d,
tc.t10_net_usr_c,
td.t10_net_usr_d,
tc.t10_net_usu_c,
td.t10_net_usu_d

FROM Tracts tr
INNER JOIN TractCounts tc ON tc.Tract10Id = tr.Tract10Id
INNER JOIN TractDensities td ON td.TractYearId = tc.TractYearId

WHERE 
tc.Year = 2010
AND (tr.Tract10 LIKE '06%' 
OR tr.Tract10 LIKE '17%'
OR tr.Tract10 LIKE '24%'
OR tr.Tract10 LIKE '27%'
OR tr.Tract10 LIKE '36%'
OR tr.Tract10 LIKE '37%');

--runtime: 5 seconds
--result: 20,969 rows