public with sharing class myclass {
	public myclass() {
		System.debug(LoggingLevel.DEBUG, 'test');
	}

	public String getAppVersion() {
		return '1.0.0';
	}
}
