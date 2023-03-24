package com.example.agribot;

import android.graphics.Typeface;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;
import com.agrawalsuneet.dotsloader.loaders.LazyLoader;
import com.bumptech.glide.Glide;
import java.util.List;


public class ChatAdapter extends RecyclerView.Adapter<RecyclerView.ViewHolder> {

    private final int SELF = 100;
    private final List<Message> messageArrayList;
    RecyclerView mRecyclerView;
    public ChatAdapter(List<Message> messageArrayList) {
        this.messageArrayList = messageArrayList;


    }

    @Override
    public void onAttachedToRecyclerView(@NonNull RecyclerView recyclerView) {
        super.onAttachedToRecyclerView(recyclerView);

        mRecyclerView = recyclerView;
    }
    @NonNull
    @Override
    public RecyclerView.ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View itemView;



        // view type is to identify where to render the chat message
        // left or right
        if (viewType == SELF) {
            // self message
            itemView = LayoutInflater.from(parent.getContext())
                    .inflate(R.layout.chat_item_self, parent, false);
        } else {
            // WatBot message

            itemView = LayoutInflater.from(parent.getContext())
                    .inflate(R.layout.chat_item_watson, parent, false);

            itemView.findViewById(R.id.dotsTVBot).setVisibility(View.VISIBLE);
            itemView.findViewById(R.id.message).setVisibility(View.INVISIBLE);
        }


        return new ViewHolder(itemView);
    }
 public void setData(String message){
     ViewHolder viewHolder = (ViewHolder) mRecyclerView.findViewHolderForAdapterPosition(messageArrayList.size()-1);
     Message m = messageArrayList.get(messageArrayList.size()-1);
     m.setMessage(message);

     assert viewHolder != null;
     viewHolder.message.setVisibility(View.VISIBLE);
     viewHolder.message.setText(m.getMessage());
     viewHolder.loader.setVisibility(View.INVISIBLE);

 }
    @Override
    public int getItemViewType(int position) {
        Message message = messageArrayList.get(position);
        if (message.getId() != null && message.getId().equals("1")) {
            return SELF;
        }

        return position;
    }

    @Override
    public void onBindViewHolder(@NonNull final RecyclerView.ViewHolder holder, int position) {
        Message message = messageArrayList.get(position);


        switch (message.type) {
            case TEXT:

                ((ViewHolder) holder).message.setText(message.getMessage());


                break;
            case BOT:
                ((ViewHolder) holder).message.setText(message.getMessage());
                ((ViewHolder) holder).loader.setVisibility(View.INVISIBLE);
                ((ViewHolder) holder).message.setVisibility(View.VISIBLE);

                break;
            case IMAGE:
                ((ViewHolder) holder).message.setVisibility(View.GONE);
                ImageView iv = ((ViewHolder) holder).image;
                Glide
                        .with(iv.getContext())
                        .load(message.getUrl())
                        .into(iv);
                break;
        }
    }

    @Override
    public int getItemCount() {
        return messageArrayList.size();
    }

    public static class ViewHolder extends RecyclerView.ViewHolder {

        TextView message;
        ImageView image;
        LazyLoader loader;


        public ViewHolder(View view) {
            super(view);

            message = (TextView) itemView.findViewById(R.id.message);
            image = (ImageView) itemView.findViewById(R.id.image);
            loader = (LazyLoader) itemView.findViewById(R.id.dotsTVBot);


            //TODO: Uncomment this if you want to use a custom Font
            String customFont = "Montserrat-Regular.ttf";
            Typeface typeface = Typeface.createFromAsset(itemView.getContext().getAssets(), customFont);
            message.setTypeface(typeface);

        }
    }


}