#!/usr/bin/env python3
"""Generate anxiety-psychoeducation.html  -  Anxiety Disorders psychoeducation tool."""

def esc(s):
    return s.replace("'", "\\'")

groups = [
    {
        "label": None,
        "optional": False,
        "items": [
            {
                "id": "anx_what_is",
                "title": "Understanding anxiety disorders",
                "body": """<p><strong>Anxiety is not a character flaw or weakness.</strong> Anxiety disorders are among the most common and treatable conditions in psychiatry. The word "anxiety" covers a family of distinct conditions that share excessive fear or worry but differ significantly in their triggers, mechanisms, and treatments. Understanding which type you have matters - because treatments are different.</p>
<p><strong>The anxiety disorders covered here:</strong></p>
<ul>
<li><strong>Social anxiety disorder:</strong> Fear of social situations involving scrutiny or embarrassment</li>
<li><strong>Panic disorder:</strong> Recurrent unexpected panic attacks with anticipatory anxiety about future attacks</li>
<li><strong>Generalised anxiety disorder (GAD):</strong> Chronic, pervasive worry across multiple domains that is difficult to control</li>
<li><strong>Agoraphobia:</strong> Avoidance of situations where escape is difficult or help unavailable during panic</li>
<li><strong>Health anxiety:</strong> Excessive preoccupation with having or developing a serious illness</li>
<li><strong>Trait anxiety:</strong> A persistent, temperament-level tendency toward anxiety responses across situations</li>
</ul>
<p><strong>Key message:</strong> Anxiety disorders are biologically-based, not a sign of weakness. They respond very well to specific psychological treatments (particularly CBT and exposure-based approaches) and to medication. Most people improve significantly with the right treatment.</p>"""
            },
            {
                "id": "anx_neuroscience",
                "title": "The neuroscience - why your brain does this",
                "body": """<p><strong>The threat detection system:</strong> Anxiety disorders reflect a threat detection system - the amygdala - that is over-sensitive or over-generalised. The amygdala rapidly evaluates incoming information for danger and triggers the fear response before conscious thought catches up. In anxiety disorders, this system fires in response to social evaluation, bodily sensations, uncertainty, or health cues as if they were genuine threats.</p>
<p><strong>The physiology of anxiety:</strong> The sympathetic nervous system activation (fight-or-flight response) produces every symptom you experience: racing heart, chest tightness, breathlessness, dizziness, sweating, nausea, trembling. These are not dangerous - they are your body preparing to run or fight. In a genuine threat they are adaptive. In anxiety disorders they are triggered by false alarms.</p>
<p><strong>Why avoidance makes it worse:</strong> When you avoid an anxiety trigger, you get immediate relief - which reinforces the avoidance. But avoidance prevents the brain from learning that the feared outcome does not happen. Over time, the anxiety expands and the safe zone contracts. Avoidance is the core mechanism that maintains every anxiety disorder. This is why effective treatment involves doing the feared thing in a controlled, planned way - not avoiding it.</p>
<p><strong>Why medication helps:</strong> Serotonin and noradrenaline modulate amygdala reactivity. SSRIs and SNRIs reduce the sensitivity of the threat detection system over weeks. They work best in combination with psychological treatment (typically exposure-based CBT).</p>"""
            }
        ]
    },
    {
        "label": "Social Anxiety",
        "optional": False,
        "items": [
            {
                "id": "social_anx_what",
                "title": "Social anxiety disorder - what it is and how it works",
                "body": """<p><strong>Not just shyness:</strong> Social anxiety disorder (SAD) is the second most common anxiety disorder (after specific phobias). It involves intense fear of social situations where you might be judged, embarrassed, or scrutinised. Unlike shyness, it causes significant distress and impairs function - relationships, work, education.</p>
<p><strong>The core fear:</strong> The anxiety is not about other people per se, but about being negatively evaluated - appearing stupid, boring, weird, anxious, incompetent. This fear is accompanied by a belief that social failure would be catastrophic.</p>
<p><strong>The maintenance cycle:</strong></p>
<ul>
<li>Anticipatory anxiety before social situations (sometimes hours or days before)</li>
<li>Safety behaviours in social situations: over-preparation, script-following, minimal self-disclosure, deflecting attention, rehearsing what to say</li>
<li>Post-event processing: reviewing performance, dwelling on perceived mistakes</li>
<li>All of these reduce anxiety short-term but maintain it long-term</li>
</ul>
<p><strong>What actually helps:</strong></p>
<ul>
<li><strong>CBT with exposure:</strong> Graded exposure to social situations, dropping safety behaviours, testing predictions. The gold standard. Expect 12-20 sessions.</li>
<li><strong>Video feedback:</strong> Recording yourself in social situations often dramatically disconfirms beliefs about how you come across</li>
<li><strong>Dropping self-focused attention:</strong> Shifting attention outward (to the other person, to the environment) reduces anxiety more than trying to control impression</li>
<li><strong>SSRIs/SNRIs:</strong> Effective. Sertraline, escitalopram, venlafaxine. Usually 6-12 months minimum.</li>
</ul>"""
            },
            {
                "id": "social_anx_practical",
                "title": "Practical social anxiety management",
                "body": """<p><strong>The most important thing you can do:</strong> Engage in social situations despite anxiety, while deliberately dropping safety behaviours. This feels counterintuitive but is the mechanism by which the brain recalibrates its threat assessment.</p>
<p><strong>Dropping safety behaviours specifically:</strong></p>
<ul>
<li>Stop over-preparing scripts or what you will say</li>
<li>Make eye contact (briefly and naturally - not a stare)</li>
<li>Let silences occur without filling them</li>
<li>Ask questions about the other person rather than only talking about facts you are confident about</li>
<li>Allow yourself to be imperfect - say something imprecise and observe that the world does not end</li>
</ul>
<p><strong>Attention retraining:</strong> In social situations, anxiety creates a spotlight effect where you focus intensely on yourself - your face, your words, your performance. This makes you less socially present, more awkward, and more anxious. Deliberately shifting attention to what the other person is saying, their facial expressions, what is happening around you reduces anxiety significantly over time.</p>
<p><strong>Post-event processing:</strong> Stop reviewing social events. Set a time limit (5 minutes maximum) if you catch yourself replaying. Write down what you predicted would happen vs. what actually happened. The gap is usually instructive.</p>
<p><strong>Building a social confidence hierarchy:</strong> Rank feared situations from least to most anxiety-provoking. Start at the bottom. Move up only when anxiety has reduced by at least 50%. Do not avoid; do not leave early; stay until anxiety naturally decreases.</p>"""
            }
        ]
    },
    {
        "label": "Panic Disorder",
        "optional": False,
        "items": [
            {
                "id": "panic_what",
                "title": "Panic disorder - explaining panic attacks",
                "body": """<p><strong>A panic attack is not dangerous.</strong> It cannot cause a heart attack, brain damage, fainting (blood pressure rises, not falls), suffocation, or "going crazy." The intense symptoms - racing heart, chest pressure, dizziness, breathlessness, tingling, derealisation - are produced by hyperventilation and sympathetic nervous system activation. They feel catastrophic but are physically harmless.</p>
<p><strong>The vicious cycle of panic:</strong></p>
<ol>
<li>Initial trigger (may be nothing detectable, or a stressful thought, physical sensation, or situation)</li>
<li>Physical sensation noticed (heart flutter, dizziness, breathlessness)</li>
<li>Catastrophic interpretation: "This is a heart attack / I am dying / I am going crazy"</li>
<li>Anxiety increases - which increases the physical sensations</li>
<li>Interpretation confirmed: "My heart is going faster - it must be serious"</li>
<li>Full panic attack</li>
</ol>
<p><strong>Panic disorder:</strong> Not just having panic attacks, but developing persistent anxiety about future attacks ("what if it happens again?") and changing behaviour because of panic (avoiding exercise, certain places, alcohol, certain feelings). This is the disorder - the attacks themselves are just the initial trigger.</p>
<p><strong>The adrenaline myth:</strong> Panic attacks feel like they last forever but the adrenaline surge that produces them peaks at 10 minutes and cannot last more than 20-30 minutes even if you do nothing. Knowing this matters: you can let a panic attack peak and pass.</p>"""
            },
            {
                "id": "panic_practical",
                "title": "Practical panic management",
                "body": """<p><strong>In the moment of panic - what to do:</strong></p>
<ul>
<li><strong>Do not fight it.</strong> Fighting a panic attack increases arousal and extends it. Acceptance is faster.</li>
<li><strong>Slow your breathing:</strong> Breathe out for longer than you breathe in (4 in, pause, 6-7 out). This activates the parasympathetic system. Do not breathe into a bag - that approach is outdated.</li>
<li><strong>Label what is happening:</strong> "This is a panic attack. It will peak and pass. I am not in danger." Say this to yourself explicitly. Labelling reduces amygdala reactivity.</li>
<li><strong>Stay where you are.</strong> Leaving the situation (the "escape") provides immediate relief but reinforces the idea that the situation was dangerous. Stay until anxiety naturally decreases - this is how the brain learns.</li>
</ul>
<p><strong>Interoceptive exposure:</strong> One of the most effective panic treatments is deliberately producing panic-like sensations in a controlled setting: spinning in a chair (dizziness), breathing through a straw (breathlessness), running on the spot (racing heart). This trains the brain that these sensations are not dangerous. Do this with your therapist initially.</p>
<p><strong>Stop checking:</strong> Checking your pulse, touching your chest, asking for reassurance, googling symptoms - all of these maintain panic disorder. Each check is a message to your brain that there might be something wrong. Stop entirely.</p>
<p><strong>Medication:</strong> SSRIs and SNRIs (sertraline, escitalopram, venlafaxine) are first-line. They take 4-8 weeks to work. Beta-blockers help with physical symptoms acutely. Benzodiazepines provide rapid relief but create dependency and worsen panic disorder long-term by preventing habituation.</p>"""
            }
        ]
    },
    {
        "label": "Generalised Anxiety Disorder",
        "optional": False,
        "items": [
            {
                "id": "gad_what",
                "title": "Generalised anxiety disorder - the worry disorder",
                "body": """<p><strong>GAD is not ordinary worry.</strong> Everyone worries. GAD involves worry that is: pervasive (about many topics simultaneously); difficult or impossible to control; disproportionate to actual risk; persistent (most days, for months); and accompanied by physical symptoms (muscle tension, fatigue, sleep disruption, irritability, concentration problems).</p>
<p><strong>Why it is hard to treat:</strong> People with GAD often have a complicated relationship with their own worrying. Common beliefs about worry: "Worrying helps me prepare," "If I worry, I won't be caught off guard," "Not worrying means I don't care." These beliefs keep worry going even when it causes suffering.</p>
<p><strong>The positive beliefs about worry</strong> are usually inaccurate. Worrying does not prevent bad things from happening. It does not improve problem-solving (evidence shows anxious worry impairs decision-making). It does not demonstrate caring - it exhausts the carer without benefiting anyone.</p>
<p><strong>What helps:</strong></p>
<ul>
<li><strong>CBT for GAD:</strong> Specifically addressing beliefs about worry, worry postponement (scheduling a "worry period"), and tolerating uncertainty - which is the core of GAD</li>
<li><strong>Acceptance-based approaches (ACT):</strong> Particularly effective - defusing from worried thoughts rather than trying to resolve them</li>
<li><strong>Mindfulness:</strong> Learning to observe worried thoughts without engaging with them</li>
<li><strong>SSRIs/SNRIs:</strong> Escitalopram, sertraline, venlafaxine, duloxetine all have good evidence</li>
<li><strong>Pregabalin:</strong> Effective for GAD, particularly where physical anxiety symptoms are prominent</li>
</ul>"""
            },
            {
                "id": "gad_practical",
                "title": "Practical GAD management",
                "body": """<p><strong>Worry postponement:</strong> One of the most effective single techniques for GAD. When a worry thought arises, notice it, and then consciously postpone it: "I will think about this at my worry time." Set a specific 20-minute period each day as your scheduled worry time. When the scheduled time arrives, worry deliberately about what you postponed. Many worries resolve themselves before the time arrives; others feel less urgent when engaged with deliberately rather than reactively.</p>
<p><strong>Tolerating uncertainty:</strong> GAD is fundamentally a disorder of uncertainty intolerance. People with GAD seek certainty where none exists and suffer when they cannot find it. The treatment is: deliberately practise tolerating uncertainty. Stop seeking reassurance. Stop checking. Stop researching worst cases. Allow yourself to not know what will happen, and to function anyway.</p>
<p><strong>The "so what" exercise:</strong> Follow a worried thought to its logical conclusion. "What if I fail the presentation?" "I'll look stupid." "And then what?" "My colleagues will think less of me." "And then what?" "My career will suffer." "And then what?" Continuing this often reveals that the ultimate feared outcome is either manageable or highly unlikely.</p>
<p><strong>Physical strategies that work:</strong></p>
<ul>
<li><strong>Progressive muscle relaxation:</strong> Systematically tensing and releasing muscle groups. Reduces the physical tension component of GAD significantly.</li>
<li><strong>Exercise:</strong> 30+ minutes of aerobic exercise 3+ times per week reduces GAD symptoms comparably to medication in some studies.</li>
<li><strong>Sleep:</strong> Sleep deprivation dramatically worsens GAD. Treating sleep problems often reduces daytime anxiety substantially.</li>
<li><strong>Reduce caffeine:</strong> Caffeine directly increases anxious arousal. Cut to 1 cup before 10am if GAD is significant.</li>
</ul>"""
            }
        ]
    },
    {
        "label": "Agoraphobia",
        "optional": True,
        "items": [
            {
                "id": "ago_what",
                "title": "Agoraphobia - what it actually is",
                "body": """<p><strong>Agoraphobia is not fear of open spaces.</strong> The word is misleading. Agoraphobia is fear and avoidance of situations where escape might be difficult, or where help might not be available if you experience panic or incapacitating symptoms. Common avoided situations: public transport, crowds, queues, shopping centres, driving, being far from home, being outside alone.</p>
<p><strong>The connection to panic disorder:</strong> Agoraphobia most commonly develops after panic attacks. After experiencing a panic attack in a particular place, the brain tags that location as dangerous. Avoidance begins. Over time, the range of "safe" situations narrows, and the range of avoided situations expands. Some people become largely housebound.</p>
<p><strong>The core treatment:</strong> Graduated exposure - systematically approaching avoided situations in a planned, deliberate way, without using safety behaviours (staying close to exits, going only with a trusted person, carrying rescue medication "just in case"), until anxiety decreases in that situation. Then moving to the next level.</p>
<p><strong>Safety behaviours that maintain agoraphobia:</strong> Staying close to exits. Only going out with a safe person. Carrying benzodiazepines "just in case." Only going at quiet times. Having a route home planned. All of these prevent the learning that the situation is safe.</p>
<p><strong>Medication:</strong> SSRIs and SNRIs reduce the underlying panic disorder. Buspirone for anticipatory anxiety. Avoid long-term benzodiazepines - they provide immediate relief but interfere with the extinction learning that exposure produces.</p>"""
            }
        ]
    },
    {
        "label": "Health Anxiety",
        "optional": True,
        "items": [
            {
                "id": "health_anx_what",
                "title": "Health anxiety - more than just worrying about your health",
                "body": """<p><strong>What health anxiety is:</strong> Excessive preoccupation with having or developing a serious illness, disproportionate to medical evidence, that persists despite reassurance and causes significant distress. Normal bodily sensations are interpreted as signs of illness. This is not hypochondria (a pejorative term) - it is a genuine anxiety disorder with specific neurobiology.</p>
<p><strong>The reassurance trap:</strong> Health anxiety typically triggers a seeking-reassurance cycle: notice symptom - anxiety rises - seek reassurance (doctor, Google, self-check) - temporary relief - anxiety returns, often higher - repeat. Each reassurance provides diminishing relief. The internet is a particularly potent amplifier: googling symptoms almost always produces cancer, autoimmune disease, or rare neurological conditions.</p>
<p><strong>What maintains health anxiety:</strong></p>
<ul>
<li>Repeated body checking (feeling lumps, taking pulse, monitoring breathing)</li>
<li>Reassurance seeking (doctors, family, Google)</li>
<li>Symptom monitoring (heightened attention to body sensations)</li>
<li>Avoidance of health-related information or situations</li>
</ul>
<p><strong>What actually helps:</strong></p>
<ul>
<li><strong>CBT for health anxiety:</strong> Reducing checking, stopping reassurance seeking, correcting catastrophic interpretations of bodily sensations</li>
<li><strong>Eliminate Google:</strong> Non-negotiable for meaningful improvement</li>
<li><strong>Set limits on doctor visits:</strong> One appointment per concern, then no further checking</li>
<li><strong>SSRIs:</strong> Effective, particularly sertraline and escitalopram</li>
<li><strong>Attention retraining:</strong> Shifting attention away from body monitoring</li>
</ul>"""
            }
        ]
    },
    {
        "label": "Trait Anxiety",
        "optional": True,
        "items": [
            {
                "id": "trait_anx_what",
                "title": "Trait anxiety - when anxiety is part of how you are wired",
                "body": """<p><strong>What trait anxiety is:</strong> A stable, temperament-level tendency to experience anxiety across situations and over time. Unlike state anxiety (anxiety in response to a specific situation), trait anxiety is a characteristic of how a nervous system processes the world. It is partly genetic and partly shaped by early experience.</p>
<p><strong>Trait anxiety vs. anxiety disorder:</strong> High trait anxiety increases vulnerability to anxiety disorders but is not itself a disorder. It means your baseline arousal level is higher, you respond more strongly to potential threats, and you return to baseline more slowly. This has real advantages (threat detection, preparation, conscientiousness) and real costs (exhaustion, overactivation, difficulty relaxing).</p>
<p><strong>What helps trait anxiety:</strong></p>
<ul>
<li><strong>Understanding your profile:</strong> High trait anxiety is a feature of a nervous system, not a moral failing. Understanding this changes how you relate to it.</li>
<li><strong>Regular aerobic exercise:</strong> Most consistently evidenced intervention for baseline anxiety reduction. Works via BDNF, serotonin, and HPA axis regulation.</li>
<li><strong>Mindfulness-based stress reduction (MBSR):</strong> Good evidence for reducing baseline anxiety in high-trait-anxiety individuals without a specific anxiety disorder.</li>
<li><strong>Sleep:</strong> Chronically anxious people often have disrupted sleep which amplifies trait anxiety. Treating sleep often reduces baseline anxiety.</li>
<li><strong>Caffeine reduction:</strong> High-trait-anxiety individuals are often more sensitive to caffeine's anxiogenic effects.</li>
<li><strong>Structured cognitive work:</strong> Identifying and modifying automatic negative interpretations before they escalate.</li>
</ul>
<p><strong>Medication:</strong> Buspirone, SSRIs, or SNRIs may be appropriate if trait anxiety significantly impairs function or quality of life. Low-dose propranolol for situational performance anxiety.</p>"""
            }
        ]
    },
    {
        "label": "Medication",
        "optional": True,
        "items": [
            {
                "id": "anx_meds",
                "title": "Medication for anxiety disorders",
                "body": """<p><strong>First-line: SSRIs and SNRIs</strong></p>
<table><thead><tr><th>Medication</th><th>Class</th><th>Best for</th><th>Notes</th></tr></thead><tbody>
<tr><td><strong>Sertraline</strong></td><td>SSRI</td><td>All anxiety disorders</td><td>Most versatile. Start 25-50mg, up to 200mg. 6-8 weeks for full effect.</td></tr>
<tr><td><strong>Escitalopram</strong></td><td>SSRI</td><td>GAD, panic, social anxiety</td><td>Very clean side effect profile. 10-20mg. Well tolerated.</td></tr>
<tr><td><strong>Venlafaxine XR</strong></td><td>SNRI</td><td>GAD, panic, social anxiety</td><td>Particularly good for physical anxiety symptoms. 75-225mg. BP check at higher doses.</td></tr>
<tr><td><strong>Duloxetine</strong></td><td>SNRI</td><td>GAD</td><td>Good for pain and anxiety comorbidity. 60-120mg.</td></tr>
</tbody></table>
<p><strong>Initial side effects:</strong> SSRIs/SNRIs often briefly worsen anxiety in the first 1-2 weeks. This is expected and temporary - it does not mean the medication is wrong. Start at half the usual dose and increase after 1-2 weeks to reduce this effect.</p>
<p><strong>Duration:</strong> At least 12 months after full response. Stopping too early is the most common reason for relapse. When stopping, taper slowly (reduce by 25% every 4-6 weeks).</p>
<p><strong>Other options:</strong></p>
<ul>
<li><strong>Pregabalin (Lyrica):</strong> Effective for GAD specifically. Rapid onset (days). Risk of dependence and weight gain. Schedule 4 in Australia.</li>
<li><strong>Buspirone:</strong> Non-addictive. Effective for GAD. Slow onset (4-6 weeks). Well tolerated. Good for long-term use.</li>
<li><strong>Beta-blockers (propranolol):</strong> Useful for situational performance anxiety (presentations, examinations). Not for chronic anxiety.</li>
<li><strong>Benzodiazepines:</strong> Effective acutely but create dependence, impair exposure-based therapy, and worsen anxiety long-term. Avoid routine use.</li>
</ul>"""
            }
        ]
    }
]


