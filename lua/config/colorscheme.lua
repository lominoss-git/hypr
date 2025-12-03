local nord_overrides = vim.api.nvim_create_augroup("nord-theme-overrides", { clear = true })
local set_hl = vim.api.nvim_set_hl

vim.api.nvim_create_autocmd("ColorScheme", {
  group = nord_overrides,
  pattern = "nord",
  callback = function()
    set_hl(0, "StatusLine", { fg = "#D8DEE9" })
    set_hl(0, "EndOfBuffer", { fg = "#2E3440" })
    set_hl(0, "WinSeparator", { fg = "#434C5E" })
    set_hl(0, "DiagnosticUnderlineWarn", { fg = "#EBCB8B", underline = true })
    set_hl(0, "DiagnosticUnderlineError", { fg = "#BF616A", underline = true })
    set_hl(0, "DiagnosticUnderlineInfo", { fg = "#A3BE8C", underline = true })
    set_hl(0, "DiagnosticUnderlineHint", { fg = "#B48EAD", underline = true })
  end,
})

vim.g.nord_bold = 0
vim.g.nord_italic = 0

vim.cmd.colorscheme("nord")


-- call s:hi("DiagnosticUnderlineWarn" , s:nord13_gui, "", s:nord13_term, "", "undercurl", "")
-- call s:hi("DiagnosticUnderlineError" , s:nord11_gui, "", s:nord11_term, "", "undercurl", "")
-- call s:hi("DiagnosticUnderlineInfo" , s:nord8_gui, "", s:nord8_term, "", "undercurl", "")
-- call s:hi("DiagnosticUnderlineHint" , s:nord10_gui, "", s:nord10_term, "", "undercurl", "")
