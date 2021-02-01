<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE eagle SYSTEM "eagle.dtd">
<eagle version="9.6.2">
<drawing>
<settings>
<setting alwaysvectorfont="no"/>
<setting verticaltext="up"/>
</settings>
<grid distance="0.1" unitdist="inch" unit="inch" style="lines" multiple="1" display="no" altdistance="0.01" altunitdist="inch" altunit="inch"/>
<layers>
<layer number="88" name="SimResults" color="9" fill="1" visible="yes" active="yes"/>
<layer number="89" name="SimProbes" color="9" fill="1" visible="yes" active="yes"/>
<layer number="90" name="Modules" color="5" fill="1" visible="yes" active="yes"/>
<layer number="91" name="Nets" color="2" fill="1" visible="yes" active="yes"/>
<layer number="92" name="Busses" color="1" fill="1" visible="yes" active="yes"/>
<layer number="93" name="Pins" color="2" fill="1" visible="no" active="yes"/>
<layer number="94" name="Symbols" color="4" fill="1" visible="yes" active="yes"/>
<layer number="95" name="Names" color="7" fill="1" visible="yes" active="yes"/>
<layer number="96" name="Values" color="7" fill="0" visible="yes" active="yes"/>
<layer number="97" name="Info" color="50" fill="10" visible="yes" active="yes"/>
<layer number="98" name="Guide" color="6" fill="1" visible="yes" active="yes"/>
</layers>
<schematic xreflabel="%F%N/%S.%C%R" xrefpart="/%S.%C%R">
<libraries>
<library name="wirepad" urn="urn:adsk.eagle:library:412">
<description>&lt;b&gt;Single Pads&lt;/b&gt;&lt;p&gt;
&lt;author&gt;Created by librarian@cadsoft.de&lt;/author&gt;</description>
<packages>
<package name="1,6/0,9" urn="urn:adsk.eagle:footprint:30812/1" library_version="2">
<description>&lt;b&gt;THROUGH-HOLE PAD&lt;/b&gt;</description>
<wire x1="-0.508" y1="0.762" x2="-0.762" y2="0.762" width="0.1524" layer="21"/>
<wire x1="-0.762" y1="0.762" x2="-0.762" y2="0.508" width="0.1524" layer="21"/>
<wire x1="-0.762" y1="-0.508" x2="-0.762" y2="-0.762" width="0.1524" layer="21"/>
<wire x1="-0.762" y1="-0.762" x2="-0.508" y2="-0.762" width="0.1524" layer="21"/>
<wire x1="0.508" y1="-0.762" x2="0.762" y2="-0.762" width="0.1524" layer="21"/>
<wire x1="0.762" y1="-0.762" x2="0.762" y2="-0.508" width="0.1524" layer="21"/>
<wire x1="0.762" y1="0.508" x2="0.762" y2="0.762" width="0.1524" layer="21"/>
<wire x1="0.762" y1="0.762" x2="0.508" y2="0.762" width="0.1524" layer="21"/>
<circle x="0" y="0" radius="0.635" width="0.1524" layer="51"/>
<pad name="1" x="0" y="0" drill="0.9144" diameter="1.6002" shape="octagon"/>
<text x="-0.762" y="1.016" size="1.27" layer="25" ratio="10">&gt;NAME</text>
<text x="0" y="0.6" size="0.0254" layer="27">&gt;VALUE</text>
</package>
</packages>
<packages3d>
<package3d name="1,6/0,9" urn="urn:adsk.eagle:package:30840/1" type="box" library_version="2">
<description>THROUGH-HOLE PAD</description>
<packageinstances>
<packageinstance name="1,6/0,9"/>
</packageinstances>
</package3d>
</packages3d>
<symbols>
<symbol name="PAD" urn="urn:adsk.eagle:symbol:30808/1" library_version="2">
<wire x1="-1.016" y1="1.016" x2="1.016" y2="-1.016" width="0.254" layer="94"/>
<wire x1="-1.016" y1="-1.016" x2="1.016" y2="1.016" width="0.254" layer="94"/>
<text x="-1.143" y="1.8542" size="1.778" layer="95">&gt;NAME</text>
<text x="-1.143" y="-3.302" size="1.778" layer="96">&gt;VALUE</text>
<pin name="P" x="2.54" y="0" visible="off" length="short" direction="pas" rot="R180"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="1,6/0,9" urn="urn:adsk.eagle:component:30858/2" prefix="PAD" uservalue="yes" library_version="2">
<description>&lt;b&gt;THROUGH-HOLE PAD&lt;/b&gt;</description>
<gates>
<gate name="1" symbol="PAD" x="0" y="0"/>
</gates>
<devices>
<device name="" package="1,6/0,9">
<connects>
<connect gate="1" pin="P" pad="1"/>
</connects>
<package3dinstances>
<package3dinstance package3d_urn="urn:adsk.eagle:package:30840/1"/>
</package3dinstances>
<technologies>
<technology name="">
<attribute name="POPULARITY" value="7" constant="no"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
</libraries>
<attributes>
</attributes>
<variantdefs>
</variantdefs>
<classes>
<class number="0" name="default" width="0" drill="0">
</class>
</classes>
<parts>
<part name="GND" library="wirepad" library_urn="urn:adsk.eagle:library:412" deviceset="1,6/0,9" device="" package3d_urn="urn:adsk.eagle:package:30840/1"/>
<part name="CTS" library="wirepad" library_urn="urn:adsk.eagle:library:412" deviceset="1,6/0,9" device="" package3d_urn="urn:adsk.eagle:package:30840/1"/>
<part name="VIN" library="wirepad" library_urn="urn:adsk.eagle:library:412" deviceset="1,6/0,9" device="" package3d_urn="urn:adsk.eagle:package:30840/1"/>
<part name="RXI" library="wirepad" library_urn="urn:adsk.eagle:library:412" deviceset="1,6/0,9" device="" package3d_urn="urn:adsk.eagle:package:30840/1"/>
<part name="TX0" library="wirepad" library_urn="urn:adsk.eagle:library:412" deviceset="1,6/0,9" device="" package3d_urn="urn:adsk.eagle:package:30840/1"/>
<part name="SDI" library="wirepad" library_urn="urn:adsk.eagle:library:412" deviceset="1,6/0,9" device="" package3d_urn="urn:adsk.eagle:package:30840/1"/>
<part name="SCK" library="wirepad" library_urn="urn:adsk.eagle:library:412" deviceset="1,6/0,9" device="" package3d_urn="urn:adsk.eagle:package:30840/1"/>
<part name="GND_" library="wirepad" library_urn="urn:adsk.eagle:library:412" deviceset="1,6/0,9" device="" package3d_urn="urn:adsk.eagle:package:30840/1"/>
<part name="VIN_" library="wirepad" library_urn="urn:adsk.eagle:library:412" deviceset="1,6/0,9" device="" package3d_urn="urn:adsk.eagle:package:30840/1"/>
<part name="5V" library="wirepad" library_urn="urn:adsk.eagle:library:412" deviceset="1,6/0,9" device="" package3d_urn="urn:adsk.eagle:package:30840/1"/>
<part name="~9" library="wirepad" library_urn="urn:adsk.eagle:library:412" deviceset="1,6/0,9" device="" package3d_urn="urn:adsk.eagle:package:30840/1"/>
<part name="~10" library="wirepad" library_urn="urn:adsk.eagle:library:412" deviceset="1,6/0,9" device="" package3d_urn="urn:adsk.eagle:package:30840/1"/>
<part name="BAT" library="wirepad" library_urn="urn:adsk.eagle:library:412" deviceset="1,6/0,9" device="" package3d_urn="urn:adsk.eagle:package:30840/1"/>
<part name="G" library="wirepad" library_urn="urn:adsk.eagle:library:412" deviceset="1,6/0,9" device="" package3d_urn="urn:adsk.eagle:package:30840/1"/>
<part name="~11" library="wirepad" library_urn="urn:adsk.eagle:library:412" deviceset="1,6/0,9" device="" package3d_urn="urn:adsk.eagle:package:30840/1"/>
<part name="A5" library="wirepad" library_urn="urn:adsk.eagle:library:412" deviceset="1,6/0,9" device="" package3d_urn="urn:adsk.eagle:package:30840/1"/>
<part name="A4" library="wirepad" library_urn="urn:adsk.eagle:library:412" deviceset="1,6/0,9" device="" package3d_urn="urn:adsk.eagle:package:30840/1"/>
<part name="BAT1" library="wirepad" library_urn="urn:adsk.eagle:library:412" deviceset="1,6/0,9" device="" package3d_urn="urn:adsk.eagle:package:30840/1"/>
</parts>
<sheets>
<sheet>
<plain>
<rectangle x1="48.26" y1="76.2" x2="134.62" y2="99.06" layer="97"/>
<rectangle x1="71.12" y1="27.94" x2="109.22" y2="66.04" layer="97"/>
<text x="86.36" y="104.14" size="1.778" layer="95">Pro Tinker</text>
<text x="86.36" y="68.58" size="1.778" layer="95">BME680</text>
<text x="-5.08" y="76.2" size="1.778" layer="95">Adafruit Friend</text>
<rectangle x1="-17.78" y1="25.4" x2="22.86" y2="73.66" layer="97"/>
<frame x1="-33.02" y1="-10.16" x2="200.66" y2="132.08" columns="8" rows="5" layer="96"/>
<rectangle x1="127" y1="17.78" x2="195.58" y2="25.4" layer="96"/>
<text x="142.24" y="20.32" size="2.54" layer="96">NNU ROCKSAT: KUAIDA</text>
<rectangle x1="127" y1="10.16" x2="195.58" y2="17.78" layer="96"/>
<rectangle x1="127" y1="2.54" x2="195.58" y2="10.16" layer="96"/>
<rectangle x1="127" y1="-5.08" x2="195.58" y2="2.54" layer="96"/>
<rectangle x1="127" y1="-5.08" x2="162.56" y2="10.16" layer="96"/>
<text x="144.78" y="12.7" size="2.54" layer="96">R.F. Experiment PCB</text>
<text x="137.16" y="5.08" size="2.54" layer="96">2/1/2021</text>
<text x="129.54" y="-2.54" size="2.54" layer="96">Drawing: N_Appleby</text>
<text x="172.72" y="5.08" size="2.54" layer="96">Sheet: 1/1</text>
<text x="165.1" y="-2.54" size="2.54" layer="96">ISGC, ROCKSAT X</text>
</plain>
<instances>
<instance part="GND" gate="1" x="-12.7" y="68.58" smashed="yes">
<attribute name="NAME" x="-13.843" y="70.4342" size="1.778" layer="95"/>
<attribute name="VALUE" x="-13.843" y="65.278" size="1.778" layer="96"/>
</instance>
<instance part="CTS" gate="1" x="12.7" y="68.58" smashed="yes">
<attribute name="NAME" x="11.557" y="70.4342" size="1.778" layer="95"/>
<attribute name="VALUE" x="11.557" y="65.278" size="1.778" layer="96"/>
</instance>
<instance part="VIN" gate="1" x="-2.54" y="68.58" smashed="yes">
<attribute name="NAME" x="-3.683" y="70.4342" size="1.778" layer="95"/>
<attribute name="VALUE" x="-3.683" y="65.278" size="1.778" layer="96"/>
</instance>
<instance part="RXI" gate="1" x="2.54" y="68.58" smashed="yes">
<attribute name="NAME" x="1.397" y="70.4342" size="1.778" layer="95"/>
<attribute name="VALUE" x="1.397" y="65.278" size="1.778" layer="96"/>
</instance>
<instance part="TX0" gate="1" x="7.62" y="68.58" smashed="yes">
<attribute name="NAME" x="6.477" y="70.4342" size="1.778" layer="95"/>
<attribute name="VALUE" x="6.477" y="65.278" size="1.778" layer="96"/>
</instance>
<instance part="SDI" gate="1" x="76.2" y="58.42" smashed="yes">
<attribute name="NAME" x="75.057" y="60.2742" size="1.778" layer="95"/>
<attribute name="VALUE" x="75.057" y="55.118" size="1.778" layer="96"/>
</instance>
<instance part="SCK" gate="1" x="76.2" y="53.34" smashed="yes">
<attribute name="NAME" x="75.057" y="55.1942" size="1.778" layer="95"/>
<attribute name="VALUE" x="75.057" y="50.038" size="1.778" layer="96"/>
</instance>
<instance part="GND_" gate="1" x="76.2" y="40.64" smashed="yes">
<attribute name="NAME" x="75.057" y="42.4942" size="1.778" layer="95"/>
<attribute name="VALUE" x="75.057" y="37.338" size="1.778" layer="96"/>
</instance>
<instance part="VIN_" gate="1" x="76.2" y="35.56" smashed="yes">
<attribute name="NAME" x="75.057" y="37.4142" size="1.778" layer="95"/>
<attribute name="VALUE" x="75.057" y="32.258" size="1.778" layer="96"/>
</instance>
<instance part="5V" gate="1" x="50.8" y="88.9" smashed="yes">
<attribute name="NAME" x="49.657" y="90.7542" size="1.778" layer="95"/>
<attribute name="VALUE" x="49.657" y="85.598" size="1.778" layer="96"/>
</instance>
<instance part="~9" gate="1" x="129.54" y="96.52" smashed="yes">
<attribute name="NAME" x="128.397" y="98.3742" size="1.778" layer="95"/>
<attribute name="VALUE" x="128.397" y="93.218" size="1.778" layer="96"/>
</instance>
<instance part="~10" gate="1" x="121.92" y="96.52" smashed="yes">
<attribute name="NAME" x="120.777" y="98.3742" size="1.778" layer="95"/>
<attribute name="VALUE" x="120.777" y="93.218" size="1.778" layer="96"/>
</instance>
<instance part="BAT" gate="1" x="129.54" y="78.74" smashed="yes">
<attribute name="NAME" x="128.397" y="80.5942" size="1.778" layer="95"/>
<attribute name="VALUE" x="128.397" y="75.438" size="1.778" layer="96"/>
</instance>
<instance part="G" gate="1" x="121.92" y="78.74" smashed="yes">
<attribute name="NAME" x="120.777" y="80.5942" size="1.778" layer="95"/>
<attribute name="VALUE" x="120.777" y="75.438" size="1.778" layer="96"/>
</instance>
<instance part="~11" gate="1" x="114.3" y="96.52" smashed="yes">
<attribute name="NAME" x="113.157" y="98.3742" size="1.778" layer="95"/>
<attribute name="VALUE" x="113.157" y="93.218" size="1.778" layer="96"/>
</instance>
<instance part="A5" gate="1" x="55.88" y="96.52" smashed="yes">
<attribute name="NAME" x="54.737" y="98.3742" size="1.778" layer="95"/>
<attribute name="VALUE" x="54.737" y="93.218" size="1.778" layer="96"/>
</instance>
<instance part="A4" gate="1" x="60.96" y="96.52" smashed="yes">
<attribute name="NAME" x="59.817" y="98.3742" size="1.778" layer="95"/>
<attribute name="VALUE" x="59.817" y="93.218" size="1.778" layer="96"/>
</instance>
<instance part="BAT1" gate="1" x="137.16" y="73.66" smashed="yes">
<attribute name="NAME" x="136.017" y="75.5142" size="1.778" layer="95"/>
<attribute name="VALUE" x="136.017" y="70.358" size="1.778" layer="96"/>
</instance>
</instances>
<busses>
</busses>
<nets>
<net name="N$2" class="0">
<segment>
<pinref part="5V" gate="1" pin="P"/>
<wire x1="53.34" y1="88.9" x2="53.34" y2="45.72" width="0.1524" layer="91"/>
<pinref part="VIN" gate="1" pin="P"/>
<wire x1="0" y1="68.58" x2="0" y2="45.72" width="0.1524" layer="91"/>
<wire x1="0" y1="45.72" x2="53.34" y2="45.72" width="0.1524" layer="91"/>
<wire x1="0" y1="68.58" x2="0" y2="73.66" width="0.1524" layer="91"/>
<junction x="0" y="68.58"/>
<wire x1="0" y1="73.66" x2="-17.78" y2="73.66" width="0.1524" layer="91"/>
<pinref part="VIN_" gate="1" pin="P"/>
<wire x1="-17.78" y1="73.66" x2="-17.78" y2="35.56" width="0.1524" layer="91"/>
<wire x1="-17.78" y1="35.56" x2="78.74" y2="35.56" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$4" class="0">
<segment>
<pinref part="RXI" gate="1" pin="P"/>
<wire x1="5.08" y1="68.58" x2="5.08" y2="116.84" width="0.1524" layer="91"/>
<pinref part="~9" gate="1" pin="P"/>
<wire x1="5.08" y1="116.84" x2="132.08" y2="116.84" width="0.1524" layer="91"/>
<wire x1="132.08" y1="116.84" x2="132.08" y2="96.52" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$5" class="0">
<segment>
<pinref part="TX0" gate="1" pin="P"/>
<wire x1="10.16" y1="68.58" x2="10.16" y2="114.3" width="0.1524" layer="91"/>
<pinref part="~10" gate="1" pin="P"/>
<wire x1="10.16" y1="114.3" x2="124.46" y2="114.3" width="0.1524" layer="91"/>
<wire x1="124.46" y1="114.3" x2="124.46" y2="96.52" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$6" class="0">
<segment>
<pinref part="CTS" gate="1" pin="P"/>
<wire x1="15.24" y1="68.58" x2="15.24" y2="111.76" width="0.1524" layer="91"/>
<wire x1="15.24" y1="111.76" x2="116.84" y2="111.76" width="0.1524" layer="91"/>
<pinref part="~11" gate="1" pin="P"/>
<wire x1="116.84" y1="111.76" x2="116.84" y2="96.52" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$1" class="0">
<segment>
<pinref part="GND" gate="1" pin="P"/>
<pinref part="GND_" gate="1" pin="P"/>
<wire x1="-10.16" y1="68.58" x2="-10.16" y2="40.64" width="0.1524" layer="91"/>
<wire x1="-10.16" y1="40.64" x2="78.74" y2="40.64" width="0.1524" layer="91"/>
<wire x1="78.74" y1="40.64" x2="124.46" y2="40.64" width="0.1524" layer="91"/>
<junction x="78.74" y="40.64"/>
<pinref part="G" gate="1" pin="P"/>
<wire x1="124.46" y1="40.64" x2="124.46" y2="78.74" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$3" class="0">
<segment>
<pinref part="SCK" gate="1" pin="P"/>
<wire x1="78.74" y1="53.34" x2="78.74" y2="50.8" width="0.1524" layer="91"/>
<wire x1="78.74" y1="50.8" x2="58.42" y2="50.8" width="0.1524" layer="91"/>
<pinref part="A5" gate="1" pin="P"/>
<wire x1="58.42" y1="50.8" x2="58.42" y2="96.52" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$7" class="0">
<segment>
<pinref part="SDI" gate="1" pin="P"/>
<wire x1="78.74" y1="58.42" x2="78.74" y2="63.5" width="0.1524" layer="91"/>
<wire x1="78.74" y1="63.5" x2="63.5" y2="63.5" width="0.1524" layer="91"/>
<pinref part="A4" gate="1" pin="P"/>
<wire x1="63.5" y1="63.5" x2="63.5" y2="96.52" width="0.1524" layer="91"/>
</segment>
</net>
</nets>
</sheet>
</sheets>
</schematic>
</drawing>
<compatibility>
<note version="8.2" severity="warning">
Since Version 8.2, EAGLE supports online libraries. The ids
of those online libraries will not be understood (or retained)
with this version.
</note>
<note version="8.3" severity="warning">
Since Version 8.3, EAGLE supports URNs for individual library
assets (packages, symbols, and devices). The URNs of those assets
will not be understood (or retained) with this version.
</note>
<note version="8.3" severity="warning">
Since Version 8.3, EAGLE supports the association of 3D packages
with devices in libraries, schematics, and board files. Those 3D
packages will not be understood (or retained) with this version.
</note>
</compatibility>
</eagle>
