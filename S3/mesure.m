function [Y,coef,Err]=mesure(E,s,Nexp,coef,spec)

% E est la matrice d'expérience
% s est la variance
if nargin==3
    coef=rand(16,1);
    spec='interaction';
    
end
    
% y=x2fx(E,'interaction')*coef;
% Err=random('normal',0,s,Nexp,1);
% Y=y+Err;

if strcmp(spec,'linear')==1
    y=x2fx(E,spec)*coef(1:6,:);
    Err=random('normal',0,s,Nexp,1);
    Y=y+Err;

elseif strcmp(spec,'interaction')==1
        
    y=x2fx(E,spec)*coef;
    Err=random('normal',0,s,Nexp,1);
    Y=y+Err;
   
    end
end