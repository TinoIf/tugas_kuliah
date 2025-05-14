<!-- resources/views/products/create.blade.php -->
<!DOCTYPE html>
<html>
<head>
    <title>Add Product</title>
</head>
<body>
    <h1>Add Product</h1>
    <form action="{{ route('products.store') }}" method="POST">
        @csrf
        <p>
            Name: <input type="text" name="name" required>
        </p>
        <p>
            Price: <input type="number" name="price" step="0.01" required>
        </p>
        <p>
            Description: <textarea name="description"></textarea>
        </p>
        <button type="submit">Save</button>
    </form>
    <a href="{{ route('products.index') }}">Back</a>
</body>
</html>
