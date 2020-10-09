import jenkins

jenkins_url = os.environ.get["JENKINS_URL"]
jenkins_username = os.environ.get["JENKINS_USERNAME"]
jenkins_password = os.environ.get["JENKINS_PASSWORD"]
jenkins_job = "job-name" 

def main():
    server = jenkins.Jenkins(jenkins_url,username=jenkins_username,password=jenkins_password)
    server.create_job(jenkins_job,job_xml)
    server.build_job(jenkins_job)

job_xml = """ 
<project>
<actions/>
<description/>
<keepDependencies>false</keepDependencies>
<properties>
<com.dabsquared.gitlabjenkins.connection.GitLabConnectionProperty plugin="gitlab-plugin@1.5.3">
<gitLabConnection>gitlab</gitLabConnection>
</com.dabsquared.gitlabjenkins.connection.GitLabConnectionProperty>
</properties>
<scm class="hudson.scm.NullSCM"/>
<canRoam>true</canRoam>
<disabled>false</disabled>
<blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
<blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
<triggers/>
<concurrentBuild>false</concurrentBuild>
<builders>
<javaposse.jobdsl.plugin.ExecuteDslScripts plugin="job-dsl@1.67">
<usingScriptText>true</usingScriptText>
<sandbox>false</sandbox>
<ignoreExisting>false</ignoreExisting>
<ignoreMissingFiles>false</ignoreMissingFiles>
<failOnMissingPlugin>false</failOnMissingPlugin>
<unstableOnDeprecation>false</unstableOnDeprecation>
<removedJobAction>IGNORE</removedJobAction>
<removedViewAction>IGNORE</removedViewAction>
<removedConfigFilesAction>IGNORE</removedConfigFilesAction>
<lookupStrategy>JENKINS_ROOT</lookupStrategy>
</javaposse.jobdsl.plugin.ExecuteDslScripts>
</builders>
<publishers/>
<buildWrappers/>
</project>
 """

main()
