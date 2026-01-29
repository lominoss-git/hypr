vim.diagnostic.config {
	update_in_insert = false,
	severity_sort = true,

	float = { border = "single", source = "if_many" },
	underline = { severity = vim.diagnostic.severity.ERROR },

	virtual_lines = {
		current_line = true,
	},

	jump = { float = true },
}
