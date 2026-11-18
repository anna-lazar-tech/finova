export const categories = [
  { id: 1, name: 'Зарплата', icon: '↙', color: '#51a58d', category_type: 'income' },
  { id: 2, name: 'Фриланс', icon: '✦', color: '#8c73dc', category_type: 'income' },
  { id: 3, name: 'Еда и кафе', icon: '◒', color: '#efaa68', category_type: 'expense' },
  { id: 4, name: 'Транспорт', icon: '↗', color: '#7299df', category_type: 'expense' },
  { id: 5, name: 'Дом', icon: '⌂', color: '#9a83db', category_type: 'expense' },
  { id: 6, name: 'Покупки', icon: '▧', color: '#df89a6', category_type: 'expense' },
  { id: 7, name: 'Впечатления', icon: '✳', color: '#64b6ad', category_type: 'expense' },
];
export const today = () => new Date().toLocaleDateString('en-CA');
export function demoOperations() {
  const now = new Date();
  const date = (day, offset = 0) => new Date(now.getFullYear(), now.getMonth() + offset, day, 12).toLocaleDateString('en-CA');
  return Array.from({ length: 6 }, (_, i) => [
    { category_id: 1, amount: 145000 + i * 3000, description: 'Зарплата · Студия', operation_date: date(1, i - 5), operation_type: 'income' },
    { category_id: 2, amount: 24000 + i * 1800, description: 'Дизайн-проект', operation_date: date(5, i - 5), operation_type: 'income' },
    { category_id: 5, amount: 38000, description: 'Аренда квартиры', operation_date: date(3, i - 5), operation_type: 'expense' },
    { category_id: 3, amount: 12800 + i * 400, description: 'Продукты на неделю', operation_date: date(8, i - 5), operation_type: 'expense' },
    { category_id: 4, amount: 3200 + i * 150, description: 'Такси и метро', operation_date: date(10, i - 5), operation_type: 'expense' },
    { category_id: 6, amount: 8500 + i * 500, description: 'Для себя и дома', operation_date: date(12, i - 5), operation_type: 'expense' },
    { category_id: 7, amount: 5400 + i * 300, description: 'Кино и выставки', operation_date: date(14, i - 5), operation_type: 'expense' },
    { category_id: 3, amount: 1250, description: 'Кофе и завтрак', operation_date: date(16, i - 5), operation_type: 'expense' },
  ]).flat().map((op, i) => ({ ...op, id: i + 1 }));
}
export const initialGoals = [
  { id: 1, name: 'Путешествие в Японию', target: 300000, saved: 186000, icon: '✈', color: 'peach' },
  { id: 2, name: 'Подушка спокойствия', target: 500000, saved: 325000, icon: '☂', color: 'mint' },
  { id: 3, name: 'Новый MacBook', target: 200000, saved: 84000, icon: '▱', color: 'lavender' },
];
export function readSaved(key, fallback) {
  try { return JSON.parse(localStorage.getItem(key)) ?? fallback; } catch { return fallback; }
}
