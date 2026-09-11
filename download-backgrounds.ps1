$ErrorActionPreference = 'Stop'
$sourceDir = Join-Path $PSScriptRoot '.photo-source'
$outputDir = Join-Path $PSScriptRoot 'assets\backgrounds'
New-Item -ItemType Directory -Path $sourceDir -Force | Out-Null
New-Item -ItemType Directory -Path $outputDir -Force | Out-Null

$photos = @(
  @{ Name='cover-qinghai'; Url='https://commons.wikimedia.org/wiki/Special:Redirect/file/QinghaiHu1.jpg?width=1600' },
  @{ Name='overview-qilian'; Url='https://unsplash.com/photos/63Dq80OGTpo/download?force=true&w=1600' },
  @{ Name='qinghai-lake'; Url='https://unsplash.com/photos/vA1YsHDYs1Y/download?force=true&w=1600' },
  @{ Name='dunhuang-desert'; Url='https://unsplash.com/photos/P28gVFGc-uM/download?force=true&w=1600' },
  @{ Name='qilian-valley'; Url='https://unsplash.com/photos/sUrW7LTHE_g/download?force=true&w=1600' },
  @{ Name='xining'; Url='https://unsplash.com/photos/9rj3wLiSSWA/download?force=true&w=1600' },
  @{ Name='jiayuguan'; Url='https://unsplash.com/photos/L4w2kdUQW7I/download?force=true&w=1600' },
  @{ Name='qaidam'; Url='https://unsplash.com/photos/b-qZ5pOjqfU/download?force=true&w=1600' },
  @{ Name='mogao'; Url='https://unsplash.com/photos/h4eHV9CRxUc/download?force=true&w=1600' },
  @{ Name='danxia'; Url='https://unsplash.com/photos/TJNVgeGVS_k/download?force=true&w=1600' }
)

foreach ($photo in $photos) {
  Write-Output ("Downloading " + $photo.Name)
  $destination = Join-Path $sourceDir ($photo.Name + '.jpg')
  if ((Test-Path -LiteralPath $destination) -and (Get-Item -LiteralPath $destination).Length -gt 10000) {
    Write-Output '  already downloaded'
    continue
  }
  $url = $photo.Url
  $downloaded = $false
  foreach ($delay in @(2, 5, 10)) {
    try {
      Start-Sleep -Seconds $delay
      Invoke-WebRequest -Uri $url -OutFile $destination -Headers @{'User-Agent'='QingganTravelAlbum/1.0 (travel album; local static site)'}
      $downloaded = $true
      break
    } catch {
      Write-Output ("  retry after download error: " + $_.Exception.Message)
    }
  }
  if (-not $downloaded) { throw "Unable to download image: $($photo.Name)" }
}

python (Join-Path $PSScriptRoot 'prepare-backgrounds.py') $sourceDir $outputDir
