# Jekyll & Github-pages

<!-- Promise: Build your own website in 5min; spend hours adjusting style & content -->

## Intro
<!-- 6min, Alex -->
* Motivation
    * control your web-identity
    * outreach/ networking
    * accessibility
    * online CV
    * demystify 'web-development'
    * see [Daniela Witten's opinion](https://twitter.com/daniela_witten/status/1321988664545570817?s=09) and [tons of other reasons](https://www.google.com/search?q=why+every+academic+should+have+a+personal+website)
* Examples
    * [Lea Duncker](https://leaduncker.github.io/)
    * [Richard Gao](http://www.rdgao.com/)
    * [Ashley Juavinett](https://ashleyjuavinett.com/)
    * [Sara Summerton](https://sara-es.github.io/)
    * [Patrick Mineault](https://xcorr.net/)
    * [Tilo Schwalger](http://page.math.tu-berlin.de/~schwalge/)
    * [SueYeon Chung](https://sites.google.com/site/sueyeonchung/)
    * [Benedikt Ehinger](https://benediktehinger.de/blog/science/)
    * [Felix Hoffman](https://felix11h.github.io/)
    * [Xenia Kobeleva](http://www.xenia-kobeleva.com/)
    * [Johannes Zierenberg](https://zierenberg.github.io/)
    * [Guillaume Bellec](http://guillaume.bellec.eu/)

## Basics
<!-- 8min, Robin -->
* HTML & CSS
    * Header, Footer, Body, Metadata
    * HTML is rendered in browser
    * structure -> HTML, style -> CSS
* [Github pages](https://pages.github.com/)
    * provides webhosting
    * based on git repositories
    * personal websites
    * (project page via gh branch)
    * (more configuration possible but not required)

## Jekyll
<!-- 10min, Alex -->
* [Getting started](https://jekyllrb.com/)
    * 'static site generator'
    * Webpage <- Jekyll <- Markdown
* Gem
    * Ruby packages
    * `Gemfile` collects dependencies
    * Bundler is the gem package manager
* `_config.yml`
    * jekyll configuration
* run Jekyll locally
    * [Ubuntu install guide](https://jekyllrb.com/docs/installation/ubuntu/)
    * `bundle exec jekyll serve --config _config.yml --drafts`
* [Themes](https://jekyllrb.com/docs/themes/)
    * takes care of style
    * takes care of display(-size, -layout, -devices)
    * [Minima](https://github.com/jekyll/minima)
    * [Minimal-Mistakes](https://github.com/mmistakes/minimal-mistakes)
    * [Beautiful-Jekyll](https://github.com/daattali/beautiful-jekyll)

## Extras
<!-- 7min, Robin -->
* Analytics
    * Counts users, characterizes usage and acquisition
    * For setup just copy your tracking ID into you theme config
* Robots & SEO
    * a robots.txt file tells search engines how to crawl you website
    * not necessary for small websites
    * [example for Jekyll](https://stackoverflow.com/questions/41033626/whats-the-best-way-to-write-robots-txt-for-github-pages-using-multiple-repos)
* Impressum & License
    * Content is automatically copyrighted
    * A [license](https://choosealicense.com/) can further specify share rights
    * Don't upload content copyrighted by others
    * Cite creative commons work [appropriately](https://libguides.midlandstech.edu/images/cc)
* You can use your own URL with Github pages
* Sharing slides
    * Most browser can display PDFs
    * Powepoints can be displayed via [office.com sharepoints](https://www.microsoft.com/en-us/microsoft-365/blog/2010/09/23/how-to-embed-a-powerpoint-presentation-on-a-web-page/)
    * Reveal.js slides are already website
    * [Encrypt](https://robinmoisson.github.io/staticrypt/) content for restricted access

## Our Websites
* [alexvanmeegen.github.io](https://alexvanmeegen.github.io)
* [rgutzen.github.io](https://rgutzen.github.io)
* [your website coming soon...](#)
