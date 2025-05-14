<!-- resources/views/products/edit.blade.php -->
<!DOCTYPE html>
<html>
<head>
    <title>Edit Product</title>
</head>
<body>
    <h1>Edit Product</h1>
    <form action="{{ route('products.update', $product->id) }}" method="POST">
        @csrf
        @method('PUT')
        <p>
            Name: <input type="text" name="name" value="{{ $product->name }}" required>
        </p>
        <p>
            Price: <input type="number" name="price" step="0.01" value="{{ $product->price }}" required>
        </p>
        <p>
            Description: <textarea name="description">{{ $product->description }}</textarea>
        </p>
        <button type="submit">Update</button>
    </form>
    <a href="{{ route('products.index') }}">Back</a>
</body>
</html>
