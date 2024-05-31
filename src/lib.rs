use pyo3::prelude::*;
use std::process::Command;

#[pymodule]
#[pyo3(name = "rust_modules")]
fn rust_modules(_py: Python, m: &PyModule) -> PyResult<()> 
{
    m.add_function(wrap_pyfunction!(check_server_status, m)?)?;
    m.add_function(wrap_pyfunction!(start_server, m)?)?;
    m.add_function(wrap_pyfunction!(is_server_dir_empty, m)?)?;
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

#[pyfunction]
fn is_server_dir_empty() -> PyResult<bool>
{
    match std::path::PathBuf::from(".\\server")
                            .read_dir()
                            .map(|mut i| i.next().is_none())
    {
        Ok(v) => return Ok(v),
        Err(_) => return Ok(true),
    }
}