package com.example.robertgutierrez.attempt2;

import java.io.File;

import android.app.Activity;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.net.Uri;
import android.nfc.NfcAdapter;
import android.os.Build;
import android.os.Bundle;
import android.os.Environment;
import android.provider.Settings;
import android.view.View;
import android.widget.Toast;

//public class MainActivity extends ActionBarActivity {
public class  MainActivity extends Activity {

    private NfcAdapter nfcAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        PackageManager pm = this.getPackageManager();
        // Check whether NFC is available on device
        if (!pm.hasSystemFeature(PackageManager.FEATURE_NFC)) {
            // NFC is not available on the device.
            Toast.makeText(this, "The device does not has NFC hardware.",
                    Toast.LENGTH_SHORT).show();
        }
        // Check whether device is running Android 4.1 or higher
        else if (Build.VERSION.SDK_INT < Build.VERSION_CODES.JELLY_BEAN) {
            // Android Beam feature is not supported.
            Toast.makeText(this, "Android Beam is not supported.",
                    Toast.LENGTH_SHORT).show();
        } else {
            // NFC and Android Beam file transfer is supported.
            Toast.makeText(this, "Android Beam is supported on your device.",
                    Toast.LENGTH_SHORT).show();
        }

    }


    public void sendFile(View view) {

        PackageManager pm = this.getPackageManager();
        // Decoding the message!
        if (!pm.hasSystemFeature(PackageManager.FEATURE_NFC)) {
            // NFC is not a functionality in this device
        } else if (Build.VERSION.SDK_INT < Build.VERSION_CODES.JELLY_BEAN) {
            // Check if device has Jelly bean or Higher  == 4.3v
        } else {
            // This device holds NFC
        }

        nfcAdapter = NfcAdapter.getDefaultAdapter(this); // used to manage exchange of data

        if (!nfcAdapter.isEnabled()) {
            // NFC is disabled! ... print out a statement
        } else {
            // NFC is enabled() and ready to !
        }
        startActivity(new Intent(Settings.ACTION_NFC_SETTINGS));


        // Check adapter to see if NFC is on 
        if (!nfcAdapter.isEnabled()) {
            // NFC is disabled, show the settings UI to enable NFC
        }
        // Check whether Android Beam feature is enabled on device

        else if (!nfcAdapter.isNdefPushEnabled()) {
            // Android Beam is disabled, show the settings UI to enable Android Beam
        } else {
            // NFC and Android Beam both are enabled
        }
        startActivity(new Intent(Settings.ACTION_NFCSHARING_SETTINGS));

        // Once all done checking then you can establish a new file for the beam

        File pictureFolder = Environment.getExternalStoragePublicDirectory(
                Environment.DIRECTORY_PICTURES);

// etc

        // Loading path to Picture Folder in my Phone ...
        File fileDirectory = Environment
                .getExternalStoragePublicDirectory(
                        Environment.DIRECTORY_PICTURES);

    // must go to phone and see an existing name
     // I tried to change name of file to something more generic, however phone changed it
     // automatically, to something that had date and time value.  Did not have enough time
     // to overide those settings.
           String fileName = "1430666089125.jpg"; // THIS image name is very specific to me.


        File fileToTransfer = new File(fileDirectory, fileName);
        fileToTransfer.setReadable(true, false);

        nfcAdapter.setBeamPushUris(new Uri[]{Uri.fromFile(fileToTransfer)}, this);
    }
}




