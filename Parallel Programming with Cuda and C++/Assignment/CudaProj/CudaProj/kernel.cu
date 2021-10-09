
#include "cuda_runtime.h"
#include "device_launch_parameters.h"

#include <stdio.h>

cudaError_t calcCubesCuda(int *c, const int *a, unsigned int size);
void initializeArray(int* a, unsigned int size);
void calcCubesCPU(int* c, const int* a, unsigned int size);

__global__ void calcCubes(int* out, const int* in) {
    int index = blockIdx.x; // Onedimensional blocks of GPU threads, each block with 1 thread
    out[index] = in[index] * in[index] * in[index];
}


int main()
{
    const int arraySize = 500000;
    int* a = new int[arraySize];

    initializeArray(a, arraySize);

    int* c = new int[arraySize];

    //calcCubesCPU(c, a, arraySize);

    // Add vectors in parallel.
    cudaError_t cudaStatus = calcCubesCuda(c, a, arraySize);

    if (cudaStatus != cudaSuccess) {
        fprintf(stderr, "addWithCuda failed!");
        return 1;
    }

    // cudaDeviceReset must be called before exiting in order for profiling and
    // tracing tools such as Nsight and Visual Profiler to show complete traces.
    cudaStatus = cudaDeviceReset();
    if (cudaStatus != cudaSuccess) {
        fprintf(stderr, "cudaDeviceReset failed!");
        return 1;
    }

    printf("a^3 = {");
    for (int i = 0; i < 100; i++) {
        if (i) printf(", ");
        printf("%d", c[i]);
    }
    printf("}\n\n");

    return 0;
}

// Helper function for using CUDA to add vectors in parallel.
cudaError_t calcCubesCuda(int *c, const int *a, unsigned int size)
{
    int *dev_a = 0;
    int *dev_c = 0;
    cudaError_t cudaStatus;

    // Choose which GPU to run on, change this on a multi-GPU system.
    cudaStatus = cudaSetDevice(0);
    if (cudaStatus != cudaSuccess) {
        fprintf(stderr, "cudaSetDevice failed!  Do you have a CUDA-capable GPU installed?");
        goto Error;
    }

    // Allocate GPU buffers for three vectors (two input, one output)    .
    cudaStatus = cudaMalloc((void**)&dev_c, size * sizeof(int));
    if (cudaStatus != cudaSuccess) {
        fprintf(stderr, "cudaMalloc failed!");
        goto Error;
    }

    cudaStatus = cudaMalloc((void**)&dev_a, size * sizeof(int));
    if (cudaStatus != cudaSuccess) {
        fprintf(stderr, "cudaMalloc failed!");
        goto Error;
    }

    // Copy input vectors from host memory to GPU buffers.
    cudaStatus = cudaMemcpy(dev_a, a, size * sizeof(int), cudaMemcpyHostToDevice);
    if (cudaStatus != cudaSuccess) {
        fprintf(stderr, "cudaMemcpy failed!");
        goto Error;
    }

    // Launch a kernel on the GPU with one thread for each element.
    calcCubes <<<size, 1 >>> (dev_c, dev_a);

    // Check for any errors launching the kernel
    cudaStatus = cudaGetLastError();
    if (cudaStatus != cudaSuccess) {
        fprintf(stderr, "addKernel launch failed: %s\n", cudaGetErrorString(cudaStatus));
        goto Error;
    }
    
    // cudaDeviceSynchronize waits for the kernel to finish, and returns
    // any errors encountered during the launch.
    cudaStatus = cudaDeviceSynchronize();
    if (cudaStatus != cudaSuccess) {
        fprintf(stderr, "cudaDeviceSynchronize returned error code %d after launching addKernel!\n", cudaStatus);
        goto Error;
    }

    // Copy output vector from GPU buffer to host memory.
    cudaStatus = cudaMemcpy(c, dev_c, size * sizeof(int), cudaMemcpyDeviceToHost);
    if (cudaStatus != cudaSuccess) {
        fprintf(stderr, "cudaMemcpy failed!");
        goto Error;
    }

Error:
    cudaFree(dev_c);
    cudaFree(dev_a);
    
    return cudaStatus;
}

void initializeArray(int* a, unsigned int size)
{
    for (int i = 0; i < size; i++) {
        a[i] = i % 10;
    }
}

void calcCubesCPU(int* c, const int* a, unsigned int size)
{
    for (int i = 0; i < size; i++) {
        c[i] = a[i] * a[i] * a[i]; // calculate cubes of ai
    }
}
