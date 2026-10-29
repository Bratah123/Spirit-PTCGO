from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm6 import cell_connector, verdict_gx

card = PokemonCardDef(
    guid="b9936c70-2929-54a3-b319-4c3a3755b33d",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZygardeGX.Name",
    display_name="Zygarde-GX",
    searchable_by=["Zygarde-GX", "Basic", "GX", "ZygardeGX"],
    subtypes=["Basic", "GX"],
    collector_number=73,
    set_code="SM6",
    rarity=Rarities.RareHoloGX,
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
