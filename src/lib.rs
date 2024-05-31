use pyo3::prelude::*;
use std::process::Command;

#[pymodule]
#[pyo3(name = "rust_modules")]
fn rust_modules(_py: Python, m: &PyModule) -> PyResult<()> 
{
    m.add_function(wrap_pyfunction!(check_server_status, m)?)?;
    m.add_function(wrap_pyfunction!(start_server, m)?)?;
    Ok(())
}

#[pyfunction]
fn check_server_status() -> PyResult<String>
{
    match Command::new("powershell")
                  .arg("Get-Process | Where-Object { $_.MainWindowTitle -like '*7c31ok9w0fbn33*' }")
                  .output()
    {
        Ok(output) => 
        {
            if String::from_utf8_lossy(&output.stdout) != ""
            {
                return Ok("Online".to_string());
            }

            return Ok("Offline".to_string())
        },

        Err(_) => return Ok("Offline".to_string()),
    }
}

#[allow(unused_must_use)]
#[pyfunction]
fn start_server() -> ()
{
    Command::new("powershell")
            .arg(".\\scripts\\start.ps1")
            .spawn();
}