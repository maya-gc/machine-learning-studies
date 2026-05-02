import torch
import torch.nn as nn

class MiniTransformer(nn.Module):
    def __init__(
        self,
        vocab_size,
        embed_dim=64,
        num_heads=4,
        hidden_dim=128,
        num_layers=2,
        max_len=100,
        num_classes=2,
        dropout=0.1
    ):
        super().__init__()

        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)
        self.pos_embedding = nn.Embedding(max_len, embed_dim)

        encoder_layer = nn.TransformerEncoderLayer(
            d_model=embed_dim,
            nhead=num_heads,
            dim_feedforward=hidden_dim,
            dropout=dropout,
            batch_first=True,
            activation="relu"
        )

        self.transformer_encoder = nn.TransformerEncoder(
            encoder_layer,
            num_layers=num_layers
        )

        self.dropout = nn.Dropout(dropout)
        self.fc = nn.Linear(embed_dim, num_classes)

    def forward(self, x):
        batch_size, seq_len = x.size()
        device = x.device

        padding_mask = (x == 0)

        positions = torch.arange(seq_len, device=device).unsqueeze(0).expand(batch_size, seq_len)
        embedded = self.embedding(x) + self.pos_embedding(positions)

        encoded = self.transformer_encoder(
            embedded,
            src_key_padding_mask=padding_mask
        )

        mask = (~padding_mask).unsqueeze(-1).float()
        summed = (encoded * mask).sum(dim=1)
        counts = mask.sum(dim=1).clamp(min=1.0)
        pooled = summed / counts

        out = self.dropout(pooled)
        out = self.fc(out)
        return out