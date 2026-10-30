from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm6 import cell_connector, verdict_gx

card = PokemonCardDef(
    guid="0f174a06-6f85-571b-9afd-7fb9ff915229",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZygardeGX.Name",
    display_name="Zygarde-GX",
    searchable_by=["Zygarde-GX", "Basic", "GX", "ZygardeGX"],
    subtypes=["Basic", "GX"],
    collector_number=136,
    set_code="SM6",
    rarity=Rarities.RareRainbow,
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
