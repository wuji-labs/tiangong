# 天工 TianGong — La obra del cielo

<p align="center">
  <a href="https://www.skills.sh/wuji-labs/tiangong"><img src="https://www.skills.sh/b/wuji-labs/tiangong" alt="skills.sh"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://github.com/wuji-labs/huaxia-skills"><img src="https://img.shields.io/badge/%E5%8D%8E%E5%A4%8F%E5%8D%81%E5%A4%A7-HuaXia%20Skills-c1272d" alt="HuaXia Skills"></a>
</p>

**[🇨🇳 简体中文](README.zh-CN.md)** · **[🇺🇸 English](README.md)** · **[🇯🇵 日本語](README.ja.md)** · **[🇰🇷 한국어](README.ko.md)** · **[🇪🇸 Español](README.es.md)** · **[🇧🇷 Português](README.pt.md)** · **[🇫🇷 Français](README.fr.md)**

> **天地有大美而不言** — El cielo y la tierra poseen una gran belleza, pero no la proclaman.

**Tu IA diseña con media paleta. Dale la otra mitad.**

La mayor parte del aprendizaje de diseño de la IA está dominada por marcos occidentales: Material Design, Bauhaus, estilo suizo. Limpios, minimalistas, modernos... pero a menudo sin alma.

**TianGong** (天工) infunde 5000 años de sabiduría estética china en el diseño con IA. No como adorno, sino como un sistema filosófico completo para comprender la belleza, el espacio, el ritmo y el significado.

## El problema

```
Tú: «Diseña una página de aterrizaje»
IA sin TianGong: Cuadrícula perfecta. Espaciado perfecto. Una perfecta... nada.
IA con TianGong: Una página que respira. Que fluye como el agua.
                 Donde el vacío habla más alto que el contenido.
                 Donde cada color porta un significado.
```

## Qué le enseña a la IA

### 🎨 Los Seis Principios (谢赫六法, siglo V)
El marco de diseño más antiguo que se conserva en el mundo:

| Principio | Chino | Significado |
|-----------|---------|---------|
| Resonancia del espíritu | 气韵生动 | El diseño debe sentirse **vivo** |
| Trazo estructural | 骨法用笔 | La belleza necesita **huesos** |
| Fiel a la naturaleza | 应物象形 | Comprender antes de diseñar |
| Color con sentido | 随类赋彩 | Color = significado, no adorno |
| Gobernar el espacio | 经营位置 | El vacío ES el diseño |
| Aprender de los maestros | 传移模写 | Estudia la tradición y luego trasciéndela |

### 🧠 Las Cinco Sabidurías (五智) — Marco de decisión

| Sabiduría | Fuente | Pregúntate |
|--------|--------|-------------|
| 道法自然 | Tao Te King, cap. 25 | ¿Se siente natural? |
| 大巧若拙 | Tao Te King, cap. 45 | ¿Estoy luciéndome o sirviendo? |
| 器以载道 | Yijing | ¿Qué significado porta? |
| 天人合一 | Yijing | ¿Armoniza con el contexto? |
| 中庸之道 | Zhongyong (Doctrina del Medio) | ¿Está equilibrado? |

### 🏺 La sabiduría de los materiales — De 4 tradiciones

| Tradición | Enseña | Aplicación al diseño |
|-----------|---------|-------------------|
| 书法 Caligrafía | Ritmo, tensión, fluidez | Tipografía, ritmo visual |
| 水墨 Pintura a la tinta | Capas, vacío, vida | Jerarquía visual, espacio en blanco |
| 园林 Jardines | Descubrimiento, encuadre, secuencia | Navegación, revelación progresiva |
| 瓷器 Porcelana | Contención, belleza oculta, forma | Paletas de color, diseño de superficie |

### 🏛️ El canon de la dinastía Song (宋代美学, 960–1279)

La cima del gusto refinado chino, 800 años antes de Dieter Rams:

```
极简 Simplicidad radical
素雅 Sobriedad elegante
格物 Indagar antes de crear
理趣 Deleite en el principio
天然 Naturalidad por encima del artificio
```

**Paleta cromática Song:**
```
月白 Blanco lunar      ████  #D6E4E1
天青 Azul celeste      ████  #68B0AB
粉青 Verde polvo       ████  #A7D7C5
影青 Azul sombra       ████  #C5D8D1
米黄 Amarillo arroz    ████  #F5E6CC
```

## Qué incluye (manifiesto del skill)

| Artefacto | Propósito |
|----------|---------|
| `SKILL.md` | Instrucciones permanentes de base: los Seis Principios ＋ el motor de decisión de las Cinco Sabidurías ＋ el método de 4 pasos |
| `.claude-plugin/plugin.json` · `marketplace.json` | Instalación del plugin con un clic |
| `commands/tiangong.md` | Comando de barra `/tiangong <goal>` |
| `examples/01-landing-page.md` · `02-color-palette.md` · `03-design-review.md` | Casos de diseño reales de entrada→salida |
| `benchmark/scenarios.json` + `README_BENCHMARK.md` | Diseño de evaluación de 6 escenarios ＋ ejecutor/analizador funcional (**los resultados aún no se han ejecutado**) |
| `reference/aesthetics.md` | Munición autónoma: los Seis Principios con fuente línea por línea, los Cinco Elementos/Colores, los Diez Clásicos, muestras de colores tradicionales, 8 recetas de diseño |
| `skills/tiangong/SKILL.md` | Versión completa en formato extenso (cada uno de los Diez Clásicos) |

## Instalación

### OpenClaw / Claude Code / Codex
```bash
# Copia a tu directorio de skills
cp -r skills/tiangong ~/.openclaw/workspace/skills/
# o
cp -r skills/tiangong ~/.claude/skills/
# o
cp -r skills/tiangong ~/.codex/skills/
```

### Cursor
Copia `cursor/rules/tiangong.mdc` a tu directorio `.cursor/rules/`.

### Kiro
Copia `kiro/skills/tiangong/` a tu directorio `.kiro/skills/`.

## Oriente se encuentra con Occidente

TianGong no reemplaza el conocimiento de diseño occidental. Lo **completa**.

| Occidental | ＋ Chino | ＝ Completo |
|---------|-----------|------------|
| Bauhaus: claridad funcional | 气韵: resonancia espiritual | Diseño que funciona Y respira |
| Suizo: disciplina de la cuadrícula | 书法: vida rítmica | Estructura que fluye |
| Material Design: consistencia | 宋代美学: gusto refinado | Consistente Y de buen gusto |
| Proporción áurea: proporción | 留白: vacío intencional | Espacio que habla |

> **知其白，守其黑，为天下式。**
> Conoce lo blanco, aférrate a lo negro: conviértete en el patrón del mundo.
> — Tao Te King, capítulo 28

## Del mismo creador

- [**NoPUA**](https://github.com/wuji-labs/nopua) — Skill anti-PUA que guía a la IA con sabiduría en lugar de miedo. ⭐ 200+

## Licencia

MIT — Úsalo con libertad. Diseña con belleza.

---

*天工 TianGong — by [WUJI](https://github.com/wuji-labs)*
*La obra del cielo abre la creación. Diseña con 5000 años de sabiduría.*
