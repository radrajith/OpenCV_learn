function [H, theta, rho] = hough_lines_acc(BW, varargin)

    % Compute Hough accumulator array for finding lines.
    %
    % BW: Binary (black and white) image containing edge pixels
    % RhoResolution (optional): Difference between successive rho values, in pixels
    % Theta (optional): Vector of theta values to use, in degrees
    %
    % Please see the Matlab documentation for hough():
    % http://www.mathworks.com/help/images/ref/hough.html
    % Your code should imitate the Matlab implementation.
    %
    % Pay close attention to the coordinate system specified in the assignment.
    % Note: Rows of H should correspond to values of rho, columns those of theta.
    %% If the values are not declared, use this default one
    rhoStep =1;         %bin size is 1
   
    %% Parse input arguments
    p = inputParser();
    addParameter(p, 'RhoResolution', 1);
    addParameter(p, 'Theta', linspace(-90, 89, 180));
    parse(p, varargin{:});

    rhoStep = p.Results.RhoResolution;
    theta = p.Results.Theta;

    %% TODO: Your code here
    %calculate size of rho
    %rho = sqrt(x^2 + y^2) converting from cartesian to polar
    rhoSize = ceil(sqrt((size(BW,1)-1)^2 + (size(BW,2)-1)^2));   % the coordinates states at (0,0) but the image starts at (1,1)
    rho = -rhoSize:rhoStep:rhoSize;           %creating array from -rhosize to +rhosize with step size of rhostep
    theta = 0:1:180;
    
    %create and intialize accumulator array
    H = zeros(length(rho), length(theta));
    
    %for every edge point increment the value in the accumulator array
    for x = 1:size(BW,1)
        for y = 1:size(BW,2)
            if(BW(x,y))                     %if there is edge then increment the bin
                for t = 0:1:179
                    r = ceil((x*cosd(t)) + (y*sind(t)));    %corresponding rho value
                    r = r + rhoSize;
                    H(r,t+1) = H(r,t+1) + 1;
                end
            end
        end
    end
         
end
