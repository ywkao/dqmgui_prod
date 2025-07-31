from Monitoring.Overview.GUI import CompWorkspace


class CompCoreWorkspace(CompWorkspace):
    class Summary:
        plugin = "CompCore"
        name = "CERN, Core Infrastructure"

    def __init__(self, gui, rank, category, name, *args):
        CompWorkspace.__init__(
            self, gui, rank, category, "core", name, [self.Summary()]
        )
        gui._addJSFragment("%s/javascript/Overview/Core.js" % gui.contentpath)

    def _state(self, session):
        print("[DEBUG] dqmgui_prod/src/python/Overview/Core.py::Core._state() called")
        print(f"[DEBUG] session keys: {list(session.keys())}")
        print(f"[DEBUG] dqm.sample.runnr = {session.get('dqm.sample.runnr', 'NOT_FOUND')}")
        print(f"[DEBUG] session data: {session}")
        result = self._dostate(session, "CERN_Core_infrastructure_monitor")
        print(f"[DEBUG] _dostate result: {result}")
        return result
