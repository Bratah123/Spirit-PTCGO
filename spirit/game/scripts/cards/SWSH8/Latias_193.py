from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="50c1332e-cf73-5e50-9daf-c50ca23daa51",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latias.Name",
    display_name="Latias",
    searchable_by=["Latias", "Basic", "Fusion Strike", "Latias"],
    subtypes=["Basic", "Fusion Strike"],
    collector_number=193,
    set_code="SWSH8",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=380,
    abilities=[
        Ability(
            title="Red Assist",
            game_text="Once during your turn, you may attach a Psychic Energy card from your hand to 1 of your Latios.",
            effect=unimplemented,
        ),
        Attack(
            title="Dyna Barrier",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Pok\u00e9mon VMAX.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=unimplemented,
        ),
    ],
)