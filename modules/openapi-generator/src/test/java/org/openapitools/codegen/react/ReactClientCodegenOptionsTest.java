package org.openapitools.codegen.react;

import org.openapitools.codegen.AbstractOptionsTest;
import org.openapitools.codegen.CodegenConfig;
import org.openapitools.codegen.languages.ReactClientCodegen;
import org.openapitools.codegen.options.ReactClientCodegenOptionsProvider;

import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.verify;

public class ReactClientCodegenOptionsTest extends AbstractOptionsTest {
    private ReactClientCodegen codegen = mock(ReactClientCodegen.class, mockSettings);

    public ReactClientCodegenOptionsTest() {
        super(new ReactClientCodegenOptionsProvider());
    }

    @Override
    protected CodegenConfig getCodegenConfig() {
        return codegen;
    }

    @SuppressWarnings("unused")
    @Override
    protected void verifyOptions() {
        // TODO: Complete options using Mockito
        // verify(codegen).someMethod(arguments)
    }
}