def build_items_js(groups):
    lines = []
    lines.append("var ANX_PE_GROUPS=[")
    for gi, g in enumerate(groups):
        label = "null" if g["label"] is None else ("'" + esc(g["label"]) + "'")
        optional = "true" if g["optional"] else "false"
        lines.append("  {label:" + label + ",optional:" + optional + ",items:[")
        for ii, item in enumerate(g["items"]):
            title = esc(item["title"])
            body = esc(item["body"])
            body = body.replace("\n", " ").replace("  ", " ")
            comma = "," if ii < len(g["items"]) - 1 else ""
            lines.append("    {id:'" + item["id"] + "',title:'" + title + "',body:'" + body + "'}" + comma)
        group_comma = "," if gi < len(groups) - 1 else ""
        lines.append("  ]}" + group_comma)
    lines.append("]")
    return "\n".join(lines)


groups_js = build_items_js(groups)

html = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>Anxiety Disorders Psychoeducation  -  Dr Benjamin Murrie</title>
<style>
:root{--bg:#f0f2f5;--surface:#fff;--border:#e2e6ed;--text:#1a1d23;--muted:#6b7280;--anx:#4f46e5;--anx-bg:#eef2ff;--anx-dark:#312e81;--anx-mid:#4338ca;--navy:#0f172a;--sans:-apple-system,BlinkMacSystemFont,\'Segoe UI\',sans-serif}
*{box-sizing:border-box;margin:0;padding:0;-webkit-tap-highlight-color:transparent}
body{font-family:var(--sans);background:var(--bg);color:var(--text);font-size:15px;min-height:100vh}
.topbar{background:var(--navy);padding:10px 14px;border-bottom:3px solid var(--anx);display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.topbar-title{font-size:13px;font-weight:800;color:#c7d2fe;letter-spacing:.05em;text-transform:uppercase;white-space:nowrap;flex-shrink:0}
.ti{background:#1e293b;border:1px solid #334155;color:#f1f5f9;padding:5px 9px;border-radius:7px;font:inherit;font-size:13px;min-width:0}
.ti::placeholder{color:#64748b}
.ti:focus{outline:1px solid var(--anx);background:#243349}
.content{max-width:900px;margin:0 auto;padding:14px 12px 40px}
.condition-block{margin-bottom:14px;border-radius:10px;overflow:hidden;border:1px solid var(--border)}
.condition-header{padding:10px 14px;font:700 12px var(--sans);letter-spacing:.06em;text-transform:uppercase;color:#fff;background:var(--anx-dark);display:flex;align-items:center;gap:10px}
.cond-sel-btns{margin-left:auto;display:flex;gap:5px;flex-shrink:0}
.cond-sel-btn{background:rgba(255,255,255,.18);border:1px solid rgba(255,255,255,.35);color:#fff;font:600 11px var(--sans);padding:3px 10px;border-radius:5px;cursor:pointer}
.cond-sel-btn:hover{background:rgba(255,255,255,.3)}
.topic-list{background:#fff}
.pe-group-label{font-size:10px;font-weight:800;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);padding:10px 14px 5px;background:#f8fafc;border-top:1px solid #f0f2f5}
.pe-section{border-top:1px solid #f4f5f8}
.pe-section:first-child{border-top:none}
.pe-header{display:flex;align-items:center;gap:9px;padding:9px 14px;cursor:pointer;user-select:none;-webkit-user-select:none}
.pe-header:hover{background:#f9fafb}
.pe-tick-btn{font-size:1rem;color:var(--muted);flex-shrink:0;min-width:20px;text-align:center;line-height:1;padding:2px;border-radius:4px}
.pe-title{font-weight:600;font-size:13px;color:var(--text);flex:1;line-height:1.35}
.pe-arrow{font-size:9px;color:var(--muted);flex-shrink:0;transition:transform .15s;margin-left:auto}
.pe-section.pe-open .pe-arrow{transform:rotate(90deg)}
.pe-body{display:none;padding:8px 14px 14px 43px;font-size:12.5px;line-height:1.65;color:#374151;border-top:1px solid #f4f5f8}
.pe-section.pe-open .pe-body{display:block}
.pe-body p{margin:0 0 7px}
.pe-body p:last-child{margin:0}
.pe-body ul,.pe-body ol{margin:4px 0 8px 16px}
.pe-body li{margin-bottom:4px}
.pe-body table{width:100%;border-collapse:collapse;font-size:11.5px;margin:6px 0 10px}
.pe-body th{background:#f1f5f9;padding:5px 8px;text-align:left;border:1px solid var(--border);font-size:11px}
.pe-body td{padding:4px 8px;border:1px solid var(--border);vertical-align:top}
.pe-section.anx-done{background:#eef2ff}
.pe-section.anx-done .pe-tick-btn{color:var(--anx)}
.pe-section.pe-optional{opacity:.88}
.export-row{background:#fff;border:1px solid var(--border);border-radius:10px;padding:11px 14px;margin-bottom:14px;display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.export-row .ex-label{font:700 12px var(--sans);color:var(--muted);flex-shrink:0}
.abtn{padding:7px 14px;border-radius:8px;border:1.5px solid var(--border);background:#fff;color:var(--text);font:600 12px var(--sans);cursor:pointer;transition:background .1s,border-color .1s}
.abtn:hover{background:#f3f4f6;border-color:#94a3b8}
.abtn.copied{background:#dcfce7;border-color:#86efac;color:#166534}
.preview-wrap{background:#fff;border:1px solid var(--border);border-radius:10px;overflow:hidden}
.preview-head{background:#f8fafc;border-bottom:1px solid var(--border);padding:9px 14px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px}
.preview-head-title{font:700 11px var(--sans);text-transform:uppercase;letter-spacing:.05em;color:var(--muted)}
.preview-body{padding:22px 26px;font-family:Arial,sans-serif;font-size:10pt;line-height:1.55;color:#111;min-height:100px}
.preview-body .empty-msg{color:var(--muted);font-style:italic;text-align:center;padding:36px 20px;font-size:11pt}
.ho-header{margin-bottom:16px;padding-bottom:12px;border-bottom:2px solid #e5e7eb}
.ho-pt{font-size:17pt;font-weight:800;color:#0f172a;margin-bottom:2px}
.ho-meta{font-size:9pt;color:#6b7280;margin-bottom:12px}
.ho-notice{font-size:9.5pt;background:#eef2ff;border-left:3px solid #4f46e5;padding:9px 12px;line-height:1.5;color:#312e81}
.ho-condition-title{font-size:15pt;font-weight:800;padding:8px 12px;border-radius:6px;margin:20px 0 10px;color:#fff;background:var(--anx-dark)}
.ho-group-label{font-size:9pt;font-weight:800;text-transform:uppercase;letter-spacing:.07em;margin:12px 0 6px;padding-bottom:3px;border-bottom-width:2px;border-bottom-style:solid}
.ho-group-label.anx-g-core{color:#312e81;border-bottom-color:#312e81}
.ho-group-label.anx-g-social{color:#0369a1;border-bottom-color:#0369a1}
.ho-group-label.anx-g-panic{color:#c2410c;border-bottom-color:#c2410c}
.ho-group-label.anx-g-gad{color:#6d28d9;border-bottom-color:#6d28d9}
.ho-group-label.anx-g-ago{color:#0f766e;border-bottom-color:#0f766e}
.ho-group-label.anx-g-health{color:#be185d;border-bottom-color:#be185d}
.ho-group-label.anx-g-trait{color:#4d7c0f;border-bottom-color:#4d7c0f}
.ho-group-label.anx-g-meds{color:#92400e;border-bottom-color:#92400e}
.ho-topic{margin-bottom:7px;padding:9px 12px;border:1px solid #e5e7eb;border-radius:7px;background:#f5f5ff}
.ho-topic-title{font-weight:700;font-size:11pt;color:#0f172a;margin:0 0 6px;padding-bottom:5px;border-bottom:1px solid #e5e7eb}
.ho-topic-body{font-size:10pt;line-height:1.65;color:#374151}
.ho-topic-body p{margin:0 0 6px}
.ho-topic-body p:last-child{margin:0}
.ho-topic-body ul,.ho-topic-body ol{margin:3px 0 7px 16px}
.ho-topic-body li{margin-bottom:3px}
.ho-topic-body table{width:100%;border-collapse:collapse;font-size:9.5pt;margin:5px 0 8px}
.ho-topic-body th{background:#eef2ff;padding:4px 7px;text-align:left;border:1px solid #d1d5db;font-size:9pt}
.ho-topic-body td{padding:3px 7px;border:1px solid #d1d5db;vertical-align:top}
.ho-footer{margin-top:24px;padding-top:12px;border-top:1px solid #e5e7eb;font-size:8.5pt;color:#9ca3af;font-style:italic}
</style>
</head>
<body>
<div class="topbar">
  <span class="topbar-title">Anxiety Psychoeducation</span>
  <input class="ti" id="ptName" placeholder="Patient name..." style="flex:1;min-width:130px;max-width:210px" oninput="refresh()">
  <input class="ti" id="ptDate" type="date" style="flex:0 0 128px" oninput="refresh()">
  <input class="ti" id="drName" placeholder="Clinician name..." style="flex:1;min-width:130px;max-width:200px" oninput="refresh()">
</div>
<div class="content">
  <div class="condition-block">
    <div class="condition-header">
      Anxiety Disorders  -  Topics
      <div class="cond-sel-btns">
        <button class="cond-sel-btn" onclick="selectAll()">Select all</button>
        <button class="cond-sel-btn" onclick="clearAll()">Clear all</button>
      </div>
    </div>
    <div class="topic-list" id="anx-topic-list"></div>
  </div>
  <div class="export-row">
    <span class="ex-label">Export</span>
    <button class="abtn" id="btn-docx" onclick="dlDocx()">Download .docx</button>
    <button class="abtn" id="btn-plain" onclick="copyPlain(this)">Copy plain text</button>
    <button class="abtn" id="btn-fmt" onclick="copyFormatted(this)">Copy formatted</button>
  </div>
  <div class="preview-wrap">
    <div class="preview-head">
      <span class="preview-head-title">Handout Preview</span>
      <button class="abtn" onclick="refresh()" style="padding:4px 11px;font-size:11px">Refresh</button>
    </div>
    <div class="preview-body" id="preview">
      <div class="empty-msg">Tick topics above to generate the handout.</div>
    </div>
  </div>
</div>
<script>
''' + groups_js + r'''

var sel = {};
var ANX_GROUP_COLORS = {
  'null': 'anx-g-core',
  'Social Anxiety': 'anx-g-social',
  'Panic Disorder': 'anx-g-panic',
  'Generalised Anxiety Disorder': 'anx-g-gad',
  'Agoraphobia': 'anx-g-ago',
  'Health Anxiety': 'anx-g-health',
  'Trait Anxiety': 'anx-g-trait',
  'Medication': 'anx-g-meds'
};

function $(id){return document.getElementById(id);}
function f(id){var el=$(id);return el?el.value.trim():'';}
function esc(s){if(!s)return '';return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}
function spaceBody(s){return s.replace(/<\/p>/gi,'</p><br>').replace(/<\/ul>/gi,'</ul><br>').replace(/<\/ol>/gi,'</ol><br>');}

function renderTopics(){
  var el=$('anx-topic-list'); if(!el) return;
  var html='';
  ANX_PE_GROUPS.forEach(function(g){
    if(g.label) html+='<div class="pe-group-label">'+(g.optional?'<span style="font-size:9px;opacity:.6;font-weight:600;margin-right:4px">OPTIONAL</span>':'')+esc(g.label)+'</div>';
    g.items.forEach(function(item){
      var done=!!sel[item.id];
      html+='<div class="pe-section'+(done?' anx-done':'')+(g.optional?' pe-optional':'')+'" data-id="'+item.id+'">';
      html+='<div class="pe-header">';
      html+='<span class="pe-tick-btn">'+(done?'&#9745;':'&#9744;')+'</span>';
      html+='<span class="pe-title">'+esc(item.title)+'</span>';
      html+='<span class="pe-arrow">&#9658;</span>';
      html+='</div>';
      html+='<div class="pe-body">'+item.body+'</div>';
      html+='</div>';
    });
  });
  el.innerHTML=html;
  el.addEventListener('click',function(e){
    var sec=e.target.closest('[data-id]'); if(!sec) return;
    var id=sec.getAttribute('data-id');
    if(e.target.classList.contains('pe-tick-btn')){
      e.stopPropagation();
      sel[id]=!sel[id];
      sec.classList.toggle('anx-done',!!sel[id]);
      sec.querySelector('.pe-tick-btn').innerHTML=sel[id]?'&#9745;':'&#9744;';
      refresh();
    } else {
      var hdr=e.target.closest('.pe-header'); if(hdr) sec.classList.toggle('pe-open');
    }
  });
}

function selectAll(){ANX_PE_GROUPS.forEach(function(g){g.items.forEach(function(item){sel[item.id]=true;});});renderTopics();refresh();}
function clearAll(){Object.keys(sel).forEach(function(k){sel[k]=false;});renderTopics();refresh();}

function getSelectedItems(){
  var result=[];
  ANX_PE_GROUPS.forEach(function(g){g.items.forEach(function(item){if(sel[item.id])result.push({group:g.label,item:item});});});
  return result;
}

function buildHandout(){
  var items=getSelectedItems(); if(!items.length) return null;
  var name=f('ptName')||'Patient';
  var dr=f('drName')||'Your clinician';
  var dv=f('ptDate'),ds=dv?new Date(dv+'T12:00:00').toLocaleDateString('en-AU',{day:'numeric',month:'long',year:'numeric'}):'';
  var h='<div class="ho-header"><div class="ho-pt">Anxiety Disorders - Psychoeducation Handout</div>';
  h+='<div class="ho-meta">Patient: <strong>'+esc(name)+'</strong>';
  if(ds) h+=' &nbsp;|&nbsp; '+esc(ds);
  h+=' &nbsp;|&nbsp; Clinician: <strong>'+esc(dr)+'</strong></div>';
  h+='<div class="ho-notice">Educational material only - all decisions should be made with your treating clinician.</div></div>';
  h+='<div class="ho-condition-title">Anxiety Disorders</div>';
  var curGroup=null;
  ANX_PE_GROUPS.forEach(function(g){
    g.items.forEach(function(item){
      if(!sel[item.id]) return;
      var gKey=g.label||'null';
      if(gKey!==curGroup){
        if(g.label){var cls=ANX_GROUP_COLORS[g.label]||'anx-g-core';h+='<div class="ho-group-label '+cls+'">'+esc(g.label)+'</div>';}
        curGroup=gKey;
      }
      h+='<div class="ho-topic"><div class="ho-topic-title">'+esc(item.title)+'</div><div class="ho-topic-body">'+item.body+'</div></div>';
    });
  });
  h+='<div class="ho-footer">Prepared for '+esc(name)+(ds?' on '+esc(ds):'')+'. Not a substitute for clinical advice.</div>';
  return h;
}

function refresh(){
  var html=buildHandout();
  var pv=$('preview');
  if(!html){pv.innerHTML='<div class="empty-msg">Tick topics above to generate the handout.</div>';return;}
  pv.innerHTML=html;
}

function buildDocxHtml(){
  var html=buildHandout(); if(!html) return null;
  return '<html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:w="urn:schemas-microsoft-com:office:word" xmlns="http://www.w3.org/TR/REC-html40"><head><meta charset="UTF-8"><style>@page{margin:2cm 2.5cm;}body{font-family:Arial,sans-serif;font-size:11pt;line-height:1.5;color:#111;}.ho-header{margin-bottom:14pt;padding-bottom:10pt;border-bottom:1pt solid #e5e7eb;}.ho-pt{font-size:17pt;font-weight:bold;color:#0f172a;margin-bottom:3pt;}.ho-meta{font-size:9pt;color:#6b7280;margin-bottom:10pt;}.ho-notice{font-size:9.5pt;background:#eef2ff;border-left:3pt solid #4f46e5;padding:8pt 10pt;color:#312e81;}.ho-condition-title{font-size:14pt;font-weight:bold;padding:7pt 10pt;background:#312e81;color:#fff;margin:18pt 0 9pt;}.ho-group-label{font-size:8.5pt;font-weight:bold;text-transform:uppercase;letter-spacing:.06em;margin:11pt 0 5pt;padding-bottom:2pt;border-bottom:1.5pt solid currentColor;}.ho-group-label.anx-g-core{color:#312e81;}.ho-group-label.anx-g-social{color:#0369a1;}.ho-group-label.anx-g-panic{color:#c2410c;}.ho-group-label.anx-g-gad{color:#6d28d9;}.ho-group-label.anx-g-ago{color:#0f766e;}.ho-group-label.anx-g-health{color:#be185d;}.ho-group-label.anx-g-trait{color:#4d7c0f;}.ho-group-label.anx-g-meds{color:#92400e;}.ho-topic{margin-bottom:7pt;padding:8pt 11pt;border:1pt solid #e5e7eb;background:#f5f5ff;}.ho-topic-title{font-weight:bold;font-size:11pt;color:#0f172a;margin:0 0 5pt;padding-bottom:4pt;border-bottom:1pt solid #e5e7eb;}.ho-topic-body{font-size:10pt;line-height:1.65;color:#374151;}.ho-topic-body p{margin:0 0 5pt;}.ho-topic-body ul,.ho-topic-body ol{margin:3pt 0 6pt 14pt;}.ho-topic-body li{margin-bottom:3pt;}.ho-footer{margin-top:20pt;padding-top:10pt;border-top:1pt solid #e5e7eb;font-size:8pt;color:#9ca3af;font-style:italic;}</style></head><body>'+html+'</body></html>';
}

function dlDocx(){
  var docx=buildDocxHtml(); if(!docx){alert('No topics selected.');return;}
  var name=(f('ptName')||'Patient').replace(/[^a-zA-Z0-9]/g,'_');
  var blob=new Blob(['﻿'+docx],{type:'application/msword;charset=utf-8'});
  var url=URL.createObjectURL(blob),a=document.createElement('a');
  a.href=url;a.download='Anxiety_Psychoeducation_'+name+'.doc';
  document.body.appendChild(a);a.click();document.body.removeChild(a);
  setTimeout(function(){URL.revokeObjectURL(url);},2000);
  flash($('btn-docx'),'Downloaded!');
}

function buildPasteHtml(){
  if(!buildHandout()) return null;
  var name=f('ptName')||'Patient';
  var dr=f('drName')||'Your clinician';
  var dv=f('ptDate'),ds=dv?new Date(dv+'T12:00:00').toLocaleDateString('en-AU',{day:'numeric',month:'long',year:'numeric'}):'';
  var sp='<p style="margin:0;line-height:1.2">&nbsp;</p>';
  var h='<div style="font-family:Arial,sans-serif;font-size:10pt;line-height:1.6;color:#111">';
  h+='<p style="font-size:14pt;font-weight:bold;margin:0"><b>Anxiety Disorders - Psychoeducation Handout</b></p>';
  h+=sp;
  h+='<p style="font-size:9pt;color:#555;margin:0">Patient: <b>'+esc(name)+'</b>';
  if(ds) h+=' | '+esc(ds);
  if(dr) h+=' | Clinician: <b>'+esc(dr)+'</b>';
  h+='</p>'+sp;
  h+='<p style="font-size:12pt;font-weight:bold;color:#fff;background:#312e81;padding:4px 8px;margin:0"><b>Anxiety Disorders</b></p>'+sp;
  var curGroup=null;
  ANX_PE_GROUPS.forEach(function(g){
    g.items.forEach(function(item){
      if(!sel[item.id]) return;
      if(g.label&&g.label!==curGroup){curGroup=g.label;h+='<p style="font-weight:bold;text-transform:uppercase;font-size:8pt;color:#444;margin:0"><b>'+esc(g.label)+'</b></p>'+sp;}
      h+='<div style="border:1px solid #ccc;padding:7px 10px">';
      h+='<p style="font-weight:bold;margin:0;padding-bottom:4px;border-bottom:1px solid #e0e0e0"><b>'+esc(item.title)+'</b></p><br>';
      h+=spaceBody(item.body);
      h+='</div>'+sp;
    });
  });
  h+='<p style="color:#999;font-size:8pt;font-style:italic;margin:0"><i>Prepared for '+esc(name)+(ds?' on '+esc(ds):'')+'. Not a substitute for clinical advice.</i></p></div>';
  return h;
}

function copyPlain(btn){
  if(!buildHandout()){alert('No topics selected.');return;}
  navigator.clipboard.writeText($('preview').innerText||$('preview').textContent).then(function(){flash(btn,'Copied!');}).catch(function(){});
}

function copyFormatted(btn){
  var content=buildPasteHtml(); if(!content){alert('No topics selected.');return;}
  var el=document.createElement('div');
  el.style.cssText='position:fixed;left:-9999px;top:0;width:780px;background:#fff;overflow:hidden';
  el.innerHTML=content;document.body.appendChild(el);
  var range=document.createRange();range.selectNodeContents(el);
  var wsel=window.getSelection();wsel.removeAllRanges();wsel.addRange(range);
  var ok=false;try{ok=document.execCommand('copy');}catch(ex){}
  wsel.removeAllRanges();document.body.removeChild(el);
  if(ok){flash(btn,'Copied!');}
  else if(window.ClipboardItem){
    var blob=new Blob([content],{type:'text/html'});
    navigator.clipboard.write([new ClipboardItem({'text/html':blob})]).then(function(){flash(btn,'Copied!');}).catch(function(){copyPlain(btn);});
  } else {copyPlain(btn);}
}

function flash(btn,msg){
  if(!btn)return;var orig=btn.textContent;
  btn.textContent=msg;btn.classList.add('copied');
  setTimeout(function(){btn.textContent=orig;btn.classList.remove('copied');},2000);
}

document.addEventListener('DOMContentLoaded',function(){
  var td=new Date().toISOString().slice(0,10);
  var dtEl=$('ptDate'); if(dtEl&&!dtEl.value) dtEl.value=td;
  renderTopics();refresh();
});
</script>
</body>
</html>'''

import os
BASE = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(BASE, 'anxiety-psychoeducation.html')
with open(out, 'w', encoding='utf-8') as fh:
    fh.write(html)
print("Written:", out)
