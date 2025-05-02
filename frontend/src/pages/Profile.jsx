import React, { useEffect, useState } from 'react';
import { Box, Typography, Alert, Card, CardContent, Avatar, Stack, Grid, CircularProgress } from '@mui/material';
import axios from 'axios';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

function parseJwt(token) {
  try {
    return JSON.parse(atob(token.split('.')[1]));
  } catch {
    return null;
  }
}

const mockChartData = [
  { month: 'Jan', signups: 5 },
  { month: 'Feb', signups: 8 },
  { month: 'Mar', signups: 12 },
  { month: 'Apr', signups: 7 },
  { month: 'May', signups: 15 },
  { month: 'Jun', signups: 10 },
];

export default function Profile() {
  const token = localStorage.getItem('jwt_token');
  const user = token ? parseJwt(token) : null;
  const [totalUsers, setTotalUsers] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchUsers() {
      try {
        const res = await axios.get('http://127.0.0.1:8000/get_users');
        setTotalUsers(res.data.length);
      } catch {
        setTotalUsers('N/A');
      } finally {
        setLoading(false);
      }
    }
    fetchUsers();
  }, []);

  if (!user) {
    return <Alert severity="warning">You are not logged in.</Alert>;
  }

  return (
    <Box sx={{ flexGrow: 1, mt: 4 }}>
      <Grid container spacing={3} justifyContent="space-evenly" alignItems="stretch">
        <Grid item xs={12} md={4}>
          <Card sx={{ p: 2, boxShadow: 6, minHeight: 260, display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
            <CardContent>
              <Stack spacing={2} alignItems="center">
                <Avatar sx={{ bgcolor: 'secondary.main', width: 64, height: 64, fontSize: 32 }}>
                  {user.name ? user.name[0].toUpperCase() : user.sub[0].toUpperCase()}
                </Avatar>
                <Typography variant="h5" fontWeight={700} color="primary.main">
                  Welcome, {user.name || user.sub}!
                </Typography>
                <Typography variant="body1"><b>Email:</b> {user.sub}</Typography>
              </Stack>
            </CardContent>
          </Card>
        </Grid>
        <Grid item xs={12} md={4}>
          <Card sx={{ p: 2, boxShadow: 6, minHeight: 260, display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
            <CardContent>
              <Typography variant="h6" color="primary.main" gutterBottom>
                Quick Stats
              </Typography>
              {loading ? (
                <CircularProgress size={24} />
              ) : (
                <>
                  <Typography variant="body1"><b>Total Users:</b> {totalUsers}</Typography>
                  <Typography variant="body1"><b>Your Name:</b> {user.name}</Typography>
                </>
              )}
            </CardContent>
          </Card>
        </Grid>
        <Grid item xs={12} md={4}>
          <Card sx={{ p: 2, boxShadow: 6, minHeight: 260, display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
            <CardContent>
              <Typography variant="h6" color="primary.main" gutterBottom>
                User Signups per Month
              </Typography>
              <Box sx={{ height: 140 }}>
                <ResponsiveContainer width="100%" height="100%">
                  <BarChart data={mockChartData} margin={{ top: 10, right: 10, left: 0, bottom: 0 }}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="month" />
                    <YAxis allowDecimals={false} />
                    <Tooltip />
                    <Bar dataKey="signups" fill="#1976d2" radius={[4, 4, 0, 0]} />
                  </BarChart>
                </ResponsiveContainer>
              </Box>
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </Box>
  );
} 