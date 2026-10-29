from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm6 import cell_connector, verdict_gx

card = PokemonCardDef(
    guid="effdb2a2-399b-5c8c-8c3d-80f3e047514b",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZygardeGX.Name",
    display_name="Zygarde-GX",
    searchable_by=["Zygarde-GX", "Basic", "GX", "ZygardeGX"],
    subtypes=["Basic", "GX"],
    collector_number=134,
    set_code="HF",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=718,
    abilities=[
        Attack(
            title="Cell Connector",
            game_text="Attach 2 Fighting Energy cards from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=cell_connector,
        ),
        Attack(
            title="Land's Wrath",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
        ),
        Attack(
            title="Verdict-GX",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from Pok\u00e9mon-GX and Pok\u00e9mon-EX during your opponent's next turn. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=verdict_gx,
        ),
    ],
)
