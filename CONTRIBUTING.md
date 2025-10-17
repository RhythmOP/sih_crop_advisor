# Contributing to Localized Crop Advisor

Thank you for your interest in contributing to the LCA project! This document provides guidelines for contributing.

---

## How to Contribute

### Reporting Bugs

**Before submitting a bug report**:
1. Check existing issues to avoid duplicates
2. Collect relevant information (OS, versions, error messages)
3. Test with the latest version

**Creating a bug report**:
```markdown
**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '...'
3. See error

**Expected behavior**
What you expected to happen.

**Screenshots**
If applicable, add screenshots.

**Environment**:
- OS: [e.g., macOS 13.0]
- Python Version: [e.g., 3.9.7]
- Node Version: [e.g., 18.0.0]
- Device: [e.g., iPhone 14, Android Emulator]
```

---

## Development Setup

### Backend Development

1. **Fork and clone the repository**
2. **Set up development environment**:
   ```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Create `.env` file** with your API keys
4. **Run tests** (when available):
   ```bash
   pytest tests/
   ```

### Mobile Development

1. **Install dependencies**:
   ```bash
   cd mobile
   npm install
   ```
2. **Start development server**:
   ```bash
   npm start
   ```

---

## Code Style Guidelines

### Python (Backend)

- Follow **PEP 8** style guide
- Use **type hints** where applicable
- Write **docstrings** for all functions
- Keep functions **small and focused**

**Example**:
```python
def calculate_suitability(
    crop_name: str,
    soil_data: Dict[str, Any],
    weather_data: Dict[str, Any]
) -> float:
    """
    Calculate suitability score for a crop.
    
    Args:
        crop_name: Name of the crop
        soil_data: Dictionary containing soil properties
        weather_data: Dictionary containing weather conditions
    
    Returns:
        Suitability score between 0.0 and 1.0
    """
    # Implementation
    pass
```

### JavaScript (Mobile)

- Use **ESLint** configuration
- Follow **React best practices**
- Use **functional components** with hooks
- Write **PropTypes** or TypeScript types

**Example**:
```javascript
/**
 * Display crop recommendation card
 * @param {Object} crop - Crop recommendation data
 * @param {number} index - Position in list
 */
const CropCard = ({ crop, index }) => {
  // Component implementation
};
```

---

## Adding New Features

### 1. New Crop

**Backend** (`app/data/crop_database.py`):
```python
'NewCrop': {
    'name': 'NewCrop',
    'scientific_name': 'Scientific Name',
    'growth_duration': 'X-Y days',
    'water_requirement': 'Low/Medium/High',
    'season': 'Season name',
    'soil_types': ['Type1', 'Type2'],
    'description': 'Brief description',
    'market_demand': 'Low/Medium/High/Very High'
}
```

**ML Model** (`app/models/crop_model.py`):
```python
'NewCrop': {
    'ph': (min, max),
    'nitrogen': 1-3,
    'phosphorus': 1-3,
    'potassium': 1-3,
    'temp': (min, max),
    'humidity': (min, max),
    'rainfall': (min, max)
}
```

### 2. New Language

**Mobile** (`src/i18n/locales/`):
1. Create `{lang_code}.json` file
2. Copy structure from `en.json`
3. Translate all strings
4. Update `src/i18n/config.js`:
   ```javascript
   import newLang from './locales/new_lang.json';
   
   resources: {
     en: { translation: en },
     hi: { translation: hi },
     newLang: { translation: newLang },
   }
   ```

### 3. New API Endpoint

**Backend** (`app/routes.py`):
```python
@api_bp.route('/new-endpoint', methods=['POST'])
def new_endpoint():
    """
    Description of endpoint
    """
    try:
        data = request.get_json()
        # Validation
        # Processing
        return jsonify({
            'success': True,
            'data': result
        }), 200
    except Exception as e:
        return jsonify({
            'error': 'Error message',
            'message': str(e)
        }), 500
```

**Mobile** (`src/services/api.js`):
```javascript
async newMethod(params) {
  try {
    const response = await this.client.post('/new-endpoint', params);
    return response.data;
  } catch (error) {
    throw this._handleError(error);
  }
}
```

---

## Testing

### Backend Tests

```python
# tests/test_recommendation.py
def test_recommendation_service():
    """Test recommendation generation"""
    service = RecommendationService()
    # Test logic
    assert result is not None
```

Run tests:
```bash
cd backend
pytest tests/ -v
```

### Mobile Tests

```javascript
// __tests__/HomeScreen.test.js
import { render } from '@testing-library/react-native';
import HomeScreen from '../src/screens/HomeScreen';

test('renders welcome message', () => {
  const { getByText } = render(<HomeScreen />);
  expect(getByText('Welcome')).toBeTruthy();
});
```

Run tests:
```bash
cd mobile
npm test
```

---

## Pull Request Process

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**:
   - Write clean, documented code
   - Add tests if applicable
   - Update documentation

3. **Commit with clear messages**:
   ```bash
   git commit -m "Add: New crop recommendation for millets"
   git commit -m "Fix: Temperature calculation in hot climates"
   git commit -m "Docs: Update API documentation"
   ```

4. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Create Pull Request**:
   - Describe what you changed and why
   - Reference any related issues
   - Include screenshots for UI changes

**PR Template**:
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Testing
How has this been tested?

## Screenshots (if applicable)
Add screenshots here

## Checklist
- [ ] Code follows project style
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] All tests passing
```

---

## ML Model Improvements

### Training with Real Data

1. **Collect farmer feedback**:
   ```python
   # app/data/farmer_feedback.py
   feedback = {
       'location': (lat, lon),
       'recommended_crop': 'Rice',
       'actual_crop': 'Rice',
       'yield_actual': 4500,
       'yield_predicted': 4600,
       'farmer_rating': 4.5
   }
   ```

2. **Prepare training dataset**:
   ```python
   # scripts/prepare_training_data.py
   X_train = prepare_features(farmer_data)
   y_train = prepare_labels(farmer_data)
   ```

3. **Train model**:
   ```python
   from sklearn.ensemble import RandomForestClassifier
   
   model = RandomForestClassifier()
   model.fit(X_train, y_train)
   model.save('models/trained/crop_rf_v2.pkl')
   ```

4. **Evaluate**:
   ```python
   accuracy = model.score(X_test, y_test)
   print(f"Model accuracy: {accuracy:.2%}")
   ```

---

## Future Enhancement Ideas

### High Priority
- [ ] Database integration (PostgreSQL)
- [ ] User authentication system
- [ ] Farmer feedback collection
- [ ] Model training pipeline
- [ ] Push notifications for recommendations

### Medium Priority
- [ ] Image-based disease detection
- [ ] Market price integration
- [ ] Weather alerts
- [ ] Crop calendar/reminders
- [ ] Community forum

### Low Priority
- [ ] Voice input (multilingual)
- [ ] AR field visualization
- [ ] Blockchain for supply chain
- [ ] Integration with agri-marketplaces

---

## Code Review Guidelines

When reviewing pull requests, check for:

- ✅ **Functionality**: Does it work as intended?
- ✅ **Code Quality**: Is it readable and maintainable?
- ✅ **Documentation**: Are changes documented?
- ✅ **Tests**: Are there adequate tests?
- ✅ **Performance**: Any performance concerns?
- ✅ **Security**: Any security vulnerabilities?

---

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

## Questions?

Feel free to:
- Open an issue for discussion
- Reach out to maintainers
- Check existing documentation

**Thank you for contributing to LCA! 🌾**
