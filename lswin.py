#!/usr/bin/env python

import Quartz

#wl = Quartz.CGWindowListCopyWindowInfo( Quartz.kCGWindowListOptionOnScreenOnly | Quartz.kCGWindowListExcludeDesktopElements, Quartz.kCGNullWindowID)
wl = Quartz.CGWindowListCopyWindowInfo( Quartz.kCGWindowListOptionAll, Quartz.kCGNullWindowID)
wl = sorted(wl, key=lambda k: k.valueForKey_('kCGWindowOwnerPID'))

print 'PID\tWinID\tonScreen\tx\ty\tw\th\tTitle\tSubTitle'

for v in wl:
	bounds = v.valueForKey_('kCGWindowBounds')
	print (\
		str(v.valueForKey_('kCGWindowOwnerPID') or '') + \
		'\t' + str(v.valueForKey_('kCGWindowNumber') or '') + \
		'\t' + str(v.valueForKey_('kCGWindowIsOnscreen') or False) + \
		'\t' + str('' if bounds is None else int(bounds.valueForKey_('X'))) + \
		'\t' + str('' if bounds is None else int(bounds.valueForKey_('Y'))) + \
		'\t' + str('' if bounds is None else int(bounds.valueForKey_('Width'))) + \
		'\t' + str('' if bounds is None else int(bounds.valueForKey_('Height'))) + \
		'\t' + (v.valueForKey_('kCGWindowOwnerName') or '') + \
		'\t' + (v.valueForKey_('kCGWindowName') or '') \
	).encode('utf8')
