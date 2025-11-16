# GitHub Actions Workflows

## Build and Deploy Pipeline

This repository uses GitHub Actions with Docker to render Manim animations and deploy to Netlify.

### Workflow: `build-and-deploy.yml`

**Purpose**: Render all GIF animations using Docker (with LaTeX support) and deploy to Netlify.

**Triggers**:
- Push to `main` branch
- Pull requests to `main` branch
- Manual workflow dispatch

**Jobs**:

#### 1. `build-gifs`
Renders all 14 Phase 1 scenes using Docker with full LaTeX support.

**Steps**:
1. **Build Docker Image**: Creates image with LaTeX, FFmpeg, and all dependencies
2. **Push to GHCR**: Stores image in GitHub Container Registry for caching
3. **Render GIFs**: Runs all scenes inside Docker container
4. **Upload Artifacts**: Saves rendered GIFs for deployment

**Docker Image**: `ghcr.io/prasincs/manim-learning:latest`
- Base: Python 3.11 slim
- Includes: LaTeX, FFmpeg, Cairo, Pango
- Pre-installed: All Python dependencies from requirements.txt

#### 2. `deploy-netlify`
Deploys the rendered GIFs to Netlify (only on main branch pushes).

**Steps**:
1. **Download GIFs**: Retrieves artifacts from build job
2. **Deploy**: Pushes to Netlify using `nwtgck/actions-netlify` action

**Required Secrets**:
- `NETLIFY_AUTH_TOKEN`: Personal access token from Netlify
- `NETLIFY_SITE_ID`: Site ID from Netlify dashboard

### Setup Instructions

#### 1. Get Netlify Credentials

```bash
# Get your site ID
netlify sites:list

# Create a personal access token
# Go to: https://app.netlify.com/user/applications#personal-access-tokens
```

#### 2. Add GitHub Secrets

Go to: `Settings` → `Secrets and variables` → `Actions`

Add:
- `NETLIFY_AUTH_TOKEN`: Your Netlify token
- `NETLIFY_SITE_ID`: Your site ID

#### 3. Enable GitHub Actions

The workflow runs automatically on push/PR. First run will:
1. Build Docker image (~5-10 minutes)
2. Render all 14 GIFs (~10-20 minutes)
3. Deploy to Netlify (~1 minute)

Subsequent runs use cached Docker layers for faster builds.

### Local Testing

Test the Docker build locally:

```bash
# Build the image
docker build -t manim-learning .

# Run rendering
docker run --rm \
  -v $(pwd)/public:/opt/build/repo/public \
  -v $(pwd)/media:/opt/build/repo/media \
  manim-learning

# Check output
ls -lh public/previews/phase1/
```

### Troubleshooting

**Problem**: Docker build fails
- Check Dockerfile syntax
- Verify LaTeX packages are available
- Check GitHub Actions logs for specific errors

**Problem**: GIFs not rendering
- Check `scripts/render_all.sh` for scene name mismatches
- Verify scene files exist in `scenes/phase1/`
- Check Docker logs for rendering errors

**Problem**: Netlify deployment fails
- Verify secrets are set correctly
- Check Netlify site ID is correct
- Ensure public/ directory contains files

### Performance

**First Build**:
- Docker image build: ~8 minutes
- GIF rendering: ~15 minutes
- Total: ~25 minutes

**Cached Build**:
- Docker layers cached: ~2 minutes
- GIF rendering: ~15 minutes
- Total: ~17 minutes

### Future Improvements

- [ ] Add parallel rendering for faster builds
- [ ] Cache rendered GIFs (only re-render changed scenes)
- [ ] Add video format exports (MP4)
- [ ] Generate video thumbnails
- [ ] Add build status badges to README
