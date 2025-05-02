import { BrowserRouter as Router, Routes, Route, Link, Outlet, useNavigate, useLocation } from 'react-router-dom';
import { AppBar, Toolbar, Typography, Button, Container, Box, Avatar, Stack, Drawer, IconButton, List, ListItem, ListItemIcon, ListItemText, Divider } from '@mui/material';
import MenuIcon from '@mui/icons-material/Menu';
import HomeIcon from '@mui/icons-material/Home';
import PersonAddIcon from '@mui/icons-material/PersonAdd';
import GroupIcon from '@mui/icons-material/Group';
import InfoIcon from '@mui/icons-material/Info';
import LoginIcon from '@mui/icons-material/Login';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import LogoutIcon from '@mui/icons-material/Logout';
import Home from './pages/Home';
import Signup from './pages/Signup';
import Users from './pages/Users';
import About from './pages/About';
import Login from './pages/Login';
import Profile from './pages/Profile';
import { useEffect, useState } from 'react';

function getUserFromToken() {
  const token = localStorage.getItem('jwt_token');
  if (!token) return null;
  try {
    return JSON.parse(atob(token.split('.')[1]));
  } catch {
    return null;
  }
}

const navLinks = [
  { text: 'Home', to: '/', icon: <HomeIcon /> },
  { text: 'Signup', to: '/signup', icon: <PersonAddIcon /> },
  { text: 'Users', to: '/users', icon: <GroupIcon /> },
  { text: 'About', to: '/about', icon: <InfoIcon /> },
];

function Layout() {
  const [user, setUser] = useState(getUserFromToken());
  const [drawerOpen, setDrawerOpen] = useState(false);
  const navigate = useNavigate();
  const location = useLocation();
  const isDashboard = location.pathname === '/profile' || location.pathname === '/dashboard';

  useEffect(() => {
    const onStorage = () => setUser(getUserFromToken());
    window.addEventListener('storage', onStorage);
    return () => window.removeEventListener('storage', onStorage);
  }, []);

  const handleLogout = () => {
    localStorage.removeItem('jwt_token');
    setUser(null);
    setDrawerOpen(false);
    navigate('/login');
  };

  const drawerContent = (
    <Box sx={{ width: 250 }} role="presentation" onClick={() => setDrawerOpen(false)}>
      <List>
        {navLinks.map((link) => (
          <ListItem button key={link.text} component={Link} to={link.to}>
            <ListItemIcon>{link.icon}</ListItemIcon>
            <ListItemText primary={link.text} />
          </ListItem>
        ))}
        <Divider sx={{ my: 1 }} />
        {user ? (
          <>
            <ListItem button component={Link} to="/profile">
              <ListItemIcon><AccountCircleIcon /></ListItemIcon>
              <ListItemText primary="Profile" />
            </ListItem>
            <ListItem button onClick={handleLogout}>
              <ListItemIcon><LogoutIcon /></ListItemIcon>
              <ListItemText primary="Logout" />
            </ListItem>
          </>
        ) : (
          <ListItem button component={Link} to="/login">
            <ListItemIcon><LoginIcon /></ListItemIcon>
            <ListItemText primary="Login" />
          </ListItem>
        )}
      </List>
    </Box>
  );

  return (
    <>
      <AppBar position="static" color="primary" elevation={2}>
        <Toolbar>
          <IconButton
            color="inherit"
            edge="start"
            sx={{ mr: 2, display: { xs: 'inline-flex', md: 'none' } }}
            onClick={() => setDrawerOpen(true)}
          >
            <MenuIcon />
          </IconButton>
          <Stack direction="row" alignItems="center" spacing={2} sx={{ flexGrow: 1 }}>
            <Avatar sx={{ bgcolor: 'secondary.main', width: 36, height: 36 }}>E</Avatar>
            <Typography variant="h6" sx={{ fontWeight: 700, display: { xs: 'none', md: 'block' } }}>
              Empire SaaS
            </Typography>
          </Stack>
          {user && (
            <Stack direction="row" alignItems="center" spacing={2}>
              <Avatar sx={{ bgcolor: 'secondary.main', width: 32, height: 32 }}>
                {user.name ? user.name[0].toUpperCase() : user.sub[0].toUpperCase()}
              </Avatar>
              <Typography sx={{ display: { xs: 'none', md: 'block' } }}>{user.name || user.sub}</Typography>
            </Stack>
          )}
        </Toolbar>
      </AppBar>
      <Drawer
        anchor="left"
        open={drawerOpen}
        onClose={() => setDrawerOpen(false)}
        sx={{
          '& .MuiDrawer-paper': { boxSizing: 'border-box', width: 250 },
        }}
      >
        {drawerContent}
      </Drawer>
      <Container maxWidth={isDashboard ? false : "md"} sx={{ mt: 6, mb: 4 }}>
        <Outlet />
      </Container>
    </>
  );
}

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="signup" element={<Signup />} />
          <Route path="users" element={<Users />} />
          <Route path="about" element={<About />} />
          <Route path="login" element={<Login />} />
          <Route path="profile" element={<Profile />} />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
