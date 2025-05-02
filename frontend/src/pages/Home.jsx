import React from 'react';
import { Box, Typography, Button, Card, CardContent, Stack } from '@mui/material';
import { Link } from 'react-router-dom';

export default function Home() {
  return (
    <Box display="flex" justifyContent="center" alignItems="center" minHeight="60vh">
      <Card sx={{ p: 4, minWidth: 350, boxShadow: 6 }}>
        <CardContent>
          <Stack spacing={3} alignItems="center">
            <Typography variant="h3" fontWeight={700} color="primary.main" gutterBottom>
              Empire SaaS
            </Typography>
            <Typography variant="h6" color="text.secondary" align="center">
              Welcome to Empire SaaS! Build, manage, and scale your business with our modern platform.
            </Typography>
            <Button
              variant="contained"
              color="primary"
              size="large"
              component={Link}
              to="/signup"
              sx={{ mt: 2 }}
            >
              Get Started
            </Button>
          </Stack>
        </CardContent>
      </Card>
    </Box>
  );
} 