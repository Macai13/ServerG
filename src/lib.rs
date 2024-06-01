use pyo3::prelude::*;
use std::{os::windows::process::CommandExt, process::Command};
#[allow(unused_imports)]
use std::thread;
#[allow(unused_imports)]
use std::time::Duration;

#[pymodule]
#[pyo3(name = "rust_modules")]
fn rust_modules(_py: Python, m: &PyModule) -> PyResult<()> 
{
    m.add_function(wrap_pyfunction!(check_server_status, m)?)?;
    m.add_function(wrap_pyfunction!(start_server, m)?)?;
    m.add_function(wrap_pyfunction!(download_create_server, m)?)?;
    m.add_function(wrap_pyfunction!(download_update_server, m)?)?;
    m.add_function(wrap_pyfunction!(is_dir_empty, m)?)?;
    m.add_function(wrap_pyfunction!(upload_server, m)?)?;
    m.add_function(wrap_pyfunction!(update_log, m)?)?;
    m.add_function(wrap_pyfunction!(pull_log_from_gith, m)?)?;
    Ok(())
}

#[pyfunction]
fn check_server_status() -> PyResult<String>
{
    match Command::new("powershell")
                  .arg("Get-Process | Where-Object { $_.MainWindowTitle -like '*7c31ok9w0fbn33*' }")
                  .creation_flags(0x08000000)
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
    thread::spawn(|| {
        Command::new("powershell")
                .arg(".\\scripts\\start.ps1")
                .spawn();
    });
}

#[pyfunction]
fn is_dir_empty(dir: String) -> PyResult<bool>
{
    match std::path::PathBuf::from(dir)
                            .read_dir()
                            .map(|mut i| i.next().is_none())
    {
        Ok(v) => return Ok(v),
        Err(_) => return Ok(true),
    }
}

#[pyfunction]
fn download_create_server() -> ()
{
    match Command::new("powershell")
            .arg("git clone https://github.com/vctorfarias/minecraft-server-01 ./server")
            .spawn()
    {
        Ok(_) => (),
        Err(_) => 
        {
            Command::new("powershell")
                    .arg("mkdir server; git clone https://github.com/vctorfarias/minecraft-server-01 ./server")
                    .spawn()
                    .unwrap();
            return ();
        }
    }
}

#[allow(unused_must_use)]
#[pyfunction]
fn upload_server() -> ()
{
    thread::spawn(|| {
        Command::new("powershell")
                .arg("Set-Location server ; git add . ; git commit -m '.' ; git push")
                .spawn();
    });
}

#[pyfunction]
fn download_update_server() -> ()
{
    match Command::new("powershell")
            .arg("Set-Location server ; git checkout . ; git pull >> ../logs/git_log.txt")
            .creation_flags(0x08000000)
            .spawn()
    {
        Ok(_) => (),
        Err(_) => download_create_server()
    }
}

#[allow(unused_must_use)]
#[pyfunction]
fn pull_log_from_gith() -> ()
{
    Command::new("powershell")
            .arg("Set-Location ./logs/minecraft-logs/ ; git pull")
            .creation_flags(0x08000000)
            .spawn();
}

#[allow(unused_must_use)]
#[pyfunction]
fn update_log() -> ()
{
    thread::spawn(|| {
        Command::new("powershell")
                .arg("cd ./logs/minecraft-logs/ ; git add * ; git commit -m '.' ; git push")
                .spawn();
    });
}